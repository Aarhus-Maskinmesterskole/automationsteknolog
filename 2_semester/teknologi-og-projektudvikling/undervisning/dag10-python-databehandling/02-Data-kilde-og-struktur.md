# 🧩 02 – Data kilde og struktur

### 🎯 Formål

Du skal finde ud af, **hvad dit datasæt indeholder**, og hvordan det ser ud — uden at ændre noget i det.

---

### 1️⃣ Tjek hvor mange rækker og kolonner der er

```python
print(df.shape)
```

👉 Det første tal er **antal rækker**, det andet er **antal kolonner**.

Skriv resultatet her:
**Antal rækker:** _______
**Antal kolonner:** _______

---

### 2️⃣ Se kolonnenavne

```python
print(df.columns)
```

👉 Det viser, hvilke målinger datasættet indeholder (fx `temperature`, `humidity`, `gas`, `lux`, `distance`).

Skriv kolonnenavnene her:
**Kolonnenavne:** ___________________________________

---

### 3️⃣ Se de første par linjer af data

```python
print(df.head())
```

👉 Kig på dataen – ser det ud som du forventer?
Fx: har du realistiske værdier, og står tallene i de rigtige kolonner?

---

### 4️⃣ (Valgfrit) Få lidt information om datatyper

```python
print(df.info())
```

👉 Det viser, hvilken **datatype** hver kolonne har (fx “float64” eller “object”)
— og hvor mange **ikke-tomme** værdier der er.

---

### 5️⃣ Beskriv dataens struktur med ord

Skriv kort herunder (maks 4 linjer):

📝 **Hvad viser dataen?**

---

---

---

---

### 6️⃣ Udfyld tabel:

| Kolonnenavn | Datatype         | Enhed      | Beskrivelse                         |
| ----------- | ---------------- | ---------- | ----------------------------------- |
| timestamp   |                  |            |                                     |
| temperature |                  |            |                                     |
| humidity    |                  |            |                                     |
| gas         |                  |            |                                     |
| lux         |                  |            |                                     |
| distance    |                  |            |                                     |


### 💡 Ekstra til refleksion (valgfrit)

* Hvilke kolonner ser ud til at være målinger fra sensorer?
* Hvilken kolonne viser tidspunktet?
* Ligner tallene realistiske målinger (f.eks. temperatur mellem -20 og 40)?

---

### ✅ Når du er færdig, skal du kunne:

* Fortælle hvor mange rækker og kolonner der er.
* Nævne kolonnenavnene.
* Forklare kort, hvad dataen indeholder.