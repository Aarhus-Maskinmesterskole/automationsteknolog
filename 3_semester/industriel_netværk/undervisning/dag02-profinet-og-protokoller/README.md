# 📡 Dag 02 – Industriel Kommunikation: S7comm, Open User Communication og Web Integration

Velkommen til dag 2! I dag skal I lære at få Siemens PLC'er (S7-1200/1500) til at kommunikere med andre systemer via tre forskellige metoder. Dette er fundamentale kompetencer for moderne industriel automation, hvor PLC'er skal integreres med IT-systemer, databaser, web-applikationer og andre PLC'er.

---

## 🎯 Læringsmål

Efter dagens undervisning og opgaver kan I:

### Teoretisk forståelse:
- ✅ Forklare forskellen mellem S7-kommunikation, Open User Communication (OUC) og Web Server
- ✅ Vælge den rette kommunikationsmetode baseret på use case
- ✅ Forstå TCP/IP kommunikation i industriel kontekst
- ✅ Beskrive fordele og begrænsninger ved hver kommunikationstype

### Praktiske færdigheder:
- ✅ Konfigurere S7-kommunikationsblokke (BSEND, TSEND, PUT, GET) i TIA Portal
- ✅ Etablere TCP-forbindelser mellem PLC'er med TCON/TDISCON
- ✅ Opsætte og teste dataudveksling med TSEND/TRECV
- ✅ Konfigurere og aktivere Siemens Web Server på PLC
- ✅ Oprette custom websider til proces-overvågning
- ✅ Implementere WebSocket kommunikation mellem PLC og Python

---

## 🧭 Dagens Indhold

### Del 1: S7-Communication (1-1.5 timer)
**Fokus:** PLC-til-PLC kommunikation med Siemens proprietære protokol

I får en introduktion til de vigtigste S7-kommunikationsblokke og deres anvendelsesområder:
- **BSEND** - Sender store datasæt (batch data, konfigurationsfiler)
- **TSEND_C** - Almindelig TCP dataoverførsel med forbindelseskontrol
- **TSEND** - Sekventiel/kontinuerlig datastrømme
- **PUT/GET** - Direkte dataudveksling mellem PLC'er

**Hvad lærer I?**
- Hvornår bruge hvilken blok
- Datatyper og strukturer der kan sendes
- Best practices for store datamængder

### Del 2: Open User Communication - OUC (2-2.5 timer)
**Fokus:** TCP/IP kommunikation med standardprotokoller

Her kommer I til at arbejde hands-on med:
- **TCON** - Etablere TCP-forbindelser
- **TDISCON** - Afslutte forbindelser korrekt
- **TSEND** - Sende data over TCP
- **TRECV** - Modtage data fra TCP

**Praktisk opgave:**
I skal opsætte kommunikation mellem to PLC'er:
- PLC A sender data til PLC B
- PLC B modtager og sender bekræftelse tilbage
- Implementer timeout og fejlhåndtering
- Test med forskellige datatyper

### Del 3: Siemens Web Server & WebSocket (2-3 timer)
**Fokus:** Web-integration og moderne API-kommunikation

**Opgave 3.1 - Web Server Konfiguration:**
- Aktivere webserver på både fysisk S7-1200 og simuleret S7-1500
- Oprette custom websider for proces-visualisering
- Vise real-time procesdata i browser
- Test og verifikation af webserver-funktionalitet

**Opgave 3.2 - WebSocket Integration:**
- Opsætte HTML-klient på PLC webserver
- Oprette Python WebSocket server
- Etablere real-time datakommunikation
- Sende/modtage beskeder mellem PLC og Python

---

## 📋 Opgavetyper

### 🔧 Type 1: Konfigurationsopgaver
**Eksempel:** Aktivere webserver, opsætte IP-adresser, konfigurere funktionsblokke

**Hvad I lærer:** 
- Navigation i TIA Portal
- Netværkskonfiguration
- Hardware setup

**Sværhedsgrad:** ⭐⭐☆☆☆

---

### 🔨 Type 2: Implementeringsopgaver
**Eksempel:** Opret TCON/TDISCON funktionsblokke, implementer TSEND/TRECV dataudveksling

**Hvad I lærer:**
- Programmering i Ladder/SCL
- Datastrukturer og buffers
- Fejlhåndtering
- Timing og synkronisering

**Sværhedsgrad:** ⭐⭐⭐☆☆

---

### 🧪 Type 3: Test og Troubleshooting
**Eksempel:** Verificer dataudveksling, fejlfind forbindelsesproblemer, test WebSocket kommunikation

**Hvad I lærer:**
- Diagnostiske værktøjer i TIA Portal
- Wireshark til netværksanalyse
- Systematisk fejlfinding
- Performance monitoring

**Sværhedsgrad:** ⭐⭐⭐⭐☆

