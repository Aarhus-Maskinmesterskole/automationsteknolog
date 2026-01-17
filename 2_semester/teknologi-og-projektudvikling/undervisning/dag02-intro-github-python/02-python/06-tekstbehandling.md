# 🔤 06 – Tekstbehandling i Python

Tekst (strenge) er en af de mest anvendte datatyper i Python. Denne guide giver dig en introduktion til, hvordan du arbejder med tekst – hvordan du opretter, ændrer, sammenligner og analyserer strenge.

---

## 🔧 Indhold

* Opret og kombiner tekst
* Brug af `len()` og `in`
* Indexering og slicing
* `split()`, `join()` og `replace()`
* Sammenligning og store/små bogstaver

---

## 📘 1. Opret og kombiner tekst

```python
sensor = "Tryk"
enhed = "bar"
besked = sensor + "-sensor måling i " + enhed
print("Log:", besked)
```

Du kan bruge `+` til at kombinere tekst og `*` til at gentage:

```python
print("Alarm! " * 3)  # Alarm! Alarm! Alarm!
```

---

## 📘 2. Brug af `len()` og `in`

`len()` fortæller hvor mange tegn der er i en tekst:

```python
alarmtekst = "Motorfejl: Lavt tryk"
print(len(alarmtekst))  # 20
```

`in` bruges til at tjekke om en delstreng findes i teksten:

```python
if "tryk" in alarmtekst:
    print("Alarmen handler om tryk!")
```

---

## 📘 3. Indexering og slicing

```python
status = "Motor_Kører"
print(status[0])    # M
print(status[6:11]) # Kører
print(status[-1])   # r
```

Du kan bruge slicing til at vende teksten:

```python
print(status[::-1])  # reørK_rotorM
```

---

## 📘 4. `split()`, `join()` og `replace()`

Disse metoder bruges til at analysere og ændre tekst:

```python
logbesked = "Pumpe startet OK"
dele = logbesked.split()  # ['Pumpe', 'startet', 'OK']

samlet = ":".join(dele)  # Pumpe:startet:OK

ny = logbesked.replace("OK", "FEJL")
print(ny)  # Pumpe startet FEJL
```

---

## 📘 5. Ændr store og små bogstaver

```python
alarm = "Lavt Tryk"
print(alarm.upper())  # LAVT TRYK
print(alarm.lower())  # lavt tryk
print(alarm.capitalize())  # Lavt tryk
```

Du kan bruge disse metoder til at gøre søgning i tekst mere robust:

```python
status = input("Indtast status: ").lower()
if status == "fejl":
    print("Alarm! Fejl registreret.")
```

---

## 🧪 Øvelser

1. Skriv et program der tager en logbesked som input og udskriver antallet af tegn
2. Spørg brugeren om et sensor-navn og udskriv det bagfra
3. Tag et input (fx status) og udskift alle mellemrum med underscores
4. Lav et program der tæller hvor mange gange bogstavet "a" optræder i en alarmtekst
5. Ekstra: Tjek om en brugers input indeholder ordet "fejl"

---

## ✅ Tjekliste

* [ ] Jeg kan kombinere og analysere tekst
* [ ] Jeg har brugt slicing til at hente dele af en streng
* [ ] Jeg har brugt `split()`, `join()` og `replace()`
* [ ] Jeg forstår hvordan `in` og `len()` bruges på tekst
* [ ] Jeg har brugt `.lower()` og `.upper()` i et program

---
