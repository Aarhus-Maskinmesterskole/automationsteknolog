# 4️⃣ Mini API Flow (GET + POST)

> **Læringsmål:** I denne opgave samler du det vigtigste fra API-opgaverne i en helt enkel version.

---

## 📋 Del A - Server (Flask)

### Opgave
Lav `server.py` med Flask:

- 📥 `GET /maalinger` - returnerer en liste med målinger
- 📤 `POST /maalinger` - tilføjer en måling til listen

### Startpunkt
Start med en tom liste:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Global liste til at gemme målinger
maalinger = []

@app.route('/maalinger', methods=['GET'])
def get_maalinger():
    return jsonify(maalinger)

@app.route('/maalinger', methods=['POST'])
def post_maaling():
    data = request.json
    maalinger.append(data)
    return jsonify({"status": "success", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### 🚀 Start serveren
```bash
python server.py
```

Serveren kører nu på: `http://localhost:5000`

---

## 📋 Del B - Client (requests)

### Opgave
Lav `client.py` med `requests`:

1. 📤 Send 2 målinger med POST
2. 📥 Hent alle målinger med GET
3. 🖨️ Print alle målinger i terminalen

### Eksempel

```python
import requests
import json

BASE_URL = "http://localhost:5000"

# 1. Send første måling
maaling1 = {"value": 22.5, "timestamp": "2026-02-14 10:00:00"}
response1 = requests.post(f"{BASE_URL}/maalinger", json=maaling1)
print(f"POST 1: {response1.status_code} - {response1.json()}")

# 2. Send anden måling
maaling2 = {"value": 23.1, "timestamp": "2026-02-14 10:05:00"}
response2 = requests.post(f"{BASE_URL}/maalinger", json=maaling2)
print(f"POST 2: {response2.status_code} - {response2.json()}")

# 3. Hent alle målinger
response_get = requests.get(f"{BASE_URL}/maalinger")
maalinger = response_get.json()

print("\n=== Alle målinger ===")
for i, m in enumerate(maalinger, start=1):
    print(f"{i}. {m}")
```

### ▶️ Kør klienten
```bash
python client.py
```

---

## 📋 Del C - Udvid med sensor_id

### Opgave
Tilføj feltet `sensor_id` til hver måling:

```python
{"sensor_id": "temp_01", "value": 22.9, "timestamp": "2026-02-14 10:00:00"}
```

### Opdateret client

```python
maaling1 = {
    "sensor_id": "temp_01",
    "value": 22.5,
    "timestamp": "2026-02-14 10:00:00"
}

maaling2 = {
    "sensor_id": "temp_02",
    "value": 23.1,
    "timestamp": "2026-02-14 10:05:00"
}
```

### Forventet output
```
POST 1: 201 - {'status': 'success', 'data': {...}}
POST 2: 201 - {'status': 'success', 'data': {...}}

=== Alle målinger ===
1. {'sensor_id': 'temp_01', 'value': 22.5, 'timestamp': '2026-02-14 10:00:00'}
2. {'sensor_id': 'temp_02', 'value': 23.1, 'timestamp': '2026-02-14 10:05:00'}
```

---

## 🌟 Ekstra udfordring

Tilføj et endpoint til at hente en enkelt måling efter index:

```python
@app.route('/maalinger/<int:index>', methods=['GET'])
def get_maaling(index):
    if 0 <= index < len(maalinger):
        return jsonify(maalinger[index])
    else:
        return jsonify({"error": "Index not found"}), 404
```

---

## ✅ Tjekliste

- [ ] Flask server starter uden fejl
- [ ] GET endpoint returnerer målinger
- [ ] POST endpoint tilføjer målinger
- [ ] Client kan sende og hente data
- [ ] Data vises korrekt i terminalen
- [ ] sensor_id er tilføjet til målingerne
