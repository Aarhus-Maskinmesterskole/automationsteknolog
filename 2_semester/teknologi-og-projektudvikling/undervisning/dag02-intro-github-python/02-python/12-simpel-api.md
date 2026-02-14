# 12 - Simpel API: GET med requests

I denne opgave henter du data fra et offentligt API med Python.
Fokus er kun paa det grundlaeggende: `requests.get()` og JSON.

---

## Indhold

* Hvad er et API?
* Installation af `requests`
* Simpelt GET-kald
* JSON i Python

---

## 1. Hvad er et API?

Et API er en maade for programmer at udveksle data pa.

Eksempler:

* hente vejrdata
* hente valutakurser
* hente prisdata

---

## 2. Installation af `requests`

```bash
pip install requests
```

---

## 3. Simpelt GET-kald

```python
import requests

url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
response = requests.get(url)

data = response.json()
pris = data["data"]["amount"]
print("Bitcoin pris i USD:", pris)
```

---

## 4. JSON i Python

```python
import json

sensor_data = {
    "temperature": 22.5,
    "pressure": 1013
}

tekst = json.dumps(sensor_data)
print(tekst)

tilbage = json.loads(tekst)
print("Temperatur:", tilbage["temperature"])
```

---

## Oevelser

1. Hent bitcoin-prisen og udskriv den.
2. Hent data to gange og udskriv begge svar.
3. Lav en funktion `hent_btc_pris()` der returnerer prisen.

---

## Tjekliste

* [ ] Jeg kan installere `requests`
* [ ] Jeg kan lave et GET-kald med `requests.get()`
* [ ] Jeg kan laese JSON-svar med `.json()`
* [ ] Jeg kan hente en vaerdi fra et JSON-objekt

---
