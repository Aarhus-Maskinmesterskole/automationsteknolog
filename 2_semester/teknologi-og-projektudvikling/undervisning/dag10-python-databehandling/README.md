# 🧠 README – Dag 10: Dataforståelse og databehandling med Python (Pandas)

## 🎯 Formål med dagen
Formålet med denne øvelsesdag er at lære at arbejde med **data i Python** — fra rå sensordata til et renset og valideret datasæt, klar til analyse.

Du vil:
- Indlæse og undersøge rå data (CSV-format)
- Forstå dataens struktur og kvalitet
- Rense data for fejl og mangler
- Validere at dataen nu er korrekt
- Dokumentere hele processen i en kort rapport

---

## 🧩 Overblik over opgaverne

### 1️⃣ Data Collection
**Formål:** Forstå hvor dataen kommer fra og hvordan den indsamles.  
Du arbejder med et færdigt datasæt, men lærer hvad “indsamling” betyder i praksis (ESP32, sensorer, CSV-logning).

---

### 2️⃣ Data Source & Structure
**Formål:** Få overblik over dataens struktur.  
Du skal indlæse filen `raw_data.csv`, se kolonner, datatyper og beskrive hvad hver kolonne repræsenterer.  
→ Afslut med at udfylde en tabel over datastrukturen.

---

### 3️⃣ Data Inspection
**Formål:** Undersøg dataen for fejl og uregelmæssigheder — uden at ændre noget.  
Du lærer at finde:
- Manglende værdier (NaN)
- Forkerte datatyper
- Urealistiske værdier
- Duplikater  
→ Du dokumenterer observationerne i en tabel.

---

### 4️⃣ Data Cleaning
**Formål:** Rense datasættet, så det bliver brugbart.  
Du fjerner duplikater, håndterer manglende værdier, konverterer datatyper og fjerner outliers.  
→ Du dokumenterer hvad du har gjort, og hvor mange ændringer der er foretaget.

---

### 5️⃣ Data Validation
**Formål:** Kontrollér, at din cleaning faktisk har virket.  
Du tester igen for NaN, duplikater og datatyper, og sammenligner med før.  
→ Du udfylder et valideringsskema og beskriver dataens kvalitet.

---

### 6️⃣ Data Reporting
**Formål:** Sammenfat alt dit arbejde i en mini-rapport.  
Du beskriver:
- Hvad datasættet indeholder  
- Hvilke problemer du fandt  
- Hvilke metoder du brugte til cleaning  
- Hvad resultatet blev efter validering  

→ Afslut med et “før/efter”-skema og en kort konklusion.

---

## 💾 Random Data Generator

Før du går i gang med øvelserne, skal du have en rå datafil.

Kør følgende script for at **generere `raw_data.csv`** med tilfældige sensorværdier og enkelte fejl (NaN og duplikerede rækker):

**Fil:** `generate_raw_data.py`

```python
import pandas as pd
import numpy as np

# --- Grunddata ---
num_rows = 1000
np.random.seed(42)

data = {
    "timestamp": pd.date_range(start="2023-01-01", periods=num_rows, freq="H"),
    "temperature": np.random.uniform(low=-20, high=40, size=num_rows),
    "humidity": np.random.uniform(low=0, high=100, size=num_rows),
    "gas": np.random.uniform(low=0, high=1000, size=num_rows),
    "lux": np.random.uniform(low=0, high=10000, size=num_rows),
    "distance": np.random.uniform(low=0, high=100, size=num_rows)
}

df = pd.DataFrame(data)

# Tilføj NaN-værdier
for col in ["temperature", "humidity", "gas", "lux", "distance"]:
    n_missing = int(num_rows * 0.02)
    missing_idx = np.random.choice(df.index, n_missing, replace=False)
    df.loc[missing_idx, col] = np.nan

# Tilføj hele NaN-rækker
full_nan_rows = np.random.choice(df.index, 5, replace=False)
df.loc[full_nan_rows, ["temperature", "humidity", "gas", "lux", "distance"]] = np.nan

# Gem CSV
df.to_csv("raw_data.csv", index=False)
print("raw_data.csv genereret med tilfældige sensordata.")
````

Efter du har kørt scriptet, ligger der en fil kaldet `raw_data.csv` i din mappe.
Den bruges i **alle efterfølgende øvelser**.

---

## 📦 Struktur (anbefalet mappeopbygning)

```
│
├── generate_raw_data.py        # Script til at generere data
├── raw_data.csv                # Rå sensordata (bliver oprettet af scriptet)
│
├── 01_Data_Source_and_Structure.md
├── 02_Data_Inspection.md
├── 03_Data_Cleaning.md
├── 04_Data_Validation.md
├── 05_Data_Reporting.md
│
└── README.md                   # Denne fil
```

---

## 🧭 Efter dagens forløb skal du kunne

✅ Læse og forstå CSV-data i pandas
✅ Undersøge og dokumentere datastruktur og kvalitet
✅ Rense og validere et datasæt
✅ Rapportere din proces på en enkel og systematisk måde

---

**Udviklet til:** undervisning i dataforståelse og databehandling med Python (Pandas)
**Målgruppe:** Automationsteknolog / Maskinmester 2. semester
**Udviklet af:** Anders Sandø Østergaard – Aarhus Maskinmesterskole
