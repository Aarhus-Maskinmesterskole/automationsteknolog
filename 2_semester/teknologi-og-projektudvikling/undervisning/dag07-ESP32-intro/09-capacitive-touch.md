### 📘 `09-capacitive-touch.md` – Kapacitiv Touch Sensor med ESP32-WROOM-32 (MicroPython)

#### 🎯 Læringsmål

* Bruge ESP32's indbyggede kapacitive touch pins
* Registrere berøring uden eksterne komponenter
* Bruge `machine.TouchPad` til touch sensing

---

### 🧰 Forberedelse

* ESP32-modellen vi bruger er ESP32-WROOM-32
* Brug en kapacitiv touch pin (f.eks. GPIO4, GPIO0, GPIO2, GPIO15, GPIO13, GPIO12, GPIO14, GPIO27, GPIO33, GPIO32)
* Ingen eksterne komponenter nødvendig – touch fungerer på ledningen/pinnen
* Touch værdi falder når der berøres

---

### 🧪 Eksempel – Læsning fra Kapacitiv Touch

```python
from machine import TouchPad, Pin
from time import sleep

touch = TouchPad(Pin(4))  # Touch pin GPIO4

while True:
    value = touch.read()
    print("Touch værdi:", value)
    
    if value < 500:  # Juster threshold efter behov
        print("Berørt!")
    else:
        print("Ikke berørt")
    
    sleep(0.5)
```

---

### ✅ Tjekliste

* [ ] Jeg har valgt en gyldig touch pin (GPIO4, GPIO0, etc.)
* [ ] Jeg har uploadet koden til ESP32
* [ ] Jeg ser touch værdier printet i terminalen
* [ ] Jeg forstår hvordan `TouchPad.read()` fungerer
* [ ] Jeg har justeret threshold for pålidelig detektion

---
