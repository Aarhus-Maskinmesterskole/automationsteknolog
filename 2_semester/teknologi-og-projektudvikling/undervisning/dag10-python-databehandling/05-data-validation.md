# ✅ 05 – Data Validation

### 🎯 Formål

Tjek at dit datasæt nu er rent, komplet og klar til analyse.
Du skal kontrollere, at cleaning-trinene fra sidste opgave har virket, og dokumentere resultaterne.

---

## 1️⃣ Kontroller for manglende værdier

```python
print(df.isna().sum())
```

👉 Tæl hvor mange manglende værdier (NaN) der stadig findes i hver kolonne.

**Notér: Er der stadig NaN i nogle kolonner?**

```
__________________________________________________________
__________________________________________________________
```

---

## 2️⃣ Kontroller for duplikater

```python
print(df.duplicated().sum())
```

👉 Tjek at alle dubletter er fjernet.

**Notér: Er der stadig duplikerede rækker tilbage?**

```
__________________________________________________________
```

---

## 3️⃣ Kontroller datatyper

```python
print(df.dtypes)
```

👉 Sørg for, at hver kolonne har den rigtige datatype
(fx `float64` for målinger, `datetime64` for timestamp).

**Notér: Har alle kolonner nu de korrekte typer?**

```
__________________________________________________________
__________________________________________________________
```

---

## 4️⃣ Kontroller værdiernes område

```python
print(df.describe())
```

👉 Brug minimum og maksimum til at tjekke, at der ikke længere findes ekstreme eller urealistiske værdier.
Fx:

* Temperatur mellem -20 og 50
* Fugtighed mellem 0 og 100
* Distance under 400 cm

**Notér: Ser værdierne realistiske ud nu?**

```
__________________________________________________________
__________________________________________________________
```

---

## 5️⃣ (Valgfrit) Kontroller kontinuitet i tidsserien

Hvis du arbejder med tidsdata, kan du tjekke, at tidspunkterne ligger jævnt:

```python
print(df['timestamp'].diff().describe())
```

👉 Det viser, om der mangler tidspunkter eller store spring mellem målinger.

**Notér: Er tidsserien jævn og uden store huller?**

```
__________________________________________________________
__________________________________________________________
```

---

## 6️⃣ Samlet valideringsskema

| Kontrolpunkt            | Resultat | Kommentar |
| ----------------------- | -------- | --------- |
| Manglende værdier       |          |           |
| Duplikater              |          |           |
| Datatyper               |          |           |
| Urealistiske værdier    |          |           |
| Tidsserie (valgfrit)    |          |           |
| Overordnet datakvalitet |          |           |

---

## 7️⃣ (Valgfrit) Sammenlign før og efter

Hvis du gemte både den rå og den rensede fil, kan du sammenligne:

```python
raw = pd.read_csv("raw_data.csv")
print("Før cleaning:", raw.shape)
print("Efter cleaning:", df.shape)
```

**Notér: Hvor mange rækker blev fjernet eller ændret under cleaning?**

```
__________________________________________________________
```

---

### ✅ Når du er færdig, skal du kunne:

* Forklare hvordan du har **valideret** din cleaning
* Dokumentere at datasættet nu er **komplet og konsistent**
* Konkludere, om datasættet er **klar til analyse eller visualisering**
