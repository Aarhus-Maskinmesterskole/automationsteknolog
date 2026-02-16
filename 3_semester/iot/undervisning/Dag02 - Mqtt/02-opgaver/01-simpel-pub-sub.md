# 📡 Opgave 01 – MQTT Pub/Sub med Node-RED

MQTT er kærneteknologien i IoT-kommunikation. I denne opgave lærer du at sende og modtage beskeder gennem et MQTT-netværk ved hjælp af Node-RED og den offentlige broker `test.mosquitto.org`.

## 🎯 Formål

I denne opgave lærer du at:
- Opsætte forbindelse til en MQTT-broker fra Node-RED
- Oprette en MQTT publisher der sender beskeder
- Oprette en MQTT subscriber der modtager beskeder
- Arbejde med MQTT topics og message payload
- Teste IoT-kommunikation i realtid

---

## ⚡ Grundkoncept

MQTT fungerer som en digital walkie-talkie for IoT-enheder:

- **Publisher** (afsender): Sender beskeder til et specifikt topic
- **Subscriber** (lytter): Lytter på et specifikt topic og modtager beskeder
- **Broker** (postbud): Formidler beskeder mellem publishers og subscribers
- **Topic** (kanal): En unik adresse/sti som beskeder sendes til, fx `stud/3semester/anders/mqtt`

I denne opgave bruger vi `test.mosquitto.org` – en offentlig broker, hvor tusindvis af udviklere verden over tester deres IoT-projekter. Din besked sendes gennem samme infrastruktur som rigtige industrielle sensorer bruger!

---

## 🛠️ Opsætning

### Vælg dit unikke topic

Hver gruppe skal have deres eget topic for at undgå sammenblandinger:

**Format**: `stud/{hold}/{navn}/mqtt`

**Eksempler**:
- `stud/3semester/anders/mqtt`
- `stud/autotek2024/gruppe1/mqtt`
- `stud/iot/maria/test`

> 💡 **Tip**: Brug dit eget navn eller gruppenavn så du er sikker på dit topic er unikt!

---

## 💡 Byg dit MQTT-flow

### Del 1: Opret Subscriber (modtager beskeder)

**Flow-struktur:**
```
[MQTT In] → [Debug]
```

**Trin-for-trin:**

1. **Træk en `mqtt in` node** ind på arbejdsfladen
2. **Dobbeltklik** på noden for at konfigurere:
   - **Server**: Klik på ✏️ blyanten
     - **Server**: `test.mosquitto.org`
     - **Port**: `1883`
     - **Klik "Add"**
   - **Topic**: Indtast dit valgte topic (fx `stud/3semester/anders/mqtt`)
   - **QoS**: `2` (garanteret levering)
   - **Output**: `auto-detect (parsed JSON object or string)`
   - **Name**: "Modtag besked"

3. **Træk en `debug` node** ind
4. **Forbind** mqtt in-noden til debug-noden
5. **Klik Deploy** 🚀

Din subscriber er nu aktiv og lytter!

---

### Del 2: Opret Publisher (sender beskeder)

**Flow-struktur:**
```
[Inject] → [MQTT Out]
```

**Trin-for-trin:**

1. **Træk en `inject` node** ind på arbejdsfladen
2. **Dobbeltklik** og konfigurer:
   - **msg.payload**: Skift til `string` og skriv: `Hello MQTT World!`
   - **msg.topic**: Tomt (sættes i mqtt out-noden)
   - **Name**: "Send besked 1"

3. **Træk en `mqtt out` node** ind
4. **Dobbeltklik** og konfigurer:
   - **Server**: Vælg `test.mosquitto.org` (samme som før)
   - **Topic**: Dit valgte topic (skal være IDENTISK med subscriber!)
   - **QoS**: `2`
   - **Retain**: `false`
   - **Name**: "Publish to broker"

5. **Forbind** inject-noden til mqtt out-noden
6. **Klik Deploy** 🚀

---

### Del 3: Test dit flow

1. **Åbn debug-panelet** (bug-ikonet i højre side)
2. **Klik på knappen** til venstre for din inject-node
3. **Observer** debug-panelet – din besked skulle vise sig!

