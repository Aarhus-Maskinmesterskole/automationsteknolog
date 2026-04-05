# V-modellen

V-modellen er en måde at strukturere udvikling og test af et automationssystem.
Venstre side handler om at **definere og designe**, bunden er selve **implementeringen**, og højre side er **test og verifikation**.

Pointen er, at hvert trin på venstre side har et modsvarende testtrin på højre side. Det er ikke tilfældigt – det er meningen.

To begreber man støder på:

* **Verification** – bygger vi systemet rigtigt (følger vi designet)?
* **Validation** – bygger vi det rigtige system (løser det opgaven)?

Det er ikke det samme, og begge dele er vigtige.

![alt text](<v-modellen.png>)

---

## 1. Requirements – kravspecifikation

Det første trin handler om at beskrive, hvad systemet skal kunne. Ikke hvordan – det kommer senere – men hvad.

Det er her man samler krav fra kunden, brugeren eller processen. I praksis spænder det fra ret overordnede ting ("operatøren skal kunne starte og stoppe fra HMI") til mere konkrete krav om svartider, sikkerhedsfunktioner og kommunikation.

Nogle eksempler:

* anlægget skal starte og stoppe fra HMI
* en motor må ikke starte, hvis en sikkerhedsbetingelse ikke er opfyldt
* data skal kunne trækkes fra PLC til PC
* kommunikationsforsinkelse må ikke overstige X ms
* anlægget skal give alarmer og kunne håndtere fejl

Man skelner gerne mellem: funktionskrav, sikkerhedskrav, driftskrav, kommunikationskrav og krav til brugerbetjening.

Det man skal have ud af fasen er en kravspecifikation – det hedder nogle gange en URS (User Requirements Specification). Det er det dokument, man til sidst tester imod i accepttesten.

---

## 2. System Design – systemdesign

Nu omsætter man kravene til en samlet teknisk løsning, men stadig på et overordnet niveau. Man beslutter hvilke hoveddele systemet består af og groft hvordan de spiller sammen – PLC, HMI, sensorer, netværk, eventuel PC eller database osv.

Man laver ikke kode her. Det handler om systemets struktur.

Det er her man typisk laver blokdiagrammer, netværksoversigter og beslutter, hvad der skal ligge i hvad. Fx: PLC styrer processen, HMI bruges til lokal betjening, og en Python-applikation trækker data til logging via Snap7.

Output: systembeskrivelse, blokdiagram, hardwareoversigt, overordnet funktionsfordeling.

---

## 3. Architecture Design – arkitekturdesign

Her går man et niveau ned og definerer, hvordan systemets dele konkret hænger sammen. Det handler ikke bare om "PLC snakker med HMI" – man skal beskrive hvad der overføres, via hvilke interfaces og i hvilken retning.

Man fastlægger bl.a.:

* ansvarsfordeling – hvad styres og besluttes hvor
* interfaces og dataflow
* kommunikationsstruktur
* navngivning og struktur i software og data

I et Snap7-projekt er det fx her man beslutter IP-adresser, hvilke DB'er der eksponeres, og hvilke adresser og datatyper der bruges. Det er altså mere end bare "IP-konfiguration" – det er selve den tekniske struktur for samspillet.

Output: interfacebeskrivelser, dataflow, softwarearkitektur, adresse- og tagstruktur.

---

## 4. Module Design – moduldesign

Her beskrives de enkelte funktioner i detaljer. Et modul kan fx være motorstyring, en ventilsekvens, temperaturregulering eller alarmhåndtering – én afgrænset funktion.

Det er på dette niveau, man designer den konkrete styringslogik:

* sekvensforløb og state machine
* interlocks og permissives
* alarmer, resetlogik
* manuelle og automatiske funktioner
* funktionsblokke og parametre

Et motormodul kan fx have tilstandene:
`Stopped → Starting → Running → Fault → Reset`

Man beslutter præcist hvilke betingelser der skal være opfyldt for at motoren må starte, og hvad der stopper den igen.

Output: funktionsbeskrivelser, sekvensdiagrammer, state machines, FB-design.

---

## 5. Coding – implementering

