## 📊 Opgave 6: Data Reporting

### 🎯 Formål

Sammenfat dit arbejde med dataindsamling, inspektion, rensning og validering.
Du skal lave en kort rapport, der dokumenterer:

* Hvilke problemer du fandt
* Hvordan du løste dem
* Hvordan datasættet ser ud nu

---

## 1️⃣ Beskriv din datakilde

Skriv et kort afsnit, der beskriver, hvor dataen kommer fra.

**Eksempler på spørgsmål, du kan svare på:**

* Hvordan blev dataen indsamlet (ESP32, Python, sensorer)?
* Hvilke sensorer blev brugt (DHT22, LDR, gas, distance)?
* Hvordan blev dataen gemt (CSV-fil, samplingfrekvens)?

**Notér her:**

```
__________________________________________________________
__________________________________________________________
__________________________________________________________
```

---

## 2️⃣ Opsummer Data Inspection

**Hvilke problemer fandt du under Data Inspection?**
Fx: manglende værdier, urealistiske målinger, forkerte datatyper, duplikater.

**Notér her:**

```
__________________________________________________________
__________________________________________________________
__________________________________________________________
```

---

## 3️⃣ Beskriv Data Cleaning

**Forklar kort, hvad du gjorde for at rense dataen.**
Fx:

* Fjernede duplikater
* Udfyldte manglende værdier
* Konverterede datatyper
* Fjernede urealistiske målinger

**Notér her:**

```
__________________________________________________________
__________________________________________________________
__________________________________________________________
```

---

## 4️⃣ Valider resultatet

Sammenfat resultaterne fra din Data Validation:

* Er der stadig NaN-værdier?
* Er datatyperne korrekte?
* Er urealistiske værdier fjernet?
* Hvor mange rækker har datasættet nu?

**Notér her:**

```
__________________________________________________________
__________________________________________________________
__________________________________________________________
```

---

## 5️⃣ Lav et sammenligningsskema (før og efter cleaning)

| Parameter            | Før Cleaning | Efter Cleaning |
| -------------------- | ------------ | -------------- |
| Antal rækker         |              |                |
| Antal kolonner       |              |                |
| NaN-værdier (samlet) |              |                |
| Duplikater           |              |                |
| Urealistiske værdier |              |                |
| Kommentar            |              |                |

---

## 6️⃣ Konklusion

Skriv 3–5 linjer, hvor du opsummerer projektets resultat:

* Er datasættet nu brugbart?
* Hvilke fejl var mest kritiske?
* Hvad kunne du forbedre i fremtidige målinger?

**Notér din konklusion:**

```
__________________________________________________________
__________________________________________________________
__________________________________________________________
__________________________________________________________
```

---

## 7️⃣ Gem og aflever din rapport

Gem dit rensede datasæt og din Markdown-rapport.

```python
df.to_csv("cleaned_data.csv", index=False)
```

Sørg for at din aflevering indeholder:

1. Koden du brugte til at rense og validere data.
2. Din udfyldte “Data Reporting”-sektion med beskrivelser og tabeller.

---

### ✅ Når du er færdig, skal du kunne:

* Forklare hele forløbet fra rå data → renset data
* Dokumentere, hvad du har gjort og hvorfor
* Fremvise resultaterne i et struktureret skema
