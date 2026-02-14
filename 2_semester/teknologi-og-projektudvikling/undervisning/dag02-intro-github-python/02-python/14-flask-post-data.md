# 14 - Flask POST: send data til server

I denne opgave sender du data til din Flask-server med POST.
Fokus er kun paa grundlaeggende GET og POST.

---

## Indhold

* Hvad er POST?
* Server med GET + POST
* Client der sender data
* Hent data bagefter

---

## 1. Hvad er POST?

* `GET` henter data
* `POST` sender data

---

## 2. Server med GET og POST

Opret `server.py`:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

sensor_data = []

@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    return jsonify(sensor_data)

@app.route('/sensor', methods=['POST'])
def add_sensor_data():
    data = request.json
    sensor_data.append(data)
    return jsonify({"status": "ok"}), 201

if __name__ == '__main__':
    app.run(port=5000)
```

---

## 3. Client: send data

Opret `client.py`:

```python
import requests

url = 'http://localhost:5000/sensor'

ny_maaling = {
    "sensor_id": "temp_01",
    "temperature": 24.2
}

response = requests.post(url, json=ny_maaling)
print("POST status:", response.status_code)
```

---

## 4. Hent data bagefter

Udvid `client.py`:

```python
import requests

url = 'http://localhost:5000/sensor'

requests.post(url, json={"sensor_id": "temp_01", "temperature": 24.2})
requests.post(url, json={"sensor_id": "temp_01", "temperature": 24.7})

response = requests.get(url)
print("Alle maalinger:")
for maaling in response.json():
    print(maaling)
```

---

## Oevelser

1. Send 1 maaling med POST og hent listen med GET.
2. Send 3 maalinger og print alle maalinger.
3. Tilfoej endpoint `/motor` med egen liste og test med POST + GET.

---

## Tjekliste

* [ ] Jeg forstaar forskellen paa GET og POST
* [ ] Jeg kan modtage data med `request.json`
* [ ] Jeg kan gemme data i en liste
* [ ] Jeg kan hente data igen med GET

---
