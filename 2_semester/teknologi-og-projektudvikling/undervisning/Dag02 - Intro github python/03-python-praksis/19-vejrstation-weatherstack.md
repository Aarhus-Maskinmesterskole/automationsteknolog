# 5️⃣ Vejrstation med WeatherStack API

> **Læringsmål:** I denne opgave laver du en simpel vejrstation, der henter live data fra WeatherStack.  
> Fokus er stadig helt grundlæggende: `requests.get()`, JSON og `print()`.

---

## 📋 Del A - Forberedelse

### Steps

1. 🌐 Opret en gratis konto på [WeatherStack](https://weatherstack.com/)
2. 🔑 Find din API-nøgle (Dashboard → Your API Access Key)
3. 📦 Installer `requests` hvis det mangler:

```bash
pip install requests
```

> **💡 Tip:** Gem din API-nøgle et sikkert sted - du skal bruge den i koden!

---

## 📋 Del B - Hent vejrdata for én by

### Opgave
Lav en fil `vejrstation.py` der henter vejrdata for Aarhus:

```python
import requests

# Konfiguration
api_key = "DIN_API_NØGLE"  # ⚠️ Indsæt din egen API-nøgle her!
by = "Aarhus"
url = "http://api.weatherstack.com/current"

# Parametre til API-kaldet
params = {
    "access_key": api_key,
    "query": by
}

# Hent data
response = requests.get(url, params=params)
data = response.json()

# Udpak vejrdata
current = data["current"]

# Vis resultat
print("\n🌤️  Vejrstation")
print("=" * 40)
print(f"📍 By: {by}")
print(f"🌡️  Temperatur: {current['temperature']}°C")
print(f"💨 Vindhastighed: {current['wind_speed']} km/t")
print(f"💧 Luftfugtighed: {current['humidity']}%")
print(f"☁️  Beskrivelse: {current['weather_descriptions'][0]}")
print("=" * 40)
```

### Forventet output
```
🌤️  Vejrstation
========================================
📍 By: Aarhus
🌡️  Temperatur: 8°C
💨 Vindhastighed: 15 km/t
💧 Luftfugtighed: 75%
☁️  Beskrivelse: Partly cloudy
========================================
```

---

## 📋 Del C - Interaktiv vejrstation

### Opgave
Udvid programmet så brugeren kan indtaste bynavn med `input()`:

```python
by = input("🌍 Skriv bynavn: ")
```

Kør programmet igen og test med 2-3 forskellige byer, fx:
- Aarhus
- København
- London
- New York

### 💡 Fejlhåndtering
Tilføj simpel fejlhåndtering:

```python
if "error" in data:
    print(f"❌ Fejl: {data['error']['info']}")
else:
    current = data["current"]
    # ... vis vejrdata
```

---

## 📋 Del D - Sammenlign flere byer

### Opgave
Lav en liste med tre byer, hent temperaturen for hver by, og udskriv dem.

```python
import requests

api_key = "DIN_API_NØGLE"
url = "http://api.weatherstack.com/current"

byer = ["Aarhus", "Odense", "København"]

print("\n🌤️  Vejrsammenligning")
print("=" * 50)

for by in byer:
    params = {
        "access_key": api_key,
        "query": by
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if "error" not in data:
        current = data["current"]
        temp = current["temperature"]
        beskrivelse = current["weather_descriptions"][0]
        
        print(f"📍 {by:15} | 🌡️  {temp:3}°C | {beskrivelse}")
    else:
        print(f"❌ {by:15} | Kunne ikke hente data")

print("=" * 50)
```

### Forventet output
```
🌤️  Vejrsammenligning
==================================================
📍 Aarhus          | 🌡️    8°C | Partly cloudy
📍 Odense          | 🌡️    7°C | Overcast
📍 København       | 🌡️    9°C | Clear
==================================================
```

---

## 🌟 Ekstra udfordringer

### 1. Find varmeste by
```python
temperaturer = {}
for by in byer:
    # ... hent data
    temperaturer[by] = current["temperature"]

varmeste = max(temperaturer, key=temperaturer.get)
print(f"\n🔥 Varmeste by: {varmeste} ({temperaturer[varmeste]}°C)")
```

### 2. Gem data til fil
```python
import json

with open('vejrdata.json', 'w') as f:
    json.dump(data, f, indent=2)
print("💾 Data gemt til vejrdata.json")
```

### 3. Tilføj mere info
- 🌅 Sol op/ned tid
- 👁️ Sigtbarhed
- 🧭 Vindretning
- ☔ Nedbør

---

## ✅ Tjekliste

- [ ] Del A: API-nøgle oprettet og requests installeret
- [ ] Del B: Kan hente vejrdata for én by
- [ ] Del C: Brugeren kan indtaste bynavn
- [ ] Del D: Kan sammenligne flere byer
- [ ] Ekstra: Implementeret mindst én ekstra feature

---

## 🔗 Nyttige links

- [WeatherStack Documentation](https://weatherstack.com/documentation)
- [Python requests library](https://requests.readthedocs.io/)
- [Working with JSON in Python](https://docs.python.org/3/library/json.html)

