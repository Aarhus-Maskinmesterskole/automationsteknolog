<!-- File: projekt/10_spec/URS_template.md -->

# User Requirement Specification (URS)

| Felt          | Indhold                                            |
| ------------- | -------------------------------------------------- |
| **Projekt**   | AAMS · Teknologi & Projektudvikling · Dag 10       |
| **System**    | ESP32 datalogger + Siemens S7‑PLC + Python‑backend |
| **Version**   | 0.1 (skitse)                                       |
| **Dato**      | <!-- YYYY‑MM‑DD -->                                |
| **Forfatter** | <!-- Navn(e) → Stud./gruppe -->                    |
| **Godkendt**  | <!-- Navn – rolle – dato -->                       |

---

## 1  Formål

Dette dokument beskriver **brugerkravene** (SMART‑formulering) til det integrerede måle‑ og styringssystem bestående af ESP32‑sensorboard, Siemens S7‑PLC og Python‑dashboard. Kravene danner grundlag for efterfølgende FS, DS samt accepttest (FAT, SAT, SIT, UAT).

## 2  Definitioner & forkortelser

| Akronym | Betydning                     |
| ------- | ----------------------------- |
| PLC     | Programmable Logic Controller |
| FAT     | Factory Acceptance Test       |
| SAT     | Site Acceptance Test          |
| SIT     | System Integration Test       |
| UAT     | User Acceptance Test          |
| BD      | Block Diagram                 |
| ST      | Structured Text               |

## 3  Kravoversigt

| ID   | Krav (SMART)                                                                                                                                     | Rationale                                             | Verifikation | Acceptkriterium                                       |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- | ------------ | ----------------------------------------------------- |
| R‑01 | **Målesignaler**: Systemet skal registrere gas‑ppm, temp (°C), RH (%), lux (lx) med en opløsning ≤ 1 % FS.                                       | Sikrer tilstrækkelig præcision til energiberegninger. | FAT‑01       | Afvigelse ≤ ±1 % FS i kalibreringsrapport.            |
| R‑02 | **Sample‑tid**: Sensordata skal logges med et interval på 1,0 ± 0,1 s i minimum 12 timer uden tab.                                               | Muliggør tidsbaseret analyse og trend.                | SAT‑02       | Ingen manglende tidsstempler > 1,1 s.                 |
| R‑03 | **Set‑point skrivning**: Brugeren skal kunne indtaste set‑punkt for pump‑RPM (0‑3000) fra dashboardet, og PLC’en skal bekræfte kvittering < 2 s. | Fjernbetjent justering under tests.                   | SIT‑03       | ACK‑bit modtaget < 2 s i log.                         |
| R‑04 | **Alarmer**: Ved gas > 1000 ppm skal en rød alarm vises på dashboard og en digital udgang aktiveres < 1 s.                                       | Sikkerhed & brugervarsling.                           | SAT‑04       | Alarm‑LED tændt og dashboard skifter farve < 1 s.     |
| R‑05 | **Fail‑safe**: Ved PLC‑kommunikationsfejl > 5 s skal pumpen stoppes automatisk.                                                                  | Beskytter hardware ved netværksfejl.                  | SIT‑05       | Pumpestatus = 0 efter simuleret netværksfejl.         |
| R‑06 | **Dataeksport**: Loggeren skal kunne eksportere CSV‑filer ≤ 5 MB/dag og automatisk arkivere pr. dato.                                            | Let analyse og begrænset filstørrelse.                | FAT‑06       | Filstørrelse målt efter 24 h ≤ 5 MB.                  |
| R‑07 | **Tegningsdokumentation** skal følge IEC 81346‑navngivning og lagres som PDF i `20_drawings/`.                                                   | Konsistens og kundekrav.                              | UAT‑07       | Audit tjekker filnavne og placering OK.               |
| R‑08 | **Versionskontrol**: Alle ST‑filer skal versioneres i Git med semver tags (v1.0.0 etc.).                                                         | Sporbarhed og rollback.                               | FAT‑08       | Git‑log viser semantiske tags og commit‑beskrivelser. |

> **Note**: Kravene er eksempler og **skal tilpasses** jeres faktiske projekt. Tilføj flere krav efter behov og opdater ID‑rækken fortløbende.

## 4  Traceability

En komplet **traceability‑matrix** findes i `traceability.xlsx`, hvor hver URS‑linje er linket til én eller flere FS‑ og DS‑paragraffer og til konkrete testcases.

## 5  Revisionhistorik

| Version | Dato                | Forfatter     | Beskrivelse            |
| ------- | ------------------- | ------------- | ---------------------- |
| 0.1     | <!-- dd‑mm‑yyyy --> | <!-- navn --> | Første skitse (8 krav) |
| 0.2     |                     |               |                        |

---

*Når kravspecifikationen er godkendt, fryses **Version 1.0** og bruges som reference for al efterfølgende test og design.*
