# 🧪 Opgave 1 – Læs og tidsstempl målinger fra DHT22-sensor

I denne opgave skal du hente målinger i realtid fra en DHT22-sensor via ESP32 og MicroPython. Målingerne skal læses i Python via seriel port, tilføjes et tidsstempel og gemmes i en Pandas DataFrame. Du skal dermed opbygge et realtidsopsamlingssystem til temperatur og luftfugtighed.

---

## 🎯 Mål for opgaven

- Modtage live data fra ESP32 og DHT22 via seriel port
- Parse og validere målinger (temperatur/fugtighed)
- Tidsstemple hver måling med `pd.Timestamp.now()`
- Gem resultatet i Pandas DataFrame til videre analyse

---

## ⚙️ Forudsætninger

- Du har installeret MicroPython på din ESP32
- Du har flash'et ESP32 med en script der sender DHT22-målinger i formatet:
  ```
  24.6, 45.2
  24.7, 45.1
  ```
- Du kender portnavnet på din ESP32 (fx COM3 eller /dev/ttyUSB0)

---

## 👨‍💻 Eksempelkode (Python på PC)

```python
import pandas as pd
import serial
import time

# Opsætning af seriel port
ser = serial.Serial('COM3', 115200, timeout=1)
data = []

print("Starter måling...")

while len(data) < 50:
    linje = ser.readline().decode().strip()
    if "," in linje:
        try:
            temp, fugt = map(float, linje.split(","))
            tidspunkt = pd.Timestamp.now()
            data.append({"tid": tidspunkt, "temp": temp, "fugt": fugt})
            print(f"{tidspunkt} → Temp: {temp} °C, Fugt: {fugt} %")
        except ValueError:
            continue
    time.sleep(0.1)

ser.close()
df = pd.DataFrame(data)
df.to_csv("dht22_log.csv", index=False)
```

---

## 🧪 Udvidelser (frivillige)

- Tilføj kolonne med `måling_id`
- Gør antal målinger konfigurerbart
- Vis live-data i Streamlit med `st.line_chart`

---

## ✅ Tjekliste

- [ ] Jeg har modtaget data korrekt fra ESP32 via seriel port
- [ ] Jeg har parsed temperatur og fugtighed til floats
- [ ] Jeg har tilføjet `pd.Timestamp.now()` til hver række
- [ ] Jeg har gemt og verificeret CSV-filen med 50 målinger

---

> Live-data er kun brugbar, hvis den er korrekt tidsstemplet og struktureret. Med denne opgave skaber du et datasæt, som kan bruges til sanity checks, visualisering og plausibilitetstest i næste trin.
