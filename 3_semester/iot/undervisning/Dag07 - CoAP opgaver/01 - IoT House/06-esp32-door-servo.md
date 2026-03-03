# 🚪 Opgave 06 – Styr Dør-Servo via CoAP

I denne opgave skal du programmere ESP32 til at modtage CoAP-kommandoer og styre en servo motor der åbner og lukker en dør. Servoen forbindes til GPIO 13.

![alt text](image-4.png)

## 🎯 Formål

Lær at:
- Styre en servo motor med PWM-signaler
- Modtage åbn/luk kommandoer via CoAP
- Konvertere grader (0–180°) til PWM duty cycle
- Oprette endpoints for preset positioner (OPEN/CLOSE)

---

## 💡 Python-kode

Opret en ny fil i Thonny og skriv følgende:

```python
# ESP32 CoAP Server - Dør Servo Kontrol
# Modtager /door/open eller /door/close kommandoer via CoAP

import network
import time
from machine import Pin, PWM
from coapmini import CoapServer

# ===== KONFIGURATION =====
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
SERVO_PIN = 13  # GPIO 13 til dør-servo

DOOR_CLOSED = 0   # 0 grader = lukket
DOOR_OPEN = 90    # 90 grader = åben
# =========================

# Opsæt PWM til servo (50Hz er standard for alle servomotorer)
servo = PWM(Pin(SERVO_PIN), freq=50)

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

def angle_to_duty(angle):
    """Omregner vinkel (0-180 grader) til ESP32 PWM duty cycle (0-1023)"""
    angle = max(0, min(180, angle))
    duty_percent = (angle / 180) * 10 + 2.5
    return int(duty_percent * 1023 / 100)

def set_servo(angle):
    servo.duty(angle_to_duty(angle))
    print(f"Dør servo: {angle}°")

def door_open():
    set_servo(DOOR_OPEN)
    return {"doer": "aaben", "vinkel": DOOR_OPEN}

def door_close():
    set_servo(DOOR_CLOSED)
    return {"doer": "lukket", "vinkel": DOOR_CLOSED}

def main():
    ip = wifi_connect(WIFI_SSID, WIFI_PASSWORD)

    # Luk døren som udgangspunkt
    set_servo(DOOR_CLOSED)

    srv = CoapServer()
    srv.add("/door/open", door_open)
    srv.add("/door/close", door_close)
    srv.serve_forever(f"Klar! Styr døren med GET coap://{ip}:5683/door/open eller /door/close")

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
2. Den ene: URL = `coap://<din-esp32-ip>:5683/door/open`
3. Den anden: URL = `coap://<din-esp32-ip>:5683/door/close`
4. Sæt en **inject**-node foran hver som knapper.
5. Sæt en **debug**-node bagved for at se JSON-svaret fra ESP32'en.

---

## 📝 Forklaring

**Forskel fra vindue-opgaven (05):**
- Servoen sidder på **GPIO 13** i stedet for GPIO 5.
- URL-endpoints hedder `/door/open` og `/door/close`.
- Ellers er PWM-logikken og CoAP-strukturen præcis den samme.

**Sådan virker servoen:**

1. **PWM frekvens**: 50Hz er standard for servomotorer. Én periode = 20ms.
2. **Pulsbredde bestemmer vinkel:**
   - 0.5ms puls (2.5% duty) = 0° → Dør lukket
   - 1.5ms puls (7.5% duty) = 90° → Dør åben
3. **Duty cycle formel**: `duty = (angle/180 * 10 + 2.5) * 1023/100`
4. **CoAP aktuation**: ESP32 bekræfter udførslen ved at svare med en JSON-pakke.


**Bonus - Dashboard med knapper:**
Du kan oprette en dashboard med OPEN/CLOSE knapper for nem styring!

---

## 📝 Forklaring

**Sådan virker servoen:**

1. **PWM frekvens**: 50Hz (standard for servomotorer)
   - En periode er 20ms (1/50Hz)
   
2. **Pulse width bestemmer vinkel:**
   - 0.5ms pulse = 0° (dør lukket)
   - 1.5ms pulse = 90° (dør åben)
   - 2.5ms pulse = 180° (helt åben)

3. **Duty cycle beregning:**
   - 0.5ms af 20ms = 2.5% duty cycle = 0°
   - 2.5ms af 20ms = 12.5% duty cycle = 180°
   - ESP32 PWM duty: 0-1023 (10-bit)
   - Formel: `duty = (angle/180 * 10 + 2.5) * 1023/100`

4. **Kommando-typer:**
   - **Preset**: `OPEN` / `CLOSE` - hurtig styring
   - **Præcis**: `0` til `180` - fuld kontrol over vinkel

**MQTT Kommandoer:**
- `OPEN` → 90° (dør åben)
- `CLOSE` → 0° (dør lukket)  
- `0-180` → Præcis vinkel (fx `60` for delvist åben)

**Forskel mellem vindue og dør:**
- Samme mekanik, forskellig funktion
- Kan tilpasses forskellige åbningsvinkler efter behov
- GPIO 13 i stedet for GPIO 5
- Topic `door` i stedet for `window`
