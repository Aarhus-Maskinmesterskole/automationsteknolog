# 🧩 01 – Indlæs data i pandas

### 🔹 Formål

Lær at indlæse en CSV-fil i pandas og kontrollér, at den er importeret korrekt.

---

### 1️⃣ Importér biblioteket

```python
import pandas as pd
```

---

### 2️⃣ Indlæs CSV-filen

```python
df = pd.read_csv("raw_data.csv")
```

> 💡 **Tip:** Hvis filen ligger i en anden mappe, skal du skrive den fulde sti – fx
> `pd.read_csv("C:/Brugere/Anders/Projekt/raw_data.csv")`

---

### 3️⃣ Se de første par linjer

```python
print(df.head())
```

Det viser de første 5 rækker i filen, så du kan se, om dataen ser rigtig ud.

---

### 4️⃣ Se information om datasættet

```python
print(df.info())
```

Her kan du se:

* hvor mange rækker og kolonner der er
* hvilke kolonnenavne filen har
* om der mangler noget data

---

### 5️⃣ (Valgfrit) Tjek at du fik alt med

```python
print("Antal rækker og kolonner:", df.shape)
```

---

### ✅ Når du er færdig, skal du kunne:

* Indlæse en CSV-fil uden fejl.
* Se de første linjer af data.
* Bekræfte, at kolonnenavne og antal rækker ser korrekte ud.

---

> 🧠 Ekstra idé til klassediskussion:
> Lad eleverne sammenligne deres `head()`-output – har alle fået samme antal kolonner og data i samme format?
> Hvis ikke, tal om hvorfor (fx forkert sti, separator, encoding).

---
