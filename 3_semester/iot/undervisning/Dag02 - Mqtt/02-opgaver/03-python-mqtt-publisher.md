# 🐍 Opgave 03 – Python MQTT Publisher til Node-RED

Nu skal du kombinere Python-programmering med MQTT! I denne opgave laver du Python-scripts der sender sensor-data via MQTT, som Node-RED derefter modtager og visualiserer. Dette er et meget almindeligt mønster i IoT-systemer.

## 🎯 Formål

I denne opgave lærer du at:
- Installere og bruge `paho-mqtt` biblioteket i Python
- Oprette en MQTT publisher i Python
- Sende sensor-data fra Python til Node-RED
- Simulere forskellige typer sensorer
- Arbejde med JSON-data mellem Python og Node-RED
- Forstå hvordan forskellige teknologier kommunikerer via MQTT

---

## 🧰 Forudsætninger

* Python 3.x installeret
* Node-RED kørende
* Mosquitto broker kørende (lokal eller `test.mosquitto.org`)
* Grundlæggende Python-kendskab
* Kendskab til MQTT fra Opgave 01-simpel-pub-sub og 02-lokal-mosquitto-broker

---

## 📦 Del 1: Installation af paho-mqtt

Paho-MQTT er det mest populære Python-bibliotek til MQTT-kommunikation.

### Installation

Åbn en terminal og installer biblioteket:

```bash
pip install paho-mqtt
```

Verificer installationen:

```bash
pip show paho-mqtt
```

Du skulle se information om pakken inkl. version (fx 1.6.1 eller nyere).

---

## 🐍 Del 2: Simpel MQTT Publisher i Python

### Opret dit første publisher-script

Opret en ny fil kaldet `mqtt_publisher.py`:

```python
import paho.mqtt.client as mqtt
import time

# MQTT Broker indstillinger
BROKER = "localhost"  # Eller "test.mosquitto.org" for offentlig broker
PORT = 1883
TOPIC = "python/test"

# Callback når forbindelse til broker er etableret
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Forbundet til MQTT broker!")
    else:
        print(f"❌ Fejl ved forbindelse. Return code: {rc}")

# Opret MQTT klient (med callback API version for nyere paho-mqtt)
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
except AttributeError:
    # Fallback for ældre versioner
    client = mqtt.Client("PythonPublisher")
client.on_connect = on_connect

# Forbind til broker
print(f"Forbinder til broker: {BROKER}:{PORT}")
client.connect(BROKER, PORT, 60)

# Start netværks-loop i baggrunden
client.loop_start()

# Send beskeder
try:
    counter = 0
    while True:
        message = f"Besked nummer {counter} fra Python"
        result = client.publish(TOPIC, message)
        
        if result.rc == 0:
            print(f"📤 Sendt: {message}")
        else:
            print(f"❌ Fejl ved afsendelse")
        
        counter += 1
        time.sleep(2)  # Vent 2 sekunder mellem beskeder

except KeyboardInterrupt:
    print("\n🛑 Stopper publisher...")

# Afbryd forbindelse
client.loop_stop()
client.disconnect()
print("👋 Afsluttet")
```

### Test dit script

1. **Start din Mosquitto broker** (hvis du bruger lokal)
2. **Kør Python-scriptet:**
   ```bash
   python mqtt_publisher.py
   ```

Du skulle se:
```
Forbinder til broker: localhost:1883
✅ Forbundet til MQTT broker!
📤 Sendt: Besked nummer 0 fra Python
📤 Sendt: Besked nummer 1 fra Python
📤 Sendt: Besked nummer 2 fra Python
...
```

---

## 💡 Del 3: Modtag data i Node-RED

Nu skal Node-RED modtage de data Python sender.

### Opret Subscriber i Node-RED

**Flow-struktur:**
```
[MQTT In] → [Debug]
```

**Trin-for-trin:**

1. **Træk en `mqtt in` node** ind
2. **Dobbeltklik** og konfigurer:
   - **Server**: `localhost:1883` (samme som i Python-scriptet)
   - **Topic**: `python/test`
   - **QoS**: `2`
   - **Output**: `auto-detect`
   - **Name**: "Python data"

3. **Træk en `debug` node** ind
4. **Forbind** mqtt in → debug
5. **Deploy** 🚀

### Test kommunikationen

1. **Kør Python-scriptet** (hvis det ikke allerede kører)
2. **Åbn debug-panelet i Node-RED**
3. **Observer** - du skulle se beskederne fra Python!

✅ **Success**: Python og Node-RED kommunikerer nu via MQTT!

---

## 🌡️ Del 4: Simuler sensor-data

Nu laver vi et mere realistisk eksempel med sensor-data i JSON-format.

### Opret `temperature_sensor.py`:

