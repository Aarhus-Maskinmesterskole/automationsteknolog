# Traceability Matrix – vejledning og skabelon

En traceability‑matrix viser **én‑til‑én** (eller én‑til‑mange) forbindelsen mellem

* **Brugerkrav (URS)**
* **Funktionel specifikation (FS)**
* **Designspecifikation (DS)**
* **Testcases** i de fire accepttestniveauer (**FAT**, **SAT**, **SIT**, **UAT**)

Målet er, at en auditor hurtigt kan se, at **alle** krav bliver demonstreret i mindst én test, og at ethvert testpunkts eksistens kan spores tilbage til et krav.

---

## Sådan udfylder du tabellen

1. **Kopier** en række for hvert URS‑ID.
2. Find det præcise **kapitel/afsnits‑nummer** i FS, hvor kravet adresseres \→ skriv fx `FS‑3.2`.
3. Gør det samme for DS (typisk hard‑ og soft‑ware‑design). Brug korte henvisninger: `DS‑4.6`.
4. Skriv **test‑case‑ID’er** som `FAT‑01`, `SAT‑03` osv. Brug det nøjagtige navn i jeres testprotokol.
5. **Status** kolonnen udfyldes under test: ✅ = bestået, ❌ = fejl fundet, ⬜ = ikke testet endnu.
6. Brug **Bemærkning** til at forklare særlige forhold, f.eks. referencer til eksterne dokumenter eller begrundelse for, at et krav kun testes på ét niveau.
7.

> **God praksis:** Hvert URS‑krav skal **mindst** mappes til én FS‑ og DS‑paragraf **og** én test. Hvis et krav ikke kan testes (eks. rent informativt krav), skal du anføre *“N/A – ikke testbart”* i testkolonnen og forklare hvorfor i *Bemærkning*.

---

## Eksempel (færdigudfyldt for de første to krav)

| URS‑ID | FS‑ref             | DS‑ref             | FAT‑TC | SAT‑TC | SIT‑TC | UAT‑TC | Status | Bemærkning                      |
| ------ | ------------------ | ------------------ | ------ | ------ | ------ | ------ | ------ | ------------------------------- |
| R‑01   | FS‑2.1 Sensorkrav  | DS‑3.4 Analoge I/O | FAT‑01 | SAT‑01 | SIT‑01 | UAT‑01 | ✅      | 1 % FS bekræftet med kalibrator |
| R‑02   | FS‑2.2 Logfrekvens | DS‑4.1 Logger      | FAT‑02 | SAT‑02 | –      | UAT‑02 | ⬜      | Logger kører 1,0 s ±0,1 s       |

---

## Skabelon – udfyld resten herunder

> Slet eksemplerne ovenfor og udfyld med **alle** URS‑krav.

| URS‑ID | FS‑ref | DS‑ref | FAT‑TC | SAT‑TC | SIT‑TC | UAT‑TC | Status | Bemærkning |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ---------- |
| R‑03   |        |        |        |        |        |        | ⬜      |            |
| R‑04   |        |        |        |        |        |        | ⬜      |            |
| R‑05   |        |        |        |        |        |        | ⬜      |            |
| R‑06   |        |        |        |        |        |        | ⬜      |            |
| R‑07   |        |        |        |        |        |        | ⬜      |            |
| R‑08   |        |        |        |        |        |        | ⬜      |            |

### Symbolforklaring

* **URS‑ID** – Refererer til linje i *User Requirement Specification* (R‑01, R‑02 …).
* **FS‑ / DS‑ref** – Kapitel + afsnit (fx `FS‑3.2`, `DS‑4.7`).
* **TC‑ID** – Test Case ID fra testdokument (fx `FAT‑03`).
* **Status** – ✅ Bestået · ❌ Fejl · ⬜ Ikke testet.
* **Bemærkning** – Kort fri tekst (maks 80 tegn).

---

> **Tip til grupper:** Del tabellen i Google Sheets og brug farvefiltre på *Status*, så I hurtigt ser, hvilke krav der mangler testdækning.
