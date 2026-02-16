# 🌡️📈 05 - ESP32 → PC: Log **temperatur** og **luftfugtighed** til CSV (Python + Pandas)

Denne repo viser, hvordan du:
1) kører et **MicroPython**-program på **ESP32** (via Thonny), som sender `temperatur,luftfugtighed` (fx `22.1,44.2`) over seriellen, og  
2) kører et **Python**-script på PC, som **appender** disse målinger til en CSV-fil med **Pandas**.

Format for CSV:  
`tid,temperature,humidity`

---

## 🎯 Læringsmål
- Læse serielle data fra en COM-port  
- Parse `temp,humid`-linjer  
- Gemme løbende til **CSV** med `pandas.to_csv`  
- Forstå `mode='a'`, `index=False`, `header=not os.path.exists(...)` og `split(',', 1)`

---

## ✅ Forudsætninger

- **ESP32** med **MicroPython** firmware (kan flashes via Thonny / esptool)
- **DHT22** sensor for temperatur/luftfugtighed
- **Thonny** installeret (vælg *MicroPython (ESP32)* som interpreter)
- **Python 3.9+** på PC

Installer Python-pakker:
```bash
pip install pyserial pandas
````

---

## 🔌 Hardware – DHT22 til ESP32

| DHT22 | ESP32                      |
| ----: | :------------------------- |
|   VCC | 3V3                        |
|   GND | GND                        |
|  DATA | GPIO4 (kan ændres i koden) |

> De fleste DHT22-breakouts har indbygget pull-up. Ellers tilføj 10 kΩ mellem DATA og 3V3.

---

## 🧪 ESP32 (Thonny) – MicroPython program

Gem som **`main.py`** på ESP32 for autostart, eller kør direkte i Thonny.
Baud: **115200** (standard), output hvert 2. sekund i formatet `22.1,44.2`.

```python
# ESP32 + DHT22 → sender "temp,humid" over seriellen hvert 2. sekund
import time
from machine import Pin
import dht

# DHT22 på GPIO4 (tilpas hvis du bruger en anden pin)
sensor = dht.DHT22(Pin(4))

while True:
    try:
        sensor.measure()
        t = sensor.temperature()   # °C
        h = sensor.humidity()      # %RH
        print("{:.1f},{:.1f}".format(t, h))  # fx "22.1,44.2"
    except Exception:
        # Spring målingen over hvis sensoren driller
        pass
    time.sleep(2)
```

---

## 🐍 PC – Python logger (Pandas)

Kører uendeligt og **appender** til `measurements.csv`.
Stop med **Ctrl+C**. Ret **COM-porten** efter dit OS.

```python
import serial, time, pandas as pd, os

ser = serial.Serial('COM3', 115200, timeout=1)  # Windows: 'COM3' / macOS: '/dev/tty.SLAB_USBtoUART' / Linux: '/dev/ttyUSB0'
csv = 'measurements.csv'

while True:
    s = ser.readline().decode('utf-8', errors='replace').strip()
    if ',' in s:
        t, h = s.split(',', 1)  # del kun ved første komma → to felter
        pd.DataFrame([{
            'tid': time.time(),
            'temperature': float(t),
            'humidity': float(h)
        }]).to_csv(
            csv,
            mode='a',                        # append: opret fil hvis den ikke findes
            index=False,                     # ingen ekstra indeks-kolonne
            header=not os.path.exists(csv)   # skriv header kun første gang
        )
        print(s)
```

**Port-navne:**

* Windows: `"COM3"` (eller COM4/COM5 …)
* macOS: `"/dev/tty.SLAB_USBtoUART"` (kan variere afhængigt af USB-driver)
* Linux: `"/dev/ttyUSB0"` eller `"/dev/ttyACM0"`

---

## 🔍 Kort forklaring af nøglestumper

* `split(',', 1)` → splitter kun én gang ved **første** komma → giver **præcis to felter** (`t`, `h`).
* `mode='a'` → **append**: skriv i bunden; opret filen hvis den ikke findes. (I modsætning til `mode='w'` der overskriver.)
* `index=False` → undgår ekstra indeks-kolonne i CSV.
* `header=not os.path.exists(csv)` → skriv kolonnenavne **kun første gang**.

---

## ▶️ Sådan kører du

1. Slut DHT22 til ESP32 (se wiring).
2. Åbn Thonny → kør ESP32-programmet (eller gem som `main.py`). Du bør se linjer som `22.1,44.2` i Thonny’s REPL.
3. Kør PC-scriptet.
4. Åbn **`measurements.csv`** i Excel / VS Code og se nye rækker tikke ind.

---

## 📄 Eksempel på CSV

```csv
tid,temperature,humidity
1726060200.351,22.10,44.20
1726060202.355,22.12,44.18
1726060204.360,22.13,44.21
```

---

## 🧪 Øvelser / Udvidelser

1. **Menneskelæselig tid**: tilføj kolonnen `iso` med `time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())`.
2. **Dato-baseret fil**: `csv = f"measurements_{time.strftime('%Y%m%d')}.csv"`.
3. **Filter** værdier (fx `-40..125 °C` og `0..100 %RH`).
4. **Plot** CSV’en i Python (matplotlib) eller i et regneark.

---

## 🔧 Fejlfinding

* Får du ingen data? Tjek **rigtig COM-port** og **baud (115200)**.
* `ValueError` ved `float(...)`? ESP32 sender måske ikke kun tal – tjek hvad der printes i Thonny.
* Intet i CSV? Kør PC-scriptet fra en mappe du har rettigheder til, og hold filen lukket i andre programmer.
