# 💧 04 – Gem serielle **humidity**-data med Pandas

I denne øvelse læser du luftfugtighed fra ESP32 via seriel port og gemmer løbende til en CSV-fil med **Pandas**.

---

## 🎯 Læringsmål

* Læse serielle data (humidity) fra en COM-port
* Lægge data i en **DataFrame**
* Append’e rækker til **CSV** med de rigtige `to_csv`-parametre

---

## ✅ Forudsætninger

* `pyserial` og `pandas` installeret:

  ```bash
  pip install pyserial pandas
  ```
* ESP32, der sender **kun tal** for luftfugtighed (fx `48.6`) én linje ad gangen

---

## 📥 Python-script: kontinuerlig log til `humidity.csv`

> Scriptet læser kontinuerligt og **appender** til `humidity.csv`. Stop med **Ctrl+C**.

```python
# Importér seriel (pyserial), time til tidsstempler og pandas til CSV-skrivning
import serial, time, pandas as pd
# Path (fra pathlib) bruges som fil-sti-objekt; p.exists() kan tjekke om filen findes
from pathlib import Path

# Åbn seriel port 'COM3' med 115200 baud; timeout=1s gør readline ikke-blokerende (returnerer b'' ved stilhed)
ser = serial.Serial('COM3', 115200, timeout=1)

# Opret et sti-objekt til CSV-filen. 'p' er "håndtaget" til filen humidity.csv
p = Path('humidity.csv')

# Uendelig løkke — stop programmet med Ctrl+C i terminalen
while True:
    # Læs én linje bytes fra seriel, dekod som UTF-8. errors='replace' undgår crash ved skæve bytes
    line = ser.readline().decode('utf-8', errors='replace').strip()

    # Kun hvis der kom indhold (tom streng = timeout uden data)
    if line:
        try:
            # Fortolk linjen som luftfugtighed i %RH (tal). float() håndterer fx "55" og "55.2"
            humidity = float(line)
        except ValueError:
            # Hvis linjen ikke er et tal (fx diagnostic/headers), spring den over
            continue

        # Opret en mini-DataFrame med én række og skriv/append til CSV:
        #   - p: filstien (Path-objekt til 'humidity.csv')
        #   - mode='a': "append" — opret filen hvis den ikke findes; tilføj ellers nederst
        #   - index=False: skriv ikke DataFrame-indekset som ekstra kolonne
        #   - header=not p.exists(): skriv kolonnenavne kun første gang (når filen ikke findes endnu)
        pd.DataFrame([{'tid': time.time(), 'humidity': humidity}]).to_csv(
            p,
            mode='a',
            index=False,
            header=not p.exists()
        )

        # Vis målingen i konsollen
        print(f"Humidity: {humidity} %RH")
```

**Port-navne:**

* Windows: `"COM3"` (eller COM4/COM5 …)
* macOS: fx `"/dev/tty.SLAB_USBtoUART"`
* Linux: fx `"/dev/ttyUSB0"` eller `"/dev/ttyACM0"`

---

## 🔧 Hvis din ESP32 sender “H: 55.2”

Indsæt før `float()`:

```python
line = line.replace('H:', '').strip()
```

---

## 🧪 Øvelser

1. **Ekstra kolonne (menneskelæselig tid):**
   Udvid dict’en med:

   ```python
   'iso': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
   ```
2. **Valider interval:**
   Log kun værdier i 0–100 %RH:

   ```python
   if 0 <= humidity <= 100:
       # skriv til CSV
   ```
3. **Fil pr. dag:**
   Skift filnavn til dato-baseret:

   ```python
   from time import strftime
   p = Path(f"humidity_{strftime('%Y%m%d')}.csv")
   ```

---

## ✅ Tjekliste

* [ ] Jeg kan se “Humidity: … %RH” i terminalen
* [ ] `humidity.csv` bliver oprettet og vokser, efterhånden som data kommer ind
* [ ] Jeg kan forklare `mode='a'`, `index=False`, `header=not p.exists()`
* [ ] Jeg kan ændre port og køre scriptet på min maskine

---

Når det virker, er næste skridt at plotte luftfugtigheden over tid eller at logge **både** temperatur og luftfugtighed i samme CSV (to kolonner).
