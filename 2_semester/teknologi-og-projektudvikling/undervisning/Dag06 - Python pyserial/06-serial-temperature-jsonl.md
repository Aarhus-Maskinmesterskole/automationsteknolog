# 🌡️➡️🧾 06 - Log temperatur som JSON Lines (ESP32 → Python + Pandas)

I denne øvelse sender ESP32 **JSON**-objekter over seriel (fx `{"temperature": 22.1}`), og din PC logger dem løbende i en **JSON Lines**-fil (`.jsonl`) med **pandas**.

**Format i filen (`measurements.jsonl`):**

```
{"temperature":22.1,"tid":1726060200.351}
{"temperature":22.2,"tid":1726060202.355}
```

---

## 🎯 Læringsmål

* Udsende målinger som **JSON** fra ESP32
* Læse serielle data i Python og gemme som **JSON Lines**
* Bruge `pandas.DataFrame.to_json(..., lines=True)` til streaming/append

---

## ✅ Forudsætninger

* ESP32 med MicroPython
* Thonny installeret (Interpreter: *MicroPython (ESP32)*)
* Python 3.9+ på PC
* Pakker:

  ```bash
  pip install pyserial pandas
  ```

---

## 🔌 Hardware (DHT22 → ESP32)

| DHT22 | ESP32 |
| ----: | :---- |
|   VCC | 3V3   |
|   GND | GND   |
|  DATA | GPIO4 |

*(De fleste DHT22-breakouts har indbygget pull-up.)*

---

## 🧪 ESP32-kode (Thonny / MicroPython)

> Sender én JSON-linje hver 2. sekund: `{"temperature": xx.x}`

```python
# ESP32: send JSON-linje med temperatur
import time
from machine import Pin
import dht

sensor = dht.DHT22(Pin(4))  # skift pin hvis nødvendigt

while True:
    try:
        sensor.measure()
        t = sensor.temperature()  # °C
        # kompakt JSON (uden mellemrum) for hurtig parsing
        print('{"temperature": %.1f}' % t)
    except Exception:
        pass
    time.sleep(2)
```

---

## 🐍 PC-logger (Python + pandas → JSONL)

> Kører uendeligt og **appender** til `measurements.jsonl`. Stop med **Ctrl+C**.
> Vi bruger `with open(...)` så filen lukkes automatisk.

```python
import serial, time, json, pandas as pd

# Ret porten:
#  Windows: 'COM3'  •  macOS: '/dev/tty.SLAB_USBtoUART'  •  Linux: '/dev/ttyUSB0' / '/dev/ttyACM0'
ser = serial.Serial('COM3', 115200, timeout=1)

with open('measurements.jsonl', 'a', encoding='utf-8') as f:
    while True:
        s = ser.readline().decode('utf-8', errors='replace').strip()
        if not s:
            continue
        try:
            obj = json.loads(s)      # forventer fx {"temperature": 22.1}
        except json.JSONDecodeError:
            continue

        obj['tid'] = time.time()     # PC-tidsstempel (sekunder siden 1970)

        # Én række → én JSON-linje (JSON Lines)
        pd.DataFrame([obj]).to_json(
            f,
            orient='records',
            lines=True
        )

        print(obj)
```

**Hvorfor JSON Lines?**
Det er append-venligt (én gyldig JSON pr. linje) og let at indlæse:

```python
import pandas as pd
df = pd.read_json('measurements.jsonl', lines=True)
print(df.head())
```

---

## ▶️ Sådan gør du

1. Kør ESP32-koden i Thonny (du bør se JSON-linjer i REPL).
2. Kør PC-scriptet (ret COM-porten).
3. Åbn `measurements.jsonl` – hver linje er ét måleobjekt.

---

## 🧪 Øvelser

1. **Tilføj luftfugtighed** på ESP32:

   ```python
   print('{"temperature": %.1f, "humidity": %.1f}' % (t, sensor.humidity()))
   ```

   (PC-scriptet virker uændret – pandas skriver blot de ekstra felter med.)
2. **Tilføj menneskelæselig tid** i PC-scriptet:

   ```python
   obj['iso'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(obj['tid']))
   ```
3. **Dagsfiler**: lav filnavn pr. dato:

   ```python
   fname = time.strftime('measurements_%Y%m%d.jsonl')
   with open(fname, 'a', encoding='utf-8') as f:
       ...
   ```

---

## ✅ Tjekliste

* [ ] Jeg ser JSON-linjer i Thonny
* [ ] `measurements.jsonl` vokser løbende
* [ ] Jeg kan indlæse filen med `pd.read_json(..., lines=True)`
* [ ] Jeg forstår hvorfor JSON Lines er egnet til streaming/append

---

**Klar til analyse!** Når det spiller, kan I udvide til flere sensorer eller plotte data direkte i Python.
