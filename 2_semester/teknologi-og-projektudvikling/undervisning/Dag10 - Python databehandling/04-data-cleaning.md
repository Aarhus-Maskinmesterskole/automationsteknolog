## 🧹 Opgave 4: Data Cleaning

### 🎯 Formål

Rens dit datasæt, så det bliver klar til analyse.
Du skal håndtere **manglende værdier**, **duplikater** og **urealistiske data**.

---

## 1️⃣ Fjern duplikerede rækker

```python
print(df.duplicated().sum())
df = df.drop_duplicates()
```

👉 Først ser du, hvor mange duplikater der findes — derefter fjerner du dem.

**Notér: Hvor mange duplikerede rækker blev fjernet?**

```
__________________________________________________________
```

---

## 2️⃣ Håndter manglende værdier (NaN)

```python
print(df.isna().sum())
```

👉 Kig på hvor mange værdier der mangler i hver kolonne.
Du kan så vælge at:

* fjerne rækker med manglende værdier, eller
* udfylde dem med en typisk værdi (fx gennemsnit eller median).

Eksempler:

```python
# Fjern rækker med NaN
df = df.dropna()

# ELLER udfyld med gennemsnit
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
```

**Notér: Hvilken metode brugte du — fjernede du NaN eller udfyldte du dem?**

```
__________________________________________________________
__________________________________________________________
```

---

## 3️⃣ Konverter datatyper (hvis nødvendigt)

```python
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
```

👉 Sørg for, at `timestamp` er i datotid-format, og at sensordata er numeriske.

**Notér: Skulle du ændre nogle datatyper?**

```
__________________________________________________________
__________________________________________________________
```

---

## 4️⃣ Find og håndter urealistiske værdier

Brug `describe()` til at finde outliers (meget høje eller lave værdier).

Eksempel:

```python
print(df.describe())
```

👉 Du kan fjerne rækker med urealistiske værdier ved fx:

```python
df = df[df['temperature'] < 60]  # Fjern temperaturer over 60°C
```

**Notér: Hvilke urealistiske værdier fandt du, og hvordan håndterede du dem?**

```
__________________________________________________________
__________________________________________________________
```

---

## 5️⃣ (Valgfrit) Interpolation for tidsserier

Hvis du har små huller i tidsserien:

```python
df = df.interpolate(method='time')
```

👉 Det udfylder manglende værdier baseret på de omkringliggende tidsstempler.

**Notér: Brugte du interpolation? Hvorfor / hvorfor ikke?**

```
__________________________________________________________
__________________________________________________________
```

---

## 6️⃣ Samlet dokumentation efter cleaning

| Handling                   | Hvad blev gjort | Hvor mange ændringer |
| -------------------------- | --------------- | -------------------- |
| Duplikater                 |                 |                      |
| Manglende værdier          |                 |                      |
| Datatyper                  |                 |                      |
| Urealistiske værdier       |                 |                      |
| Interpolation (hvis brugt) |                 |                      |

---

## 7️⃣ Gem dit rensede datasæt

```python
df.to_csv("cleaned_data.csv", index=False)
```

👉 Nu har du en ren version af dataen, klar til analyse.

**Notér: Hvor blev filen gemt, og hvad hedder den?**

```
__________________________________________________________
```

---

### ✅ Når du er færdig, skal du kunne:

* Forklare hvilke trin du har udført
* Dokumentere hvordan du håndterede manglende og forkerte værdier
* Gemme et nyt, renset datasæt
