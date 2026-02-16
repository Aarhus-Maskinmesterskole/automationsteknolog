# 🧪 Opgave 2 – Sanity Checks på DHT22-målinger

I denne opgave skal du validere dine målinger fra DHT22 vha. en sanity check-funktion. Formålet er at sikre, at de indsamlede temperatur- og fugtdata er plausible og inden for rimelige grænser.

---

## 🎯 Mål for opgaven

- Oprette en funktion til sanity check af temperatur og fugt
- Tilføje en kolonne `valid` med True/False for hver række
- Analysere hvor mange målinger der er uden for det forventede område
- Forberede datasættet til plausibilitetstest og watchdog i næste opgave

---

## 📌 Typiske måleområder for DHT22

- Temperatur: -40°C til 80°C (realistisk: 10°C til 35°C indendørs)
- Fugt: 0% til 100% (realistisk: 20% til 80% indendørs)

---

## 👨‍💻 Eksempelkode

```python
import pandas as pd

# Indlæs data fra opgave 1
df = pd.read_csv("dht22_log.csv")

# Sanity check-funktion
def sanity_check(temp, fugt):
    if not (10 <= temp <= 35):
        return False
    if not (20 <= fugt <= 80):
        return False
    return True

# Tilføj ny kolonne 'valid'
df["valid"] = df.apply(lambda row: sanity_check(row["temp"], row["fugt"]), axis=1)

# Gem opdateret datasæt
df.to_csv("dht22_log_valid.csv", index=False)

# Statistik
print("Antal valide målinger:", df["valid"].sum())
print("Antal ugyldige målinger:", len(df) - df["valid"].sum())
```

---

## 🧪 Udvidelser (frivillige)

- Udskriv rækkenummer og årsag ved ugyldige målinger
- Tilføj kolonnen `fejlkode` med fx: "temp_high", "fugt_low", etc.
- Visualisér valide og ugyldige målinger med farver i `matplotlib` eller `Streamlit`

---

## ✅ Tjekliste

- [ ] Jeg har defineret en sanity check-funktion
- [ ] Jeg har tilføjet en kolonne med valideringsstatus (`True`/`False`)
- [ ] Jeg har opdateret og gemt det filtrerede datasæt
- [ ] Jeg har overblik over hvor mange målinger der er plausible

---

> En simpel sanity check giver dig langt bedre tillid til dine data – og beskytter resten af dit system mod fejlmålinger.
