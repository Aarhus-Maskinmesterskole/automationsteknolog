import os

folder = r'c:\Users\aso\Documents\Github\aams\automationsteknolog\3_semester\iot\undervisning\Dag07 - CoAP opgaver\01 - IoT House'

files = {
"01-esp32-dht11.md": """# 🌡️ Opgave 01 – Del DHT11 Data via CoAP

I denne opgave skal du programmere ESP32 til at læse data fra en DHT11 temperatursensor og gøre den tilgængelig via en CoAP server.

![alt text](image.png)

## 🎯 Formål

Lær at:
- Læse temperatur og fugtighed fra DHT11
- Forbinde til WiFi fra ESP32
- Dele sensordata via CoAP GET anmodninger

---

## 💡 Python-kode

Opret en ny fil i Thonny og skriv følgende:

```python
# ESP32 + DHT11 CoAP Server
# Gør temperatur og fugtighed tilgængelig via CoAP

import machine
import dht
from coapmini import wifi_connect, CoapServer

# ===== KONFIGURATION =====
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
DHT_PIN = 4  # GPIO 4
# =========================

sensor = dht.DHT11(machine.Pin(DHT_PIN))

def read_dht():
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f'Målt: {temp}°C, {hum}%')
        return {"temperatur": temp, "fugtighed": hum}
    except OSError as e:
        return {"error": "Kunne ikke læse sensor"}

def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    srv = CoapServer()
    srv.add("/dht", read_dht)
    srv.serve_forever("Klar! Hent data med GET coap://<IP>:5683/dht")

if __name__ == '__main__':
    main()
```

### Sådan tester du
Vælg en **coap request** node i Node-RED, sæt den til `GET` og url til `coap://<din-ip>:5683/dht`. Forbind en inject-node foran, og en debug-node bagefter!
""",

"02-esp32-pir-sensor.md": """# 🚶 Opgave 02 – Del PIR Bevægelsesdata via CoAP

I denne opgave skal du programmere ESP32 til at gøre data fra en PIR bevægelsessensor tilgængelig via en CoAP endpoint.

![alt text](image-1.png)

## 🎯 Formål
Lær at aflæse digitalt input (bevægelse) og udstille det på CoAP.

---

## 💡 Python-kode

```python
from machine import Pin
from coapmini import wifi_connect, CoapServer

WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
PIR_PIN = 14  # GPIO 14

pir = Pin(PIR_PIN, Pin.IN)

def read_pir():
    bevægelse = pir.value() == 1
    return {"bevægelse": bevægelse}

def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    srv = CoapServer()
    srv.add("/pir", read_pir)
    srv.serve_forever("Klar! Hent data med GET coap://<IP>:5683/pir")

if __name__ == '__main__':
    main()
```

### Sådan tester du
Brug Node-RED's CoAP node til at pege på `/pir`. Sæt din inject-node til at hente dataen hvert 1. sekund, så du kan se bevægelses-opdateringer live!
""",

"03-esp32-fan-control.md": """# 🌀 Opgave 03 – Styr Blæser med ESP32 via CoAP

I denne opgave skal du programmere ESP32 til at eksponere CoAP-endpoints, som f.eks. `/fan/on` og `/fan/off`, så du kan styre en blæser udefra.

![alt text](image-2.png)

## 🎯 Formål
Lær at lytte efter eksterne CoAP kald for at aktivere fysisk hardware.

---

## 💡 Python-kode

```python
from machine import Pin
from coapmini import wifi_connect, CoapServer

WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
FAN_PIN1 = 18
FAN_PIN2 = 19

fan_pin1 = Pin(FAN_PIN1, Pin.OUT, value=0)
fan_pin2 = Pin(FAN_PIN2, Pin.OUT, value=0)
tilstand = "OFF"

def fan_on():
    global tilstand
    fan_pin1.value(1); fan_pin2.value(0)
    tilstand = "ON"
    print('🌀 Blæser: ON')
    return {"fan": tilstand}

def fan_off():
    global tilstand
    fan_pin1.value(0); fan_pin2.value(0)
    tilstand = "OFF"
    print('🌀 Blæser: OFF')
    return {"fan": tilstand}

def fan_status():
    return {"fan": tilstand}

def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    srv = CoapServer()
    srv.add("/fan/on", fan_on)
    srv.add("/fan/off", fan_off)
    srv.add("/fan", fan_status)
    srv.serve_forever("Klar! Brug GET /fan/on eller GET /fan/off")

if __name__ == '__main__':
    main()
```

### Sådan tester du
Kald `/fan/on` fra Node-RED via en CoAP GET-node. Blæseren starter, og du får et JSON-svar tilbage om at `fan = ON`.
""",

"04-esp32-button.md": """# 🔘 Opgave 04 – Del Knaptryk via CoAP

Vis om en fysisk knap er trykket nede via en CoAP GET anmodning.

![alt text](image-3.png)

## 💡 Python-kode

```python
from machine import Pin
from coapmini import wifi_connect, CoapServer

WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
BUTTON_PIN = 12

# Definer knap med intern Pull-Up modstand (0 = trykket ned)
btn = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

def read_button():
    trykket = (btn.value() == 0)
    return {"knap_trykket": trykket}

def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    srv = CoapServer()
    srv.add("/knap", read_button)
    srv.serve_forever("Klar! Hent status med GET /knap")

if __name__ == '__main__':
    main()
```
""",

"05-esp32-window-servo.md": """# 🪟 Opgave 05 – Servo Motor (Vindue) via CoAP

Styr en simulering af et vindue, der laves ved hjælp af en lille Servo motor.

![alt text](image-4.png)

## 💡 Python-kode

```python
from machine import Pin, PWM
from coapmini import wifi_connect, CoapServer

WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
SERVO_PIN = 15

servo = PWM(Pin(SERVO_PIN), freq=50)
vindue_tilstand = "lukket"

def set_angle(angle):
    duty = int(((angle / 180) * 102) + 26)  # Omregning: angle -> duty cycle
    servo.duty(duty)

def aaben_vindue():
    global vindue_tilstand
    set_angle(90)
    vindue_tilstand = "aabent"
    return {"vindue": vindue_tilstand}

def luk_vindue():
    global vindue_tilstand
    set_angle(0)
    vindue_tilstand = "lukket"
    return {"vindue": vindue_tilstand}

def status():
    return {"vindue": vindue_tilstand}

def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    srv = CoapServer()
    srv.add("/vindue/aaben", aaben_vindue)
    srv.add("/vindue/luk", luk_vindue)
    srv.add("/vindue", status)
    srv.serve_forever("Klar! Brug GET /vindue/aaben eller /vindue/luk")

if __name__ == '__main__':
    main()
```
""",

"06-esp32-door-servo.md": """# 🚪 Opgave 06 – Servo Motor (Dør) via CoAP

Ligesom det smarte vindue, skal vi nu lave en dør der kan åbne af sig selv via CoAP endpoints.

![alt text](image-6.png)

## 💡 Python-kode

```python
from machine import Pin, PWM
from coapmini import wifi_connect, CoapServer

WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
SERVO_PIN = 13

servo = PWM(Pin(SERVO_PIN), freq=50)

def aaben_doer():
    servo.duty(128) # Ca 90 grader
    return {"doer": "aaben"}

def luk_doer():
    servo.duty(26)  # Ca 0 grader
    return {"doer": "lukket"}

def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    srv = CoapServer()
    srv.add("/doer/aaben", aaben_doer)
    srv.add("/doer/luk", luk_doer)
    srv.serve_forever("Klar! Brug GET /doer/aaben eller /doer/luk")

if __name__ == '__main__':
    main()
```
""",

"07-esp32-yellow-led.md": """# 💡 Opgave 07 – Styr LED (Lys) via CoAP

Simulering af en stuelampe styret via ESP32 over CoAP-protokollen.

![alt text](image-7.png)

## 💡 Python-kode

```python
from machine import Pin
from coapmini import wifi_connect, CoapServer

WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
LED_PIN = 2

led = Pin(LED_PIN, Pin.OUT, value=0)

def light_on():
    led.value(1)
    return {"lys": "ON"}

def light_off():
    led.value(0)
    return {"lys": "OFF"}

def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    srv = CoapServer()
    srv.add("/lys/on", light_on)
    srv.add("/lys/off", light_off)
    srv.serve_forever("Klar! Brug GET /lys/on eller /lys/off")

if __name__ == '__main__':
    main()
```
""",

"08-esp32-rgb-led.md": """# 🔴🟢 Opgave 08 – Styr RGB LED (Smart Light)

Brug CoAP til at vælge farven på en RGB LED-pære. Da ren GET ikke sender avanceret variabel-data med, laver vi endpoints for hver farve i denne super simple version.

![alt text](image-8.png)

## 💡 Python-kode

```python
from machine import Pin
from coapmini import wifi_connect, CoapServer

WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
PIN_R, PIN_G, PIN_B = 27, 26, 25

r = Pin(PIN_R, Pin.OUT, value=0)
g = Pin(PIN_G, Pin.OUT, value=0)
b = Pin(PIN_B, Pin.OUT, value=0)

def off():
    r.value(0); g.value(0); b.value(0); return {"color": "OFF"}
def red():
    r.value(1); g.value(0); b.value(0); return {"color": "RED"}
def green():
    r.value(0); g.value(1); b.value(0); return {"color": "GREEN"}
def blue():
    r.value(0); g.value(0); b.value(1); return {"color": "BLUE"}

def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    srv = CoapServer()
    srv.add("/rgb/off", off)
    srv.add("/rgb/red", red)
    srv.add("/rgb/green", green)
    srv.add("/rgb/blue", blue)
    srv.serve_forever("Klar! Brug GET /rgb/red, /rgb/green osv.")

if __name__ == '__main__':
    main()
```
""",

"09-esp32-lcd-display.md": """# 📟 Opgave 09 – LCD 1602 Display (Prædefineret besked)

Displays kan bruges til at vise beskeder om husets tilstand. Da CoAP GET (i vores mini version) kalder dedikerede funktioner på specifikke URL'er, styrer vi her forskellige præ-programmerede velkomster.

![alt text](image-9.png)

## 💡 Python-kode

(Husk at dit LCD i2c bibliotek `lcd1602.py` eller lignende også skal ligge på ESP32'en).

```python
from machine import Pin, I2C
from coapmini import wifi_connect, CoapServer
# Forudsætter du har en lokal kopi af LCD biblioteket!
# from lcd1602 import LCD1602  

WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
I2C_SDA, I2C_SCL = 21, 22

def main():
    # wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    # i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=100000)
    # lcd = LCD1602(i2c, 0x27)
    # lcd.clear()

    # --- PSEUDO KODE SOM EKSEMPEL --- #
    def welcome():
        # lcd.display("Velkommen", "Mit Smarte Hjem")
        print("LCD: Velkommen Mit Smarte Hjem")
        return {"lcd": "velkommen vist"}
        
    def alert():
        # lcd.display("ALARM!", "BEVAEGELSE FUNDET")
        print("LCD: ALARM! BEVAEGELSE FUNDET")
        return {"lcd": "alarm vist"}
        
    def clear():
        # lcd.clear()
        print("LCD ryddet")
        return {"lcd": "ryddet"}

    srv = CoapServer()
    srv.add("/lcd/welcome", welcome)
    srv.add("/lcd/alert", alert)
    srv.add("/lcd/clear", clear)
    
    # Kør server!
    srv.serve_forever("Klar! Brug GET /lcd/welcome osv.")

if __name__ == '__main__':
    main()
```
"""
}

# Overskriv alle filer
for filename, content in files.items():
    path = os.path.join(folder, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Opdateret: {filename}")
