<!-- File: projekt/20_drawings/SM/state_machine_guide.md -->

# Guide til State Machine – Sekvensstyring i PLC & Dokumentation

Denne vejledning beskriver bedste praksis for at modellere, dokumentere og implementere en **tilstands­maskine (state machine)** til jeres projekt – fra papirskitse til kodet **Structured Text (ST)** og test.

> *Hvorfor en state machine?*
> • Gør sekvenslogik **gennemsigtig** og **testbar**
> • Forhindrer udefinerede mellem­tilstande (race‑conditions)
> • Giver enkel mapping til FAT/SAT‑testcases (én test pr. tilstand / overgang)

---

## 1. Terminologi

| Begreb                    | Forklaring                                                            | Notation                                                     |
| ------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Tilstand (State)**      | Veldefineret system­modus, hvor bestemte outputs er stabile.          | Rektangel el. rundet boks (fx *IDLE*)                        |
| **Overgang (Transition)** | Betingelse, der flytter systemet fra én tilstand til en anden.        | Pil med vinkelbeskåret label (fx *StartCmd AND Safe = TRUE*) |
| **Entry‑/Exit‑action**    | Kode der køres, når man **går ind i** eller **forlader** en tilstand. | Kommentar i ST‑CASE eller aktiverings‑bit                    |
| **State ID**              | Numerisk værdi gemt i PLC‑word / enum.                                | `0 = IDLE`, `10 = STARTING`                                  |
| **HFE (Hold for Exit)**   | Krav om, at outputs fastholdes under overgang.                        | Overgangsbetingelse inkluderer timer/ACK                     |

---

## 2. Tegnestandard & værktøjer

* Brug **UML State Diagram** symboler – tilgængelige i *draw\.io / diagrams.net* under *Advanced > UML*.
* Filnavn: `SM_001_ProcessSequence.drawio` + PDF‑export `SM_001_ProcessSequence.pdf`.
* Version‑tag som `v1.0` i rev‑blok.

### Layout‑regler

1. **Venstre→højre** tidsakse: Tidligste tilstande til venstre.
2. Overgangspile krydser **aldrig** hinanden.
3. Brug **fork‑/join‑symbolet** til parallelle grene.

---

## 3. Mapping til ST‑kode

> Eksempel på ST‑snippet (Siemens TIA Portal):

```pascal
(* Define state IDs *)
TYPE tState : (
    IDLE         := 0,
    STARTING     := 10,
    RUNNING      := 20,
    ALARM        := 30
);
END_TYPE
VAR
    curState  : tState := IDLE;
    nxtState  : tState := IDLE;
END_VAR

(* Main state machine *)
CASE curState OF
IDLE:
    PumpEnable := FALSE;
    IF StartCmd AND Safe THEN nxtState := STARTING; END_IF;
STARTING:
    MotorRamp();
    IF RampDone THEN nxtState := RUNNING; END_IF;
RUNNING:
    PumpEnable := TRUE;
    IF GasPPM > 1000 THEN nxtState := ALARM; END_IF;
ALARM:
    PumpEnable := FALSE;
    AlarmHooter := TRUE;
    IF ResetCmd THEN nxtState := IDLE; END_IF;
END_CASE;
curState := nxtState;
```

* **Entry‑actions** = kode i hvert CASE‑gren.
* **Transitions** = `IF`‑betingelser.
* **Traceability**: Hver tilstand/transition får en **TC‑ID** i FAT‑protokollen.

---

## 4. Test & dokumentation

| Dokument                 | Hvordan relaterer det til state machine?                                     |
| ------------------------ | ---------------------------------------------------------------------------- |
| **FAT‑TC‑liste**         | Én test for hver overgang (verificerer betingelse + output).                 |
| **SIT‑Interface‑matrix** | Bekræfter signaler til/fra eksterne systemer i hver tilstand.                |
| **UAT‑Bruger­scenarier** | Step‑for‑step drejebog (f.eks. normal opstart → produktion → alarm → reset). |

---

## 5. Kvalitetscheck før review

* [ ] Alle tilstande har **unik** State ID og navngives i UPPER\_SNAKE\_CASE.
* [ ] Der er **ingen** udefinerede outputs i nogen tilstand.
* [ ] Alle overgangsbetingelser er **udtømmende** (no “dead ends”).
* [ ] PDF‑export ligger i `20_drawings/SM/` og er linket i DS‑kapitel.
* [ ] ST‑kodefil (`ProcessSequence.st`) er versioneret og refererer til diagram ID.

---

## 6. Ekstra tips

* Overvej **hierarkiske state machines** (sub‑states) til komplekse processer.
* Brug **enum‑typede variabler** frem for rene ints for at få navne i watch‑tables.
* Kør **time‑in‑state** statistik (en COUNTER per state) – nyttigt i OEE‑rapporter.

---

*Når state‑diagrammet, ST‑kode og tests er på plads og signeret, fryses version 1.0 og arkiveres.*