```python
import paho.mqtt.client as mqtt
import json
import time
import random

# MQTT konfiguration
BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/temperature"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Temperatursensor forbundet til broker")
    else:
        print(f"❌ Forbindelsesfejl: {rc}")

# Opret klient (med callback API version)
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
except AttributeError:
    client = mqtt.Client("TempSensor01")
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)
client.loop_start()

# Simuler temperatursensor
try:
    print("🌡️  Starter temperatursensor...")
    while True:
        # Generér tilfældig temperatur (mellem 18 og 28 grader)
        temperature = round(random.uniform(18.0, 28.0), 1)
        
        # Opret sensor-data som JSON
        sensor_data = {
            "sensor_id": "temp_001",
            "type": "temperature",
            "value": temperature,
            "unit": "celsius",
            "location": "Klasselokale",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Konverter til JSON-string
        json_data = json.dumps(sensor_data)
        
        # Send til MQTT
        client.publish(TOPIC, json_data)
        print(f"📤 Temperatur sendt: {temperature}°C")
        
        time.sleep(5)  # Send data hvert 5. sekund

except KeyboardInterrupt:
    print("\n🛑 Stopper sensor...")

client.loop_stop()
client.disconnect()
print("👋 Sensor afsluttet")
```

### Modtag sensor-data i Node-RED

**Flow-struktur:**
```
[MQTT In] → [Debug]
            ↓
         [Function] → [Debug "Kun værdi"]
```

**Opsætning:**

1. **MQTT In node:**
   - Topic: `sensors/temperature`
   - Output: `auto-detect (parsed JSON object)`

2. **Debug node 1:**
   - Output: `complete msg object`
   - Name: "Komplet besked"

3. **Function node:**
   ```javascript
   // Udtræk kun temperaturværdien
   msg.payload = msg.payload.value + "°C";
   return msg;
   ```

4. **Debug node 2:**
   - Output: `msg.payload`
   - Name: "Kun værdi"

5. **Deploy og test!**

---

## 🏋️ Øvelser

### Øvelse 1: Multi-sensor system

Udvid dit system til at have flere sensorer:

```python
import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "localhost"
PORT = 1883

# Ingen callbacks bruges, så Client() uden version er OK
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        # Temperatursensor
        temp_data = {
            "sensor": "temp_001",
            "value": round(random.uniform(18, 28), 1),
            "unit": "celsius"
        }
        client.publish("sensors/temperature", json.dumps(temp_data))
        
        # Luftfugtighedssensor
        humidity_data = {
            "sensor": "hum_001",
            "value": round(random.uniform(40, 70), 1),
            "unit": "percent"
        }
        client.publish("sensors/humidity", json.dumps(humidity_data))
        
        # Bevægelsessensor
        motion_data = {
            "sensor": "motion_001",
            "detected": random.choice([True, False])
        }
        client.publish("sensors/motion", json.dumps(motion_data))
        
        print("📤 Sensor-data sendt")
        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Stopper sensorer...")

client.loop_stop()
client.disconnect()
```

**I Node-RED:**
- Opret 3 separate mqtt in-noder (en til hver sensor-type)
- Brug forskellige visualiseringer til hver

---

### Øvelse 2: Alarmsystem med grænseværdier

**Python-side:**
```python
import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "localhost"
PORT = 1883

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)
client.loop_start()

TEMP_THRESHOLD = 26.0  # Alarmgrænse

try:
    while True:
        temp = round(random.uniform(20, 30), 1)
        
        alarm = temp > TEMP_THRESHOLD
        
        data = {
            "temperature": temp,
            "alarm": alarm,
            "message": "ADVARSEL: Høj temperatur!" if alarm else "Normal",
            "timestamp": time.strftime("%H:%M:%S")
        }
        
        client.publish("sensors/temp_alarm", json.dumps(data))
        print(f"📤 Temp: {temp}°C {'🚨 ALARM!' if alarm else '✅'}")
        
        time.sleep(3)

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
```

**I Node-RED:**
- Brug en switch-node til at route alarm-beskeder til en separat output
- Visualiser normale og alarm-værdier forskelligt

---

### Øvelse 3: Kommando fra Node-RED til Python

Nu skal Python også kunne *modtage* kommandoer fra Node-RED!

**Python script med subscriber:**
```python
import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "localhost"
PORT = 1883
TOPIC_PUB = "sensors/motor"
TOPIC_SUB = "commands/motor"

motor_speed = 0  # Start hastighed

def on_connect(client, userdata, flags, rc, properties=None):
    print("✅ Forbundet til broker")
    client.subscribe(TOPIC_SUB)
    print(f"📥 Lytter på: {TOPIC_SUB}")

def on_message(client, userdata, msg):
    global motor_speed
    try:
        command = json.loads(msg.payload.decode())
        if "speed" in command:
            motor_speed = command["speed"]
            print(f"⚙️  Motor hastighed ændret til: {motor_speed} RPM")
    except:
        print("❌ Ugyldig kommando")

# Opret klient med callback API version
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
except AttributeError:
    client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        # Send motor status
        status = {
            "motor_id": "motor_001",
            "speed": motor_speed,
            "temperature": round(random.uniform(40, 80), 1),
            "status": "running" if motor_speed > 0 else "stopped"
        }
        
        client.publish(TOPIC_PUB, json.dumps(status))
        print(f"📤 Status: {motor_speed} RPM")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Stopper motor controller...")

client.loop_stop()
client.disconnect()
```

