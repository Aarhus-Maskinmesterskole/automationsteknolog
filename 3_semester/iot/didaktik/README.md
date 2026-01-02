Ja. Her er MD’en, synkroniseret til forløbsplanen i PDF.

# IoT-Bootcamp – Node-RED, ESP32 & Industrial Integration

12 × 3 timer • Aarhus Maskinmesterskole • 2025 • Foreløbig version

Hands-on forløb hvor automationsteknologer konfigurerer sensorer, dashboards, OTA og netværkssikkerhed uden fuld programmeringsbaggrund.

## 🎯 Læringsmål

Efter endt forløb kan du:

* Opbygge komplette Node-RED-flows (inject, debug, function, change, switch, template, ui\_\*).
* Publicere telemetri via MQTT/TLS og anvende topics, QoS, LWT og heartbeat.
* Udsende kommandoer via REST/HTTP(S) og bygge enkle webhooks.
* Integrere Home Assistant via MQTT discovery og designe Lovelace-views.
* Implementere CoAP-endpoints og bygge CoAP→MQTT gateway.
* Gateway’e Modbus TCP-registre til MQTT.
* Integrere Firebase Realtime Database for real-time synkronisering.
* Segmentere IoT-trafik i VLAN og teste firewall/heartbeat i pfSense.
* Analysere trafik i Wireshark og anvende TLS/DTLS korrekt.
* Levere mini-projekt med video-demo og dokumentation i Git.

## 📦 Teknologier & værktøjer

| Kategori        | Værktøj / bibliotek                        |
| --------------- | ------------------------------------------ |
| Flow-motor      | Node-RED (Docker eller lokal)              |
| Hardware        | ESP32 DevKit, IoT-sensorkit                |
| Visualisering   | node-red-dashboard, Home Assistant         |
| Protokoller     | MQTT + TLS, HTTP/REST, CoAP, Modbus TCP    |
| Databaser       | Firebase Realtime Database                 |
| Netværk         | Docker-networks, pfSense (GNS3), Wireshark |
| OTA             | MicroPython-baseret OTA via HTTPS          |
| Sikkerhed       | Certifikat-auth, VLAN-segmentering         |
| Versionsstyring | Git/GitHub (én branch pr. dag)             |

## 📁 Repo-struktur (eksempel)

```
iot-bootcamp/
├── README.md
├── COURSE_SCHEDULE.md
├── common/
│   ├── certificates/
│   ├── docker-compose.core.yml
│   └── assets/       # firmware, scripts, billeder
│
├── dag1-node-red-intro/
├── dag2-iot-monitoring-mqtt/
├── dag3-smart-house-integration/
├── dag4-rest-og-data-storage/
├── dag5-home-assistant/
├── dag6-coap-resource-discovery/
├── dag7-smart-house-integration-2/
├── dag8-modbus-integration/
├── dag9-firebase-rtdb/
├── dag10-netvaerk-og-sikkerhed/
├── dag11-mini-projekt/
└── dag12-afslutning/
```

**Hver dags-mappe** indeholder: `README.md` (teori, mål, opgaver) • Node-RED-flows (.json) klar til import • `assets/` (firmware, certifikater, billeder, scripts) • `extras/` til stretch goals.

## 🧩 Oversigt pr. dag

| Dag | Lek.  | Emne                           | Indhold                                                                                                                       | Læringsaktiviteter & materialer                                                                                                 |
| --- | ----- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 1   | 1–3   | Node-RED Introduktion          | Installation og opstart; editor-tour; simpelt flow: inject → debug → ui\_gauge; grundlæggende databehandling i function-nodes | Øvelser med inject/debug og function/debug; export/import af flows; materialer: Node-RED-opgaver, JSON-export til GitHub.       |
| 2   | 4–6   | IoT Monitoring (MQTT)          | Mosquitto broker; topics og payload; ESP32 publicerer; Node-RED subscriber                                                    | Simuler og visualiser sensordata; Wireshark-analyse af MQTT; materialer: MQTT-flow og capture.                                  |
| 3   | 7–9   | Smart house integration        | Integration af IoT-sensorer i Node-RED; dashboard; automatisering                                                             | Byg flows til automatisering af IoT-house; materialer: hands-on med Node-RED og MQTT.                                           |
| 4   | 10–12 | REST Kommandoer & Data Storage | REST-grundbegreber; POST/GET endpoints i Node-RED; lagring i flow-memory og JSON-fil; CRUD-principper                         | Opret POST/GET for temperatur; gem data; implementer CRUD-API; materialer: `flow.set()`, file-node.                             |
| 5   | 13–15 | Home Assistant & Integrering   | MQTT discovery; integration af sensorer/aktuatorer; Lovelace                                                                  | Opsæt Home Assistant; konfigurer devices via MQTT discovery; visning/styring i Lovelace; materialer: compose-fil, sample YAML.  |
| 6   | 16–18 | CoAP & Resource Discovery      | ESP32 som CoAP-server; Node-RED CoAP-client; GET/OBSERVE; resource discovery                                                  | Implementer CoAP-endpoints; gateway CoAP→MQTT; sammenlign CoAP vs HTTP/MQTT; materialer: battery-test, discovery-log.           |
| 7   | 19–21 | Smart house integration        | Gentagelse/udbygning af dag 3                                                                                                 | Automatiser yderligere; materialer: hands-on med IoT-house.                                                                     |
| 8   | 22–24 | Modbus-integration             | Modbus TCP opsætning; Node-RED Modbus; gateway-mønster: Modbus→MQTT                                                           | Læs Modbus-data; publicér via MQTT; materialer: Node-RED-flows.                                                                 |
| 9   | 25–27 | Firebase RTDB Integration      | Opsæt Firebase RTDB; ESP32/Node-RED/HA integration; real-time sync                                                            | Opret projekt; ESP32→Firebase; Node-RED-flows; HA-integration; materialer: setup-guide, biblioteker.                            |
| 10  | 28–30 | Netværk & Sikkerhed            | VLAN i pfSense; sikkerhedstjek og firewall-rules; MQTT heartbeat/timeout                                                      | Sæt pfSense med flere VLANs; test firewall og heartbeat; materialer: GNS3-projekt, checklist.                                   |
| 11  | 31–33 | Mini-projekt                   | Sensor → cloud → visualisering; færdiggørelse; præsentation; dokumentation                                                    | Udarbejd komplet løsning i grupper; dokumentér og præsenter; materialer: projekt-canvas, SAT/FAT worksheet, video.              |
| 12  | 34–36 | Afslutning                     | Refleksion over læring; feedback og evaluering; afsluttende diskussion                                                        | Refleksion og feedback; diskussion af IoT-udfordringer.                                                                         |

