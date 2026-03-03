# 🚶 Opgave 02 – Del PIR Bevægelsesdata via CoAP

I denne opgave skal du programmere ESP32 til at læse data fra en PIR bevægelsessensor og gøre den tilgængelig via en CoAP server.

![alt text](image-1.png)

## 🎯 Formål

Lær at:
- Læse digital input fra en PIR sensor
- Forbinde til WiFi fra ESP32
- Dele bevægelsesdata via CoAP GET anmodninger

---

## 💡 Python-kode

Opret en ny fil i Thonny og skriv følgende:

```python
# ESP32 + PIR Bevægelsessensor CoAP Server
# Svarer med 1 ved bevægelse, 0 ved ingen bevægelse

from machine import Pin
import network
import time
from coapmini import CoapServer

# ===== KONFIGURATION =====
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
PIR_PIN = 14  # GPIO 14 til PIR sensor
# =========================

# Opsæt PIR sensor som input
pir = Pin(PIR_PIN, Pin.IN)

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

# Funktion der aflæser sensoren og returnerer data
def read_motion():
    # Læser værdien (1 = bevægelse, 0 = ingen bevægelse)
    state = pir.value()
    status_tekst = "Bevægelse" if state == 1 else "Ingen bevægelse"
    print(f'Målt: {status_tekst} ({state})')
    
    # Returnerer json-pakket data
    return {"motion": state}

def main():
    # Forbind til WiFi (Gemmer IP)
    ip = wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    
    # Start CoAP Server
    srv = CoapServer()
    
    # Kobl en URL (/pir) sammen med vores funktion
    srv.add("/pir", read_motion)
    
    # Start server-loopet så den altid lytter efter forespørgsler
    srv.serve_forever(f"Klar! Hent data med GET coap://{ip}:5683/pir")

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

### Sådan tester du det:
I Node-RED (eller et andet CoAP værktøj):
1. Vælg en **coap request** node.
2. Sæt metoden til `GET`.
3. Sæt URL til `coap://<din-esp32-ip>:5683/pir` (Husk IP fra Thonny).
4. Forbind en **inject**-node foran (sæt den evt. til at gentage hvert 2. sekund).
5. Forbind en **debug**-node bagefter for at se dataen.

---

## 📝 Forklaring

**Sådan virker koden:**
- I modsætning til MQTT, hvor sensoren *skubber* data ud (Push), venter denne CoAP-server på at blive spurgt (Pull).
- Når Node-RED sender en GET anmodning, kaldes funktionen `read_motion()`.
- PIR-sensoren indlæses med `pir.value()`.
- Sensoren returnerer **1** når der er bevægelse, og **0** når der er ro.
- Værdien pakkes som en Dictionary (`{"motion": 1}`) og sendes tilbage til Node-RED i JSON-format.
