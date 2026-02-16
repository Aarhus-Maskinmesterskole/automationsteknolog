
# Dag 10 – Dokumentation & Test

> Teknologi & Projektudvikling · 2. semester · 5 ECTS

---

## 📘 Introduktion

En velbygget automationsløsning er kun så god som den **dokumentation** og de **tester** der følger med. Dag 10 sætter fokus på hele dokumentations‑ og test­livscyklussen: fra de første krav i en **kravspecifikation**, over formelle accept­tests (FAT, SAT, SIT, UAT), til strukturering af tekniske tegninger, **blokdiagrammer (BD)** og kildekode i **Structured Text (ST)**.

---

## 🎯 Læringsmål

Efter dagen kan du

1. udforme en kravspecifikation (URS → FS → DS) med entydige, testbare krav,
2. planlægge og beskrive de fire klassiske accepttest‑niveauer (FAT, SAT, SIT, UAT),
3. udarbejde en BD‑tegning, ST‑kodeudsnit og tilhørende versionskontrol, og
4. etablere mappestruktur + navngivningskonvention for tegnings‑ og dokument­filer.

---

## 🧑‍🏫 Teori

| Akronym | Lang titel                     | Formål                                        | Hvem udfører / hvor       |
| ------- | ------------------------------ | --------------------------------------------- | ------------------------- |
| **URS** | User Requirement Specification | Hvad skal systemet kunne?                     | Kunde ↔️ Systemleverandør |
| **FS**  | Functional Specification       | Funktionsbeskrivelse, signal­liste, sekvenser | Automationsingeniør       |
| **DS**  | Design Specification           | Detaljeret HW/SW‑design (BD, ST, I/O‑kort)    | Projektteam               |
| **FAT** | Factory Acceptance Test        | Bevise at systemet opfylder FS/DS i fabrik    | Leverandør + kunde repr.  |
| **SAT** | Site Acceptance Test           | Gentage kritiske FAT‑tests on‑site            | Kunde, evt. tredjepart    |
| **SIT** | System Integration Test        | Test af interfaces mellem delsystemer         | Integrator                |
| **UAT** | User Acceptance Test           | End‑to‑end, brugerorienteret test             | Slutbruger                |

> *BD:* Blokdiagram viser signal­flow og modul­grænser.
> *ST:* Structured Text‑kode skal dokumenteres med inline‑kommentarer og versionsmærker.

For tegningsdokumentation bruges ofte **IEC/ISO 81346**‑navngivning og fil­hierarki:

```
projekt/
├── 10_spec/
│   ├── URS_v1.0.pdf
│   ├── FS_v1.0.pdf
│   └── DS_v1.0.pdf
├── 20_drawings/
│   ├── BD/
│   │   └── BD_001_System_Overview.dwg
│   └── EL/
│       └── EL_001_Main_Cabinet.dwg
├── 30_software/
│   └── PLC/
│       ├── ST/
│       │   └── PumpControl.st
│       └── VersionHistory.md
└── 40_test/
    ├── FAT_Form.xlsx
    ├── SAT_Report.docx
    └── UAT_Checklist.xlsx
```

---

## 🛠️ Kompetencer

Når dagen er omme, vil du kunne:

* skrive **SMART**‑formulerede krav og knytte hvert krav til en test,
* anvende *traceability matrix* til at sikre fuld dækning,
* versionere BD‑tegninger og ST‑kode i Git med meningsfulde commits,
* bruge Markdown‑skabeloner til test­protokoller og review‑checklister.

---

## 📝 Dagens opgaver

1. **Kravspec‑skitse**
   Udfyld `URS_template.md` med mindst **otte** målbare krav for jeres PLC‑løsning.
2. **Traceability‑matrix**
   I `traceability.xlsx` knytter du hver URS‑linje til mindst én test (FAT #, SAT # …).
3. **FAT‑protokol**
   Lav en testskabelon (`FAT_Form.xlsx`) med kolonner: *Test‑ID, Krav‑ref, Forventet resultat, OK/NOK*.
4. **BD‑tegning**
   Tegn et blokdiagram (draw\.io, AutoCAD, eller PowerPoint) af signalflowet og gem som `BD_001_System_Overview.pdf`.
5. **ST‑kode & docstring**
   Tilføj omfattende header‑kommentarer (funktion, version, WHO/WHEN) i `PumpControl.st`.
6. **Dok‑mappestruktur**
   Opret mappetræet som vist i teorien og commit til GitHub.

*Aflever alt i en Pull Request. Review hinandens URS‑formuleringer og BD‑layout, inden I merger.*

---

## ✅ Checkliste

* [ ] URS‑fil har versions‑ og godkendelsesblok.
* [ ] Traceability‑matrix refererer alle krav.
* [ ] FAT‑protokol har mindst **5** testcases.
* [ ] BD‑tegning følger IEC‑symboler og entydige tag‑numre.
* [ ] ST‑kode har changelog og inline‑kommentar på alle netværk.

---

*Tip:* Brug Git‑releases til at signere version 1.0 af dokumentationen, inden I overdrager til kunde.\*
