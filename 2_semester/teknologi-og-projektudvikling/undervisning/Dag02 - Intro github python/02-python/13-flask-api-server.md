# 13 - Flask API server: grundlaeggende GET endpoints

I denne opgave laver du din egen API-server med Flask.
Fokus er kun paa det grundlaeggende: routes og JSON-svar.

---

## Indhold

* Installation af Flask
* Simpel server
* To GET endpoints
* Simpel client med `requests`

---

## 1. Installation

```bash
pip install flask
```

---

## 2. Simpel server

Opret `server.py`:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Velkommen"})

@app.route('/sensor')
def sensor():
    return jsonify({
        "sensor_id": "temp_01",
        "temperature": 23.5,
        "unit": "celsius"
    })

if __name__ == '__main__':
    app.run(port=5000)
```

Start serveren:

```bash
python server.py
```

---

## 3. Simpel client

Opret `client.py`:

```python
import requests

response = requests.get('http://localhost:5000/sensor')
data = response.json()

print("Sensor:", data["sensor_id"])
print("Temperatur:", data["temperature"], data["unit"])
```

---

## Oevelser

1. Tilfoej endpoint `/motor` med `motor_id` og `running`.
2. Hent `/motor` fra client og print vaerdierne.
3. Tilfoej endpoint `/status` med teksten `online`.

---

## Tjekliste

* [ ] Jeg kan starte en Flask-server
* [ ] Jeg kan lave et GET endpoint med `@app.route()`
* [ ] Jeg kan returnere JSON med `jsonify()`
* [ ] Jeg kan hente data fra serveren i en client

---
