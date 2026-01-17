# 🕒 05 – Tidsserier og tidsstempler i Pandas

I denne guide lærer du at arbejde med tidsstemplede data i `pandas`. Det er vigtigt når du logger målinger over tid – fx fra sensorer – og skal analysere eller visualisere forløb.

---

## 🎯 Mål for modulet

* Konvertere kolonner til datetime
* Sætte tid som index
* Filtrere og resample tidsserier

---

## 🗓️ Konverter kolonne til datetime

```python
import pandas as pd

data = pd.read_csv("sensor.csv")
data["tid"] = pd.to_datetime(data["tid"])
```

> Kolonnen skal være i et format som `2024-01-20 14:23:00`

---

## 🔁 Brug tidspunkt som index

```python
data = data.set_index("tid")
print(data.head())
```

Nu kan du sortere og filtrere direkte på tid:

```python
udsnit = data["2024-01-20 14:00":"2024-01-20 15:00"]
```

---

## 🧪 Resample – lav gennemsnit hver 5. minut

```python
fem_min = data.resample("5min").mean()
print(fem_min.head())
```

Andre intervaller: `"15s"`, `"1H"`, `"D"`

---

## 🧠 Tip

* Brug `.plot()` direkte efter resample til at se resultaterne
* Hvis `tid` ikke er sorteret: `data = data.sort_index()`

---

## 🧪 Øvelser

1. Indlæs og konverter kolonnen `tid` til datetime
2. Brug `set_index()` til at sætte tid som index
3. Filtrér data til en bestemt dag eller time
4. Lav en ny DataFrame med gennemsnit hver 10. minut
5. Plot det resamplede datasæt

---

## ✅ Tjekliste

* [ ] Jeg har konverteret tid til datetime
* [ ] Jeg har brugt `set_index()` og forstået tidsindeks
* [ ] Jeg har resamplet og lavet en ny tidsserie
* [ ] Jeg har visualiseret en tidsserie med `.plot()`

---

Dette modul forbereder dig på at analysere trends og forløb i dine måledata.
