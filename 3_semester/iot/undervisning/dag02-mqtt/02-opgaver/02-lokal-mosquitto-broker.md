# 🐳 Opgave 02 – Lokal MQTT Broker med Docker

Nu hvor du har lært at arbejde med en offentlig MQTT-broker, skal du opsætte din egen lokale Mosquitto broker ved hjælp af Docker. Dette giver dig fuld kontrol over broker-konfigurationen og er tættere på hvordan det fungerer i produktionsmiljøer.

## 🎯 Formål

I denne opgave lærer du at:
- Opsætte Mosquitto MQTT broker med Docker
- Konfigurere Mosquitto til ekstern adgang
- Forbinde Node-RED til din lokale broker
- Forstå forskellen mellem lokal og offentlig broker
- Teste kommunikation mellem forskellige PC'er i netværket

---

## 🧰 Forudsætninger

* Docker Desktop installeret og kørende
* Node-RED installeret og kørende
* Grundlæggende kendskab til MQTT (se Opgave 01)
* Adgang til at udpakke .rar filer (WinRAR, 7-Zip eller lignende)

---

## 📦 Del 1: Opsætning af Mosquitto via Docker

### Metode A: Brug den medfølgende Docker Compose-fil

1. **Find og udpak .rar filen**
   - Lokalisér filen `mosquitto-docker.rar` i kursusmaterielet
   - Højreklik → "Extract Here" eller brug dit udpakningsprogram
   - Du får en mappe med følgende struktur:
     ```
     mosquitto-docker/
     ├── docker-compose.yml
     ├── mosquitto/
     │   ├── config/
     │   │   └── mosquitto.conf
     │   ├── data/
     │   └── log/
     ```

2. **Åbn terminal i mappen**
   - Åbn PowerShell eller Command Prompt
   - Navigér til `mosquitto-docker` mappen:
     ```bash
     cd sti\til\mosquitto-docker
     ```
     eller højreklik på mappen i VS Code og vælg "Open in Terminal"

3. **Start Mosquitto**
   - find docker-compose filen i terminalen og kør:
   ```bash
   docker-compose up -d
   ```
   eller højreklik på `docker-compose.yml` i VS Code og vælg "Compose Up"

   Forventede output:
   ```
   Creating network "mosquitto-docker_default" with the default driver
   Creating mosquitto ... done
   ```

4. **Verificér at containeren kører**
   ```bash
   docker ps
   ```
   
   Du skulle se noget lignende:
   ```
   CONTAINER ID   IMAGE                    STATUS         PORTS
   xxxxxxxxxxxx   eclipse-mosquitto:latest Up X minutes   0.0.0.0:1883->1883/tcp
   ```

---

### Metode B: Opret din egen Docker Compose-fil (hvis Metode A ikke virker)

Hvis den medfølgende setup ikke virker, lav din egen:

1. **Opret mappestruktur**
   ```bash
   mkdir mosquitto-broker
   cd mosquitto-broker
   mkdir -p mosquitto/config mosquitto/data mosquitto/log
   ```

2. **Opret `docker-compose.yml`**
   
   Opret en fil kaldet `docker-compose.yml` i `mosquitto-broker` mappen:

   ```yaml
   version: '3.8'
   
   services:
     mosquitto:
       image: eclipse-mosquitto:latest
       container_name: mosquitto
       restart: unless-stopped
       ports:
         - "1883:1883"
         - "9001:9001"
       volumes:
         - ./mosquitto/config:/mosquitto/config
         - ./mosquitto/data:/mosquitto/data
         - ./mosquitto/log:/mosquitto/log
       networks:
         - mqtt-network
   
   networks:
     mqtt-network:
       driver: bridge
   ```

3. **Opret `mosquitto.conf`**
   
   Opret filen `mosquitto/config/mosquitto.conf`:

   ```conf
   # Mosquitto Configuration File
   
   # Lyt på alle netværksinterfaces
   listener 1883
   allow_anonymous true
   
   # WebSocket support (valgfrit)
   listener 9001
   protocol websockets
   
   # Persistens - gem beskeder
   persistence true
   persistence_location /mosquitto/data/
   
   # Log til fil
   log_dest file /mosquitto/log/mosquitto.log
   log_dest stdout
   
   # Log-typer
   log_type error
   log_type warning
   log_type notice
   log_type information
   
   # Tillad adgang fra eksterne hosts
   # VIGTIGT: Dette er kun til test! Brug authentication i produktion
   ```

