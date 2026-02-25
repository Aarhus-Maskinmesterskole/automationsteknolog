# ⚙️ 01 – Installation og test af PySerial

I denne guide installerer du `pyserial` og lærer at identificere hvilken COM-port din ESP32 bruger. Du kører også et simpelt testscript for at sikre, at din Python kan modtage seriel data.

---

## 🎯 Mål for modulet

* Installere `pyserial`
* Finde og vælge korrekt seriel port
* Teste forbindelse til ESP32 med simpelt script

---

## 🧰 Installation af PySerial

Åbn din terminal i VS Code og kør:

```bash
pip install pyserial
```

> Hvis det ikke virker, prøv `python -m pip install pyserial`

---

## 🔌 Find ESP32’s COM-port

På **Windows**:

* Åbn Enhedshåndtering → Porte (COM & LPT)
* Se fx: `USB Serial Device (COM3)`

På **macOS/Linux**:

* I terminalen, kør:

```bash
ls /dev/tty.*     # macOS
ls /dev/ttyUSB*   # Linux
```

* Typisk noget som `/dev/ttyUSB0` eller `/dev/tty.SLAB_USBtoUART`

---

## 🧪 Testscript: modtag seriel data

```python
import serial

# Opretter serial connection gennem port 'COM3' ved en baudrate 115200
ser = serial.Serial('COM3', 115200)  

# Main loop
while True: 

    # ser er et objekt af serial. Serial indeholder funktionen (member) readline som læser den inkommende serielle string. Serial indeholder også decode og strip.
    # decode('utf-8') er en bestemt måde at repræsentere tegn på hvor strip fjerner alle whitespaces i en string. 
    linje = ser.readline().decode('utf-8').strip() 
    print(linje)
```

> Åbn først Thonny og kør ESP32-scriptet, så det sender data.
> Start derefter Python-scriptet i VS Code for at læse det.

---

## ✅ Tjekliste

* [ ] Jeg har installeret `pyserial` uden fejl
* [ ] Jeg kender hvilken COM-port min ESP32 bruger
* [ ] Jeg har kørt et Python-script som læser data fra ESP32
* [ ] Jeg kan se tekstlinjer fra ESP32 i min terminal

---

> Du er nu klar til at læse og gemme dine data direkte i Python.