---

### 📝 Type 4: Dokumentationsopgaver
**Eksempel:** Netværksdiagrammer, konfigurationsdokumentation, testrapporter

**Hvad I lærer:**
- Teknisk dokumentation
- Skærmbilleder og annoteringer
- Struktureret rapportering
- Best practices

**Sværhedsgrad:** ⭐⭐☆☆☆

---

## ✅ Kompetencer Efter Opgaverne

### 🎓 Grundlæggende niveau (alle skal kunne):
- [x] Konfigurere IP-adresser på Siemens PLC
- [x] Etablere TCP-forbindelse mellem to PLC'er
- [x] Sende og modtage simple data (integers, booleans)
- [x] Aktivere og tilgå Siemens Web Server
- [x] Oprette basic webside på PLC
- [x] Bruge diagnostiske værktøjer til fejlfinding

### 🚀 Avanceret niveau (ekstra udfordringer):
- [x] Implementere komplekse datastrukturer (arrays, UDT'er)
- [x] Bygge robust fejlhåndtering med timeout og retry-logik
- [x] Oprette interaktive websider med JavaScript
- [x] Implementere WebSocket kommunikation med Python
- [x] Analysere netværkstrafik med Wireshark
- [x] Optimere dataudveksling for performance

### 💼 Professionelle færdigheder:
- [x] **Systemintegration:** Forbinde PLC med IT-systemer
- [x] **Protokol-valg:** Vælge rigtig kommunikationsmetode for opgaven
- [x] **Netværksdesign:** Designe industrielle netværksarkitekturer
- [x] **Fejlhåndtering:** Implementere robust error handling
- [x] **Dokumentation:** Professionel teknisk dokumentation
- [x] **Troubleshooting:** Systematisk fejlfinding i komplekse systemer

---

## 🗂️ Opgavestruktur

### 📄 [01-S7communication.md](01-S7communication.md)
**Indhold:**
- Teori om BSEND, TSEND_C, TSEND, PUT/GET
- Datatyper og use cases
- Best practices for dataudveksling

**Estimeret tid:** 45-60 minutter

---

### 📄 [02-Open-User-Communication.md](02-Open-User-Communication.md)
**Indhold:**
- TCON/TDISCON konfiguration
- TSEND/TRECV implementering
- Praktisk opgave: PLC A ↔ PLC B kommunikation
- Fejlhåndtering og timeout
- Netværksdiagrammer og dokumentation

**Estimeret tid:** 2-2.5 timer

---

### 📂 [03-web-server/](03-web-server/)
**Indhold:**

#### [01-webserver-configuration.md](03-web-server/01-webserver-configuration.md)
- Aktivere webserver på S7-1200 (fysisk)
- Simulere webserver på S7-1500 med PLCSIM Advanced
- Oprette custom websider
- Test og verifikation

**Estimeret tid:** 1-1.5 timer

#### [02-Websocket.md](03-web-server/02-Websocket.md)
- HTML-klient på PLC webserver
- Python WebSocket server setup
- Real-time datakommunikation
- Test med browser og Python

**Estimeret tid:** 1.5-2 timer

---

## 💡 Tips til Succes

### 🎯 Før I går i gang:
1. **Læs teorien først** - Forstå forskellen mellem de tre metoder
2. **Tjek netværk** - Verificer IP-adresser og forbindelser
3. **Backup projekter** - Gem ofte, især før store ændringer
4. **Arbejd systematisk** - Fuldfør én opgave ad gangen

### 🔧 Under opgaverne:
- Brug **Online & Diagnostics** i TIA Portal til at overvåge kommunikation
- Test med **simple data først** (fx integers) før komplekse strukturer
- Dokumenter **alle konfigurationer** med skærmbilleder
- Spørg underviser hvis I **sidder fast i >15 minutter**

### ✅ Efter opgaverne:
- Verificer at **alle test-cases fungerer**
- Tjek at **dokumentationen er komplet**
- Eksperimentér med **bonus-udfordringer**
- Reflekter over **hvad I har lært**

---

## 🆘 Hjælp og Ressourcer

### Dokumentation:
- **TIA Portal Help** - F1 i TIA Portal
- **Siemens Industry Online Support** - support.industry.siemens.com
- **GitHub repositorie** - Se eksempler og kode

### Spørgsmål?
- Ræk hånden op 🙋
- Spørg klassekammeraterne
- Check Siemens dokumentation
- Brug diagnostiske værktøjer

---

## 🎉 Held og Lykke!

I dag lærer I fundamentale skills til industriel netværkskommunikation. Disse kompetencer er **essentielle** for moderne automationsingeniører og bruges dagligt i industrien.

**Gå i gang med opgave 01 og arbejd jer gennem dem systematisk!** 🚀