4. **Start brokeren**
   ```bash
   docker-compose up -d
   ```

5. **Tjek logs for fejl**
   ```bash
   docker-compose logs -f mosquitto
   ```
   eller højreklik på containeren i Docker Desktop og vælg "View Logs"

---

## 🌐 Del 2: Find din IP-adresse

For at andre kan forbinde til din broker, skal du finde din lokale IP-adresse ved hjælp af følgende kommando i terminalen:

**Windows:**
```bash
ipconfig
```
Kig efter "IPv4 Address" under din netværksadapter (typisk noget som `192.168.1.x`)

**Linux/Mac:**
```bash
ip addr show
# eller
ifconfig
```

> 💡 **Eksempel IP**: `192.168.1.209`  
> Notér din IP – du skal bruge den senere!

---

## 💡 Del 3: Opret MQTT-flow i Node-RED

### Subscriber (modtager beskeder)

**Flow-struktur:**
```
[MQTT In] → [Debug]
```

**Trin-for-trin:**

1. **Træk en `mqtt in` node** ind på arbejdsfladen
2. **Dobbeltklik** på noden for at konfigurere:
   - **Server**: Klik på ✏️ blyanten
     - **Server**: `localhost` (eller `127.0.0.1` hvis du kører lokalt)
     - **Port**: `1883`
     - **Klik "Add"**
   - **Topic**: `local/test/mqtt`
   - **QoS**: `2`
   - **Output**: `auto-detect (parsed JSON object or string)`
   - **Name**: "Lokal Modtager"

3. **Træk en `debug` node** ind
4. **Forbind** mqtt in-noden til debug-noden
5. **Klik Deploy** 🚀

---

### Publisher (sender beskeder)

**Flow-struktur:**
```
[Inject] → [MQTT Out]
```

**Trin-for-trin:**

1. **Træk en `inject` node** ind
2. **Dobbeltklik** og konfigurer:
   - **msg.payload**: `string` → `"Hello fra min egen broker!"`
   - **Name**: "Test lokal broker"

3. **Træk en `mqtt out` node** ind
4. **Dobbeltklik** og konfigurer:
   - **Server**: Vælg `localhost:1883` (samme som før)
   - **Topic**: `local/test/mqtt`
   - **QoS**: `2`
   - **Name**: "Send til lokal broker"

5. **Forbind** inject til mqtt out
6. **Klik Deploy** 🚀

---

### Test dit lokale flow

1. **Åbn debug-panelet**
2. **Klik på inject-knappen**
3. **Observer** – beskeden skulle vise sig øjeblikkeligt!

✅ **Success**: Din lokale broker virker!

---

## 🏋️ Øvelser

### Øvelse 1: Kommunikation mellem PC'er i samme netværk

Denne øvelse kræver minimum 2 studerende i samme netværk.

**PC A (broker-host):**
1. Find din IP-adresse (fx `192.168.1.209`)
2. Del din IP med din makker
3. Sørg for at Mosquitto kører (`docker ps`)

**PC B (klient):**
1. I Node-RED, opret en ny mqtt in-node
2. Klik på blyanten ved Server
3. Indtast PC A's IP-adresse (fx `192.168.1.209`)
4. Port: `1883`
5. Topic: Aftale et fælles topic, fx `gruppe/test`
6. Deploy og test ved at sende beskeder frem og tilbage!

> 💡 **Firewall-problem?** Hvis det ikke virker, skal I eventuelt tillade port 1883 gennem Windows Firewall på broker-PC'en eller sikre at den i docker-compose er tilføjet under ports som
```yaml
- "1883:1883"
```

---

### Øvelse 2: Sensor-data med timestamps

Opret et flow der simulerer en sensor:

