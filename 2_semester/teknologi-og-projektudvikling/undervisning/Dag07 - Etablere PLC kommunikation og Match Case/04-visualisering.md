# 📈 Opgave 4 – Visualisering af valide og ugyldige målinger

I denne opgave skal du visualisere resultaterne fra dine sanity checks og plausibilitetstests. Formålet er at få et visuelt overblik over hvilke målinger der er valide, og hvilke der er blevet afvist. Du skal bruge Matplotlib til at lave grafisk fremstilling af både temperatur og luftfugtighed – og markere fejlmålinger tydeligt.

---

## 🎯 Mål for opgaven

- Indlæse datasættet fra tidligere opgaver
- Visualisere temperatur- og fugtværdier over tid
- Markere ugyldige eller uplausible målinger med farve eller symbol
- Forstå hvordan grafisk feedback styrker analyse og fejlfinding

---

## 👨‍💻 Eksempelkode

```python
import pandas as pd
import matplotlib.pyplot as plt

# Indlæs data med validitet og plausibilitet
df = pd.read_csv("dht22_log_plausibel.csv")

# Del datasæt op i valide og fejlende målinger
valide = df[df["valid"] & df["plausibel"]]
fejl = df[~(df["valid"] & df["plausibel"])]

# Plot temperatur
plt.figure(figsize=(10, 5))
plt.plot(valide["tid"], valide["temp"], label="Temperatur – valid", color="green")
plt.scatter(fejl["tid"], fejl["temp"], label="Fejlmålinger", color="red")
plt.title("Temperaturmålinger med fejlindikatorer")
plt.xlabel("Tid")
plt.ylabel("Temperatur [°C]")
plt.legend()
plt.grid(True)
plt.show()

# Plot luftfugtighed (valgfri ekstra)
plt.figure(figsize=(10, 5))
plt.plot(valide["tid"], valide["fugt"], label="Fugtighed – valid", color="blue")
plt.scatter(fejl["tid"], fejl["fugt"], label="Fejlmålinger", color="orange")
plt.title("Fugtighedsmålinger med fejlindikatorer")
plt.xlabel("Tid")
plt.ylabel("Fugt [%]")
plt.legend()
plt.grid(True)
plt.show()
```

---

## 🧪 Udvidelser (frivillige)

- Brug forskellige figurer (🔺, ⚠️) til at markere fejltyper
- Brug farver til at skelne mellem `valid=False` og `plausibel=False`
- Lav et samlet plot med `subplots` for begge måletyper
- Brug Streamlit til live-visualisering med `st.line_chart`

---

## ✅ Tjekliste

- [ ] Jeg har indlæst datasættet med valideringskolonner
- [ ] Jeg har visualiseret temperatur og fugt over tid
- [ ] Jeg har markeret ugyldige målinger grafisk
- [ ] Jeg forstår hvordan fejl identificeres visuelt

---

> En god visualisering afslører hurtigt mønstre og fejl, der ellers kan være svære at opdage i rå data. Det er en afgørende del af din datavalidering.
