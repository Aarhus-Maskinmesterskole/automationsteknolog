# 🔌 01 – Opsætning af ESP32 med MicroPython og Thonny

Denne guide hjælper dig med at installere MicroPython på ESP32 og bruge Thonny som udviklingsmiljø. Målet er at sikre, at du kan flashe firmwaren korrekt og køre dit første script direkte på enheden.

---

## 🎯 Mål for modulet

* Installere Thonny og MicroPython firmware
* Flashe ESP32 med MicroPython
* Skrive og køre et simpelt script via Thonny

---

## 🧰 Krav

* USB-kabel (data, ikke kun strøm)
* ESP32 DevKit (f.eks. DOIT eller NodeMCU)
* Windows/macOS/Linux + internet

---

## 🛠️ Trin 1 – Installer Thonny

1. Gå til: [https://thonny.org](https://thonny.org)
2. Download og installer Thonny IDE
3. Start Thonny, og gå til **Værktøjer → Indstillinger → Interpreter**
4. Vælg:

   * **Interpreter**: MicroPython (ESP32)
   * **Port**: Den port hvor din ESP32 sidder (fx COM3, /dev/ttyUSB0)

---

## ⚙️ Trin 2 – Flash MicroPython firmware

1. Tilslut ESP32 via USB
2. Gå til **Værktøjer → Installer MicroPython-firmware**
3. Vælg:

   * **Board**: ESP32
   * Vælg nyeste firmware (eller angiv `.bin` manuelt)
   * Tryk på “Installer eller geninstaller”

> Hvis ESP32 ikke findes, prøv at holde `BOOT` nede mens du klikker "Installer"

---

## 💡 Trin 3 – Kør første script

1. Gå til editoren og indsæt:

```python
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
```

2. Tryk på **Kør** eller `Ctrl+R`
3. LED'en på ESP32 bør blinke

---

## ✅ Tjekliste

* [ ] Jeg har installeret Thonny
* [ ] Jeg har flashed MicroPython på ESP32
* [ ] Jeg kan vælge korrekt port og køre kode
* [ ] Jeg har blinket LED via `Pin` og `sleep`

---

> Du er nu klar til at bruge ESP32 som sensorplatform i MicroPython!
