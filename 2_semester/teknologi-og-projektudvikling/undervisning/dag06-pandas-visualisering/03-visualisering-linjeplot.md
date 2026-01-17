# 📈 03 – Visualisering med linjediagrammer

I denne guide lærer du at bruge Matplotlib til at visualisere målinger som linjediagram. Det gør data nemmere at forstå og sammenligne, især når du arbejder med tidsserier.

---

## 🎯 Læringsmål

* Oprette simple line-plots med `matplotlib`
* Tilføje labels, titler, gitter og farver
* Formatere akser og gøre grafen læsbar og præsentabel

---

## 📊 Eksempel – Enkelt sensorplot

```python
import pandas as pd
import matplotlib.pyplot as plt
from math import pow

# Simuleret datasæt
data = pd.DataFrame({
    "tid": pd.date_range(start="2023-01-01", periods=100, freq="s"),
    "værdi": pd.Series(range(100)).apply(lambda x: 1 - 2.71**(-x/10))
})

plt.plot(data["tid"], data["værdi"], color="royalblue", label="Sensorværdi")
plt.title("Sensorens måleforløb")
plt.xlabel("Tid")
plt.ylabel("Værdi")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

> `tight_layout()` hjælper med at undgå overlap i tekst og akser.

---

## 🎨 Tilpasning og farver

* Brug `color="navy"`, `linestyle="--"` og `linewidth=2` for variation
* Overvej `alpha=0.7` for gennemsigtighed
* Tilføj `marker="o"` hvis du vil vise datapunkter

---

## 🧪 Øvelser

1. Lav et line-plot over dine egne målinger
2. Brug labels og titler på både x- og y-aksen
3. Eksperimentér med farver, stregtyper og baggrund
4. Tilføj både rå data og glidende gennemsnit i samme graf

---

## ✅ Tjekliste

* [ ] Jeg har lavet en graf med `plt.plot()` og mine måledata
* [ ] Jeg har brugt titler, aksetekster og labels korrekt
* [ ] Jeg har eksperimenteret med styling og forbedret læsbarhed
* [ ] Jeg har visualiseret både rå og bearbejdede data

---

> En god visualisering gør dine målinger forståelige – også for dem, der ikke selv har målt dem.