```javascript
// I en function-node:
msg.payload = {
    sensor: "temperatur_lokalt",
    value: Math.random() * 25 + 15,  // 15-40°C
    location: "Klasselokale",
    timestamp: new Date().toISOString(),
    broker: "lokal"
};
return msg;
```

Forbind til din lokale broker og observer dataene.

---

### Øvelse 3: Sammenlign lokal vs. offentlig broker

Opret to identiske flows – én til `localhost` og én til `test.mosquitto.org`.

**Observer:**
- Forskel i responstid
- Pålidighed
- Hvad sker der hvis din Docker container stopper?

**Spørgsmål til diskussion:**
- Hvornår skal man bruge lokal broker?
- Hvornår er en cloud-broker bedre?
- Hvilke sikkerhedsforskelle er der?

---

### Øvelse 4: Persistens-test

1. Send nogle beskeder til din lokale broker
2. Stop Mosquitto containeren:
   ```bash
   docker-compose down
   ```
3. Start den igen:
   ```bash
   docker-compose up -d
   ```
4. Hvad sker der med dine beskeder?
5. Prøv at tilføje `retain: true` på mqtt out-noden og test igen

---

## ⚠️ Fejlfindingstips

**Container starter ikke:**
```bash
docker-compose logs mosquitto
```
Kig efter fejl i konfigurationen.

**Kan ikke forbinde fra Node-RED:**
- Tjek at containeren kører: `docker ps`
- Tjek at porten er åben: `netstat -an | findstr 1883` (Windows)
- Prøv at bruge `127.0.0.1` i stedet for `localhost`

**Andre kan ikke forbinde:**
- Verificér IP-adresse er korrekt
- Tjek firewall-indstillinger på host-PC
- Sørg for at I er på samme netværk
- Prøv at pinge IP-adressen først

**Permission denied fejl:**
- På Linux/Mac: Sørg for at mapperne har korrekte rettigheder:
  ```bash
  sudo chown -R 1883:1883 mosquitto/
  ```

---

## 🔍 Vigtige forskelle mellem lokal og offentlig broker

| Aspekt | Lokal Broker | Offentlig Broker (test.mosquitto.org) |
|--------|--------------|---------------------------------------|
| **Hastighed** | Meget hurtig (millisekunder) | Afhængig af internet |
| **Privatliv** | Dine data forbliver lokalt | Alle kan lytte på dine topics |
| **Pålidelighed** | Afhænger af din PC/Docker | Meget stabil, men kan være overbelastet |
| **Konfiguration** | Fuld kontrol | Ingen kontrol |
| **Brug** | Udvikling, test, lokale projekter | Hurtig prototyping, demo |
| **Sikkerhed** | Kan konfigureres med authentication | Ingen sikkerhed |

---

## 🚀 Næste skridt

Nu hvor du har din egen broker:

1. **Tilføj authentication** – Mosquitto kan konfigureres med brugernavn/password
2. **TLS/SSL encryption** – Krypter kommunikationen mellem klienter og broker
3. **Persistence og backup** – Lær hvordan data gemmes sikkert
4. **Bridge til cloud** – Forbind din lokale broker til en cloud-broker
5. **Monitoring** – Opsæt logging og overvågning af broker-aktivitet

---

## 🔍 Yderligere ressourcer

- [Eclipse Mosquitto Documentation](https://mosquitto.org/documentation/)
- [Docker Hub - Eclipse Mosquitto](https://hub.docker.com/_/eclipse-mosquitto)
- [MQTT Security Fundamentals](https://www.hivemq.com/mqtt-security-fundamentals/)
- [Mosquitto Configuration File Manual](https://mosquitto.org/man/mosquitto-conf-5.html)

---

## ✅ Hvad har du lært?

✅ Opsætte en MQTT broker med Docker  
✅ Konfigurere Mosquitto til ekstern adgang  
✅ Arbejde med Docker Compose  
✅ Teste netværkskommunikation mellem PC'er  
✅ Forstå forskellen mellem lokal og cloud-baseret infrastruktur  

> Din egen broker er et kraftfuldt værktøj til udvikling og test. I produktionsmiljøer ville man ofte bruge managed services (AWS IoT, Azure IoT Hub) eller selvhostede brokers med fuld sikkerhedskonfiguration.
