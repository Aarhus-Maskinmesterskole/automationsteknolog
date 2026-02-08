# 🌐 12 – Simpel API: Kommunikation mellem systemer

API'er (Application Programming Interfaces) gør det muligt for programmer at kommunikere med hinanden. I automation bruges API'er til at hente data fra sensorer, sende kommandoer til udstyr, eller dele produktionsdata mellem systemer.

---

## 🔧 Indhold

* Hvad er et API?
* HTTP requests med `requests`
* GET requests – hent data
* JSON data format
* Eksempel: Hent vejrdata
* Eksempel: Hent bitcoin-pris

---

## 📘 1. Hvad er et API?

Et API er en grænseflade, der lader to programmer udveksle data. I automation kan det fx være:

* Hent temperatur fra en vejrtjeneste
* Send maskindata til en SCADA-server
* Modtag ordrer fra et ERP-system
* Styre et PLC via HTTP

---

## 📘 2. Installation af `requests`

For at arbejde med API'er installerer vi biblioteket `requests`:

```bash
pip install requests
```

---

## 📘 3. GET request – hent data

En GET request bruges til at hente data fra et API:

```python
import requests

# Hent vejrdata fra WeatherStack
# Opret gratis API-nøgle på: https://weatherstack.com/
api_key = "din_api_nøgle_her"
url = "http://api.weatherstack.com/current"

params = {
    "access_key": api_key,
    "query": "Aarhus"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    if 'current' in data:
        temperatur = data['current']['temperature']
        beskrivelse = data['current']['weather_descriptions'][0]
        print(f"Vejret i Aarhus: {temperatur}°C, {beskrivelse}")
    else:
        print(f"Fejl i data: {data}")
else:
    print(f"Fejl: {response.status_code}")
```

---

## 📘 4. JSON data format
JSON (JavaScript Object Notation) er det mest anvendte dataformat til API'er. Det er et letvægts, tekstbaseret format, der er let for mennesker at læse og skrive, og let for maskiner at parse og generere. JSON er bygget op omkring nøgle-værdi-par, svarende til Python dictionaries, og understøtter også lister/arrays af værdier.

```python
import json

# Python dict til JSON string
sensor_data = {
    "temperature": 22.5,
    "humidity": 65,
    "pressure": 1013
}

json_string = json.dumps(sensor_data, indent=2)
print(json_string)

# JSON string til Python dict
data = json.loads(json_string)
print(f"Temperatur: {data['temperature']}")
```

---

## 📘 5. Praktisk eksempel: Hent bitcoin-pris

```python
import requests

url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pris = data['data']['amount']
    print(f"Bitcoin pris: ${pris}")
else:
    print("Kunne ikke hente pris")
```

---

## 🧪 Øvelser

1. Opret en gratis konto på WeatherStack og brug API'et til at hente vejrdata for din by og vis temperatur, vindhastighed og beskrivelse.
2. Hent og vis aktuelle bitcoin-pris ved hjælp af Coinbase API'et.
3. Lav en funktion `hent_vejr(by)` der tager en by som parameter og returnerer temperaturen.

---

## For de øvede

5. Kombiner PyQt/Tkinter GUI fra tidligere opgaver med API-kald: Lav en knap der henter vejrdata og viser det i en label.
6. Brug `requests` til at hente data fra et offentligt API (fx Random User API, Cat Facts API eller JokeAPI) og vis det pænt formateret.
7. Lav et program der sammenligner vejret i 3 forskellige byer og viser hvilken by der har den højeste temperatur.

---

## For de advanced

8. Lav en funktion der henter data fra flere forskellige API'er og sammensætter informationen (fx vejr + tid + cryptocurrency).
9. Implementer error handling og retry-logik hvis API'et ikke svarer.
10. Lav et dashboard der henter data fra flere forskellige API'er (vejr, cryptocurrency, random facts) og viser dem samlet i et GUI.

---

## ✅ Tjekliste

* [ ] Jeg forstår hvad et API er
* [ ] Jeg kan lave GET requests med `requests`
* [ ] Jeg kan arbejde med JSON format i Python
* [ ] Jeg har hentet data fra et offentligt API
* [ ] Jeg kan håndtere API-svar og fejl korrekt

---

## 📚 Nyttige links

* [Requests dokumentation](https://requests.readthedocs.io/)
* [WeatherStack API (gratis vejrdata)](https://weatherstack.com/)
* [HTTPBin (test API)](https://httpbin.org/)
* [Flask dokumentation](https://flask.palletsprojects.com/)
* [JSONPlaceholder (test API)](https://jsonplaceholder.typicode.com/)

---
