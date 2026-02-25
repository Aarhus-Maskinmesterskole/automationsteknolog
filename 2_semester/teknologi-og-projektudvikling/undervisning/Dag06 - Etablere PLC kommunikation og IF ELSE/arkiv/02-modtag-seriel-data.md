# 🧾 02 – Modtag seriel data i Python

I denne guide lærer du trin for trin at modtage simple beskeder fra ESP32 via seriel kommunikation. Vi holder det simpelt: ESP32 sender tekst, og Python modtager og printer det.

---

## 🎯 Mål for modulet

* Forstå seriel kommunikation mellem ESP32 og PC
* Modtage og printe data i Python
* Bruge `pyserial` til at læse fra COM-port

---

## 📤 Trin 1: Sørg for at ESP32 sender data

På din ESP32 (i Thonny eller VS Code), kør et simpelt script der printer beskeder:

```python
# ESP32 script (MicroPython)
while True:
    print("Hej fra ESP32!")
```

> Dette sender "Hej fra ESP32!" igen og igen via USB.

---

## 📥 Trin 2: Installer pyserial (hvis ikke gjort)

Hvis du ikke har gjort det i trin 1, installer pyserial:

```bash
pip install pyserial
```

---

## 📥 Trin 3: Find din COM-port

* **Windows:** Åbn Enhedshåndtering → Porte (COM & LPT) → Noter COM-port (fx COM3)
* **macOS/Linux:** Kør `ls /dev/ttyUSB*` eller `ls /dev/tty.*` i terminal → Noter port (fx /dev/ttyUSB0)

---

## 📥 Trin 4: Lav Python-script til at modtage

Opret en ny Python-fil i VS Code:

```python
import serial

# Erstat 'COM3' med din port og indstil den rigtige baudrate.
ser = serial.Serial('COM3', 115200)

# Main loop
while True:
    # Denne linje er det samme som forrige opgave men her har vi anvendt parameteren error=replace hvilket betyder at,
    # istedet for at crash programmet hvis der kommer en byte den ikke kan oversætte så vil den bare fortsætte med den mærkelige tegn.
    linje = ser.readline().decode('utf-8', error=replace).strip()
    print("Modtaget:", linje)
```

> Dette læser en linje ad gangen og printer den.

---

## 📥 Trin 5: Kør scriptet

1. Start ESP32-scriptet først (så det sender data).
2. Kør Python-scriptet i VS Code.
3. Du skal se "Modtaget: Hej fra ESP32!" i terminalen.

---

## 🧠 Tip

* Hvis du ser fejl, tjek portnavnet og baudrate (115200).
* Brug `Ctrl+C` for at stoppe scriptet.

---

## 🧪 Øvelser

1. Ændr ESP32-scriptet til at sende "Temperatur: 25°C".
2. Modtag det i Python og print det.
3. Prøv at sende tal i stedet for tekst.

---

## ✅ Tjekliste

* [ ] Jeg har fået ESP32 til at sende simple beskeder
* [ ] Jeg har fundet den rigtige COM-port
* [ ] Jeg har kørt Python-scriptet og set beskederne
* [ ] Jeg forstår hvordan data sendes via USB

---

## 🔧 DIY: Lav dit eget serielle projekt

**Opgave:** Lav et ESP32-script der sender "DIY: Min besked!" hver 2. sekund. Modtag det i Python og print det med et timestamp.

**Trin:**
1. På ESP32: Tilføj `import time` og `time.sleep(2)` i loopet.
2. I Python: Tilføj `import time` og print `time.time()` sammen med teksten.
3. Test det og se outputtet.

> Prøv selv – det er nemmere end det ser ud!

---

> Du har nu lært det grundlæggende i seriel kommunikation – klar til mere avancerede ting!
