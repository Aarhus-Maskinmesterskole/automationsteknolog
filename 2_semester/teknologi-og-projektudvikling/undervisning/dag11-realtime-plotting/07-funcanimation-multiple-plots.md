# 07 – FuncAnimation: Flere sensorer i ét plot (med legend)

Mål: Læs flere sensorer fra ESP32 over USB/seriel og vis dem **på samme akse** som flere linjer med **legend**. For at dele skalaen nemt skalerer vi ADC-værdier (LDR/MQ2) til **0–100 %**.

## Forudsætninger

* `01-setup-realtime-plot.md` (venv + `matplotlib`, `pyserial`) er kørt.
* Kender din serielle port (`COM4` / `/dev/ttyUSB0` / `/dev/tty.usbserial-*`).
* ESP32 sender **CSV-linje** pr. måling: `temp,hum,ldr,gas`

## ESP32 (MicroPython) – print alle 4 værdier som CSV

```python
# esp32/main.py
from machine import Pin, ADC
from dht import DHT22
import time

dht = DHT22(Pin(14))
ldr = ADC(Pin(34)); ldr.atten(ADC.ATTN_11DB); ldr.width(ADC.WIDTH_12BIT)
mq2 = ADC(Pin(35)); mq2.atten(ADC.ATTN_11DB); mq2.width(ADC.WIDTH_12BIT)

while True:
    try:
        dht.measure()
        temp = dht.temperature()   # °C
        hum  = dht.humidity()      # %RH
        lys  = ldr.read()          # 0..4095
        gas  = mq2.read()          # 0..4095
        # KUN CSV (ingen ekstra tekst)
        print(f"{temp:.1f},{hum:.1f},{lys},{gas}")
    except:
        pass
    time.sleep(1)
```

## PC (Python) – flere linjer i samme plot + legend

```python
# python/multi_live_plot.py
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PORT = "COM4"     # Windows: COM3/COM4 | Linux: /dev/ttyUSB0 | macOS: /dev/tty.usbserial-*
BAUD = 115200
ser = serial.Serial(PORT, BAUD, timeout=1)

N = 200           # rullende vindue (seneste N samples)
xs, tC, rh, ldrp, gasp = [], [], [], [], []  # °C, %RH, LDR%, GAS%

fig, ax = plt.subplots()
(line_t,) = ax.plot([], [], label="Temp (°C)")
(line_h,) = ax.plot([], [], label="Fugt (%)")
(line_l,) = ax.plot([], [], label="Lys (%)")
(line_g,) = ax.plot([], [], label="Gas (%)")
ax.set_ylim(0, 100)               # fælles 0–100 % skala
ax.set_xlabel("Samples")
ax.set_ylabel("Skaleret værdi")
ax.legend(loc="upper left")

def init():
    for ln in (line_t, line_h, line_l, line_g):
        ln.set_data([], [])
    return line_t, line_h, line_l, line_g

def update(i):
    s = ser.readline().decode(errors="ignore").strip()
    parts = s.split(",")
    if len(parts) >= 4:
        try:
            temp = float(parts[0])        # °C
            hum  = float(parts[1])        # %RH
            ldr  = float(parts[2])        # 0..4095
            gas  = float(parts[3])        # 0..4095
            # Skaler ADC til procent, temp mappes groft til 0–100 via *2
            t_pct   = max(0, min(100, temp * 2.0))  # fx 0–50°C → ~0–100%
            ldr_pct = max(0, min(100, 100.0 * ldr / 4095.0))
            gas_pct = max(0, min(100, 100.0 * gas / 4095.0))

            xs.append(i); tC.append(t_pct); rh.append(hum); ldrp.append(ldr_pct); gasp.append(gas_pct)
            xs[:]   = xs[-N:]; tC[:] = tC[-N:]; rh[:] = rh[-N:]; ldrp[:] = ldrp[-N:]; gasp[:] = gasp[-N:]

            line_t.set_data(xs, tC)
            line_h.set_data(xs, rh)
            line_l.set_data(xs, ldrp)
            line_g.set_data(xs, gasp)

            ax.set_xlim(max(0, i - N), max(N, i))
        except ValueError:
            pass
    return line_t, line_h, line_l, line_g

ani = FuncAnimation(fig, update, init_func=init, interval=200, blit=False)
plt.show()
```

### Noter

* **Legend** kommer fra `label=` ved oprettelse af linjerne og `ax.legend(...)`.
* Vi skalerer for at dele **én akse**:

  * Temp mappes groft: `°C * 2 ≈ %` (så 0–50 °C → 0–100 %)
  * LDR/MQ2 konverteres til `%` af 12-bit‐skalaen.
    Hvis du hellere vil undgå skalering, så brug to akser eller `subplots(2,1)`.
* Hold ESP32-output **stille** (kun CSV), ellers fejler parsen.
