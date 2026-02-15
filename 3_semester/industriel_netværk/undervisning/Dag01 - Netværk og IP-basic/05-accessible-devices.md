# 05 - Accessible devices i TIA Portal – find og identificér enheder på netværket

## 📝 Formål

Formålet er at lære at bruge funktionen "Accessible devices" i Siemens TIA Portal til at finde og identificere PLC’er og andre Siemens-enheder på det lokale netværk.

## 🎯 Kompetencer

* Kan bruge "Accessible devices" til at scanne efter Siemens-enheder
* Forstår forskellen på at finde enheder via IP og via "Accessible devices"
* Kan aflæse MAC- og IP-adresser på fundne enheder
* Kan forklare, hvordan TIA Portal finder enheder på netværket

---


## Forudsætninger

* Du har adgang til TIA Portal på din PC
* Din PC er forbundet til samme netværk som en eller flere Siemens PLC’er
* **PLC’en skal have en unik IP-adresse, som ikke bruges af andre enheder på netværket.**
	- Indstil PLC’ens IP-adresse via TIA Portal eller direkte på enheden, så der ikke opstår IP-konflikter.

---

## Sådan gør du


### 1. Åbn TIA Portal og et projekt

Start TIA Portal og åbn et eksisterende projekt, eller opret et nyt projekt.

---

### 2. Start "Accessible devices"

Klik på "Online access" i projekttræet til venstre.

Klik på det relevante netværkskort (fx din Ethernet-adapter).

Klik på "Accessible devices"-knappen (eller højreklik og vælg "Accessible devices").

---

### 3. Scan efter enheder

TIA Portal scanner nu netværket for Siemens-enheder.

Vent til listen over fundne enheder vises.

---

### 4. Aflæs information om enhederne

For hver fundet enhed kan du se:
* Enhedstype (fx S7-1200, S7-1500, HMI)
* IP-adresse `______________`
* MAC-adresse `______________`
* Navn (hvis konfigureret) `______________`

---

## Noter

Udfyld nedenstående:

* Hvor mange enheder fandt du? `_____________`
* Hvilke typer? `_____________`
* IP-adresser: `_____________`
* MAC-adresser: `_____________`
* Var der enheder uden IP-adresse? `_____________`

---

## Observation

Beskriv kort, hvad der sker i netværket, når du bruger "Accessible devices":

* Hvordan finder TIA Portal enhederne? (fx broadcast, protokol)
* Kan du finde enheder, selvom du ikke kender deres IP-adresse?
* Hvilke oplysninger får du, som du ikke får med ping/arp?

*(Skriv dine observationer herunder)*

---

## Refleksion

* Hvornår er "Accessible devices" nyttigt i praksis?
* Hvilke begrænsninger har metoden?
* Hvordan adskiller det sig fra almindelig netværksscanning?

*(Skriv dine svar herunder)*