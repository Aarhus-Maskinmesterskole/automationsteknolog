# 🔁 04 – Loops og If-Else

Denne guide introducerer dig til kontrolstrukturer i Python: `if`, `else`, `elif`, `for` og `while`. Du lærer at styre flowet i dine programmer og udføre gentagelser. Det er fundamentalt i al programmering at kunne styre, hvornår og hvor mange gange en kode skal køres, og hvordan programmet reagerer på forskellige inputs.

---

## 🔧 Indhold

* `if`, `else`, `elif`
* Betingelser og logiske operatorer
* `for`-løkker
* `while`-løkker
* Brug af `break` og `continue`

---

## 📘 1. Betinget logik med `if`

Med `if`-udsagn kan du få Python til at træffe beslutninger baseret på data.


```python
temperatur = int(input("Indtast temperatur fra sensor: "))

if temperatur > 60:
    print("Alarm: Temperaturen er for høj!")
else:
    print("Temperaturen er normal.")
```

> Bemærk: Vi bruger `int()` til at konvertere input fra tekst til tal, så vi kan sammenligne det numerisk.

Du kan også udvide logikken med `elif` (else if):

```python
status = input("Indtast status på motor (kører/stop): ")
if status == "kører":
    print("Motoren er i drift.")
elif status == "stop":
    print("Motoren er stoppet.")
else:
    print("Ukendt status på motor.")
```

Du kan bruge så mange `elif`-blokke, du vil. Programmet kører kun den første betingelse, der er sand.

---

## 📘 2. Sammenlignings- og logiske operatorer

| Operator | Betydning        |
| -------- | ---------------- |
| `==`     | er lig med       |
| `!=`     | er ikke lig med  |
| `>`      | større end       |
| `<`      | mindre end       |
| `>=`     | større eller lig |
| `<=`     | mindre eller lig |

Du kan kombinere betingelser med `and`, `or` og `not`:

```python
tryk = int(input("Indtast tryk fra sensor: "))
if tryk >= 2 and tryk < 6:
    print("Trykket er inden for normal drift")
else:
    print("Advarsel: Trykket er uden for normalområdet!")
```

---

## 📘 3. `for`-løkker

En `for`-løkke bruges til at gentage noget et bestemt antal gange.  

```python
for i in range(1, 6):
    print("Pumpe ", i, " er startet")
```

Dette skriver: Pumpe 1 er startet ... Pumpe 5 er startet. Funktionen `range(inital value, stop, step)` kan bruges til at kontrollere rækken.
Inital value er inkluderet, stop er ekskluderet, og step er valgfrit (standard er 1). Hvis step er negativ, tælles der nedad:

Du kan også bruge `for` til at gå gennem lister:

```python
aktuatorer = ["ventil", "motor", "pumpe"]
for a in aktuatorer:
    print("Status for", a, ": OK")
```

---

## 📘 4. `while`-løkker

`while`-løkker gentager noget så længe en betingelse er sand:


```python
tryk = 1
while tryk <= 5:
    print("Tryksensor måling:", tryk, "bar")
    tryk += 1
```

Du skal selv huske at ændre variablerne inde i løkken, ellers kører programmet i uendelighed.

---

## 📘 5. Styring af løkker med `break` og `continue`

`break` stopper løkken med det samme:


```python
for niveau in range(10):
    if niveau == 4:
        print("Tankniveau kritisk, stopper måling!")
        break
    print("Tankniveau:", niveau)
```

`continue` springer til næste iteration:

```python
for motor in range(5):
    if motor == 2:
        continue  # Motor 2 springes over
    print("Motor", motor, "er startet")
```

---

## 📘 6. Indlejret (nested) loop

En indlejret løkke bruges ofte, når man har data i flere dimensioner – fx målinger fra flere sensorer over flere tidspunkter.

```python
sensor_data = [
    [21.5, 22.0, 22.3],  # Målinger fra sensor 1
    [19.8, 20.1, 20.4],  # Målinger fra sensor 2
    [23.0, 23.2, 23.5]   # Målinger fra sensor 3
]

for sensor_nr, maalinger in enumerate(sensor_data, start=1):
    for tid, vaerdi in enumerate(maalinger, start=1):
        print(f"Sensor {sensor_nr}, tid {tid}: {vaerdi} °C")
```

Dette udskriver alle målinger for hver sensor og hvert tidspunkt.

---

## 🧪 Øvelser


1. Lav et program der spørger om en temperatur og skriver:

    * "Alarm!" hvis temperaturen er over 70
    * "OK" hvis ikke

2. Skriv et program der udskriver "Pumpe X er startet" for X fra 1 til 10 ved hjælp af `for`

3. Skriv et program med `while`, der tæller ned fra 5 til 1 og afslutter med "Maskine starter!"

4. Lav et program der beder brugeren om en status ("kører"/"stop") indtil de indtaster "stop" (brug `while` og `break`)

5. Lav et program der skriver alle værdier fra 1 til 20 undtagen dem der er delelige med 4 (brug `continue`)

---

## ✅ Tjekliste

* [ ] Jeg forstår forskellen på `if`, `elif` og `else`
* [ ] Jeg kan skrive betingelser med `==`, `>`, `!=` osv.
* [ ] Jeg har skrevet både `for` og `while`-løkker
* [ ] Jeg har brugt `break` og `continue` korrekt

---
