# 🐍 01 – Intro til Python

Denne guide introducerer de mest grundlæggende begreber i Python. Du lærer at skrive simple programmer, bruge variabler og udskrive tekst til skærmen.

---

## 🔧 Indhold

* `print()` og `input()`
* Variabler og datatyper
* Kommentarer
* Eksekvering af kode

---

## 📘 1. Udskriv tekst med `print()`

```python
print("Velkommen til Python!")
```

`print()` bruges til at vise tekst eller resultater i terminalen.

---

## 📘 2. Læs input fra brugeren

```python
navn = input("Bruger navn: ")
print("Bruger", navn, "er logget ind.")
```

`input()` læser tekst fra brugeren og returnerer det som en streng (`str`).

---

## 📘 3. Brug af variabler og datatyper

```python
motorRunTimeHour = 20          # heltal (int)
motorRunTimeSeconds = 3.14     # decimaltal (float)
isMotorOn = True               # boolesk værdi (True/False)
motorStatus = "OK"             # tekst (str)
```

Python bruger dynamisk typning: du skal ikke skrive typen eksplicit.

---

## 📘 4. Kommentarer i Python

```python
# Dette er en kommentar
print("Kommentarer bliver ikke kørt")
```

Kommentarer starter med `#` og bruges til at forklare din kode.

---

## 🧪 Øvelse

Lav et program, der:
1. Spørger om bruger input for: 
    1. pumpens navn
    2. antallet af driftstimer i timer.
    3. antallet af driftstimer i minutter.
    4. antallet af driftstimer i sekunder.
    5. om pumpen er i drift (ja/nej).
    6. pumpens status (fx "OK", "Fejl", "Vedligeholdelse").
2. Udskriver en sætning med disse oplysninger, fx:

```text
Pumpen "Alpha" har kørt i 150 timer, 30 minutter og 45 sekunder, er i drift, og har status "OK".
```

Brug `input()`, gem data i variabler, og vis det med `print()`.

---

## ✅ Tjekliste
* [ ] Jeg har brugt `print()` og `input()` korrekt
* [ ] Jeg forstår forskellen på `int`, `float`, `str` og `bool`
* [ ] Jeg har skrevet og kørt et program med brugerinput

---
