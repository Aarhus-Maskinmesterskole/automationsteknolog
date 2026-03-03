# 🪟 Opgave 05 – Styr Vindue-Servo via CoAP

I denne opgave skal du programmere ESP32 til at modtage CoAP-kommandoer og styre en servo motor der åbner og lukker et vindue. Servoen forbindes til GPIO 5.

![alt text](image-5.png)

## 🎯 Formål

Lær at:
- Styre en servo motor med PWM-signaler
- Modtage åbn/luk kommandoer via CoAP
- Konvertere grader (0–180°) til PWM duty cycle
- Oprette flere endpoints for preset positioner (OPEN/CLOSE)

---

## 💡 Python-kode

Opret en ny fil i Thonny og skriv følgende:

```python
# ESP32 CoAP Server - Vindue Servo Kontrol
# Modtager /window/open eller /window/close kommandoer via CoAP

import network
import time
from machine import Pin, PWM
from coapmini import CoapServer

# ===== KONFIGURATION =====
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
SERVO_PIN = 5  # GPIO 5 til vindue-servo

WINDOW_CLOSED = 0   # 0 grader = lukket
WINDOW_OPEN = 90    # 90 grader = åben
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
    print(f"Vindue servo: {angle}°")

def window_open():
    set_servo(WINDOW_OPEN)
    return {"vindue": "aaben", "vinkel": WINDOW_OPEN}

def window_close():
    set_servo(WINDOW_CLOSED)
    return {"vindue": "lukket", "vinkel": WINDOW_CLOSED}

def main():
    ip = wifi_connect(WIFI_SSID, WIFI_PASSWORD)

    # Luk vinduet som udgangspunkt
    set_servo(WINDOW_CLOSED)

    srv = CoapServer()
    srv.add("/window/open", window_open)
    srv.add("/window/close", window_close)
    srv.serve_forever(f"Klar! Styr vinduet med GET coap://{ip}:5683/window/open eller /window/close")

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
2. Den ene: URL = `coap://<din-esp32-ip>:5683/window/open`
3. Den anden: URL = `coap://<din-esp32-ip>:5683/window/close`
4. Sæt en **inject**-node foran hver af dem som knapper.
5. Sæt en **debug**-node bagved for at se JSON-svaret fra ESP32'en.

---

## 📝 Forklaring

**Sådan virker servoen:**

1. **PWM frekvens**: 50Hz er standard for servomotorer. Én periode = 20ms.

2. **Pulsbredde bestemmer vinkel:**
   - 0.5ms puls (2.5% duty) = 0° → Vindue lukket
   - 1.5ms puls (7.5% duty) = 90° → Vindue åbent
   - 2.5ms puls (12.5% duty) = 180° → Fuldt åbent

3. **Duty cycle formel**: `duty = (angle/180 * 10 + 2.5) * 1023/100`

4. **CoAP aktuation**: I stedet for at abonnere passivt (MQTT), eksponerer servoen to aktive endpoints Node-RED kan kalde. ESP32 bekræfter udførslen ved at svare med en JSON-pakke med resultatet.
