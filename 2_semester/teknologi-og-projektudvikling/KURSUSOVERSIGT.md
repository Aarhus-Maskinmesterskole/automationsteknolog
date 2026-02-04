# 🗂️ KURSUS-OVERSIGT: Teknologi og Projektudvikling (5 ECTS)

## 📌 Kursusstruktur

Dette kursus strækker sig over 12 undervisningsdage og fokuserer på dataanalyse i Python, sensorintegration via ESP32, PLC-kommunikation via Snap7 og dokumentationspraksis med GitHub.

Node-RED indgår ikke i dette forløb for at sikre fokus på kernekompetencer inden for måling, databehandling og systemintegration.

Kursusplanen følger mappestrukturen i projektmappen:


```
📂 teknologi-og-projektudvikling/
├── undervisning/
│   ├── dag01-teknisk-dokumentation-og-tests/
│   ├── dag02-intro-github-python/
│   ├── dag03-arbejde-med-dag02/
│   ├── dag04-python-plc-kommunikation/
│   ├── dag05-ESP32-intro/
│   ├── dag06-Python-pyserial/
│   ├── dag07-Python-CSV-Pandas-intro/
│   ├── dag08-pandas-visualisering/
│   ├── dag09-sanity-timestamp/
│   ├── dag10-python-databehandling/
│   ├── dag11-realtime-plotting/
│   └── dag12-Opsummering-evaluering/
```

## 📅 Kursusforløb med fokusområder


| Dag | Emne                                      | Hovedtema                                                      |
|-----|--------------------------------------------|----------------------------------------------------------------|
| 1   | Teknisk dokumentation og tests             | Kravspec, blokdiagram, flowchart, state machine, testplan      |
| 2   | Intro til GitHub og Python                 | GitHub-workflow, Python intro, commits, branches, merge        |
| 3   | Arbejde med dag 2                         | Repetition af GitHub og Python, mini-automation case           |
| 4   | Python-PLC kommunikation                   | Snap7, Ethernet/IP, læs/skriv PLC-data i Python                |
| 5   | ESP32 intro og sensorer                    | Opsætning af ESP32, seriel output, simple sensorer             |
| 6   | Python + pyserial                         | Modtag seriel data, gem som CSV, real-time visualisering       |
| 7   | Python-CSV-Pandas intro                   | Pandas basics, import/export, data cleaning, time series, vis. |
| 8   | Pandas visualisering                      | Rolling average, flere sensorer, annotering, dashboards        |
| 9   | Sanity checks og timestamp                | Sanity checks, plausibilitetstest, watchdog, visualisering     |
| 10  | Python databehandling                     | Data import, cleaning, validation, reporting                   |
| 11  | Realtime plotting                         | Opsætning af real-time plots, flere sensorer, multiple plots   |
| 12  | Opsummering og evaluering                 | Fremlæggelse, peer-review, opsamling                          |

Forstået – her er den justerede version med "studerende" i stedet for "elever":

---


### 📆 Dag-for-dag beskrivelse

**📘 Dag 1 – Teknisk dokumentation og tests**
Fokus på kravspecifikation, blokdiagram, flowchart, state machine og testplan. De studerende lærer at dokumentere og teste et simpelt system, og får skabeloner til teknisk dokumentation.

**💻 Dag 2 – Intro til GitHub og Python**
Introduktion til versionsstyring med GitHub og grundlæggende Python-programmering. De studerende opretter et repo, laver commits og branches, og skriver simple scripts.

**🔁 Dag 3 – Arbejde med dag 2**
Repetition og fordybelse i GitHub-workflow og Python. Dagen bruges på at færdiggøre og uddybe opgaverne fra dag 2, så alle får styr på versionsstyring og grundlæggende Python.

**🔌 Dag 4 – Python-PLC kommunikation**
Snap7 og Ethernet/IP: Læs/skriv PLC-data i Python. Fokus på integration mellem Python og Siemens PLC.

**📡 Dag 5 – ESP32 intro og sensorer**
Opsætning af ESP32, seriel output og simple sensorer. Målinger logges og visualiseres.

**🔗 Dag 6 – Python + pyserial**
Modtag seriel data fra ESP32, gem som CSV, real-time visualisering i Python.

**📊 Dag 7 – Python-CSV-Pandas intro**
Pandas basics, import/export, data cleaning, time series og visualisering. Fokus på databehandling og analyse.

**📈 Dag 8 – Pandas visualisering**
Rolling average, flere sensorer, annotering, dashboards og avanceret visualisering.

**🧠 Dag 9 – Sanity checks og timestamp**
Sanity checks, plausibilitetstest, watchdog og visualisering af måledata.

**🧹 Dag 10 – Python databehandling**
Data import, cleaning, validation og reporting. Rensning og strukturering af datasæt.

**📉 Dag 11 – Realtime plotting**
Opsætning af real-time plots, flere sensorer og multiple plots i Python.

**🎤 Dag 12 – Opsummering og evaluering**
Fremlæggelse, peer-review og opsamling. Projekter præsenteres og evalueres på funktion, dokumentation og refleksion.

## 🧰 Brugte teknologier

* **Python**: `pandas`, `matplotlib`, `pyserial`, `snap7`, `datetime`
* **ESP32**: sensorer, `analogRead()`, `Serial.print()`
* **Git/GitHub**: versionsstyring, `README.md`, projektsamarbejde
* **Siemens PLC**: Snap7-integration via Python

## 📋 Dokumentation

Studerende arbejder løbende med:

* Kravspecifikation (`README.md`)
* Signalbeskrivelser og blokdiagrammer (`docs/`)
* Testlog og dokumentation af datakvalitet og fejl
* Versionshistorik via Git

## ✅ Aflevering og evaluering

* Ét GitHub-repository per gruppe
* Indeholder ESP32-kode, Python scripts, CSV-filer og dokumentation
* Mundtlig fremlæggelse i slutningen af kurset (dag 12)

**Vurdering baseres på:**

* Funktionalitet og realiseret løsning
* Kvalitet af dokumentation og datastruktur
* Refleksion og præsentation

---

Denne kursusoversigt supplerer `LEKTIONSPLAN.md` og de daglige undervisningsfiler i `undervisning/`.
