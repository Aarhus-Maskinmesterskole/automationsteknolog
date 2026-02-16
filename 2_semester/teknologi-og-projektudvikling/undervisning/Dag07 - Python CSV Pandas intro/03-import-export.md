# 📥 03 – Import og eksport af CSV-filer

I denne guide lærer du, hvordan man importerer data fra CSV-filer til en `pandas` DataFrame og hvordan du gemmer ændringer tilbage i nye filer. Det er en grundlæggende færdighed, når man arbejder med målinger fra ESP32 eller PLC.

---

## 🎯 Mål for modulet

* Importere CSV-filer med `read_csv()`
* Gemme DataFrames som CSV med `to_csv()`
* Forstå forskellen på separatorer, encoding og index

---

## 📥 Læs en CSV-fil

```python
import pandas as pd

data = pd.read_csv("data.csv")
print(data.head())
```

> Sørg for at filen `data.csv` ligger i samme mappe som dit script.

Hvis filen bruger semikolon i stedet for komma:

```python
data = pd.read_csv("data.csv", sep=";")
```

---

## 🧾 Udforskning af data

Efter import, brug:

```python
print(data.info())
print(data.describe())
```

---

## 💾 Gem ændringer til ny fil

```python
# Gem til ny CSV uden index
data.to_csv("ny_fil.csv", index=False)
```

---

## 🧠 Værd at vide

* `index=False` er vigtigt hvis du ikke vil gemme rækkeindeks i CSV
* Brug `sep=";"` hvis du eksporterer til programmer der forventer semikolon (fx Excel DK)
* Brug `encoding="utf-8-sig"` for at sikre æøå fungerer korrekt i Excel

---

## 🧪 Øvelser

1. Download eller lav en fil `sensor.csv` med kolonner `tid`, `værdi`
2. Indlæs den med `read_csv()` og vis de første rækker
3. Filtrer værdier over 100 og gem til `sensor_renset.csv`
4. Åbn CSV-filen i Excel og tjek at tallene er rigtige

---

## ✅ Tjekliste

* [ ] Jeg har brugt `read_csv()` til at læse måledata
* [ ] Jeg har forstået brugen af separator og encoding
* [ ] Jeg har gemt nye CSV-filer med `to_csv()` korrekt
* [ ] Jeg har testet output i både Python og Excel

---

Dette modul giver dig de basale redskaber til at arbejde med rigtige måledata fra næste lektion.
