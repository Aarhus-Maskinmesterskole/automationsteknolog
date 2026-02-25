# 📊 02 – Pandas Basics

Denne guide introducerer dig til det grundlæggende i at bruge `pandas` i Python. Du lærer at oprette og udforske DataFrames, som er centrale for arbejdet med CSV-filer og sensordata.

---

## 🎯 Mål for modulet

* Forstå hvad en `DataFrame` og `Series` er
* Kunne oprette simple datasæt selv
* Bruge `.head()`, `.info()` og `.describe()` til at udforske data

---

## 📦 Hvad er en DataFrame?

En `DataFrame` er en todimensionel tabel-lignende datastruktur fra `pandas`. Du kan tænke på den som et Excel-ark med kolonner og rækker.

```python
import pandas as pd

# Opret eksempeldata
maalinger = pd.DataFrame({
    "tid": [1, 2, 3, 4, 5],
    "værdi": [23, 45, 67, 12, 89]
})

print(maalinger)
```

---

## 🧪 Udforskning af DataFrames

```python
print(maalinger.head())        # De første 5 rækker
print(maalinger.info())        # Kolonner, typer og antal
print(maalinger.describe())    # Statistisk oversigt (mean, std, min, max)
```

---

## 🧠 Værd at vide

* `.head()` viser standard 5 rækker – brug `.head(10)` for flere
* `.info()` viser datatype, manglende værdier og struktur
* `.describe()` virker kun på tal-kolonner

---

## 🧪 Øvelser

1. Opret et nyt DataFrame med temperaturmålinger over 50 målinger
2. Brug `head()`, `info()` og `describe()` til at analysere det
3. Tilføj en ekstra kolonne, fx `målepunkt = "sensor A"`
4. Filtrer rækker hvor værdien er over 23

```python
filtreret = maalinger[maalinger["værdi"] > 23]
print(filtreret)
```

---

## ✅ Tjekliste

* [ ] Jeg kan oprette en `DataFrame` med egne data
* [ ] Jeg har brugt `.head()`, `.info()` og `.describe()`
* [ ] Jeg har filtreret rækker ud fra en betingelse
* [ ] Jeg forstår forskellen på DataFrame og Series

---

Dette modul forbereder dig på at arbejde med importerede CSV-filer i næste lektion.
