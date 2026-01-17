# 📘 06 – PIR Sensor med ESP32 (MicroPython)

#### 🎯 Læringsmål

* Tilslutte en PIR (Passive Infrared) sensor til ESP32
* Registrere bevægelse med PIR
* Bruge `machine.Pin` til digital læsning

---

### 🧰 Forberedelse

* Brug 3.3V (IKKE 5V) til PIR
* Tilslut PIR signal-pin til en GPIO-pin (f.eks. GPIO19)
* PIR output er digital (HIGH ved bevægelse, LOW ellers)

---

### 🧪 Eksempel – Læsning fra PIR

```python
from machine import Pin
from time import sleep

pir = Pin(19, Pin.IN)  # PIR til GPIO19

while True:
    if pir.value():
        print("Bevægelse registreret!")
    else:
        print("Ingen bevægelse")
    sleep(0.5)
```

---

### ✅ Tjekliste

* [ ] Jeg har tilsluttet PIR korrekt
* [ ] Jeg har uploadet koden til ESP32
* [ ] Jeg ser bevægelsesdetektion printet i terminalen
* [ ] Jeg forstår hvordan `Pin.value()` fungerer

---
