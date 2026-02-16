<!-- File: projekt/40_test/FAT_Form_template.md -->

# Factory Acceptance Test (FAT) – Skabelon

> **Formål:** Dokumentere, at alle funktionelle og designmæssige krav er opfyldt **før** udstyr og software forlader værkstedet. Skabelonen kan importeres til Excel eller Google Sheets, men findes her som Markdown for entydig versionskontrol.

---

## Vejledning til udfyldelse

1. **Test‑ID** – Fortløbende nummer (FAT‑01, FAT‑02 …).
2. **URS‑ref** – Det krav, testen hovedsageligt dækker (fra URS‑dokumentet).
3. **FS/DS‑ref** – Referencer til relevante designafsnit.
4. **Forudsætninger** – Initiale betingelser (f.eks. “PLC i RUN”, “sensor kalibreret”).
5. **Testtrin** – Beskriv logisk rækkefølge af handlinger (Step 1, 2, 3 …).
6. **Forventet resultat** – Målbart output, incl. tolerancer.
7. **Faktisk resultat** – Udfyldes under testen.
8. **OK/NOK** – ✔ eller ✖.
9. **Tester & dato** – Signatur og dato for udførsel.

> **Tip:** Hvis testen består af mange trin, kan du opdele i under‑tabeller (f.eks. FAT‑03a, FAT‑03b).

---

## Eksempel (FAT‑01 udfyldt)

| Test‑ID | URS‑ref | FS/DS‑ref       | Forudsætninger                     | Testtrin                                              | Forventet resultat            | Faktisk resultat | OK/NOK | Tester & dato   |
| ------- | ------- | --------------- | ---------------------------------- | ----------------------------------------------------- | ----------------------------- | ---------------- | ------ | --------------- |
| FAT‑01  | R‑01    | FS‑2.1 / DS‑3.4 | Sensor er kalibreret <br>PLC i RUN | 1. Inject 1000 ppm testgas <br>2. Læs dashboard‑værdi | Dashboard viser 1000 ± 10 ppm | 1005 ppm         | ✔      | AA · 2025‑08‑05 |

---

## Skabelon – kopier én tabel per test

> Erstat pladsholderne med reelle data. Tilføj eller fjern kolonner efter behov.

| Test‑ID  | URS‑ref | FS/DS‑ref         | Forudsætninger | Testtrin | Forventet resultat | Faktisk resultat | OK/NOK | Tester & dato |
| -------- | ------- | ----------------- | -------------- | -------- | ------------------ | ---------------- | ------ | ------------- |
| FAT‑\_\_ | R‑\_\_  | FS‑\_\_ / DS‑\_\_ |                |          |                    |                  | ⬜      |               |

---

### Sign‑off

| Rolle              | Navn | Dato | Underskrift |
| ------------------ | ---- | ---- | ----------- |
| Test‑ingeniør      |      |      |             |
| QA‑repræsentant    |      |      |             |
| Kunde‑repræsentant |      |      |             |

*Når alle tests i protokollen er markeret ✔ og sign‑off er komplet, kan systemet pakkes og sendes til SAT.*
