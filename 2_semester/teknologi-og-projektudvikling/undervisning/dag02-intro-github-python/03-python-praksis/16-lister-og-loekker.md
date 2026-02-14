# Opgavesæt: Lister og Løkker

**Læringsmål:** I denne opgave træner du lister, `for`-løkker og simple beregninger.

---

## 1) Del A – Print alle temperaturer

### Opgave

Opret en liste med 5 temperaturmålinger (komma-tal).

### Krav til funktionalitet

* Brug en `for`-løkke til at gennemløbe listen.
* Udskriv hver temperatur på sin egen linje.
* Udskrivningen skal indeholde:

  * Målingens nummer (1–5)
  * Temperaturens værdi
  * Enheden `°C`

### Krav til output-format

Udskriften skal følge dette format:

`Temperatur <nr>: <værdi>°C`

---

## 2) Del B – Beregn statistik

### Opgave

Ud fra temperatur-listen skal du beregne og udskrive:

* Højeste temperatur
* Laveste temperatur
* Gennemsnitstemperatur

### Krav til output

* Højeste og laveste temperatur skal udskrives med enheden `°C`.
* Gennemsnittet skal udskrives med **2 decimaler** og enheden `°C`.

---

## 3) Del C – Status baseret på temperatur

### Opgave

Lav en statusvurdering for hver temperaturmåling og udskriv resultatet.

### Regler

* Hvis temperaturen er **mindre end 23.0** → status skal være `OK`
* Hvis temperaturen er **større end eller lig med 23.0** → status skal være `HØJ`

### Krav til output

For hver temperatur skal der udskrives én linje i formatet:

`<temperatur>°C - <status>`

---

## 4) Ekstra udfordring – Brugeren indtaster nye målinger

### Opgave

Lav et program der:

1. Spørger brugeren om **3 nye temperaturmålinger**
2. Gemmer de 3 målinger i en liste
3. Beregner gennemsnittet af de 3 nye målinger
4. Udskriver gennemsnittet med **2 decimaler** og `°C`

### Krav

* Input skal kunne håndtere komma-tal (temperaturer med decimaler).
* Alle 3 målinger skal bruges i beregningen.

---

## Tjekliste

* [ ] Del A: Alle temperaturer udskrives korrekt med nummerering
* [ ] Del B: Højeste, laveste og gennemsnit beregnes korrekt
* [ ] Del C: Status vises korrekt for hver måling
* [ ] Ekstra: Brugeren kan indtaste 3 nye målinger og få et gennemsnit

---
