# 08 - Download til PLC med "IP address is set directly at the device"

## 📝 Formål

Formålet er at lære, hvordan man downloader et projekt til en Siemens PLC, når indstillingen "IP address is set directly at the device" er valgt i TIA Portal.

## 🎯 Kompetencer

* Kan konfigurere PLC’en til at få IP-adresse direkte på enheden
* Kan navigere til de relevante indstillinger i TIA Portal
* Kan downloade projektet til PLC’en korrekt
* Forstår forskellen på IP-konfiguration via software vs. direkte på enheden

---

## Forudsætninger

* Du har adgang til TIA Portal på din PC
* Din PC er forbundet til samme netværk som PLC’en
* PLC’en har en unik og statisk IP-adresse, sat direkte på enheden

---

## Sådan gør du

### 1. Åbn Device Configuration

I projekttræet, klik på din PLC under **Project tree → Device configuration**.

---

### 2. Gå til Properties på PLC’en

Klik på **Properties** for PLC’en.

---

### 3. Vælg Ethernet addresses

Find sektionen **Ethernet addresses**.

---

### 4. Sæt "IP address is set directly at the device"

Vælg indstillingen **IP address is set directly at the device**.

Indtast den IP-adresse, som er sat fysisk på PLC’en.

---

### 5. Download projektet til PLC’en

Klik på **Download** for at overføre projektet til PLC’en.

Vent til overførslen er færdig og kontroller, at PLC’en er online.

---

## Noter

Udfyld nedenstående:

* Hvilken IP-adresse har du sat på PLC’en? `_____________`
* Var download succesfuld? `_____________`
* Kan du se PLC’en online efter download? `_____________`

---

## Observation

Beskriv kort, hvad der sker, når du downloader til PLC’en med denne indstilling:

* Hvordan adskiller det sig fra at sætte IP via TIA Portal?
* Hvilke fordele/ulemper ser du?

*(Skriv dine observationer herunder)*

---

## Refleksion

* Hvornår er det en fordel at sætte IP-adressen direkte på enheden?
* Hvilke situationer kan give problemer med denne metode?

*(Skriv dine svar herunder)*