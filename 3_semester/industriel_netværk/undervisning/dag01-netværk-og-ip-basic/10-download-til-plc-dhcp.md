# 10 - Download til simuleret PLC med "IP address from DHCP server"

## 📝 Formål

Formålet er at lære, hvordan man downloader et projekt til en simuleret PLC i PLCsim Advanced, hvor indstillingen "IP address from DHCP server" er valgt i TIA Portal, og observere at PLC’en får tildelt en IP-adresse fra VMware’s DHCP-server.

## 🎯 Kompetencer

* Kan konfigurere PLC’en til at få IP-adresse fra DHCP-server
* Kan navigere til de relevante indstillinger i TIA Portal
* Kan downloade projektet til PLC’en korrekt
* Kan observere og forklare IP-tildeling via DHCP

---

## Forudsætninger

* Du har opsat en simuleret PLC i PLCsim Advanced (se opgave 09)
* Du har adgang til TIA Portal på din PC
* Din PC og PLC’en er forbundet til samme VMware-netkort (vmnet8, NAT)

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

### 4. Sæt "IP address from DHCP server"

Vælg indstillingen **IP address from DHCP server**.

Gem indstillingerne.

---

### 5. Download projektet til PLC’en

Klik på **Download** for at overføre projektet til PLC’en.

Vent til overførslen er færdig og kontroller, at PLC’en er online.

---

### 6. Observer IP-adresse

Se hvilken IP-adresse PLC’en har fået tildelt fra VMware’s DHCP-server.

Notér, at adressen typisk ligger i vmnet8’s DHCP-område (fx 192.168.207.x).

---

## Noter

Udfyld nedenstående:

* Hvilken IP-adresse fik PLC’en fra DHCP-serveren? `_____________`
* Var download succesfuld? `_____________`
* Kan du se PLC’en online efter download? `_____________`

---

## Observation

Beskriv kort, hvad der sker, når du downloader til PLC’en med denne indstilling:

* Hvordan får PLC’en sin IP-adresse?
* Hvilken rolle spiller DHCP-serveren i VMware?

*(Skriv dine observationer herunder)*

---

## Refleksion

* Hvilke fordele og ulemper er der ved at bruge DHCP til simulerede PLC’er?
* Hvordan kan du bruge denne viden i fejlfinding og netværksopsætning?

*(Skriv dine svar herunder)*