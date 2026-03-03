# 📟 Opgave 09 – LCD 1602 Display med ESP32 og CoAP

I denne opgave skal du programmere ESP32 til at **modtage** CoAP-kommandoer og vise tekst på et LCD 1602 display. Displayet har 16 karakterer x 2 linjer og kommunikerer via I2C.

![alt text](image-9.png)

## 🎯 Formål

Lær at:
- Styre et I2C LCD display fra ESP32
- Modtage CoAP GET anmodninger og vise foruddefinerede beskeder
- Arbejde med I2C kommunikation (SDA/SCL)
- Formatere tekst til LCD (16x2 karakterer)

---

## 💡 Python-kode

Opret en ny fil i Thonny og skriv følgende:

```python
# ESP32 CoAP Server - LCD 1602 Display
# Viser tekst på LCD via CoAP endpoints

import network
import time
from machine import Pin, I2C
from coapmini import CoapServer

# ===== KONFIGURATION =====
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"

# I2C pins (ESP32 standard)
I2C_SDA = 21   # GPIO 21
I2C_SCL = 22   # GPIO 22
I2C_ADDR = 0x27  # I2C adresse (0x27 eller 0x3F)
# =========================


# LCD 1602 I2C driver (grundlæggende implementering)
class LCD1602:
    def __init__(self, i2c, addr=0x27):
        self.i2c = i2c
        self.addr = addr
        self.backlight = 0x08
        time.sleep_ms(20)
        self._write(0x03)
        self._write(0x03)
        self._write(0x03)
        self._write(0x02)
        self._write(0x28)  # 2 linjer, 5x8 dots
        self._write(0x0C)  # Display on, cursor off
        self._write(0x06)  # Entry mode
        self.clear()

    def _write_nibble(self, data):
        self.i2c.writeto(self.addr, bytearray([data | self.backlight]))
        time.sleep_us(1)
        self.i2c.writeto(self.addr, bytearray([data | 0x04 | self.backlight]))
        time.sleep_us(1)
        self.i2c.writeto(self.addr, bytearray([data | self.backlight]))
        time.sleep_us(50)

    def _write(self, data, mode=0):
        self._write_nibble((data & 0xF0) | mode)
        self._write_nibble(((data << 4) & 0xF0) | mode)

    def clear(self):
        """Ryd display"""
        self._write(0x01)
        time.sleep_ms(2)

    def set_cursor(self, col, row):
        """Flyt cursor til position (col, row)"""
        addr = 0x80 + (0x40 * row) + col
        self._write(addr)

    def print(self, text):
        """Udskriv tekst på nuværende cursor position"""
        for char in text:
            self._write(ord(char), 0x01)

    def display(self, line1="", line2=""):
        """Vis tekst på linje 1 og 2 (max 16 karakterer hver)"""
        self.clear()
        self.set_cursor(0, 0)
        self.print(line1[:16])
        self.set_cursor(0, 1)
        self.print(line2[:16])


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


# Globalt LCD-objekt (sættes i main())
lcd = None

# Én funktion per CoAP endpoint – viser en foruddefineret besked
def show_welcome():
    lcd.display("Velkommen!", "ESP32 CoAP")
    print("LCD: Velkommen! / ESP32 CoAP")
    return {"linje1": "Velkommen!", "linje2": "ESP32 CoAP"}

def show_temp():
    lcd.display("Temperatur:", "Maaler...")
    print("LCD: Temperatur: / Maaler...")
    return {"linje1": "Temperatur:", "linje2": "Maaler..."}

def show_status():
    lcd.display("System OK", "Alt virker!")
    print("LCD: System OK / Alt virker!")
    return {"linje1": "System OK", "linje2": "Alt virker!"}

def show_clear():
    lcd.clear()
    print("LCD: ryddet")
    return {"linje1": "", "linje2": ""}


def main():
    ip = wifi_connect(WIFI_SSID, WIFI_PASSWORD)

    # Opsæt I2C og LCD
    print("Initialiserer LCD...")
    i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=100000)

    devices = i2c.scan()
    if devices:
        print(f"I2C enheder fundet: {[hex(d) for d in devices]}")
    else:
        print("Ingen I2C enheder fundet! Tjek forbindelser.")
        return

    global lcd
    lcd = LCD1602(i2c, I2C_ADDR)
    print("LCD initialiseret!")

    # Velkomstbesked ved opstart
    lcd.display("ESP32 Klar", f"{ip}")

    srv = CoapServer()
    srv.add("/lcd/welcome", show_welcome)
    srv.add("/lcd/temp",    show_temp)
    srv.add("/lcd/status",  show_status)
    srv.add("/lcd/clear",   show_clear)
    srv.serve_forever(
        f"Klar! LCD endpoints:\n"
        f"  GET coap://{ip}:5683/lcd/welcome\n"
        f"  GET coap://{ip}:5683/lcd/temp\n"
        f"  GET coap://{ip}:5683/lcd/status\n"
        f"  GET coap://{ip}:5683/lcd/clear"
    )

if __name__ == '__main__':
    main()
```

