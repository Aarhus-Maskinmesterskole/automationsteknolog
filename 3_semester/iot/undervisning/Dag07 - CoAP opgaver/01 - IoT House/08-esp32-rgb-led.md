# 🌈 Opgave 08 – Styr RGB LED via CoAP

I denne opgave skal du programmere ESP32 til at modtage CoAP-kommandoer og styre en RGB LED (SK6812). LED'en kan skifte farve via CoAP GET anmodninger. SK6812 er en adresserbar RGB LED der styres med en enkelt data-pin.

![alt text](image-8.png)

## 🎯 Formål

Lær at:
- Styre en adresserbar RGB LED (NeoPixel/SK6812)
- Modtage farve-kommandoer via CoAP endpoints
- Arbejde med RGB farveværdier (0-255)
- Bruge NeoPixel biblioteket i MicroPython

---

## 💡 Python-kode

Opret en ny fil i Thonny og skriv følgende:

```python
# ESP32 CoAP Server - RGB LED Kontrol (SK6812)
# Modtager /led/<farvenavn> kommandoer via CoAP

import network
import time
from machine import Pin
from neopixel import NeoPixel
from coapmini import CoapServer

# ===== KONFIGURATION =====
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
RGB_PIN = 26   # GPIO 26
NUM_LEDS = 4   # Antal LED'er i kæden
# =========================

# Opsæt NeoPixel (SK6812)
np = NeoPixel(Pin(RGB_PIN), NUM_LEDS)

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

def set_color(r, g, b):
    """Sæt alle LED'er til samme farve og skriv til hardware"""
    for i in range(NUM_LEDS):
        np[i] = (r, g, b)
    np.write()
    print(f"RGB LED: R={r}, G={g}, B={b}")

# Én funktion per farve – kobles til hvert sit CoAP endpoint
def color_red():
    set_color(255, 0, 0)
    return {"farve": "roed", "r": 255, "g": 0, "b": 0}

def color_green():
    set_color(0, 255, 0)
    return {"farve": "groen", "r": 0, "g": 255, "b": 0}

def color_blue():
    set_color(0, 0, 255)
    return {"farve": "blaa", "r": 0, "g": 0, "b": 255}

def color_yellow():
    set_color(255, 255, 0)
    return {"farve": "gul", "r": 255, "g": 255, "b": 0}

def color_white():
    set_color(255, 255, 255)
    return {"farve": "hvid", "r": 255, "g": 255, "b": 255}

def color_off():
    set_color(0, 0, 0)
    return {"farve": "slukket", "r": 0, "g": 0, "b": 0}

def main():
    ip = wifi_connect(WIFI_SSID, WIFI_PASSWORD)

    # Sluk LED'erne som udgangspunkt
    set_color(0, 0, 0)

    srv = CoapServer()
    srv.add("/led/red",    color_red)
    srv.add("/led/green",  color_green)
    srv.add("/led/blue",   color_blue)
    srv.add("/led/yellow", color_yellow)
    srv.add("/led/white",  color_white)
    srv.add("/led/off",    color_off)
    srv.serve_forever(f"Klar! Skift farve med GET coap://{ip}:5683/led/<farve> (red/green/blue/yellow/white/off)")

if __name__ == '__main__':
    main()
```

### Konfigurér og kør

1. **Rediger følgende i koden:**
   - `WIFI_SSID` → Dit WiFi-navn
   - `WIFI_PASSWORD` → Dit WiFi-password
   - `NUM_LEDS` → Antal LED'er i din LED-strip (oftest 4)

2. **Husk `coapmini.py`:**
   Sørg for at du også har uploadet biblioteket `coapmini.py` til roden af din ESP32.

3. **Kør programmet:**
   - Gem filen som `main.py`
   - Tryk **F5**
   - Notér den IP-adresse, der udskrives i Shell-vinduet.

### Sådan tester du det:
I Node-RED:
1. Opret 6 **CoAP Request** nodes (én per farve), alle med Method = `GET`.
2. Sæt URL'erne til henholdsvis:
   - `coap://<ip>:5683/led/red`
   - `coap://<ip>:5683/led/green`
   - `coap://<ip>:5683/led/blue`
   - `coap://<ip>:5683/led/yellow`
   - `coap://<ip>:5683/led/white`
   - `coap://<ip>:5683/led/off`
3. Sæt en **inject**-node foran hver som farveknapper.
4. Sæt en **debug**-node bagved for at se JSON-svaret.

---

## 📝 Forklaring

**Sådan virker SK6812/NeoPixel:**

1. **One-wire protokol**: Alle LED'er forbindes i en kæde. Én data-pin styrer alle. Data sendes serielt fra ESP32 til LED'erne.

2. **RGB farveværdier**: Hver LED har 3 kanaler: Red, Green, Blue (hver 0–255).
   - `(255, 0, 0)` = Ren rød
   - `(255, 255, 0)` = Gul (rød + grøn)
   - `(0, 0, 0)` = Slukket

3. **NeoPixel bibliotek**:
   - `NeoPixel(pin, antal)` opretter LED-objekt
   - `np[i] = (r, g, b)` sætter farve for LED nummer `i`
   - `np.write()` sender farver til hardware

4. **Én funktion per endpoint**: I stedet for ét MQTT-topic der modtager farvens navn som tekst, har vi et CoAP-endpoint per farve. URL'en bestemmer farven – ingen tekstparsing nødvendig!