✅ **Success**: Du har nu sendt din første MQTT-besked gennem internettet!

---

## 🏋️ Øvelser

### Øvelse 1: Send flere beskeder

1. **Kopiér** din inject-node (Ctrl+C, Ctrl+V) to gange
2. **Rediger** hver inject-node til at sende forskellige beskeder:
   - Besked 1: `"Hello MQTT World!"`
   - Besked 2: `"Temperature: 22.5°C"`
   - Besked 3: `"Motor status: RUNNING"`
3. **Forbind** alle tre inject-noder til samme mqtt out-node
4. **Deploy** og test hver besked

### Øvelse 2: JSON payload

MQTT kan også sende struktureret data i JSON-format. Dette er meget brugt i industrielle systemer.

1. **Opret ny inject-node**
2. **Skift payload type til JSON** (`{}`)
3. **Indtast**:
   ```json
   {
     "sensor": "temp001",
     "value": 22.5,
     "unit": "celsius",
     "timestamp": "2026-02-09T10:30:00Z"
   }
   ```
4. **Giv den navnet**: "Send sensor-data"
5. **Forbind** til mqtt out og test
6. **Observer** i debug-panelet hvordan JSON vises

### Øvelse 3: Dynamisk timestamp

1. **Tilføj en function-node** mellem inject og mqtt out:
   ```javascript
   msg.payload = {
       sensor: "temp001",
       value: Math.random() * 30 + 10,  // Tilfældig temp 10-40°C
       unit: "celsius",
       timestamp: new Date().toISOString()
   };
   return msg;
   ```
2. **Opdater flowet:**
   ```
   [Inject] → [Function] → [MQTT Out]
   ```
3. **Test** flere gange – se hvordan timestamp og værdi ændres

### Øvelse 4: Udforskning af QoS

Quality of Service (QoS) bestemmer leveringsgaranti:
- **QoS 0**: Best effort (ingen garanti)
- **QoS 1**: Minimum én gang (kan duplikeres)
- **QoS 2**: Præcis én gang (garanteret)

**Eksperiment:**
1. Skift QoS til 0 på både publisher og subscriber
2. Send flere beskeder hurtigt efter hinanden
3. Observer forskellen (hvis nogen)
4. Diskutér hvornår forskellige QoS-niveauer er relevante

---

## ⚠️ Fejlfindingstips

- **Ser du ikke dine beskeder?**  
  → Tjek at topic er identisk på både mqtt in og mqtt out
  → Må ikke have mellemrum eller specialtegn

- **Får du fejlbesked om broker?**  
  → Tjek internet-forbindelsen  
  → Prøv at redeploy

- **Ser du andres beskeder?**  
  → I bruger samme topic! Lav et mere unikt topic-navn

- **Debug-panelet viser ingenting?**  
  → Tjek at debug-noden ikke er deaktiveret (grå vs. grøn)  
  → Klik på bug-ikonet for at åbne debug-panelet

---

## 🚀 Udvidelser (hvis du vil gå videre)

### Retained Messages
Prøv at sætte **Retain** til `true` på mqtt out-noden. Dette får brokeren til at gemme den sidste besked, så nye subscribers straks får den seneste værdi.

### Wildcard Topics
Prøv at subscribe til `stud/3semester/#` for at modtage beskeder fra alle i klassen. Wildcards:
- `#` = flere niveauer (fx `stud/#` fanger alt under stud)
- `+` = ét niveau (fx `stud/+/mqtt` fanger alle hold)

### Last Will and Testament (LWT)
I advanced broker-settings kan du opsætte en "sidste vilje" – en besked der sendes automatisk hvis din forbindelse brydes.

---

## 🔍 Yderligere ressourcer

- [MQTT.org - Official MQTT Protocol Documentation](https://mqtt.org/)
- [Node-RED MQTT Nodes Documentation](https://cookbook.nodered.org/mqtt/)
- [Eclipse Mosquitto - Test Broker](https://test.mosquitto.org/)
- [HiveMQ - MQTT Essentials Guide](https://www.hivemq.com/mqtt-essentials/)