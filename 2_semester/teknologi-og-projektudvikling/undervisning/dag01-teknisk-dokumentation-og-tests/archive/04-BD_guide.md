<!-- File: projekt/20_drawings/BD/BD_guide.md -->

# Guide til blokdiagram (BD) – System Overview

Denne vejledning beskriver, hvordan du tegner og dokumenterer blokdiagrammet **BD\_001\_System\_Overview** – et overblik over signalflow og modulgrænser i jeres måle‑ og styringssystem.

---

## 1. Formål og scope

Blokdiagrammet skal give både teknikere og ikke‑teknikere et hurtigt overblik over:

* Hovedhardware (ESP32‑sensorboard, Siemens S7‑1200, HMI/PC).
* Kommunikationskanaler (UART, Ethernet, Modbus/TCP).
* Kritiske I/O‑signaler (AI, AO, DI, DO) og deres retning.
* Eksterne enheder (pumpe, alarm‑sirene, reference‑sensorer).

Diagrammet bruges i **Design Specification (DS)** og danner reference for testcases samt fejlsøgning.

---

## 2. Symbolik og standarder

| Symbol | Betydning                   | Notation                                         |
| ------ | --------------------------- | ------------------------------------------------ |
| ▭      | Hardware‑enhed (CPU, modul) | Rektangel med titel (fx *“S7‑1200 CPU 1212C”*)   |
| →      | Data‑ eller styresignal     | Pil med tekst (fx *Ethernet / Snap7*)            |
| ◉      | Analog sensor               | Cirkel + label (fx *Gas ppm (AI0)*)              |
| ◌      | Digital I/O                 | Lille cirkel på rektangelkant (fx *DO0 Pump ON*) |

Følg **IEC 61082** for generelle symboler og **IEC/ISO 81346‑1** for tag‑numre (f.eks. =A1 for PLC‑skab, –K1 for relæ).

---

## 3. Navngivning & filformat

* Filnavn: **`BD_001_System_Overview.dwg`** (AutoCAD) **og** PDF‑export `BD_001_System_Overview.pdf`.
* Versionér med **semver** suffix, fx `BD_001_System_Overview_v1-0.pdf` ved release.
* Gem kildefil (draw\.io, AutoCAD, Visio) i samme mappe for fremtidig redigering.

---

## 4. Tegne‑workflow (step‑by‑step)

1. **Skitse på papir**: Indtegn bokse for PLC, sensorboard, PC/HMI, strømforsyning.
2. **Placer I/O‑punkter**: Marker analoge sensorer (gas, temp, RH, lux) på sensorboard; digitale udgange på PLC.
3. **Træk kommunikationslinjer**:

   * UART (ESP32 → PC) – stiplede linjer.
   * Ethernet (PLC ↔ PC) – fuldtrukken pil.
4. **Tilføj labels**: For hver pil angiv protokol (*Snap7*, *Modbus/TCP*, *CSV over UART*).
5. **Indsæt ref. dokumenter**: Notér “Se EL\_001\_Main\_Cabinet.dwg for ledningsdetaljer” nær PLC‑boksen.
6. **Tjek layout**: Alle pile læses venstre→højre eller top→bund.
7. **Export PDF**: A3‑landscape anbefales.
8. **Review & version**: Tilføj rev‑blok nederst: Rev, Dato, Beskrivelse, Initialer.

---

## 5. Kvalitetskontrol‑checkliste

* [ ] Diagrammet viser **alle** hovedkomponenter (HW‑bokse).
* [ ] Alle signal‑piler har tydelige labels og pile‑retning.
* [ ] Tag‑numre følger IEC/ISO 81346.
* [ ] Filnavn og rev‑blok stemmer med Git‑revision.
* [ ] PDF‑export ligger i repo under `20_drawings/BD/`.

---

## 6. Eksempel (mini‑PNG)

*(Indsæt lille referencebillede eller link til færdig demo i repo når klar).*

---

*Når BD‑filen er reviewet og signeret, fryses den sammen med DS v1.0 og bruges som basis for FAT‑testcases.*
