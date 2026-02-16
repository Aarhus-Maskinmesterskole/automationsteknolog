# Gateway Opgaver

Her er nogle spændende opgaver, der hjælper dig med at øve og forstå IoT-gateways og dataoverførsel. Følg trinene og udforsk, hvordan forskellige protokoller kan arbejde sammen.

---

## 📖 Scenarie: IoT-gateway i praksis
Forestil dig, at du arbejder i en moderne fabrik, hvor forskellige maskiner og sensorer skal kommunikere med hinanden og med et centralt system. Nogle enheder bruger Modbus TCP, mens andre anvender CoAP, og fabrikken ønsker at sende data til en cloud-platform via MQTT. For at få dette til at fungere, skal du opsætte gateways, der kan oversætte mellem protokollerne og sikre, at data flyder problemfrit mellem enhederne. 

Dit mål er at:
- Forstå, hvordan gateways fungerer som bro mellem forskellige protokoller.
- Opsætte enheder og software til at konvertere data mellem Modbus TCP, CoAP og MQTT.
- Visualisere og styre data i realtid via dashboards.

---

## 🛠️ Opgave 1 – Forstå Gateway-konceptet
**Formål:**
- Læs om, hvad en IoT-gateway er, og hvordan den fungerer som en bro mellem IoT-enheder og skyen eller andre netværk.
- **Opgave:** Skriv en kort beskrivelse (3-5 sætninger) af gatewayens rolle i et IoT-system.

---

## 🔄 Opgave 2 – Opsæt en simpel Gateway (Modbus TCP til MQTT)
**Formål:**
- Lær at konvertere data fra Modbus TCP til MQTT og visualisere det.

**Trin:**
1. Arbejd i grupper af mindst to personer (person A og B).
2. **Person A:**
   - Konfigurer en ESP32 til at sende Modbus TCP-data (f.eks. temperaturmålinger) til Node-RED.
   - Konverter dataen til MQTT og send det til en MQTT-broker (f.eks. test.mosquitto.org).
3. **Person B:**
   - Opsæt en Node-RED-instans, der abonnerer på MQTT-brokeren.
   - Præsenter dataen i et dashboard.

---

## 🌐 Opgave 3 – Opsæt en simpel Gateway (CoAP til MQTT)
**Formål:**
- Forstå, hvordan CoAP-data kan konverteres til MQTT og distribueres.

**Trin:**
1. Arbejd i grupper af mindst to personer (person A og B).
2. **Person A:**
   - Konfigurer en CoAP-enhed (ESP32) til at sende data til Node-RED.
   - Konverter dataen til MQTT og send det til en MQTT-broker.
3. **Person B:**
   - Opsæt en Node-RED-instans, der abonnerer på MQTT-brokeren.
   - Præsenter dataen i et dashboard.

---

## ⚙️ Opgave 4 – Opsæt en simpel Gateway (MQTT til Modbus TCP)
**Formål:**
- Lær at konvertere data fra MQTT til Modbus TCP for at styre aktuatorer.

**Trin:**
1. Arbejd i grupper af mindst to personer (person A og B).
2. **Person A:**
   - Opsæt en Node-RED-instans, der publicerer data (styringssignaler) til en MQTT-broker (f.eks. test.mosquitto.org).
3. **Person B:**
   - Opsæt en Node-RED-instans, der abonnerer på dette topic.
   - Konverter dataen til Modbus TCP, som ESP32-enheden kan bruge til at tænde og slukke for diverse aktuatorer.

---

**💡 Tip:**
- Brug Node-RED's indbyggede værktøjer til at debugge og overvåge dataflowet.
- Eksperimentér med forskellige datatyper og protokoller for at få en dybere forståelse.