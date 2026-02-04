# 06 - Tildel ny IP-adresse til PLC via TIA Portal

## 📝 Formål

Formålet er at lære, hvordan man tildeler en ny IP-adresse til en Siemens PLC direkte fra TIA Portal, efter enheden er fundet med "Accessible devices".

## 🎯 Kompetencer

* Kan finde PLC’en med "Accessible devices"
* Kan navigere til Online Access og diagnosticere enheden
* Kan tildele og ændre IP-adresse på PLC’en via TIA Portal
* Forstår betydningen af unik og korrekt IP-adresse på netværket

---

## Forudsætninger

* Du har adgang til TIA Portal på din PC
* Din PC er forbundet til samme netværk som PLC’en
* Du har fundet PLC’en med "Accessible devices"

---

## Sådan gør du

### 1. Find PLC’en med "Accessible devices"

Følg opgave 05 for at scanne og finde PLC’en på netværket.

---

### 2. Vis PLC’en i projekttræet

Klik på "Show" ud for PLC’en i listen over fundne enheder.

Nu vises PLC’en under:
* **Project tree → Online Access → [dit netkort] → [PLC’en]**

---

### 3. Gå til Online & Diagnostic

Klik på PLC’en under dit netkort i projekttræet.

Vælg **Online & Diagnostic** i højre side.

---

### 4. Vælg Functions og assign ny IP

Klik på **Functions** i menuen.

Vælg **Assign IP address**.

Indtast den ønskede (unikke) IP-adresse og tryk OK.

Vent til PLC’en har fået den nye IP-adresse.

---

## Noter

Udfyld nedenstående:

* Hvilken IP-adresse havde PLC’en før? `_____________`
* Hvilken IP-adresse har du tildelt? `_____________`
* Fik PLC’en den nye adresse? `_____________`

---

## Observation

Beskriv kort, hvad der sker, når du tildeler ny IP-adresse:

* Hvordan kan du se, at PLC’en har fået den nye IP?
* Hvilke netværksændringer observerer du?

*(Skriv dine observationer herunder)*

---

## Refleksion

* Hvorfor er det vigtigt at kunne tildele og ændre IP-adresse på PLC’er?
* Hvilke fejl kan opstå, hvis IP-adressen ikke er unik eller korrekt?

*(Skriv dine svar herunder)*