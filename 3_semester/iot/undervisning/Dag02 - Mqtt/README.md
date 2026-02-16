# MQTT
MQTT (Message Queuing Telemetry Transport) er en letvægtsprotokol designet til at forbinde enheder i IoT (Internet of Things) miljøer. Den fungerer efter et publicer/abonner (publish/subscribe) mønster, hvor enheder kan sende (publicere) data til en central broker, som derefter distribuerer disse data til andre enheder, der har abonneret på de relevante emner (topics).

publisher/abonner (publish/subscribe) adskiller sig fra traditionelle klient-server modeller ved, at enheder ikke behøver at kende hinandens adresser direkte. I stedet kommunikerer de via en broker, hvilket gør systemet mere fleksibelt og skalerbart.

Analogi: Tænk på MQTT som et postvæsen, hvor enheder sender breve (data) til en postcentral (broker), som derefter leverer dem til modtagere (abonnenter) baseret på deres interesser (topics).

MQTT sender data i små pakker på 2 bytes, hvilket gør det ideelt til enheder med begrænsede ressourcer og netværk med lav båndbredde. Protokollen er designet til at være enkel og effektiv, hvilket gør den velegnet til realtidsapplikationer som fjernovervågning, hjemmeautomatisering og industrielle IoT-løsninger.

MQTT Features:
- **Last will and testament**: En funktion, der tillader enheder at sende en besked, hvis de mister forbindelsen uventet.
    - Dette er nyttigt for at informere andre enheder om enhedens status.
- **Keep alive**: En mekanisme, der sikrer, at forbindelsen mellem enheden og broker forbliver aktiv ved at sende regelmæssige "ping" beskeder.
    - Hvis broker ikke modtager en ping inden for en bestemt tidsramme, antager den, at enheden er offline.
- **Quality of Service (QoS)**: Tre niveauer af leveringstjenester for beskeder, der sikrer pålidelighed.
    - QoS 0: Beskeden leveres "højst én gang" (ingen bekræftelse).
    - QoS 1: Beskeden leveres "mindst én gang" (bekræftelse kræves).
    - QoS 2: Beskeden leveres "præcis én gang" (sikrer ingen duplikater).
- **Retained messages**: Beskeder, der gemmes af broker, så nye abonnenter straks modtager den seneste besked ved tilmelding.
---

## Installation af MQTT Broker i Docker compose
For at installere en MQTT broker som Mosquitto i en Docker container, kan du følge disse trin:
1. Sørg for, at Docker er installeret på din maskine.
2. Opret en `docker-compose.yml` fil med følgende indhold:
```yaml
version: '3'
services:
  mosquitto:
    image: eclipse-mosquitto
    ports:
      - "1883:1883"
      - "8883:8883"
      - "9001:9001"
    volumes:
      - mosquitto_data:/mosquitto/data
      - mosquitto_config:/mosquitto/config
volumes:
  mosquitto_data:
  mosquitto_config:
```
3. Kør kommandoen `docker-compose up -d` i terminalen for at starte Mosquitto broker i baggrunden.
4. Broker vil nu være tilgængelig på din lokale maskine via port 1883 (standard MQTT port).
5. Konfigurationsfilen kan findes i den mappe, der er bundet til `/mosquitto/config` i containeren, da vi ønsker at ændre standardindstillinger.
- Du skal finde den fil `mosquitto.conf` og redigere.
- Filen skal indeholde følgende indstillinger for at tillade anonyme forbindelser (til testformål):
    ```plaintext
    log_timestamp true
    log_type all
    log_dest stdout

    persistence true
    persistence_location /mosquitto/data/

    per_listener_settings true

    # MQTT/TCP
    listener 1883 0.0.0.0
    protocol mqtt
    allow_anonymous true         # ← Sæt her, fordi per_listener_settings=true

    # MQTT over WebSockets
    listener 9001 0.0.0.0
    protocol websockets
    socket_domain ipv4
    allow_anonymous true         # ← Sæt også her
    ```
- Gem filen og genstart broker med `docker-compose restart mosquitto`.
6. For at stoppe broker, brug kommandoen `docker-compose down`.

---

## Test MQTT fra Kommandoprompt
1. Åbn en ny terminal og kør følgende kommando for at abonnere på et emne (topic):

```bash
mosquitto_sub -h localhost -t "test/topic"
```
2. Åbn en anden terminal og kør følgende kommando for at publicere en besked til det samme emne:

```bash
mosquitto_pub -h localhost -t "test/topic" -m "Hello MQTT"
```
3. Du skulle nu se beskeden "Hello MQTT" i den første terminal, hvor du abonnerede på emnet.

---

