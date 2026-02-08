# 📤 14 – Flask POST: Send data til serveren

I opgave 12 lærte du at **hente** data med GET requests. I opgave 13 lavede du din egen Flask server. Nu skal du lære at **sende** data til serveren med POST requests.

---

## 🔧 Indhold

* Hvad er POST?
* Modtag data på serveren
* Send data fra client
* Gem data i en liste
* Eksempel: Log sensorværdier

---

## 📘 1. Hvad er POST?

**GET** bruges til at **hente** data (som du allerede har lært).
**POST** bruges til at **sende** data til serveren.

I automation bruges POST til:
* Send sensorværdier til en database
* Opdater PLC indstillinger
* Log maskindata
* Registrer alarmer

---

## 📘 2. Server med POST endpoint

Opret en fil `server.py`:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Liste til at gemme data
sensor_data = []

# GET endpoint - hent alle data
@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    return jsonify({
        "count": len(sensor_data),
        "data": sensor_data
    })

# POST endpoint - modtag nye data
@app.route('/sensor', methods=['POST'])
def add_sensor_data():
    # Modtag JSON data fra client
    data = request.json
    
    # Tilføj til listen
    sensor_data.append(data)
    
    # Send bekræftelse tilbage
    return jsonify({
        "status": "success",
        "message": "Data modtaget",
        "total_entries": len(sensor_data)
    }), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**Forklaring:**
- `methods=['GET']` = kun GET requests accepteres
- `methods=['POST']` = kun POST requests accepteres
- `request.json` = JSON data sendt fra client
- `201` = HTTP statuskode for "Created" (data oprettet)

---

## 📘 3. Send data fra client

Opret en fil `client.py`:

```python
import requests

url = 'http://localhost:5000/sensor'

# Data vi vil sende
sensor_data = {
    "sensor_id": "temp_01",
    "temperature": 23.5,
    "unit": "celsius"
}

# Send POST request
response = requests.post(url, json=sensor_data)

if response.status_code == 201:
    print("Data sendt succesfuldt!")
    print(response.json())
else:
    print(f"Fejl: {response.status_code}")
```

**Workflow:**
1. Start `server.py` i én terminal
2. Kør `client.py` i en anden terminal
3. Client sender data til serveren
4. Serveren bekræfter modtagelse

---

## 📘 4. Hent data efter POST

Udvid `client.py` til også at hente data:

```python
import requests

url = 'http://localhost:5000/sensor'

# 1. Send data (POST)
sensor_data = {
    "sensor_id": "temp_01",
    "temperature": 23.5,
    "unit": "celsius"
}

response = requests.post(url, json=sensor_data)
if response.status_code == 201:
    print("✅ Data sendt!")
    print(response.json())

# 2. Hent alle data (GET)
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"\n📊 Total entries: {data['count']}")
    print("Data:")
    for entry in data['data']:
        print(f"  - {entry}")
```

---

## 📘 5. Udvid serveren med flere endpoints

```python
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

sensor_data = []
motor_logs = []

# Sensor endpoints
@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    return jsonify({"count": len(sensor_data), "data": sensor_data})

@app.route('/sensor', methods=['POST'])
def add_sensor_data():
    data = request.json
    data['timestamp'] = time.time()  # Tilføj timestamp
    sensor_data.append(data)
    return jsonify({"status": "success"}), 201

# Motor endpoints
@app.route('/motor', methods=['GET'])
def get_motor_logs():
    return jsonify({"count": len(motor_logs), "logs": motor_logs})

@app.route('/motor', methods=['POST'])
def add_motor_log():
    data = request.json
    data['timestamp'] = time.time()
    motor_logs.append(data)
    return jsonify({"status": "success"}), 201

# Slet alle data
@app.route('/reset', methods=['POST'])
def reset_data():
    sensor_data.clear()
    motor_logs.clear()
    return jsonify({"status": "all data cleared"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 🧪 Øvelser

1. Send en temperatur måling til serveren og verificér at den er modtaget ved at hente alle data.
2. Send 3 forskellige temperaturer manuelt (kør client 3 gange) og hent alle målinger bagefter.
3. Tilføj et `/motor` endpoint til serveren og send motor data (speed, status) fra client.

---

## For de øvede

4. Lav en løkke i client der sender 10 forskellige temperatur målinger med tilfældige værdier.
5. Tilføj validering på serveren: Acceptér kun temperatur mellem 0-50°C, ellers returner fejl.
6. Lav et GUI med Tkinter/PyQt hvor brugeren kan indtaste temperatur og sende det til serveren ved knapklik.
7. Udvid serveren til at gemme data i en fil (JSON eller CSV) i stedet for kun i liste.

---

## For de advanced

8. Lav et script der sender data hvert 5. sekund i en uendelig løkke (brug `while True` og `time.sleep(5)`).
9. Implementér timestamp på serveren og vis kun data fra de sidste 5 minutter.
10. Tilføj authentication: Serveren skal tjekke en API-nøgle før den accepterer POST requests.
11. Implementér error handling: Tjek om serveren kører før du sender data, ellers gem lokalt.

---

## ✅ Tjekliste

* [ ] Jeg forstår forskellen på GET og POST
* [ ] Jeg kan lave POST endpoints i Flask
* [ ] Jeg kan sende data med requests.post()
* [ ] Jeg kan modtage og gemme data på serveren
* [ ] Jeg kan kombinere GET og POST i samme application
* [ ] Jeg forstår hvordan `request.json` virker

---

## 💡 Tips

* **Test POST i Postman:** Du kan også bruge Postman eller Thunder Client (VS Code extension) til at teste POST requests
* **Debug:** Print `request.json` på serveren for at se hvad der modtages
* **Statuskoder:** 
  - `200` = OK (GET success)
  - `201` = Created (POST success)
  - `400` = Bad Request (fejl i data)
  - `404` = Not Found (endpoint findes ikke)

---

## 📚 Nyttige links

* [Flask Request Object](https://flask.palletsprojects.com/en/stable/api/#flask.Request)
* [HTTP Methods explained](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
* [Requests POST documentation](https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests)

---

## 🔄 Sammenhæng med tidligere opgaver

| Opgave | Fokus |
|--------|-------|
| **12** | Hent data fra eksterne API'er (GET) |
| **13** | Lav din egen server med GET endpoints |
| **14** | Send data til serveren (POST) |

Nu kan du både hente og sende data mellem systemer! 🎉

---