**I Node-RED:**

Flow 1 - Modtag motor status:
```
[MQTT In: sensors/motor] → [Debug]
```

Flow 2 - Send kommandoer:
```
[Inject] → [Change: set speed] → [MQTT Out: commands/motor]
```

Opret flere inject-noder med forskellige hastigheder (0, 500, 1000, 1500 RPM).

---

### Øvelse 4: Data-logging til fil

Udvid Node-RED til at gemme sensor-data:

```
[MQTT In] → [Function: Format data] → [File Out: sensor_log.txt]
```

**Function node:**
```javascript
const timestamp = new Date().toISOString();
const temp = msg.payload.value;
const logLine = `${timestamp}, ${temp}\n`;

msg.payload = logLine;
return msg;
```

**File node:**
- Filename: `sensor_log.txt`
- Action: `append to file`

---

## ⚠️ Fejlfindingstips

**ModuleNotFoundError: No module named 'paho'**
```bash
pip install paho-mqtt
# Eller hvis du har flere Python-versioner:
python -m pip install paho-mqtt
```

**Connection refused:**
- Tjek at Mosquitto broker kører
- Verificer IP-adresse og port
- Prøv `127.0.0.1` i stedet for `localhost`

**JSON parse error i Node-RED:**
- Tjek at Python sender valid JSON: `json.dumps(data)`
- Sæt MQTT In node output til "auto-detect"

**Ingen data modtages:**
- Verificer at topic er identisk i Python og Node-RED
- Tjek at Python-scriptet kører uden fejl
- Se efter fejlbeskeder i begge systemer

---

## 📊 Best Practices for Python MQTT Publishers

### 1. Brug classes for struktur

```python
class TemperatureSensor:
    def __init__(self, broker, port, sensor_id):
        self.broker = broker
        self.port = port
        self.sensor_id = sensor_id
        # Brug CallbackAPIVersion hvis du har callbacks
        try:
            self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        except AttributeError:
            self.client = mqtt.Client(sensor_id)
        
    def connect(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()
    
    def publish_reading(self, temperature):
        data = {
            "sensor_id": self.sensor_id,
            "value": temperature,
            "timestamp": time.time()
        }
        self.client.publish(f"sensors/{self.sensor_id}", json.dumps(data))
    
    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
```

### 2. Håndter fejl korrekt

```python
try:
    result = client.publish(topic, message)
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("✅ Besked sendt")
    else:
        print(f"❌ Fejl: {result.rc}")
except Exception as e:
    print(f"❌ Exception: {e}")
```

### 3. Brug QoS korrekt

```python
# QoS 0: Fire and forget (hurtigst)
client.publish(topic, message, qos=0)

# QoS 1: Mindst én gang (anbefalet for mest data)
client.publish(topic, message, qos=1)

# QoS 2: Præcis én gang (langsomst, men garanteret)
client.publish(topic, message, qos=2)
```

### 4. Brug retained messages til status

```python
# Seneste værdi gemmes på broker
client.publish("sensors/temp/status", json.dumps(data), retain=True)
```

---

## 🔍 Arkitektur-oversigt

```
┌─────────────────┐
│  Python Script  │
│  (Publisher)    │
│                 │
│  - Simulerer    │
│    sensor-data  │
│  - Sender JSON  │
│  - paho-mqtt    │
└────────┬────────┘
         │
         │ MQTT Publish
         │ Topic: sensors/temperature
         ↓
┌─────────────────┐
│ MQTT Broker     │
│ (Mosquitto)     │
│                 │
│ - Port 1883     │
│ - Formidler     │
│   beskeder      │
└────────┬────────┘
         │
         │ MQTT Subscribe
         │ Topic: sensors/temperature
         ↓
┌─────────────────┐
│   Node-RED      │
│  (Subscriber)   │
│                 │
│  - Modtager     │
│  - Visualiserer │
│  - Logger       │
└─────────────────┘
```

---

## 🔍 Yderligere ressourcer

- [Paho MQTT Python Client Documentation](https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php)
- [MQTT QoS Explained](https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels/)
- [JSON in Python Tutorial](https://realpython.com/python-json/)
- [Node-RED Function Node Guide](https://nodered.org/docs/user-guide/writing-functions)

---

## ✅ Hvad har du lært?

✅ Installere og bruge paho-mqtt i Python  
✅ Oprette MQTT publishers i Python  
✅ Sende struktureret data (JSON) via MQTT  
✅ Modtage Python-data i Node-RED  
✅ Simulere sensor-systemer  
✅ Kombinere forskellige teknologier via MQTT  
✅ Forstå publisher/subscriber arkitektur  

> Python + MQTT + Node-RED er en meget kraftfuld kombination til IoT-projekter. Python giver dig direkte kontrol over hardware og komplekse beregninger, mens Node-RED gør det nemt at visualisere og orkestrere systemet.
