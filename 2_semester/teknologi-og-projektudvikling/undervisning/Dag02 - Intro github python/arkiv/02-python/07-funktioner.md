# 🧮 07 – Funktioner i Python

Funktioner er en grundsten i al programmering. De hjælper dig med at genbruge kode, skabe overblik og organisere dine programmer i mindre bidder. I denne guide lærer du at skrive dine egne funktioner og bruge dem effektivt.

---

## 🔧 Indhold

* Hvad er en funktion?
* `def` og `return`
* Parametre og argumenter
* Lokale variabler
* Brug af funktioner i praksis

---

## 📘 1. Hvad er en funktion?

En funktion er en blok af kode, som du kan kalde (starte), når du har brug for den. Det svarer til en maskine med input og output.

---

## 📘 2. Sådan definerer du en funktion

```python
def start_motor():
    print("Motoren er startet!")
```

Du kalder funktionen ved at skrive dens navn efterfulgt af `()`:

```python
start_motor()
```

---

## 📘 3. Funktion med parametre

```python
def vis_sensorvaerdi(sensor_navn):
    print("Sensor:", sensor_navn)

vis_sensorvaerdi("Temperatur")
vis_sensorvaerdi("Tryk")
```

Parametre er "pladsholdere", og argumenter er de konkrete værdier, du giver med, når du kalder funktionen.

---

## 📘 4. Brug `return` til at sende værdier tilbage

```python
def beregn_effekt(spaending, strom):
    return spaending * strom

print(beregn_effekt(400, 5))  # 2000
```

En funktion stopper ved `return` og sender værdien tilbage til det sted, hvor funktionen blev kaldt.

---

## 📘 5. Lokale variabler

Variabler oprettet inde i en funktion findes kun dér:

```python
def beregn_alarmgrænse(maaling):
    grænse = maaling + 10
    return grænse

print(beregn_alarmgrænse(50))
```

Variablen `grænse` findes kun inde i funktionen og kan ikke bruges udenfor.

---

## 📘 6. Funktioner og flow

Du kan bruge funktioner til at dele dit program op i trin:

```python
def system_start():
    print("Systemet starter op...")

def vis_menu():
    print("1. Start motor")
    print("2. Stop pumpe")

system_start()
vis_menu()
```

---

## 🧪 Øvelser

1. Skriv en funktion `stop_motor()` der printer "Motoren er stoppet!"
2. Lav en funktion `beregn_effekt(spaending, strom)` der returnerer effekten (P = U * I)
3. Lav en funktion `omregn_bar_til_psi(bar)` der returnerer trykket omregnet til psi (1 bar = 14.5 psi)
4. Skriv en funktion `gennemsnit(maalinger)` der beregner gennemsnittet af en liste målinger
5. Ekstra: Brug input og funktion sammen: spørg brugeren om en temperatur og vis alarmgrænsen (fx +10)

---

## ✅ Tjekliste

* [ ] Jeg kan definere en funktion med `def`
* [ ] Jeg kan give en funktion parametre
* [ ] Jeg forstår forskellen på `print()` og `return`
* [ ] Jeg har lavet en funktion der returnerer et resultat
* [ ] Jeg har brugt en funktion i et program

---
