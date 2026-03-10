# 🧠 Opgave 3 – Plausibilitetstest af målinger over tid

Denne opgave bygger videre på sanity check. Nu skal du analysere, om målingerne udvikler sig realistisk over tid – altså om de ændrer sig i et plausibelt tempo og mønster. Det hjælper dig med at identificere outliers, sensorfejl eller dataglitches, der ikke nødvendigvis fanges af et simpelt intervalcheck.

---

## 🎯 Mål for opgaven

- Udvide valideringen med en plausibilitetstest baseret på ændring siden sidst
- Udelukke målinger hvor ændringen er for brat (pludselig stigning/fald)
- Forstå forskellen mellem simpel sanity check og dynamisk plausibilitetstest
- Tilføje fejlkoder eller årsagsforklaring til ugyldige målinger

---

## 📏 Eksempel på plausibilitetsregel

> En temperaturmåling må ikke ændre sig mere end ±1.5 °C pr. måling  
> En luftfugtighedsmåling må ikke ændre sig mere end ±3 % pr. måling

---

## 👨‍💻 Eksempelkode

```python
import pandas as pd

# Indlæs data med sanity status
df = pd.read_csv("dht22_log_valid.csv")

# Initialiser kolonne
df["plausibel"] = True

# Tjek ændring siden sidste måling
for i in range(1, len(df)):
    d_temp = abs(df.loc[i, "temp"] - df.loc[i-1, "temp"])
    d_fugt = abs(df.loc[i, "fugt"] - df.loc[i-1, "fugt"])

    if d_temp > 1.5 or d_fugt > 3:
        df.loc[i, "plausibel"] = False

# Gem resultat
df.to_csv("dht22_log_plausibel.csv", index=False)

# Statistik
print("Uplausible målinger:", len(df) - df["plausibel"].sum())
```

---

## 🧪 Udvidelser (frivillige)

- Kombinér `valid` og `plausibel` i en samlet statuskolonne
- Tilføj kolonnen `ændring_temp` og `ændring_fugt` til inspektion
- Visualisér de målinger der afviger i plot (f.eks. røde prikker for fejl)

---

## ✅ Tjekliste

- [ ] Jeg har sammenlignet målinger med deres foregående
- [ ] Jeg har sat regler for maksimal ændring pr. måling
- [ ] Jeg har markeret rækker der bryder disse regler
- [ ] Jeg har gemt datasættet med en ny kolonne `plausibel`

---

> En plausibilitetstest opdager de fejlværdier, der ligner rigtige målinger – men opfører sig forkert. Det er en vigtig del af enhver automatiseret validering.
