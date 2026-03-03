# MQTT TLS Sikkerhed - Læringsmodul

## 📋 Oversigt

Dette modul introducerer studerende til sikker MQTT-kommunikation gennem Transport Layer Security (TLS). Gennem praktiske øvelser lærer de at implementere end-to-end krypteret MQTT-kommunikation, der er essentiel for sikker IoT-infrastruktur i produktionsmiljøer.

## 🎯 Læringsmål

Ved gennemførelse af dette modul vil studerende kunne:

### Tekniske Færdigheder
- **Konfigurere sikker MQTT-broker** med TLS-kryptering og brugergodkendelse
- **Generere og administrere digitale certifikater** (CA, server-certifikater)
- **Implementere TLS-baseret MQTT-klienter** i Python
- **Anvende Docker Compose** til orchestrering af sikre tjenester
- **Fejlfinde TLS-forbindelsesproblemer** og certificeringsfejl

### Sikkerhedsforståelse
- **Forstå forskellen** mellem sikker (TLS) og usikker MQTT-kommunikation
- **Implementere autentificering** med brugernavn/adgangskode
- **Analysere netværkstrafik** med Wireshark for at verificere kryptering
- **Identificere sikkerhedsrisici** i IoT-kommunikation

### Industriel Anvendelse
- **Konfigurere produktionsklare MQTT-setup** med sikkerhed
- **Forstå certifikatadministration** i større systemer
- **Implementere best practices** for IoT-sikkerhed

## 📚 Modulindhold

### Del A-B: Projektopsætning
- Installation af værktøjer og projektstruktur
- Docker-baseret udviklingsmiljø

### Del C-D: Sikker MQTT Broker
- Docker Compose konfiguration med certifikatgenerering
- Mosquitto broker opsætning med TLS og autentificering
- Certificeringshieraki (CA → Server certifikat)

### Del E: Certificering og Brugerstyring
- Automatisk certifikatgenerering med OpenSSL
- Oprettelse af godkendte MQTT-brugere
- Verifikation af broker-funktion

### Del F: CLI Testing
- Container-baseret test af MQTT TLS-forbindelse
- Publish/Subscribe mønster med kryptering

### Del G: Python Implementation
- Udvikling af sikre MQTT-klienter
- Håndtering af TLS-certifikater i Python
- Error handling og debugging

### Del H: Netværksanalyse og Fejlfinding
- Wireshark analyse af krypteret trafik
- Almindelige TLS-fejl og løsninger
- Troubleshooting guide

## 🔧 Teknologier og Værktøjer

- **Docker & Docker Compose**: Containerisering og tjeneste-orchestrering
- **Eclipse Mosquitto**: Open source MQTT broker
- **OpenSSL**: Certifikatgenerering og TLS-opsætning
- **Python paho-mqtt**: MQTT klient bibliotek
- **Wireshark**: Netværksanalyse og pakke-inspektion

## 🚀 Praktisk Relevans

Dette modul forbereder studerende til:
- **Industrielle IoT-projekter** hvor datasikkerhed er kritisk
- **Automation systemer** med sikker fjernkommunikation
- **Smart building** løsninger med krypteret sensorkommunikation
- **Compliance** med industrielle sikkerhedsstandarder

## ⚡ Forudsætninger

- Grundlæggende kendskab til MQTT protokollen
- Docker Desktop installation
- Python 3.10+ installation
- Grundlæggende kommandolinje erfaring

## 📖 Anvendelse

1. **Læs `mqtt-tls.md`** for detaljeret step-by-step guide
2. **Følg alle trin systematisk** - hver sektion bygger på den forrige
3. **Test løbende** - verificer funktionalitet efter hver sektion
4. **Eksperimentér** med forskellige konfigurationer og parametre

## 🔍 Uddybende Læring

Efter gennemførsel kan studerende udforske:
- Mutual TLS (mTLS) med klient-certifikater
- Integration med cloud MQTT-tjenester
- MQTT over WebSockets med TLS
- Skalering til flere brokers med load balancing

