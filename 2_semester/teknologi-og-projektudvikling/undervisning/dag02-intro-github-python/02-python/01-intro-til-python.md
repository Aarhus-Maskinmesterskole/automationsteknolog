# ğŸ 01 â€“ Intro til Python

Denne guide introducerer de mest grundlÃ¦ggende begreber i Python. Du lÃ¦rer at skrive simple programmer, bruge variabler og udskrive tekst til skÃ¦rmen.

---

## ğŸ”§ Indhold

* `print()` og `input()`
* Variabler og datatyper
* Kommentarer
* Eksekvering af kode

---

## ğŸ“˜ 1. Udskriv tekst med `print()`

```python
print("Velkommen til Python!")
```

`print()` bruges til at vise tekst eller resultater i terminalen.

---

## ğŸ“˜ 2. LÃ¦s input fra brugeren

```python
navn = input("Bruger navn: ")
print("Bruger", navn, "er logget ind.")
```

`input()` lÃ¦ser tekst fra brugeren og returnerer det som en streng (`str`).

---

## ğŸ“˜ 3. Brug af variabler og datatyper

```python
motorRunTimeHour = 20Â  Â  Â  Â  Â  Â # heltal (int)
motorRunTimeSeconds = 3.14Â  Â  Â  # decimaltal (float)
isMotorOn = TrueÂ  Â  Â            # boolesk vÃ¦rdi (True/False)
motorStatus = "OK"Â  Â  Â  Â  Â      # tekst (str)
```

Python bruger dynamisk typning: du skal ikke skrive typen eksplicit.

---

## ğŸ“˜ 4. Kommentarer i Python

```python
# Dette er en kommentar
print("Kommentarer bliver ikke kÃ¸rt")
```

Kommentarer starter med `#` og bruges til at forklare din kode.

---

## ğŸ§ª Ã˜velse

Lav et program, der:
1. SpÃ¸rger om bruger input for: 
    1. pumpens navn
    2. antallet af driftstimer i timer.
    3. antallet af driftstimer i minutter.
    4. antallet af driftstimer i sekunder.
    5. om pumpen er i drift (ja/nej).
    6. pumpens status (fx "OK", "Fejl", "Vedligeholdelse").
2. Udskriver en sÃ¦tning med disse oplysninger, fx:

```text
Pumpen "Alpha" har kÃ¸rt i 150 timer, 30 minutter og 45 sekunder, er i drift, og har status "OK".
```

Brug `input()`, gem data i variabler, og vis det med `print()`.

---

## âœ… Tjekliste
* [ ] Jeg har brugt `print()` og `input()` korrekt
* [ ] Jeg forstÃ¥r forskellen pÃ¥ `int`, `float`, `str` og `bool`
* [ ] Jeg har skrevet og kÃ¸rt et program med brugerinput

---