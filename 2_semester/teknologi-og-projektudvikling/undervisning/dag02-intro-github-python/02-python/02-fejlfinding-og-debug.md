# 🐞 02 – Fejlfinding og Debugging

Alle laver fejl i deres kode – det er en helt normal del af programmering. Det vigtige er at kunne finde og rette fejlene hurtigt. Denne guide lærer dig, hvordan du identificerer og forstår typiske fejltyper i Python, og hvordan du kan bruge `print()` og andre teknikker til at debugge din kode.

---

## 🔧 Indhold

* Almindelige fejltyper i Python
* Brug af `print()` til fejlsøgning
* Forstå traceback (fejlbeskeder)
* Strategier til at finde fejl
* Brug af online værktøjer og editor-features

---

## 📘 1. Almindelige fejltyper

Her er nogle af de mest almindelige fejl, du vil støde på:

**`SyntaxError`** – Du har skrevet noget forkert:

```python
print("Hej"  # Mangler slut-parentes
```

**`NameError`** – Du bruger en variabel der ikke er defineret:

```python
print(navn)  # navn er ikke oprettet endnu
```

**`TypeError`** – Du prøver at kombinere uforenelige typer:

```python
alder = 20
print("Du er " + alder + " år")  # str + int fejler
```

**`IndexError`** – Du prøver at få adgang til et element, der ikke findes:

```python
tal = [1, 2, 3]
print(tal[3])  # Kun indeks 0-2 findes
```

---

## 📘 2. Brug `print()` til fejlsøgning

En af de bedste måder at forstå, hvad der sker i din kode, er at udskrive værdier undervejs:

```python
def beregn_total(priser):
    print("priser:", priser)
    total = sum(priser)
    print("total:", total)
    return total
```

Brug `print()` til at kontrollere, hvad variabler indeholder, og hvilke dele af koden der bliver kørt.

---

## 📘 3. Forstå traceback

Når en fejl opstår, viser Python en "traceback" – en fejlrapport:

```text
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    print(tal[3])
IndexError: list index out of range
```

Læs nedefra og op. Den nederste linje fortæller, hvilken type fejl det er.

---

## 📘 4. Strategier til fejlfinding

* Læs fejlen nøje og forstå, hvilken linje der fejler
* Brug `print()` før og efter problemet
* Test med små bidder af koden ad gangen
* Kommentér midlertidigt dele ud for at isolere problemet

---

## 📘 5. Editor-hjælp og online værktøjer

De fleste editors som VS Code og Replit giver dig advarsler eller forslag i realtid.

Du kan også bruge online værktøjer som:

* [Python Tutor](https://pythontutor.com)
* [Replit](https://replit.com)

---

## 🧪 Øvelser

1. Lav en bevidst `NameError` og ret den
2. Skriv et program med en `IndexError` og brug `print()` til at finde fejlen
3. Lav et regnestykke med `input()` og `int()`, og test hvad der sker, hvis brugeren skriver tekst
4. Ret en `TypeError` ved at konvertere tal til tekst med `str()`
5. Ekstra: Skriv en funktion og brug `print()` til at vise alle mellemregninger

---

## ✅ Tjekliste

* [ ] Jeg kender de mest almindelige fejltyper i Python
* [ ] Jeg kan bruge `print()` til at debugge kode
* [ ] Jeg forstår traceback-fejlbeskeder
* [ ] Jeg har brugt debugging-strategier aktivt i mit arbejde

---
