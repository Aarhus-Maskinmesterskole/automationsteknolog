# 📈 06 – Visualisering med Matplotlib og Pandas

I denne guide lærer du at visualisere måledata med `matplotlib` og `pandas`. Du bruger grafer til at præsentere dataoversigter, trends og sammenhænge – vigtigt når du dokumenterer dit arbejde.

---

## 🎯 Mål for modulet

* Forstå forskellen på linjeplot, histogram og scatter plot
* Bruge `.plot()` og `matplotlib.pyplot`
* Formatere akser, titler og farver

---

## 📉 Linjediagram med Pandas `.plot()`

```python
import pandas as pd
import matplotlib.pyplot as plt

# Eksempeldata
maalinger = pd.read_csv("sensor.csv")
maalinger["tid"] = pd.to_datetime(maalinger["tid"])

maalinger.plot(x="tid", y="værdi", kind="line")
plt.title("Sensorværdi over tid")
plt.xlabel("Tid")
plt.ylabel("Værdi")
plt.grid()
plt.show()
```

---

## 📊 Histogram

```python
maalinger["værdi"].plot(kind="hist", bins=20)
plt.title("Fordeling af målinger")
plt.xlabel("Værdi")
plt.grid()
plt.show()
```

---

## 🔴 Scatter Plot

```python
maalinger.plot(kind="scatter", x="tid", y="værdi")
plt.title("Spredning af målepunkter")
plt.grid()
plt.show()
```

---

## 🧠 Tip

* Brug `figsize=(10,5)` i `plot()` for bredere grafer
* Brug `.legend()` hvis du plotter flere dataserier
* Gem grafer med `plt.savefig("navn.png")`

---

## 🧪 Øvelser

1. Lav et linjediagram med dine egne data (fra ESP32 eller simulation)
2. Tilføj titler, aksetekster og gitter
3. Lav et histogram af dine værdier
4. Lav et scatter plot over tid
5. Gem dine grafer som `.png`

---

## ✅ Tjekliste

* [ ] Jeg har lavet mindst 2 forskellige plottetyper
* [ ] Jeg har tilføjet titler og aksebeskrivelser
* [ ] Jeg har gemt en graf som billede
* [ ] Jeg forstår forskellen på line, hist og scatter

---

Denne guide giver dig det visuelle værktøj du skal bruge til dokumentation og rapportering.
