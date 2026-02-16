# 🧩 03 – Data Inspection

### 🎯 Formål

Undersøg data for fejl, mangler og urealistiske værdier — **uden at ændre noget**.
Du skal kun kigge, ikke rette.

---

## 1️⃣ Se de første og sidste rækker

```python
print(df.head())
print(df.tail())
```

👉 Giver et hurtigt indtryk af starten og slutningen af måleserien.
Tjek fx om tidspunkterne virker korrekte, og om kolonnerne har de rigtige værdier.

**Notér: Ser tidsstempler og værdier korrekte ud?**

```
__________________________________________________________
__________________________________________________________
```

---

## 2️⃣ Datatyper og manglende værdier

```python
print(df.info())
```

👉 Her kan du se:

* Hvilken datatype hver kolonne har
* Hvor mange værdier der mangler (Non-Null Count)

**Notér: Er alle kolonner af den rigtige type? Er der mange manglende værdier?**

```
__________________________________________________________
__________________________________________________________
```

---

## 3️⃣ Tæl manglende værdier (NaN)

```python
print(df.isna().sum())
```

👉 Viser hvor mange tomme felter (NaN) der findes i hver kolonne.

**Notér: Hvor mange NaN’er har hver kolonne?**

```
__________________________________________________________
__________________________________________________________
```

---

## 4️⃣ Grundlæggende statistik

```python
print(df.describe())
```

👉 Viser minimum, maksimum, gennemsnit og spredning.
Kig efter **urealistiske værdier** (fx temperatur over 80 °C eller luftfugtighed over 100 %).

**Notér: Finder du ekstreme eller urealistiske værdier?**

```
__________________________________________________________
__________________________________________________________
```

---

## 5️⃣ Duplikerede rækker

```python
print(df.duplicated().sum())
```

👉 Hvis resultatet er større end 0, findes der **gentagelser i data**.

**Notér: Hvor mange duplikater blev fundet?**

```
__________________________________________________________
```

---

## 6️⃣ Samlet observationsskema

| Observation                            | Beskrivelse / Noter |
| -------------------------------------- | ------------------- |
| Antal rækker og kolonner               |                     |
| Kolonner med manglende værdier         |                     |
| Urealistiske værdier                   |                     |
| Duplikerede rækker                     |                     |
| Første indtryk af datasættets kvalitet |                     |

---

### ✅ Når du er færdig, skal du kunne:

* Forklare, hvordan du har inspiceret dataen
* Nævne mindst én mulig fejl eller uregelmæssighed
* Have udfyldt tabellen med dine observationer
