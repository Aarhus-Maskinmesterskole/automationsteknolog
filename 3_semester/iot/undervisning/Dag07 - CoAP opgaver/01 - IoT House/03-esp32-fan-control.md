# 🌀 Opgave 03 – Modtag Kommandoer og Styr Blæser via CoAP

I denne opgave skal du programmere ESP32 til at køre en CoAP-server der lytter på to forskellige adresser (endpoints) for at styre en blæser (fan). Dette viser, hvordan vi kan modtage kommandoer (actuation) udefra!

![alt text](image-2.png)

## 🎯 Formål

Lær at:
- Styre hardware (blæser med to pins) baseret på modtagne CoAP-anmodninger
- Oprette flere "endpoints" (URL'er) på samme CoAP-server, knyttet til forskellige handlinger

---

## 💡 Python-kode

Opret en ny fil i Thonny og skriv følgende:

```python
# ESP32 CoAP Server - Blæser kontrol
# Modtager /fan/on eller /fan/off kommandoer

from machine import Pin
import network
import time
from coapmini import CoapServer

# ===== KONFIGURATION =====
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"

# Blæser-pins (H-bro eller motor driver IN1/IN2)
FAN_PIN1 = 18  # GPIO 18
FAN_PIN2 = 19  # GPIO 19
# =========================

# Opsæt pins til blæser
fan_pin1 = Pin(FAN_PIN1, Pin.OUT, value=0)
fan_pin2 = Pin(FAN_PIN2, Pin.OUT, value=0)

def wifi_connect(ssid, password):
    print("Forbinder til WiFi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    
    ip = wlan.ifconfig()[0]
    print(f"Forbundet! IP Adresse: {ip}")
    return ip

def fan_off():
    """Sluk blæseren"""
    fan_pin1.value(0)
    fan_pin2.value(0)
    status = '🌀 Blæser: OFF'
    print(status)
    # Vi returnerer status som JSON via CoAP, 
    # så afsenderen ved at beskeden blev modtaget og udført.
    return {"fan": "off", "status": status}

def fan_on():
    """Tænd blæseren (forward)"""
    fan_pin1.value(1)  # IN1 HIGH
    fan_pin2.value(0)  # IN2 LOW
    status = '🌀 Blæser: ON'
    print(status)
    return {"fan": "on", "status": status}

# Hovedprogram
def main():
    # Forbind til WiFi og gem IP
    ip = wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    
    # Start CoAP Server
    srv = CoapServer()
    
    # Kobl URL'er sammen med vores blæser-funktioner
    srv.add("/fan/on", fan_on)
    srv.add("/fan/off", fan_off)
    
    # Initial tilstand: Sluk blæser
    fan_off()
    
    # Start lytte-loop
    srv.serve_forever(f"Klar! Styr blæseren med GET coap://{ip}:5683/fan/on eller /fan/off")

if __name__ == '__main__':
    main()
```

### Konfigurér og kør

1. **Rediger følgende i koden:**
   - `WIFI_SSID` → Dit WiFi-navn
   - `WIFI_PASSWORD` → Dit WiFi-password

2. **Husk `coapmini.py`:**
   Sørg for at du også har uploadet biblioteket `coapmini.py` til roden af din ESP32.

3. **Kør programmet:**
   - Gem filen som `main.py`
   - Tryk **F5**
   - Notér den IP-adresse, der udskrives i Shell-vinduet.

**Forventet output:**
```
WiFi forbundet! IP-adresse: 192.168.1.123
🌀 Blæser: OFF
Klar! Styr blæseren med GET coap://<IP>:5683/fan/on eller /fan/off
```

✅ Din ESP32 lytter nu og venter på, at nogen anmoder om `/fan/on` eller `/fan/off`!

---

## 📝 Test med Node-RED

For at teste din ESP32, skal du sende forespørgsler til den fra Node-RED.

Du skal bruge to flows i Node-RED: ét til at tænde, og ét til at slukke.

`[Inject "TEND"] → [CoAP Request: /fan/on] → [Debug]`
`[Inject "SLUK"] → [CoAP Request: /fan/off] → [Debug]`

**Sådan gør du:**
1. Opret to **CoAP Request** nodes.
2. Sæt Method til `GET` i begge.
3. I den ene sætter du URL til `coap://<din-esp32-ip>:5683/fan/on`
4. I den anden sætter du URL til `coap://<din-esp32-ip>:5683/fan/off`
5. Forbind almindelige **inject**-noder foran dem for at kunne trykke på "knapper".
6. Sæt en **debug**-node bagved begge, så du kan se din ESP32 svare dig tilbage, når kommandoen er udført.

Når du klikker "Tænd" (Inject), anmoder CoAP-noden om URL'en `/fan/on`. Din ESP32 kører funktionen, starter blæseren, og svarer tilbage med en JSON-bekræftelse!

---

## 🔍 Forklaring

**Sådan virker koden:**

1. **CoAP Router**: Serveren har indbygget en router, der lytter på forespørgsler fra klienter.
2. **Endpoints (`/fan/on` & `/fan/off`)**: Når ESP32 modtager et opkald på en af disse adresser, aktiverer den den tilknyttede Python funktion (`fan_on` eller `fan_off`).
3. **Hardware control**: 
   - I `fan_on()` laves IN1=HIGH, IN2=LOW → Blæser kører fremad.
   - I `fan_off()` laves IN1=LOW, IN2=LOW → Blæser stopper.

Denne teknik bruges også professionelt – ofte refereret til som at lave et **API** (Application Programming Interface), fordi vi tilbyder et grænseflade, som andre programmer (som Node-RED) kan interagere med.
