# 05 – FuncAnimation: Live-plot gas (MQ2)

Mål: Læs **MQ2** (gas) fra ESP32 over USB/seriel og vis værdien i **real-time** med `matplotlib.animation.FuncAnimation(fig, update, init_func, interval)`.

> MQ2 er en analog sensor. Vi læser rå ADC-tal (0–4095). Kort opvarmning anbefales, men til workshoppen kan du godt begynde at læse med det samme — værdierne stabiliserer sig efter lidt tid.

## Forudsætninger

* Har kørt `01-setup-realtime-plot.md` (venv + `matplotlib`, `pyserial`).
* Kender din serielle port (fx `COM4` / `/dev/ttyUSB0` / `/dev/tty.usbserial-*`).

## ESP32 (MicroPython) – enkel MQ2-output

Udskriv **kun ét tal pr. linje** (ADC 0–4095). Ingen ekstra tekst.

```python
# esp32/main.py
from machine import Pin, ADC
import time

mq2 = ADC(Pin(35))             # tilpas pin hvis nødvendigt (fx 34/35/36/39)
mq2.atten(ADC.ATTN_11DB)       # ~0–3.3V område
mq2.width(ADC.WIDTH_12BIT)     # 0..4095

# kort "warm-up" (valgfrit)
for _ in range(10):
    _ = mq2.read()
    time.sleep_ms(100)

while True:
    try:
        val = mq2.read()       # int 0..4095
        print(val)             # KUN tal, én linje pr. måling
    except:
        pass
    time.sleep_ms(200)         # ~5 Hz
```

## PC (Python) – live-plot med FuncAnimation

```python
# python/gas_live_plot.py
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PORT = "COM4"          # Windows: COM3/COM4  | Linux: /dev/ttyUSB0  | macOS: /dev/tty.usbserial-*
BAUD = 115200
ser = serial.Serial(PORT, BAUD, timeout=1)

N = 200                # rullende vindue (seneste N punkter)
xs, ys = [], []

fig, ax = plt.subplots()
(line,) = ax.plot([], [], label="MQ2 (ADC)")
ax.set_ylim(0, 4095)   # 12-bit ADC-range
ax.set_xlabel("Samples")
ax.set_ylabel("ADC værdi")
ax.legend(loc="upper left")

def init():
    line.set_data([], [])
    return line,

def update(i):
    s = ser.readline().decode(errors="ignore").strip()  # forventer fx "1234"
    if not s:
        return line,
    try:
        v = int(float(s))           # håndtér både heltal og evt. float-output
        v = max(0, min(4095, v))    # klip til skala
        xs.append(i); ys.append(v)
        xs[:] = xs[-N:]; ys[:] = ys[-N:]
        line.set_data(xs, ys)
        ax.set_xlim(max(0, i - N), max(N, i))
    except ValueError:
        pass
    return line,

ani = FuncAnimation(fig, update, init_func=init, interval=100, blit=False)
plt.show()
```

## Kørsel

1. Kør ESP32-scriptet (MicroPython).
2. Sæt korrekt `PORT` i PC-scriptet.
3. Kør: `python gas_live_plot.py`.

> Note: Vi viser rå ADC-tal for enkelhed. Konvertering til ppm kræver kalibrering af MQ2 (R0/Rs) og afhænger af forsyning, belastningsmodstand og sensorens “burn-in”. For workshoppen er live-kurven af råværdier rigeligt.
