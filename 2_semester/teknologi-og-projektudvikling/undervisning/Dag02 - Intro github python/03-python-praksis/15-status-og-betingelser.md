# Opgavesæt: Status og Betingelser

**Læringsmål:** I denne opgave træner du `input()`, `if/elif/else`, `while` og `print()`.

---

## 1) Del A – Grundlæggende status

### Opgave

Lav et program, der spørger brugeren om:

1. Maskinens navn
2. Maskinens status (mulige værdier: `kører`, `stop`, `fejl`)

### Krav til output

Programmet skal udskrive en besked baseret på status:

* Hvis status er `kører` → udskriv: `Maskine <navn> er i drift`
* Hvis status er `stop` → udskriv: `Maskine <navn> er stoppet`
* Hvis status er `fejl` → udskriv: `Maskine <navn> har fejl`

---

## 2) Del B – Udvid med driftstilstand

### Opgave

Udvid programmet med et ekstra input:

3. Driftstilstand (mulige værdier: `manuel` eller `auto`)

### Krav til output

Programmet skal til sidst udskrive en samlet statuslinje i dette format:

`Maskine <navn> | Status: <status> | Tilstand: <tilstand>`

---

## 3) Ekstra udfordring – Menu med while-løkke

### Opgave

Lav en menu i en `while`-løkke, der gentager sig indtil brugeren afslutter.

Menuen skal vise følgende valg:

1. Vis status
2. Skift status til `stop`
3. Afslut

### Krav til funktionalitet

* Når brugeren vælger **1**, skal programmet udskrive den aktuelle statuslinje (som i Del B).
* Når brugeren vælger **2**, skal programmet ændre status til `stop` og give en tydelig besked om ændringen.
* Når brugeren vælger **3**, skal programmet afslutte løkken og stoppe programmet.
* Hvis brugeren indtaster et ugyldigt valg, skal programmet give en fejlbesked og vise menuen igen.

---

## Tjekliste

* [ ] Del A: Programmet håndterer alle tre statustyper (`kører`, `stop`, `fejl`)
* [ ] Del B: Programmet viser samlet status med driftstilstand
* [ ] Ekstra: Menu-løkke fungerer og kan afsluttes korrekt

---
