# 🌐 13 – Flask API Server: Lav dit eget API

I opgave 12 lærte du at hente data fra eksterne API'er. Nu skal du lave dit eget API med Flask, så andre programmer kan hente data fra din server.

---

## 🔧 Indhold

* Hvad er Flask?
* Installation
* Simpel Flask server
* Lav endpoints med data
* Hent data fra din egen server
* Test og debugging

---

## 📘 1. Hvad er Flask?

Flask er et letvægts Python framework til at lave webservere og API'er. I automation kan det bruges til:

* Dele sensordata mellem systemer
* Lave et API til PLC-data
* Oprette et dashboard backend
* Modtage data fra IoT enheder

---

## 📘 2. Installation

```bash
pip install flask
```

---

## 📘 3. Hvad betyder @ (decorator)?

I Flask bruges `@` til at definere **routes** (stier/endpoints). Det er en Python decorator der fortæller Flask: "når nogen besøger denne URL, kør denne funktion".

```python
@app.route('/sensor')  # <- Dette er decoratoren
def sensor_data():      # <- Dette er funktionen der køres
    return {"data": "her"}
```

**Sådan virker det:**
- `@app.route('/sensor')` betyder: "Når nogen besøger `/sensor`, kør funktionen nedenunder"
- Funktionen returnerer data som sendes tilbage til brugeren
- Du kan have mange routes i samme Flask app

**Eksempel:**
```python
@app.route('/')           # Besøg http://localhost:5000/
def home():
    return "Velkommen!"

@app.route('/temperatur') # Besøg http://localhost:5000/temperatur
def temp():
    return "25°C"
```

---

## 📘 4. Simpel Flask server

Opret en fil `server.py`:

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Simpelt endpoint der returnerer en besked
@app.route('/')
def home():
    return jsonify({"message": "Velkommen til Automation API"})

# Endpoint med sensor data
@app.route('/sensor')
def sensor_data():
    data = {
        "sensor_id": "temp_01",
        "temperature": 23.5,
        "unit": "celsius",
        "status": "online"
    }
    return jsonify(data)

# Endpoint med motor status
@app.route('/motor')
def motor_status():
    return jsonify({
        "motor_id": "motor_01",
        "running": True,
        "speed_rpm": 1450,
        "temperature": 65
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Start serveren:
```bash
python server.py
```

Serveren kører nu på `http://localhost:5000`

---

## 📘 5. Hent data fra din server

Opret en ny fil `client.py`:

```python
import requests

# Hent fra home endpoint
response = requests.get('http://localhost:5000/')
print(response.json())

# Hent sensor data
response = requests.get('http://localhost:5000/sensor')
if response.status_code == 200:
    data = response.json()
    print(f"Sensor: {data['sensor_id']}")
    print(f"Temperatur: {data['temperature']}°C")
    print(f"Status: {data['status']}")

# Hent motor status
response = requests.get('http://localhost:5000/motor')
if response.status_code == 200:
    data = response.json()
    print(f"\nMotor: {data['motor_id']}")
    print(f"Kører: {data['running']}")
    print(f"Hastighed: {data['speed_rpm']} RPM")
```

**Vigtigt:** Start først `server.py` i én terminal, derefter kør `client.py` i en anden terminal.

---

## 📘 6. Dynamisk data med random værdier

Gør serveren mere realistisk ved at simulere skiftende værdier:

```python
from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/sensor')
def sensor_data():
    # Simuler temperatur mellem 20-30 grader
    temp = round(20 + random.random() * 10, 1)
    
    data = {
        "sensor_id": "temp_01",
        "temperature": temp,
        "unit": "celsius",
        "timestamp": time.time(),
        "status": "online"
    }
    return jsonify(data)

@app.route('/tank')
def tank_status():
    # Simuler tank niveau 0-100%
    niveau = round(random.random() * 100, 1)
    
    return jsonify({
        "tank_id": "tank_01",
        "level_percent": niveau,
        "capacity_liters": 1000,
        "alarm": niveau < 20  # Alarm hvis under 20%
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 📘 7. Flere endpoints

Udvid serveren med flere endpoints:

```python
from flask import Flask, jsonify
import random

app = Flask(__name__)

# Liste over alle tilgængelige endpoints
@app.route('/')
def home():
    return jsonify({
        "message": "Automation API",
        "endpoints": [
            "/sensor",
            "/motor",
            "/tank",
            "/alarm",
            "/status"
        ]
    })

@app.route('/status')
def system_status():
    return jsonify({
        "system": "online",
        "sensors": 3,
        "motors": 2,
        "alarms": 0
    })

@app.route('/alarm')
def alarm_status():
    return jsonify({
        "active_alarms": [],
        "alarm_count": 0,
        "system_ok": True
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 🧪 Øvelser

1. Lav en Flask server med et `/temperatur` endpoint der returnerer en tilfældig temperatur mellem 15-25°C.
2. Tilføj et `/status` endpoint der returnerer system status (online/offline).
3. Lav en client.py der henter data fra begge endpoints og printer det pænt.
4. Ekstra: Lav en løkke i client.py der henter data hvert 5. sekund og printer temperaturen.

---

## For de øvede

5. Tilføj flere endpoints til serveren: `/pump`, `/valve`, `/pressure` med relevante data.
6. Lav en client der henter data fra alle endpoints og gemmer det i en liste.
7. Tilføj timestamp til alle server responses, så du kan se hvornår data blev hentet.
8. Kombiner med GUI fra tidligere opgaver: Lav en knap der henter sensor data og viser det i en label.

---

## For de advanced

9. Lav en server der logger alle requests til en fil med timestamp.
10. Implementér en simpel alarm-funktion: Hvis temperatur > 28°C, skal `/alarm` endpoint returnere en advarsel.
11. Lav et dashboard med GUI der viser data fra flere endpoints i realtid (opdaterer automatisk hvert 2. sekund).
12. Tilføj fejlhåndtering på serveren med custom error messages (404, 500 etc.).

---

## ✅ Tjekliste

* [ ] Jeg har installeret Flask
* [ ] Jeg kan lave en simpel Flask server
* [ ] Jeg kan oprette endpoints der returnerer JSON data
* [ ] Jeg kan hente data fra min egen server med requests
* [ ] Jeg forstår forskellen på server og client
* [ ] Jeg kan teste mine endpoints i browseren eller med client script

---

## 💡 Tips

* **Test i browser:** Åbn `http://localhost:5000/sensor` i din browser for at se JSON data
* **Debug mode:** `debug=True` gør at serveren genstarter automatisk når du ændrer koden
* **Host:** `host='0.0.0.0'` gør at serveren er tilgængelig fra andre computere på netværket
* **Port:** Hvis port 5000 er optaget, skift til fx 5001, 8080 eller 3000

---

## 📚 Nyttige links

* [Flask dokumentation](https://flask.palletsprojects.com/)
* [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
* [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## 🔄 Workflow

1. **Start serveren:** Kør `python server.py` i én terminal
2. **Test i browser:** Åbn `http://localhost:5000/sensor`
3. **Brug client:** Kør `python client.py` i en anden terminal
4. **Stop serveren:** Tryk `Ctrl+C` i server-terminalen

---
