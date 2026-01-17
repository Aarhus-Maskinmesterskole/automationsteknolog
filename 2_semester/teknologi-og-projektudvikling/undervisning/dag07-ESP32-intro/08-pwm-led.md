### 📘 `08-pwm-led.md` – PWM Styring af LED med ESP32-WROOM-32 (MicroPython)

#### 🎯 Læringsmål

* Tilslutte en LED til ESP32-WROOM-32
* Styre LED lysstyrke med PWM (Pulse Width Modulation)
* Bruge `machine.PWM` til analog output

---

### 🧰 Forberedelse

* ESP32-modellen vi bruger er ESP32-WROOM-32
* Tilslut LED anode (+) til GPIO2 via en modstand (f.eks. 220Ω)
* Tilslut LED katode (-) til GND
* Brug 3.3V fra ESP32 – LED'en kan godt holde til det med modstand
* PWM giver analog effekt via digital pin

---

### 🧪 Eksempel – PWM Styring af LED

```python
from machine import Pin, PWM
from time import sleep

led = PWM(Pin(2), freq=1000)  # LED til GPIO2, frekvens 1kHz

while True:
    # Fade op
    for duty in range(0, 1024, 50):
        led.duty(duty)
        sleep(0.1)
    
    # Fade ned
    for duty in range(1023, -1, -50):
        led.duty(duty)
        sleep(0.1)
```

---

### ✅ Tjekliste

* [ ] Jeg har tilsluttet LED korrekt med modstand
* [ ] Jeg har uploadet koden til ESP32
* [ ] Jeg ser LED'en fade op og ned
* [ ] Jeg forstår hvordan `PWM.duty()` fungerer

---
