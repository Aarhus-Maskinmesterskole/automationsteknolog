# 07 - Fabriksindstil PLC og reflekter over ISO-adresse

## 📝 Formål

Formålet er at lære, hvordan man fabriksindstiller en Siemens PLC via TIA Portal, og at reflektere over den ISO-adresse (standard IP-adresse), som PLC’en får efter reset.

## 🎯 Kompetencer

* Kan fabriksindstille PLC via TIA Portal
* Kan finde PLC’en med "Accessible devices" efter reset
* Kan aflæse og forstå PLC’ens ISO-adresse
* Kan reflektere over betydningen af fabriksadresser og netværkssikkerhed

---

## Forudsætninger

* Du har adgang til TIA Portal på din PC
* Din PC er forbundet til samme netværk som PLC’en

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

### 4. Fabriksindstil PLC’en

Klik på **Functions** i menuen.

Vælg **Factory reset** eller tilsvarende funktion.

Bekræft, at du vil fabriksindstille PLC’en.

Vent til PLC’en har genstartet og er fabriksindstillet.

---

### 5. Find PLC’ens ISO-adresse

Brug "Accessible devices" til at finde PLC’en igen.

Aflæs den ISO-adresse (standard IP-adresse), som PLC’en har fået efter reset.

---

## Noter

Udfyld nedenstående:

* Hvilken ISO-adresse har PLC’en efter fabriksindstilling? `_____________`
* Var det den samme som før? `_____________`
* Kan du tilgå PLC’en med denne adresse? `_____________`

---

## Observation

Beskriv kort, hvad der sker, når du fabriksindstiller PLC’en:

* Hvordan ændres PLC’ens IP/ISO-adresse?
* Hvilke netværksændringer observerer du?

*(Skriv dine observationer herunder)*

---

## Refleksion

* Hvorfor har PLC’er en fabriks-ISO-adresse?
* Hvilke sikkerheds- eller netværksmæssige overvejelser skal man gøre sig?
* Hvad er fordelene og ulemperne ved fabriksadresser?

*(Skriv dine svar herunder)*