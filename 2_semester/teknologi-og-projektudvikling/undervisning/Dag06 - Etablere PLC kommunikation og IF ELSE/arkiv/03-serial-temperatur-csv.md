# 💾 03 – Gem serielle data med Pandas

I denne øvelse lærer du at læse data fra en ESP32 via seriel port og gemme dem i en CSV-fil med **Pandas**. Eksemplet antager, at ESP32 sender **temperatur** som tal (fx `23.7`).

---

## 🎯 Læringsmål

* Læse serielle data fra en COM-port
* Strukturere data i en **DataFrame**
* Gemme løbende data til **CSV** med `pandas.to_csv`

---

## ✅ Forudsætninger

* Python installeret
* Pakker: `pyserial` og `pandas`

  ```bash
  pip install pyserial pandas
  ```
* ESP32, der sender temperatur som én linje ad gangen (fx `23.5`)

---

## 📤 Trin 1: Sørg for at ESP32 sender data

Genbrug jeres ESP32-script fra tidligere, men sørg for at **kun tal** sendes (evt. uden “T:” prefix), én linje pr. måling.

---

## 📥 Trin 2: Python-script (kontinuerlig log til CSV)

> Koden nedenfor læser kontinuerligt fra COM-porten og **appender** til `data.csv`. Stop med **Ctrl+C**.

```python
# Importér seriel (pyserial) til COM-port, time til tidsstempler og pandas til CSV-skrivning
import serial, time, pandas as pd
# Path (fra pathlib) bruges som fil-sti-objekt; p.exists() kan tjekke om filen findes
from pathlib import Path

# Åbn seriel port 'COM3' med 115200 baud; timeout=1s gør readline ikke-blokerende (returnerer b'' ved stilhed)
ser = serial.Serial('COM3', 115200, timeout=1)

# Opret et sti-objekt til CSV-filen. 'p' er "håndtaget" til filen data.csv
p = Path('data.csv')

# Uendelig løkke — stop programmet med Ctrl+C i terminalen
while True:
    # Læs én linje bytes fra seriel, dekod som UTF-8. errors='replace' erstatter ugyldige bytes med � i stedet for at crashe.
    line = ser.readline().decode('utf-8', errors='replace').strip()

    # Kun hvis der kom indhold (tom streng betyder typisk timeout uden data)
    if line:
        try:
            # Fortolk linjen som temperatur (tal). float() håndterer både "23" og "23.5".
            temperature = float(line)
        except ValueError:
            # Hvis linjen ikke er et tal (fx headers/diagnose), spring den over
            continue

        # Opret en mini-DataFrame med én række og skriv/append til CSV:
        #   - p: filstien (Path-objektet til 'data.csv')
        #   - mode='a': "append" — opret filen hvis den ikke findes, ellers tilføj i bunden (overskriver ikke)
        #   - index=False: skriv ikke DataFrame-indekset som ekstra kolonne i CSV
        #   - header=not p.exists(): skriv kolonnenavne KUN første gang (når filen endnu ikke findes)
        pd.DataFrame([{'tid': time.time(), 'temperature': temperature}]).to_csv(
            p,
            mode='a',
            index=False,
            header=not p.exists()
        )

        # Vis temperaturen i konsollen, så man kan se hvad der blev logget
        print(f"Temp: {temperature}")
```

**Port-navne:**

* Windows: `"COM3"` (eller COM4/COM5 …)
* macOS: fx `"/dev/tty.SLAB_USBtoUART"`
* Linux: fx `"/dev/ttyUSB0"` eller `"/dev/ttyACM0"`

---

## 🔎 Hvad betyder de vigtigste parametre?

* `p = Path('data.csv')` — et sti-objekt der peger på `data.csv`. `p.exists()` fortæller om filen findes.
* `mode='a'` — **append**: opret filen hvis den ikke findes; ellers tilføj i bunden. (I modsætning til `mode='w'`, der overskriver hele filen.)
* `index=False` — undgå at få en ekstra kolonne med DataFrame-indeks.
* `header=not p.exists()` — skriv kun kolonnenavne første gang (når filen ikke findes endnu).

---

## ▶️ Trin 3: Kør

1. Start ESP32-måleprogrammet.
2. Kør Python-scriptet.
3. Åbn `data.csv` i Excel eller VS Code og se, at rækkerne kommer ind løbende.

---

## 🧪 Øvelser

1. **Tilføj menneskelæselig tid:**
   Tilføj en kolonne `iso`:

   ```python
   {'tid': time.time(), 'iso': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), 'temperature': temperature}
   ```
2. **Filnavn pr. dag:**
   Skift `p = Path('data.csv')` til fx:

   ```python
   from time import strftime
   p = Path(f"data_{strftime('%Y%m%d')}.csv")
   ```
3. **Filtrér støj:**
   Log kun værdier i intervallet `-40 .. 125` (typisk temperatur):

   ```python
   if -40 <= temperature <= 125:
       # skriv til CSV
   ```

---

## ✅ Tjekliste

* [ ] Jeg kan se data i terminalen
* [ ] Jeg ser nye rækker i `data.csv`
* [ ] Jeg kan forklare `mode='a'`, `index=False`, `header=not p.exists()`
* [ ] Jeg kan ændre COM-porten og køre scriptet på min maskine

---

## 🔧 Ekstra: Hvis din ESP32 sender tekst som “T: 23.7”

Indsæt før `float()`:

```python
line = line.replace('T:', '').strip()
```

---

Du har nu et pænt, begyndervenligt workflow til at logge målinger fra ESP32 i realtid med Pandas. Næste naturlige skridt er at plotte CSV’en i Python eller i et regneark og tale om samplingfrekvens og sensorkalibrering.