## 📚 Dag-for-dag detaljer

**Dag 1: Node-RED Introduktion**
Indhold: installation, palette/workspace/deploy, inject→debug→ui\_gauge, function-nodes.
Aktiviteter: simple flows, import/eksport, cheat-sheet. Materialer: opgaver, JSON-export.&#x20;

**Dag 2: IoT Monitoring (MQTT)**
Indhold: broker-setup, topics/payload, ESP32→MQTT, Node-RED subscriber.
Aktiviteter: simulér og visualisér data; Wireshark capture. Materialer: MQTT-flow, capture.&#x20;

**Dag 3: Smart house integration**
Indhold: flere sensorer i Node-RED, smart-home dashboard, automatisering.
Aktiviteter: automatiseringsflows.&#x20;

**Dag 4: REST Kommandoer & Data Storage**
Indhold: REST-koncepter; POST/GET; flow-memory og JSON-fil; CRUD; sikkerhedsovervejelser.
Aktiviteter: endpoints for temperatur; gem data; CRUD-API; ekstra: adgangskontrol, backup, dashboard-integration.&#x20;

**Dag 5: Home Assistant & Integrering**
Indhold: MQTT discovery; sensorer/aktuatorer; Lovelace.
Aktiviteter: opsæt HA; konfigurer devices; visning/styring.&#x20;

**Dag 6: CoAP & Resource Discovery**
Indhold: ESP32 som CoAP-server; Node-RED CoAP-client; GET/OBSERVE; discovery.
Aktiviteter: implementér endpoints; gateway CoAP→MQTT; sammenlign med HTTP/MQTT; power/battery-test.&#x20;

**Dag 7: Smart house integration**
Indhold og aktiviteter som dag 3, udbygget.&#x20;

**Dag 8: Modbus-integration**
Indhold: Modbus TCP; Node-RED Modbus; gateway til MQTT.
Aktiviteter: læs registre; publicér til MQTT.&#x20;

**Dag 9: Firebase RTDB Integration**
Indhold: RTDB setup; ESP32/Node-RED/HA integration; real-time sync.
Aktiviteter: projektoprettelse; ESP32-kode; Node-RED-flows; HA-opsætning; real-time test.&#x20;

**Dag 10: Netværk & Sikkerhed**
Indhold: VLAN-segmentering i pfSense; firewall-regler; MQTT heartbeat/timeout; checklist og threat-model.
Aktiviteter: opsæt VLANs; test firewall/heartbeat; GNS3-projekt.&#x20;

**Dag 11: Mini-projekt**
Indhold: sensor→cloud→visualisering; færdiggørelse; præsentation; dokumentation/video.
Aktiviteter: gruppearbejde; dokumentation; demo.&#x20;

**Dag 12: Afslutning**
Indhold: refleksion, feedback, evaluering, diskussion af IoT-udfordringer.&#x20;

## ✅ Slutresultat

* Fuld IoT-prototype fra sensor til dashboard med sikker netværkskonfiguration.
* Versionsstyret repo med flows, konfiguration og dokumentation.
* 5-min demo-video med live data og sikkerhedsovervejelser.

*Synkroniseret til “Detaljeret Forløbsplan • IoT-undervisning (12 dage)”.*&#x20;

Ønsker du, at jeg gemmer dette som `README.md` + `COURSE_SCHEDULE.md` med adskilt dagsoversigt?
