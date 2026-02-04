# 09 - PLCsim Advanced og VMware: IP-adresser via NAT/DHCP

## 📝 Formål

Formålet er at lære, hvordan man opsætter en simuleret PLC i PLCsim Advanced, forbinder den til et VMware-netkort (fx vmnet8), og observerer at PLC’en får tildelt en IP-adresse fra VMware’s indbyggede DHCP-server.

## 🎯 Kompetencer

* Kan konfigurere PLCsim Advanced med TCP/IP single adapter
* Kan vælge korrekt VMware-netkort (fx vmnet8, bridged/NAT)
* Kan opsætte og starte en simuleret PLC
* Kan observere og forklare IP-tildeling via VMware’s DHCP/NAT

---

## Forudsætninger

* Du har adgang til PLCsim Advanced og TIA Portal
* Du har VMware Workstation eller lignende med netkortet vmnet8 (NAT)

---

## Sådan gør du

### 1. Start PLCsim Advanced

Åbn PLCsim Advanced på din PC.

---

### 2. Vælg TCP/IP single adapter

Gå til **Online access** i PLCsim Advanced.

Vælg **TCP/IP single adapter** som forbindelsestype.

---

### 3. Vælg VMware-netkort (vmnet8)

Vælg det netkort, der hedder **vmnet8** (eller tilsvarende), som er konfigureret til NAT i VMware.

---

### 4. Opsæt og start en simuleret PLC

Opret en ny simuleret PLC i PLCsim Advanced.

Start PLC’en og observer, at den dukker op under Online access.

---

### 5. Observer IP-adresse

Se hvilken IP-adresse PLC’en har fået tildelt.

Notér, at adressen typisk ligger i vmnet8’s DHCP-område (fx 192.168.207.x).

---

## Noter

Udfyld nedenstående:

* Hvilket netkort valgte du? `_____________`
* Hvilken IP-adresse fik PLC’en? `_____________`
* Var det en adresse fra VMware’s DHCP/NAT-område? `_____________`

---

## Observation

Beskriv kort, hvad der sker, når du starter den simulerede PLC:

* Hvordan får PLC’en sin IP-adresse?
* Hvilken rolle spiller VMware’s NAT og DHCP?

*(Skriv dine observationer herunder)*

---

## Refleksion

* Hvorfor har VMware en indbygget DHCP-server på vmnet8?
* Hvilke fordele og ulemper er der ved at bruge NAT og DHCP til simulerede PLC’er?
* Hvordan kan du bruge denne viden i fejlfinding og netværksopsætning?

*(Skriv dine svar herunder)*