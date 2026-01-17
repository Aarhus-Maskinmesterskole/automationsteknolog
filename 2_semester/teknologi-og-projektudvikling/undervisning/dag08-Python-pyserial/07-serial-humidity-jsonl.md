# 💧➡️🧾 07 - Log **humidity** som JSON Lines (ESP32 → Python + Pandas)

ESP32 sender JSON-objekter som `{"humidity": 44.2}` over seriel. PC’en logger løbende til en **JSON Lines**-fil (`.jsonl`) med **pandas**.

Eksempel på fil (`humidity.jsonl`):
```

{"humidity":44.2,"tid":1726060200.351}
{"humidity":44.1,"tid":1726060202.358}

````

---

## 🎯 Læringsmål
- Udsende målinger som **JSON** fra ESP32  
- Læse serielle data i Python og gemme som **JSON Lines**  
- Bruge `pandas.DataFrame.to_json(..., lines=True)` til streaming/append

---

## ✅ Forudsætninger
- ESP32 med MicroPython  
- Thonny installeret (Interpreter: *MicroPython (ESP32)*)  
- Python 3.9+ på PC  
- Pakker:

```bash
  pip install pyserial pandas
````

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

> Sender én JSON-linje hver 2. sekund: `{"humidity": xx.x}`

```python
# ESP32: send JSON-linje med luftfugtighed
import time
from machine import Pin
import dht

sensor = dht.DHT22(Pin(4))  # skift pin hvis nødvendigt

while True:
    try:
        sensor.measure()
        h = sensor.humidity()  # %RH (float)
        # kompakt JSON (uden mellemrum) for hurtig parsing
        print('{"humidity": %.1f}' % h)
    except Exception:
        pass
    time.sleep(2)
```

---

## 🐍 PC-logger (Python + pandas → JSONL)

> Kører uendeligt og **appender** til `humidity.jsonl`. Stop med **Ctrl+C**.
> Vi bruger `with open(...)`, så filen lukkes automatisk.

```python
import serial, time, json, pandas as pd

# Ret porten:
#  Windows: 'COM3'  •  macOS: '/dev/tty.SLAB_USBtoUART'  •  Linux: '/dev/ttyUSB0' / '/dev/ttyACM0'
ser = serial.Serial('COM3', 115200, timeout=1)

with open('humidity.jsonl', 'a', encoding='utf-8') as f:
    while True:
        s = ser.readline().decode('utf-8', errors='replace').strip()
        if not s:
            continue
        try:
            obj = json.loads(s)      # forventer fx {"humidity": 44.2}
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
Append-venligt (én gyldig JSON pr. linje) og let at indlæse i pandas:

```python
import pandas as pd
df = pd.read_json('humidity.jsonl', lines=True)
print(df.head())
```

---

## ▶️ Sådan gør du

1. Kør ESP32-koden i Thonny (du bør se JSON-linjer i REPL).
2. Kør PC-scriptet (ret COM-porten).
3. Åbn `humidity.jsonl` – hver linje er ét måleobjekt.

---

## 🧪 Øvelser

1. **Tilføj temperatur også** på ESP32:

   ```python
   print('{"humidity": %.1f, "temperature": %.1f}' % (sensor.humidity(), sensor.temperature()))
   ```

   (PC-scriptet virker uændret – pandas skriver blot begge felter.)
2. **Menneskelæselig tid** i PC-scriptet:

   ```python
   obj['iso'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(obj['tid']))
   ```
3. **Dagsfiler** (PC):

   ```python
   fname = time.strftime('humidity_%Y%m%d.jsonl')
   with open(fname, 'a', encoding='utf-8') as f:
       ...
   ```

---

## ✅ Tjekliste

* [ ] Jeg ser JSON-linjer i Thonny
* [ ] `humidity.jsonl` vokser løbende
* [ ] Jeg kan indlæse filen med `pd.read_json(..., lines=True)`
* [ ] Jeg kan forklare fordelen ved JSON Lines til streaming/append