## MQTT Clients
Der findes mange forskellige MQTT-klienter til forskellige programmeringssprog og platforme. Nogle populære MQTT-klientbiblioteker inkluderer:
- **Paho MQTT**: Tilgængelig for Python, Java, JavaScript, C/C++, og flere.
- **MQTT.js**: En populær MQTT-klient til Node.js og browseren.
- **Eclipse Mosquitto Clients**: Kommando-linje værktøjer som `mosquitto_pub` og `mosquitto_sub`.
- **HiveMQ MQTT Client**: En robust MQTT-klient til Java-applikationer.

Disse klienter gør det nemt at integrere MQTT i dine applikationer og enheder, uanset hvilket sprog eller platform du arbejder med.

---

## MQTT i Node-RED
Node-RED har indbyggede noder til at arbejde med MQTT, hvilket gør det nemt at integrere MQTT-baserede enheder og tjenester i dine flows.
### Brug af MQTT noder i Node-RED:
1. **MQTT Input Node**: Bruges til at abonnere på et MQTT-emne og modtage beskeder.
2. **MQTT Output Node**: Bruges til at publicere beskeder til et MQTT-emne.
3. **MQTT Broker Konfiguration**: Du skal konfigurere forbindelsen til din MQTT-broker i Node-RED's indstillinger.

### Opgave: Opsætning af MQTT i Node-RED
1. Åbn Node-RED og træk en MQTT-in node ind i dit flow.
2. Dobbeltklik på noden for at konfigurere den:
   - Klik på blyantikonet ved siden af "Server" for at tilføje din MQTT-broker (f.eks. `localhost:1883`).
   - Indtast det emne, du vil abonnere på (f.eks. `test/topic`).
3. Tilslut MQTT Input noden til en Debug node for at se modtagne beskeder.
4. Træk en Inject node ind i dit flow for at sende testbeskeder.
5. Træk en MQTT-Out node ind i dit flow.
6. Dobbeltklik på MQTT-Out noden for at konfigurere den:
   - Vælg den samme broker som før.
   - Indtast det emne, du vil publicere til (f.eks. `test/topic`).
7. Tilslut Inject noden til MQTT-Out noden.
8. Deploy dit flow og test ved at trykke på Inject noden. Du skulle nu se beskeden i Debug-vinduet.


## Sky baserede MQTT Brokers
Der findes flere sky-baserede MQTT-brokers, som tilbyder hosting og skalerbarhed til dine MQTT-applikationer. Nogle populære muligheder inkluderer:
- **AWS IoT Core**: Amazon Web Services tilbyder en fuldt administreret MQTT-broker med integration til andre AWS-tjenester.
- **Azure IoT Hub**: Microsofts IoT-platform understøtter MQTT og tilbyder skalerbarhed og sikkerhed.
- **Google Cloud IoT Core**: Google Cloud tilbyder en MQTT-broker som en del af deres IoT-løsninger.
- **HiveMQ Cloud**: En kommerciel MQTT-broker service, der tilbyder høj tilgængelighed og skalerbarhed.
- **Eclipse Mosquitto**: Tilbyder også en sky-baseret MQTT-broker løsning. Eclipse har en gratis broker til testformål på *test.mosquitto.org*, men man skal være opmærksom på at alle kan tilgå den ikke kun lokalt på skolen men globalt.

### Opgave: Node-RED Konfiguration for Sky-baseret MQTT Broker
Når du bruger en sky-baseret MQTT-broker, skal du konfigurere din Node-RED MQTT-in og MQTT-out noder med de relevante broker-adresser (*test.mosquitto.org*), portnumre (1883 for ukrypteret, 8883 for TLS), og eventuelle nødvendige autentificeringsoplysninger (brugernavn, adgangskode, certifikater osv.).

1. Åbn Node-RED og træk en MQTT-in node ind i dit flow.
2. Dobbeltklik på noden for at konfigurere den:
   - Klik på blyantikonet ved siden af "Server" for at tilføje din sky-baserede MQTT-broker (f.eks. `test.mosquitto.org:1883`).
   - Indtast det emne, du vil abonnere på (f.eks. `test/topic`).
3. Tilslut MQTT Input noden til en Debug node for at se modtagne beskeder.
4. Træk en Inject node ind i dit flow for at sende testbeskeder.
5. Træk en MQTT-Out node ind i dit flow.
6. Dobbeltklik på MQTT-Out noden for at konfigurere den:
   - Vælg den samme sky-baserede broker som før.
   - Indtast det emne, du vil publicere til (f.eks. `test/topic`).
7. Tilslut Inject noden til MQTT-Out noden.
8. Deploy dit flow og test ved at trykke på Inject noden. Du skulle nu se beskeden i Debug-vinduet.

### Opgave: Kommunikere med klasse kammerater via Sky-baseret MQTT Broker
1. Få dine klassekammeraters broker-adresse og emne (topic).
2. Konfigurer dine MQTT-in og MQTT-out noder i Node-RED med de relevante oplysninger fra dine klassekammerater.
3. Test kommunikationen ved at sende beskeder mellem jeres flows.