# 🧮 01 – Glidende gennemsnit med Pandas

I denne guide lærer du, hvordan man beregner og visualiserer glidende gennemsnit i måledata ved hjælp af Pandas. Glidende gennemsnit bruges til at udglatte svingninger og give et klarere billede af trends i støjfyldte datasæt.

---

## 🎯 Læringsmål

* Forstå hvad et glidende gennemsnit er og hvordan det beregnes
* Anvende `.rolling().mean()` i Pandas på en kolonne med måledata
* Sammenligne rå data med glidende gennemsnit i graf

---

## 📊 Eksempel – Beregning i Pandas

Antag, at du har et datasæt med kolonnen `"værdi"`:

```python
import pandas as pd

# Eksempel på datasæt
data = pd.DataFrame({"værdi": [101, 103, 100, 105, 98, 96, 102, 99, 95, 97]})

# Tilføj glidende gennemsnit med vindue på 3 målinger
data["glidende"] = data["værdi"].rolling(window=3).mean()

print(data)
```

> De første 2 rækker i kolonnen `glidende` vil være NaN, da vinduet ikke er fyldt endnu.

---

## 📈 Visualisering med matplotlib

```python
import matplotlib.pyplot as plt

plt.plot(data["værdi"], label="Rå data")
plt.plot(data["glidende"], label="Glidende gns.", linestyle="--")
plt.legend()
plt.title("Sammenligning af rå data og glidende gennemsnit")
plt.xlabel("Tidsindeks")
plt.ylabel("Sensorværdi")
plt.grid()
plt.show()
```

---

## 🧪 Øvelser

1. Anvend `.rolling(window=5).mean()` på et større datasæt
2. Visualisér forskellen mellem `window=3` og `window=10`
3. Hvad sker der med `NaN`-værdier i starten? Prøv `min_periods=1`
4. Brug glidende gennemsnit til at finde jævne trends i dine ESP32-målinger

---

## ✅ Tjekliste

* [ ] Jeg har beregnet glidende gennemsnit med `.rolling()` i Pandas
* [ ] Jeg har visualiseret både rå data og glidende gennemsnit
* [ ] Jeg forstår hvordan vinduets størrelse påvirker udglatningen
* [ ] Jeg har prøvet forskellige `window`-størrelser og sammenlignet resultater

---

> Glidende gennemsnit er et vigtigt redskab til at forstå signaler i støjfyldt data og præsentere stabile tendenser visuelt.
