# 📘 07 – Distance Sensor (HC-SR04) med ESP32 (MicroPython)

#### 🎯 Læringsmål

* Tilslutte en HC-SR04 ultrasonic distance sensor til ESP32
* Måle afstand ved hjælp af ultralyd
* Bruge `machine.Pin` og `time.ticks_us` til timing

---

### 🧰 Forberedelse

* Brug 5V til HC-SR04 (VCC og GND)
* Tilslut HC-SR04 Trig til GPIO5 (output)
* Tilslut HC-SR04 Echo til GPIO18 (input)
* HC-SR04 måler afstand i cm

---

### 🧪 Eksempel – Måling af afstand med HC-SR04

```python
from machine import Pin
from time import sleep_us, sleep
import time

trigger = Pin(5, Pin.OUT)  # Trig til GPIO5
echo = Pin(18, Pin.IN)     # Echo til GPIO18

def measure_distance():
    # Send trigger pulse
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(10)
    trigger.low()
    
    # Wait for echo start
    while echo.value() == 0:
        pass
    start = time.ticks_us()
    
    # Wait for echo end
    while echo.value() == 1:
        pass
    end = time.ticks_us()
    
    # Calculate distance
    duration = time.ticks_diff(end, start)
    distance = (duration * 0.0343) / 2  # Speed of sound 343 m/s
    return distance

while True:
    dist = measure_distance()
    print("Afstand:", round(dist, 2), "cm")
    sleep(1)
```

---

### ✅ Tjekliste

* [ ] Jeg har tilsluttet HC-SR04 korrekt (Trig og Echo)
* [ ] Jeg har uploadet koden til ESP32
* [ ] Jeg ser afstandsmålinger printet i terminalen
* [ ] Jeg forstår hvordan ultralyd timing fungerer

---
