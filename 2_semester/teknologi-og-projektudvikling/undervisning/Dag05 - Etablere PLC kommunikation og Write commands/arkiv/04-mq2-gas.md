### 📘 `04-mq2-gas.md` – MQ2 Gas Sensor med ESP32 (MicroPython)

#### 🎯 Læringsmål

* Tilslutte en MQ2 gas sensor til ESP32
* Kalibrere MQ2 i ren luft
* Læse analoge værdier og beregne PPM ved hjælp af formel
* Bruge `ADC` til analog læsning

---

### 🧰 Forberedelse

* Brug 3.3V (IKKE 5V) til MQ2
* Tilslut MQ2 analog out til en GPIO-pin (f.eks. GPIO34)
* MQ2 har en indbygget load resistor, så ingen ekstern modstand er nødvendig

---

### 🧪 Kalibrering af MQ2

Før brug skal MQ2 kalibreres i ren luft for at finde Ro (sensor modstand i ren luft).

```python
from machine import ADC, Pin
from time import sleep
import math

gas = ADC(Pin(34))
gas.atten(ADC.ATTN_11DB)

# Kalibrer i ren luft (lad sensoren varme op i 1-2 minutter)
print("Kalibrerer MQ2 i ren luft...")
sleep(120)  # Vent 2 minutter

analog_clean = gas.read()
Rs_clean = (4095 - analog_clean) / analog_clean * 1000  # RL = 1kΩ
Ro = Rs_clean / 9.8  # For MQ2 i ren luft (ca. værdi)

print("Ro:", Ro)
```

---

### 🧪 Eksempel – Læsning og beregning af PPM

Efter kalibrering kan du beregne PPM for f.eks. LPG.

```python
# Brug Ro fra kalibrering
Ro = 10000  # Erstat med din Ro værdi

while True:
    analog = gas.read()
    Rs = (4095 - analog) / analog * 1000  # RL = 1kΩ
    ratio = Rs / Ro
    
    # Formel for LPG: PPM = 10^((log10(Rs/Ro) - 0.5) / 0.3)
    if ratio > 0:
        ppm = 10 ** ((math.log10(ratio) - 0.5) / 0.3)
        print("Gas værdi:", analog, "PPM:", round(ppm, 2))
    else:
        print("Ugyldig måling")
    
    sleep(1)
```

---

### ✅ Tjekliste

* [ ] Jeg har kalibreret MQ2 i ren luft
* [ ] Jeg har noteret Ro værdien
* [ ] Jeg har uploadet koden med formlen
* [ ] Jeg ser PPM værdier printet i terminalen
* [ ] Jeg forstår hvordan Rs og PPM beregnes

---
