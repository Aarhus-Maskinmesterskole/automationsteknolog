# 🧹 04 – Data Cleaning: Rens dine måledata

Denne guide viser dig, hvordan du opdager og håndterer fejl i dine data: tomme værdier, dubletter og urealistiske målinger. Du lærer at gøre datasættet klar til analyse og visualisering.

---

## 🎯 Mål for modulet

* Identificere og håndtere manglende værdier
* Fjerne dubletter og outliers
* Forberede datasæt til videre behandling

---

## 🔍 Find fejl i datasættet

### Tjek for tomme værdier:

```python
print(data.isnull().sum())
```

### Fjern rækker med manglende data:

```python
data = data.dropna()
```

### Erstat manglende værdier med gennemsnit:

```python
data["værdi"] = data["værdi"].fillna(data["værdi"].mean())
```

---

## 🔁 Fjern dubletter

```python
før = len(data)
data = data.drop_duplicates()
efter = len(data)
print("Fjernet", før - efter, "dubletter")
```

---

## ⚠️ Fjern urealistiske værdier (outliers)

```python
# Filtrer fx værdier uden for 0–1023 (ESP32 analog)
data = data[(data["værdi"] >= 0) & (data["værdi"] <= 1023)]
```

---

## 🧪 Øvelser

1. Indlæs et datasæt med `read_csv()`
2. Brug `isnull()` og `dropna()` eller `fillna()`
3. Fjern dubletter og tæl forskellen
4. Fjern værdier uden for et fornuftigt interval
5. Gem det rensede datasæt som `renset.csv`

---

## ✅ Tjekliste

* [ ] Jeg har undersøgt datasættet for tomme felter
* [ ] Jeg har fjernet eller udfyldt manglende værdier
* [ ] Jeg har fjernet dubletter og outliers
* [ ] Jeg har gemt et renset datasæt klar til analyse

---

Dette modul forbereder dine data til grafisk analyse og præsentation.
