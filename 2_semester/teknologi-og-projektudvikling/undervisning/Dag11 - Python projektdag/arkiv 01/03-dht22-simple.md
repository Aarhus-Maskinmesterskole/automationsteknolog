# 📘 03 – DHT22 Sensor med ESP32 (MicroPython)

#### 🎯 Læringsmål

* Tilslutte en DHT22 sensor til ESP32
* Læse temperatur og fugtighed fra DHT22
* Bruge `dht`-modulet i MicroPython

---

### 🧰 Forberedelse

* Brug 3.3V (IKKE 5V) til DHT22
* Tilslut DHT22 data-pin til en GPIO-pin (f.eks. GPIO4)
* DHT22 har en indbygget modstand, så ingen ekstern modstand er nødvendig

---

### 🧪 Eksempel – Læsning fra DHT22

```python
import dht
from machine import Pin
from time import sleep

sensor = dht.DHT22(Pin(4))  # DHT-data til GPIO4

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temp:", temp, "°C", "Fugt:", hum, "%")
    sleep(2)
```

---

### ✅ Tjekliste

* [ ] Jeg har tilsluttet DHT22 korrekt
* [ ] Jeg har uploadet koden til ESP32
* [ ] Jeg ser temperatur og fugtighed printet i terminalen
* [ ] Jeg forstår hvordan `dht.DHT22` fungerer

---
