# 🔗 02 – Håndtering af flere sensorer i én DataFrame

Når du har målinger fra flere sensorer – f.eks. temperatur og lys – er det en god idé at strukturere dine data i samme DataFrame. Det gør det nemmere at analysere sammenhænge og sammenligne udvikling over tid.

---

## 🎯 Læringsmål

* Lære at kombinere flere kolonner i ét datasæt
* Forstå hvordan man lægger data fra flere CSV-filer sammen
* Visualisere målinger fra flere sensorer i samme graf

---

## 📂 Eksempel – Simuleret datasæt med to sensorer

```python
import pandas as pd
import numpy as np

# Simulerede målinger
data = pd.DataFrame({
    "tid": pd.date_range(start="2023-01-01", periods=50, freq="s"),
    "temperatur": np.random.normal(loc=22, scale=1, size=50),
    "lys": np.random.randint(300, 900, size=50)
})

print(data.head())
```

---

## 📈 Visualisering af flere måletyper

```python
import matplotlib.pyplot as plt

plt.plot(data["tid"], data["temperatur"], label="Temperatur")
plt.plot(data["tid"], data["lys"], label="Lys")
plt.xlabel("Tid")
plt.ylabel("Sensorværdi")
plt.legend()
plt.title("Sammenligning af to sensorer")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

> Hvis værdierne ligger i meget forskellige størrelsesordener, kan du overveje at bruge to y-akser (se `twinx()` i matplotlib).

---

## 🧪 Øvelser

1. Kombinér dine egne målinger fra to CSV-filer i én DataFrame
2. Brug `merge()` eller `concat()` til at lægge dem sammen på tid
3. Visualisér begge sensorer i samme plot – evt. med to y-akser
4. Beregn glidende gennemsnit for begge sensorer og vis forskellen

---

## ✅ Tjekliste

* [ ] Jeg har arbejdet med datasæt med flere sensorer i samme tabel
* [ ] Jeg har visualiseret flere kolonner samtidigt i ét plot
* [ ] Jeg har brugt Pandas til at kombinere eller merge datasæt
* [ ] Jeg har forstået hvordan målinger kan sammenlignes over tid

---

> Når du kombinerer flere sensorer i én analyse, får du større forståelse for systemets samlede adfærd og sammenhænge.
