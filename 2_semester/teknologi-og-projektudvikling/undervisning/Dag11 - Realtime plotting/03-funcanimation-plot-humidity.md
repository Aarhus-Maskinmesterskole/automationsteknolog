# 03 – FuncAnimation: Live-plot luftfugtighed

Mål: Læs **luftfugtighed** fra ESP32 over USB/seriel og vis den i **real-time** med `matplotlib.animation.FuncAnimation(fig, update, init_func, interval)`.

## Forudsætninger

* Har kørt `01-setup-realtime-plot.md` (venv + `matplotlib`, `pyserial`).
* Kender din serielle port (fx `COM4` / `/dev/ttyUSB0` / `/dev/tty.usbserial-*`).

## ESP32 (MicroPython) – enkel luftfugtigheds-output

Udskriv **kun ét tal pr. linje** (%RH). Ingen ekstra tekst.

```python
# esp32/main.py
from machine import Pin
from dht import DHT22
import time

dht = DHT22(Pin(14))   # tilpas pin

while True:
    try:
        dht.measure()
        print(f"{dht.humidity():.1f}")  # fx 45.6
    except:
        pass
    time.sleep(1)
```

## PC (Python) – live-plot med FuncAnimation

```python
# python/hum_live_plot.py
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PORT = "COM4"          # Windows: COM3/COM4  | Linux: /dev/ttyUSB0  | macOS: /dev/tty.usbserial-*
BAUD = 115200
ser = serial.Serial(PORT, BAUD, timeout=1)

N = 200                # rullende vindue (seneste N punkter)
xs, ys = [], []

fig, ax = plt.subplots()
(line,) = ax.plot([], [], label="Humidity (%)")
ax.set_ylim(0, 100)    # %RH
ax.set_xlabel("Samples")
ax.set_ylabel("%")
ax.legend(loc="upper left")

def init():
    line.set_data([], [])
    return line,

def update(i):
    s = ser.readline().decode(errors="ignore").strip()  # forventer fx "45.6"
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

1. Kør ESP32-scriptet (MicroPython).
2. Sæt korrekt `PORT` i PC-scriptet.
3. Kør: `python hum_live_plot.py`.

> Note: `return line,` (med komma) er med vilje—`FuncAnimation` forventer en **iterabel** af artists at opdatere.
> Når det virker, kan du senere tilføje et rullende gennemsnit eller markere out-of-range værdier (fx <20 % eller >90 %).
