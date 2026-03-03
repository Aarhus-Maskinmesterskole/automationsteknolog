# 💡 Opgave 07 – Styr Gul LED via CoAP

I denne opgave skal du programmere ESP32 til at modtage CoAP-kommandoer og styre en gul LED. LED'en kan tændes og slukkes via CoAP GET anmodninger.

![alt text](image-6.png)
![alt text](image-7.png)

## 🎯 Formål

Lær at:
- Styre en digital output (LED) fra ESP32
- Modtage tænd/sluk kommandoer via CoAP endpoints
- Arbejde med GPIO output pins

---

## 💡 Python-kode

Opret en ny fil i Thonny og skriv følgende:

```python
# ESP32 CoAP Server - Gul LED Kontrol
# Modtager /led/on eller /led/off kommandoer via CoAP

import network
import time
from machine import Pin
from coapmini import CoapServer

# ===== KONFIGURATION =====
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
LED_PIN = 12  # GPIO 12 til gul LED
# =========================

# Opsæt LED som output
led = Pin(LED_PIN, Pin.OUT)

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

def led_on():
    """Tænd LED og returner status"""
    led.value(1)
    print("💡 Gul LED: ON")
    return {"led": "on"}

def led_off():
    """Sluk LED og returner status"""
    led.value(0)
    print("💡 Gul LED: OFF")
    return {"led": "off"}

def main():
    ip = wifi_connect(WIFI_SSID, WIFI_PASSWORD)

    # Sluk LED som udgangspunkt
    led.value(0)

    srv = CoapServer()
    srv.add("/led/on", led_on)
    srv.add("/led/off", led_off)
    srv.serve_forever(f"Klar! Styr LED'en med GET coap://{ip}:5683/led/on eller /led/off")

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
I Node-RED:
1. Opret to **CoAP Request** nodes, begge med Method = `GET`.
2. Den ene: URL = `coap://<din-esp32-ip>:5683/led/on`
3. Den anden: URL = `coap://<din-esp32-ip>:5683/led/off`
4. Sæt en **inject**-node foran hver som knapper.
5. Sæt en **debug**-node bagved for at se JSON-svaret.

---

## 📝 Forklaring

**Sådan virker koden:**

1. **GPIO Output**: `led.value(1)` tænder LED'en (3.3V på GPIO). `led.value(0)` slukker den (0V).

2. **Separate endpoints**: I stedet for ét topic der modtager `"ON"` eller `"OFF"` som tekst (MQTT), har vi to separate CoAP-adresser `/led/on` og `/led/off`. Ruten bestemmer handlingen.

3. **JSON-svar**: Funktionen returnerer en dict (`{"led": "on"}`), som `coapmini` automatisk sender tilbage som JSON til Node-RED. Det bekræfter at kommandoen er modtaget og udført.

**Elektrisk:**
- GPIO output: 3.3V når HIGH
- LED + modstand forbindes mellem GPIO og GND
- Strømbegrænsende modstand (220–330Ω) beskytter LED
---


