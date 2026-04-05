# 02 – FuncAnimation: Live-plot temperatur

Mål: Læs **temperatur** fra ESP32 over USB/seriel og vis den i **real-time** med `matplotlib.animation.FuncAnimation`.

## Forudsætninger

* Du har fulgt `01-setup-realtime-plot.md` (venv + `matplotlib`, `pyserial`).
* Kender din serielle port (fx `COM4` / `/dev/ttyUSB0` / `/dev/tty.usbserial-*`).

## ESP32 (MicroPython) – enkel temperatur‐output

Udskriv **kun ét tal pr. linje** (°C). Ingen ekstra tekst.

```python
# esp32/main.py
from machine import Pin
from dht import DHT22
import time

dht = DHT22(Pin(14))   # tilpas pin

while True:
    try:
        dht.measure()
        print(f"{dht.temperature():.1f}")  # fx 23.4
    except:
        pass
    time.sleep(1)
```

## PC (Python) – live-plot med FuncAnimation

```python
# python/temp_live_plot.py
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PORT = "COM4"          # Windows: COM3/COM4  | Linux: /dev/ttyUSB0  | macOS: /dev/tty.usbserial-*
BAUD = 115200
ser = serial.Serial(PORT, BAUD, timeout=1)

N = 200                # rullende vindue (seneste N punkter)
xs, ys = [], []

fig, ax = plt.subplots()
(line,) = ax.plot([], [], label="Temp (°C)")
ax.set_ylim(0, 50)     # typisk rum-temp interval
ax.set_xlabel("Samples")
ax.set_ylabel("°C")
ax.legend(loc="upper left")

def init():
    line.set_data([], [])
    return line,

def update(i):
    s = ser.readline().decode(errors="ignore").strip()  # forventer fx "23.4"
    try:
        val = float(s)
        xs.append(i); ys.append(val)
        xs[:] = xs[-N:]; ys[:] = ys[-N:]
        line.set_data(xs, ys)
        ax.set_xlim(max(0, i - N), max(N, i))
    except ValueError:
        pass
    return line,

ani = FuncAnimation(fig, update, init_func=init, interval=200, blit=False)
plt.show()
```

## Kørsel

1. Flash/afvikl ESP32-scriptet.
2. Opdatér `PORT` i PC-scriptet.
3. Kør: `python temp_live_plot.py`.

> Note: `return line,` (med komma) er med vilje—`FuncAnimation` forventer en **iterabel** af artists at opdatere.
