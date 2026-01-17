### 📘 `05-ldr.md` – LDR Sensor med ESP32 (MicroPython)

#### 🎯 Læringsmål

* Tilslutte en LDR (Light Dependent Resistor) til ESP32
* Læse analoge værdier fra LDR
* Bruge `ADC` til analog læsning

---

### 🧰 Forberedelse

* Brug 3.3V (IKKE 5V) til LDR
* Tilslut LDR i serie med en modstand (f.eks. 10kΩ) til en GPIO-pin (f.eks. GPIO35)
* Tilslut den ene ende af LDR til 3.3V, den anden ende til modstanden og GPIO

---

### 🧪 Eksempel – Læsning fra LDR

```python
from machine import ADC, Pin
from time import sleep

ldr = ADC(Pin(35))  # LDR til GPIO35
ldr.atten(ADC.ATTN_11DB)  # Spændingsområde 0–3.3V

while True:
    lux = ldr.read()
    print("LDR værdi:", lux)
    sleep(1)
```

---

### ✅ Tjekliste

* [ ] Jeg har tilsluttet LDR korrekt i serie med modstand
* [ ] Jeg har uploadet koden til ESP32
* [ ] Jeg ser LDR værdier printet i terminalen
* [ ] Jeg forstår hvordan `ADC.read()` fungerer

---