### Konfigurér og kør

1. **Rediger følgende i koden:**
   - `WIFI_SSID` → Dit WiFi-navn
   - `WIFI_PASSWORD` → Dit WiFi-password
   - `I2C_ADDR` → Tjek I2C adresse (0x27 eller 0x3F)

2. **Husk `coapmini.py`:**
   Sørg for at du også har uploadet biblioteket `coapmini.py` til roden af din ESP32.

3. **Kør programmet:**
   - Gem filen som `main.py`
   - Tryk **F5**
   - Notér den IP-adresse, der udskrives i Shell-vinduet.

**Forventet output:**
```
Forbinder til WiFi...
Forbundet! IP Adresse: 192.168.1.123
Initialiserer LCD...
I2C enheder fundet: ['0x27']
LCD initialiseret!
Klar! LCD endpoints:
  GET coap://192.168.1.123:5683/lcd/welcome
  GET coap://192.168.1.123:5683/lcd/temp
  GET coap://192.168.1.123:5683/lcd/status
  GET coap://192.168.1.123:5683/lcd/clear
```

---

## 🧪 Test systemet

### Metode 1: Node-RED

**Opret flow med knapper til hvert endpoint:**

1. Opret 4 **CoAP Request** nodes (én per endpoint), alle med Method = `GET`.
2. Sæt URL'erne til:
   - `coap://<ip>:5683/lcd/welcome`
   - `coap://<ip>:5683/lcd/temp`
   - `coap://<ip>:5683/lcd/status`
   - `coap://<ip>:5683/lcd/clear`
3. Sæt en **inject**-node foran hver.
4. Sæt en **debug**-node bagved for at se JSON-svaret.

**Eksempel – kombiner med DHT11 (opgave 01):**
```
[DHT11 CoAP Response] → [function: format til LCD] → [CoAP Request: /lcd/temp]
```

---

## 📝 Forklaring

**Sådan virker LCD 1602 I2C:**

1. **I2C kommunikation**:
   - **SDA** (Serial Data) = GPIO 21 – Data linje
   - **SCL** (Serial Clock) = GPIO 22 – Clock linje
   - **Adresse**: Hver I2C enhed har en unik adresse (typisk 0x27 eller 0x3F)
   - I2C kan forbinde mange enheder på de samme 2 ledninger

2. **LCD display**:
   - **16x2** = 16 karakterer bredt, 2 linjer højt
   - Hver karakter er 5x8 pixels
   - HD44780 controller (standard for LCD 1602)

3. **Display opdatering**:
   - `clear()` – Sletter hele displayet
   - `set_cursor(col, row)` – Flytter cursor til position
   - `print(text)` – Skriver tekst fra cursor position
   - `display(line1, line2)` – Rydder og viser 2 linjer

4. **Koap vs MQTT – LCD er en aktuator**:
   - MQTT: Displayet *abonnerer* på et topic og viser alt der sendes til det
   - CoAP: Displayet *lytter* på faste endpoints – hvert endpoint udløser en bestemt besked
   - Fordelen ved CoAP: Displayet behøver ikke forbinde til en broker; Node-RED initierer kommunikationen

**I2C scanning:**
Programmet scanner automatisk for I2C enheder ved opstart.
Hvis LCD ikke findes – tjek SDA/SCL forbindelser, VCC og GND, og prøv anden adresse.

```python
# Kør i REPL for at finde adresse:
from machine import Pin, I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
print([hex(d) for d in i2c.scan()])
```