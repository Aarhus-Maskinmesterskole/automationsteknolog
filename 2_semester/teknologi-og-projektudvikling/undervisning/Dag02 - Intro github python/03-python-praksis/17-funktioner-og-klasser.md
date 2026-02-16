# Opgavesæt: Funktioner og Klasser

**Læringsmål:** I denne opgave træner du funktioner med `def` og `return` samt en simpel klasse med metoder og objekter.

---

## 1) Del A – Funktioner

### Opgave

Opret tre funktioner med følgende krav:

#### Funktion 1: `vis_velkomst(navn)`

* Input: et navn (tekst)
* Funktion: udskriver en velkomsthilsen, der inkluderer navnet

#### Funktion 2: `beregn_effekt(spaending, strom)`

* Input: spænding (tal) og strøm (tal)
* Funktion: beregner effekten i watt som spænding gange strøm
* Output: funktionen skal **returnere** beregnet effekt (ikke kun udskrive)

#### Funktion 3: `er_hoej_temp(temp)`

* Input: temperatur (tal)
* Funktion: vurderer om temperaturen er høj
* Output: skal **returnere** `True` hvis temperaturen er **større end eller lig med 23.0**, ellers `False`

### Testkrav

I bunden af dit program skal du:

* kalde velkomst-funktionen med et eksempelnavn
* beregne en effekt ud fra eksempelværdier og udskrive resultatet
* bruge temperatur-funktionen i en betingelse (`if`) og udskrive en advarsel, hvis temperaturen er høj

---

## 2) Del B – Simpel klasse

### Opgave

Lav en klasse med navnet `Sensor`.

### Krav til klassen

Klassen skal indeholde:

1. En constructor (`__init__`) som modtager:

   * navn (tekst)
   * værdi (tal)

2. En metode `vis()` som:

   * udskriver sensorens navn og værdi i én linje
   * formatet skal være tydeligt, så man kan se både navn og værdi

### Testkrav

* Opret mindst ét `Sensor`-objekt
* Kald `vis()` på objektet
* Output skal vise sensorens navn og værdi

---

## 3) Del C – Liste med objekter

### Opgave

Opret en liste med **3 Sensor-objekter**.

### Krav til funktionalitet

* Brug en løkke til at gennemløbe listen
* For hvert objekt i listen skal du kalde metoden `vis()`
* Inden du udskriver sensorerne, skal du udskrive en overskrift, fx “Alle sensorer”

---

## 4) Ekstra udfordring – Udvid klassen med status

### Opgave

Udvid `Sensor`-klassen med en metode `er_hoej()`.

### Regler

* Metoden skal returnere `True` hvis sensorens værdi er **større end eller lig med 23.0**
* Ellers skal den returnere `False`

### Krav til output

Når du gennemløber listen af sensorer, skal du:

* udskrive en linje pr. sensor
* markere sensoren som “HØJ” hvis `er_hoej()` er `True`
* ellers markere den som “OK”
* gøre markeringen tydelig (fx med symboler eller tekst)

---

## Tjekliste

* [ ] Del A: Alle tre funktioner er oprettet og virker korrekt
* [ ] Del B: `Sensor`-klassen kan oprettes og udskrive data med `vis()`
* [ ] Del C: Liste med 3 objekter gennemløbes og `vis()` kaldes på alle
* [ ] Ekstra: Metoden `er_hoej()` er implementeret og bruges til statusvisning

---
