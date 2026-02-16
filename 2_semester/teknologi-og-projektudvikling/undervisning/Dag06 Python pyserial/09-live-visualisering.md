# 📡 09 – Live-visualisering af ESP32-data

Denne guide viser dig, hvordan du kan vise ESP32-målinger direkte i en graf i realtid, mens Python modtager data via `pyserial`. Det giver et hurtigt overblik og gør det lettere at spotte fejl og trends under målingen.

---

## 🎯 Mål for modulet

* Modtage og plotte målinger løbende
* Bruge `matplotlib` sammen med `pyserial`
* Visualisere sensordata uden at vente på filgemning

---

## 📦 Krav

```bash
pip install matplotlib
```

---

## 📊 Live-plot af seriel data

```python
import serial
import matplotlib.pyplot as plt
from collections import deque

ser = serial.Serial("COM3", 115200)

data = deque(maxlen=100)  # de sidste 100 målinger

plt.ion()
fig, ax = plt.subplots()
linje, = ax.plot([], [], label="Sensor")
ax.set_ylim(0, 1100)
ax.set_xlim(0, 100)
plt.xlabel("Tid")
plt.ylabel("Værdi")
plt.title("Live målinger")
plt.grid()

while True:
    rå = ser.readline().decode().strip()
    try:
        _, værdi = rå.split(",")
        værdi = int(værdi)
        data.append(værdi)
        linje.set_ydata(data)
        linje.set_xdata(range(len(data)))
        ax.set_xlim(0, len(data))
        plt.pause(0.05)
    except:
        print("Fejl i linje")
```

---

## 🧠 Tip

* Brug `plt.ion()` for interaktiv opdatering
* Brug `deque` til fast længde på datastrømmen
* `plt.pause()` styrer opdateringshastigheden

---

## 🧪 Øvelser

1. Tilpas y-akse efter dine egne sensorværdier (fx `0–50` for temperatur)
2. Skift farve, linjetype og titel i grafen
3. Stop scriptet og brug `plt.savefig("graf.png")`

---

## ✅ Tjekliste

* [ ] Jeg har modtaget og visualiseret data live
* [ ] Jeg har brugt `deque` og `matplotlib`
* [ ] Jeg har justeret akser og labels
* [ ] Jeg har brugt grafen til at observere data i realtid

---

> Live-visualisering giver dig hurtigt overblik over dine sensorer – brug det til fejlsøgning, eksperimenter og præsentationer.
