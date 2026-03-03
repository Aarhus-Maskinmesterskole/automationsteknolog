# CoAP Server på ESP32 (MicroPython)

Dette er en super simpel opsætning, der lader din ESP32 dele sensordata over protokollen **CoAP**. Det er bygget til at være meget nemt at bruge sammen med f.eks. Node-RED.

## 1. Installation

1. Åbn Thonny.
2. Upload filen **`coapmini.py`** (som ligger i denne mappe) direkte til roden af din ESP32.
3. Åbn filen **`main.py`** (fra denne mappe) og upload også den til din ESP32.
4. Åbn `main.py` på din ESP, og ret navn og kodeord til dit WiFi:
   ```python
   SSID = "DIT_WIFI_NAVN"
   PSK  = "DIT_WIFI_KODE"
   ```
5. Tryk på Kør (Play-knappen) i Thonny. I konsollen vil du nu se, at den forbinder til WiFi og udskriver sin IP-adresse.

## 2. Hvordan bygger jeg mine egne sensorer ind?

Koden i `main.py` binder en funktion til en specifik URL. Det er faktisk alt, du behøver at forstå for at udvide den.

Hvis du f.eks. har en rigtig temperaturmåler, gør du bare sådan her i din `main.py`:

```python
# 1. Lav en simpel funktion, der læser din sensor
def læs_temperatur():
    # Her ville du skrive koden til at aflæse f.eks. en DHT11 / en analog pin
    min_temperatur = 24.5 
    
    # Returnér data som et "Dictionary" (det bliver automatisk til JSON)
    return {"temperatur": min_temperatur, "enhed": "C"}

# 2. Før "srv.serve_forever..." tilføjer du denne linje for at få din data delt:
srv.add("/temp", læs_temperatur)
```

Når du gør dette, kan andre enheder på netværket bede om data på adressen `/temp`.

## 3. Test det i Node-RED

Den letteste måde at teste, om din ESP32 virker, er ved at modtage dataene i Node-RED:

1. Træk en `inject` node ind (for at trigge læsningen, evt. sat til "repeat" hvert 5. sekund).
2. Træk en `coap request` node ind i dit flow.
3. Dobbeltklik på den og sæt metoden til **`GET`**.
4. Skriv URL'en til din ESP32 og tilføj navnet på din sensor. For eksempel: 
   `coap://<DIN_ESPs_IP_ADRESSE>:5683/dht` (eller `/temp` fra eksemplet ovenfor).
5. Forbind den til en `debug` node og tryk Deploy. 

Når du trykker på inject-noden, burde ESP'en nu svare med sensordataene direkte i dit debug-vindue!

---

**Troubleshooting / Typiske fejl:**
* Får du ingenting tilbage? Tjek at ESP32'en stadig kører, at I er på samme WiFi, og at IP-adressen er stavet rigtigt.
* Husk portnummeret `:5683` i din URL. Det er standard-porten for CoAP.
