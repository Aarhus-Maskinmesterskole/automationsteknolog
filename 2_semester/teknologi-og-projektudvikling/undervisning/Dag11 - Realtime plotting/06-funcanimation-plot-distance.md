# 06 – FuncAnimation: Live-plot distance (bar-plot)

Mål: Læs **afstand** fra ESP32 over USB/seriel og vis **én aktuel værdi** som en vandret **bar** i real-time med
`matplotlib.animation.FuncAnimation(fig, update, init_func, interval)`.

## Forudsætninger

* `01-setup-realtime-plot.md` (venv + `matplotlib`, `pyserial`) er kørt.
* Kender din serielle port (`COM4` / `/dev/ttyUSB0` / `/dev/tty.usbserial-*`).
* Afstandssensor, fx **HC-SR04** (ultralyd).

## ESP32 (MicroPython) – enkel distance‐output (HC-SR04)

Udskriv **kun ét tal pr. linje** (cm). Ingen ekstra tekst.

```python
# esp32/main.py
from machine import Pin, time_pulse_us
import time

TRIG = Pin(5, Pin.OUT)                 # tilpas pins efter din wiring
ECHO = Pin(18, Pin.IN, Pin.PULL_DOWN)

def distance_cm():
    TRIG.off(); time.sleep_us(2)
    TRIG.on();  time.sleep_us(10); TRIG.off()
    t = time_pulse_us(ECHO, 1, 30000)  # vent på HIGH, timeout 30 ms (~5 m)
    if t < 0:
        return None
    # lydhastighed ~0.0343 cm/µs, frem-og-tilbage => del med 2
    return (t * 0.0343) / 2

while True:
    d = distance_cm()
    if d is not None:
        print(f"{d:.1f}")             # fx "123.4"
    time.sleep_ms(100)                 # ~10 Hz
```

## PC (Python) – bar-plot med FuncAnimation

```python
# python/distance_bar_live.py
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Vælg port:
# Windows: 'COM3'/'COM4' | Linux: '/dev/ttyUSB0' | macOS: '/dev/tty.usbserial-*'
PORT = "COM4"
BAUD = 115200
ser = serial.Serial(PORT, BAUD, timeout=1)

MAX = 200  # cm – akse/skalering (tilpas til dit setup)

fig, ax = plt.subplots(figsize=(6, 1.4))
bars = ax.barh(["distance"], [0])
bar = bars.patches[0]

ax.set_xlim(0, MAX)
ax.set_yticks([])                # gem label hvis du vil
ax.set_xlabel("cm")
txt = ax.text(MAX, 0, "0.0 cm", va="center", ha="right")

def init():
    bar.set_width(0)
    txt.set_text("0.0 cm")
    return bar, txt

def update(_):
    s = ser.readline().decode(errors="ignore").strip()   # forventer fx "123.4"
    if not s:
        return bar, txt
    try:
        d = float(s)
        # klip til skala og opdater bar + tekst
        d = max(0.0, min(d, float(MAX)))
        bar.set_width(d)
        # valgfri farvegradation grøn→rød efter afstand:
        bar.set_color(plt.cm.RdYlGn_r(d / MAX))
        txt.set_text(f"{d:.1f} cm")
    except ValueError:
        pass
    return bar, txt

ani = FuncAnimation(fig, update, init_func=init, interval=100, blit=False)
plt.tight_layout()
plt.show()
```

## Kørsel

1. Kør ESP32-scriptet (MicroPython).
2. Indstil `PORT` i PC-scriptet.
3. `python distance_bar_live.py`.

> Tip: Vil du også se **historik**, så lav et 2×1-subplot: bar-plot øverst og en linjegraf nederst af de seneste $N$ målinger. Bar-plottet holder fokus på **nu**-værdien, linjen viser udviklingen.
