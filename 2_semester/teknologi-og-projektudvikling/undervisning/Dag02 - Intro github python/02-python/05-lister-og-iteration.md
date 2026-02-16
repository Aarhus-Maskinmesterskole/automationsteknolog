# 📚 05 – Lister og Iteration

Denne guide introducerer arbejdet med lister i Python og hvordan du gennemløber dem med løkker. Lister bruges til at gemme flere værdier i én variabel og er en af de vigtigste datastrukturer i Python. De giver dig mulighed for at strukturere og manipulere samlinger af data på en effektiv måde og danner grundlag for mere avancerede datastrukturer og funktioner i programmeringssproget.

---

## 🔧 Indhold

* Opret og brug lister
* Tilføj, fjern og redigér elementer
* Gennemløb med `for`
* Indeks og slicing
* Brug af `len()` og `range()` sammen
* Indlejrede løkker (intro)
* Brug af lister med input og funktioner

---

## 📘 1. Opret en liste

Lister skrives med kantede parenteser. En liste kan indeholde tekst, tal, boolean og mere:

```python
maalinger = [23.5, 24.1, 22.8, 23.9]
motorer = ["Motor1", "Motor2", "Motor3"]
```

Du kan blande typer i en liste, men det er normalt bedst at holde samme type:

```python
blandet = [400, "Pumpe1", True]
```

Du kan også starte med en tom liste og tilføje elementer:

```python
sensornavne = []
sensornavne.append("Temperatur")
sensornavne.append("Tryk")
```

---

## 📘 2. Tilgå og ændr elementer med indeks

Python starter med indeks 0:

```python
motorer = ["Motor1", "Motor2", "Motor3"]
print(motorer[0])  # Motor1
print(motorer[2])  # Motor3
```

Du kan ændre værdier med tildeling:

```python
motorer[1] = "Pumpe1"
print(motorer)  # ['Motor1', 'Pumpe1', 'Motor3']
```

Brug `len()` til at finde antal elementer:

```python
print(len(motorer))  # 3
```

---

## 📘 3. Brug slicing til at få dele af listen

Slicing giver dig et udsnit af listen baseret på start og slut:

```python
temperaturer = [21.5, 22.0, 22.8, 23.1, 23.7, 24.0]
print(temperaturer[1:4])  # [22.0, 22.8, 23.1]
print(temperaturer[:3])   # [21.5, 22.0, 22.8]
print(temperaturer[3:])   # [23.1, 23.7, 24.0]
```

Du kan også bruge negative indeks:

```python
print(temperaturer[-1])  # 24.0 (sidste måling)
print(temperaturer[-3:-1])  # [23.1, 23.7]
```

---

## 📘 4. Gennemløb en liste med `for`

En `for`-løkke kan bruges til at gennemgå alle elementer:

```python
for pumpe in ["Pumpe1", "Pumpe2", "Pumpe3"]:
    print("Status på", pumpe, ": OK")
```

Du kan kombinere `range()` og `len()` for at bruge indeks:

```python
tryk_maalinger = [2.1, 2.3, 2.2, 2.4]
for i in range(len(tryk_maalinger)):
    print("Måling", i, "er", tryk_maalinger[i], "bar")
```

---

## 📘 5. Ændr lister under iteration

Lister kan opdateres undervejs, men pas på at undgå fejl ved at ændre listen direkte:

```python
statusser = ["kører", "stop", "fejl"]
for i in range(len(statusser)):
    statusser[i] = statusser[i].upper()
print(statusser)  # ['KØRER', 'STOP', 'FEJL']
```

---

## 📘 6. Indlejrede løkker (liste i liste)

En liste kan indeholde andre lister (2D-lister):

```python
sensor_data = [[21.5, 22.0], [22.8, 23.1], [23.7, 24.0]]
for række in sensor_data:
    for måling in række:
        print(måling)
```

Indlejrede løkker er nyttige til fx at gennemgå målinger fra flere sensorer eller tidspunkter.

---

## 📘 7. Liste og brugerinput

Du kan opbygge en liste dynamisk med input fra brugeren:

```python
maalinger = []
for i in range(3):
    maaling = float(input("Indtast måling (fx temperatur): "))
    maalinger.append(maaling)

print("Du indtastede målingerne:", maalinger)
```

---

## 🧪 Øvelser

1. Lav en liste med navne på tre pumper og udskriv dem én ad gangen
2. Brug `for` til at udskrive målingerne i listen `[2.1, 2.3, 2.2, 2.4, 2.5]`
3. Brug slicing til at udskrive de midterste tre temperaturer i `[21.5, 22.0, 22.8, 23.1, 23.7]`
4. Lav en liste med fem strøm-målinger og beregn summen ved hjælp af en `for`-løkke og en variabel til at akkumulere værdierne
5. Ekstra: lav en liste af lister med to rækker sensor-data og brug indlejrede løkker til at udskrive alle værdier
6. Bonus: lav et program, hvor brugeren kan indtaste fem tryk-målinger, som bliver gemt i en liste og derefter udskrives i omvendt rækkefølge

---

## ✅ Tjekliste

* [ ] Jeg kan oprette og tilgå en liste
* [ ] Jeg forstår hvordan slicing fungerer
* [ ] Jeg kan bruge `for` og `range()` sammen
* [ ] Jeg har arbejdet med indlejrede lister
* [ ] Jeg har brugt lister sammen med input

---