Nu laves selve programmet og den fysiske løsning. Det kan være PLC-kode, HMI-billeder, alarmopsætning, netværkskonfiguration eller Python-kode til Snap7.

Det vigtige er at kodningen **følger designet**. Man bør ikke "finde på løsninger undervejs" – det giver dårlig sporbarhed og gør det sværere at teste bagefter.

Output: færdigt PLC-program, HMI-projekt, kommunikationsopsætning, kode.

---

# Højre side – test og verifikation

Nu testes systemet trin for trin mod det der blev designet på venstre side.

---

## 6. Unit Testing – modultest

Her testes de enkelte moduler isoleret. Altså én funktion ad gangen:

* virker motorblokken rigtigt?
* skifter state machine korrekt mellem Idle, Run og Fault?
* reagerer alarmmodulet som forventet?

I PLC-sammenhæng bruger man her simulation, forcing af signaler og kontrol af transitions. Formålet er at sikre at hver funktion virker, inden man kobler den sammen med resten.

---

## 7. Integration Testing – integrationstest

Her testes om modulerne virker korrekt **sammen**. Man tester nu de interfaces og sammenhænge man definerede i Architecture Design.

Eksempler:

* PLC og HMI udveksler de rigtige data
* Python med Snap7 kan læse og skrive korrekte værdier i PLC
* alarmer vises rigtigt på HMI
* frekvensomformer reagerer korrekt på PLC-kommandoer

Formålet er at sikre at grænseflader og kommunikation fungerer i praksis.

---

## 8. System Testing – systemtest

Her testes hele det samlede system som én enhed – svarer til System Design-trinnet.

Man kigger nu på om hele løsningen opfører sig som beskrevet: starter anlægget korrekt, virker sekvenser i rækkefølge, fungerer betjening fra HMI, håndteres fejl og reset som planlagt?

I automationsprojekter ligner dette typisk en **FAT** (Factory Acceptance Test), men det er vigtigt at skelne: FAT er en praktisk testform, systemtest er V-modellens faglige testniveau.

---

## 9. Acceptance Testing – accepttest

Her vurderes om systemet opfylder de **oprindelige krav** og kan godkendes. Accepttesten modsvarer Requirements-fasen.

Man validerer nu om systemet løser den opgave det blev bestilt til: er kravene opfyldt, kan operatøren bruge systemet, er kapacitet og svartider i orden?

I praksis hedder det SAT eller UAT, afhængigt af projektet.

---

# Koblinger i modellen

Det vigtige at huske:

* **Requirements** ↔ **Acceptance Testing**
* **System Design** ↔ **System Testing**
* **Architecture Design** ↔ **Integration Testing**
* **Module Design** ↔ **Unit Testing**

Hvert designtrin skal altså kunne testes. Hvis man ikke kan formulere en test for et designtrin, er designet sandsynligvis ikke præcist nok.

---

# Et konkret eksempel

**Krav:** Operatøren skal kunne starte og stoppe en motor fra HMI, og en PC skal kunne læse motorstatus via Snap7.

**Systemdesign:** PLC, HMI, motorstarter og PC med Python.

**Arkitekturdesign:** PLC styrer og håndterer sikkerhedslogik. HMI sender kommandoer og viser status. Python læser status fra DB via Snap7.

**Moduldesign:** Motormodul med start, stop, fejl, reset, statusbits og interlock mod overlast.

**Kodning:** PLC-program, HMI-billede og Python-script.

**Modultest:** Test af motormodulet alene.

**Integrationstest:** PLC–HMI og PLC–PC kommunikation.

**Systemtest:** Hele motorstyringen som samlet funktion.

**Accepttest:** Kan operatøren bruge løsningen, og er kravene opfyldt?

---

# Opsummering

V-modellen er en udviklings- og testmodel, hvor krav og design specificeres på venstre side, implementeres i bunden og verificeres/valideres på højre side.

For automationsteknologer er den brugbar fordi den skaber en tydelig sammenhæng mellem krav, design, programmering og test. Det gør det lettere at arbejde systematisk – og dokumentere hvad man har gjort og testet.

---