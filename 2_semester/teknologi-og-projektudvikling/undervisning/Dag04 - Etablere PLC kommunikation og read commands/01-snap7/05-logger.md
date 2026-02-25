# 📝 05 – Logger til .txt

I denne guide lærer du at logge data fra PLC eller sensorer direkte til en tekstfil (.txt) med Python. Det er nyttigt til simpel datalogning, fejlfinding eller dokumentation.

---

## 🔧 Indhold

* Hvorfor logge data?
* Skriv til fil med `open()`
* Eksempel: Log sensorværdier
* Eksempel: Log PLC-data
* Tips til filnavne og formatering

---

## 📘 1. Hvorfor logge data?

Logning gør det muligt at gemme målinger, status eller fejl til senere analyse. Det kan bruges til dokumentation, fejlfinding eller rapportering.

---

## 📘 2. Skriv til fil med `open()`

```python
with open('log.txt', 'a') as f:
    f.write('Dette er en logbesked\n')
```

- `'a'` betyder append (tilføj til filen, uden at slette det gamle).
- Husk `\n` for at få linjeskift.

---


## 📘 3. Eksempel: Log PLC-værdier fra Emulate3D (snap7)

```python
import time
import snap7
from snap7.util import get_real, get_int
from datetime import datetime

PLC_IP = "192.168.0.100"  # Emulate3D PLC IP
RACK = 0
SLOT = 1
DB = 1

client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

for i in range(10):
    data = client.db_read(DB, 0, 8)  # Læs 8 bytes fra DB1
    temperatur = get_real(data, 0)   # DBD0
    tryk = get_real(data, 4)         # DBD4
    tid = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('plc_log.txt', 'a') as f:
        f.write(f'{tid} | Temperatur: {temperatur:.1f} C | Tryk: {tryk:.1f} bar\n')
    time.sleep(1)

client.disconnect()
```

---


## 📘 4. Eksempel: Log Emulate3D motorstatus og niveau

```python
import snap7
from snap7.util import get_bool, get_int
from datetime import datetime

PLC_IP = "192.168.0.100"
RACK = 0
SLOT = 1
DB = 2

client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

for i in range(10):
    data = client.db_read(DB, 0, 4)  # Læs 4 bytes fra DB2
    motor_on = get_bool(data, 0, 0)  # DBX0.0
    niveau = get_int(data, 2)        # DBW2
    tid = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('plc_log.txt', 'a') as f:
        f.write(f'{tid} | Motor: {"KØRER" if motor_on else "STOP"} | Niveau: {niveau}\n')
    time.sleep(1)

client.disconnect()
```

---

## 📘 5. Tips til filnavne og formatering

- Brug dato/tid i filnavnet for at holde styr på logs, fx `log-2026-01-16.txt`
- Brug altid `with open(...)` så filen lukkes korrekt
- Skriv én måling pr. linje
- Brug evt. `,` eller `;` som separator hvis du vil importere i Excel senere

---

## 🧪 Øvelser

1. Lav et TIA Portal-projekt med en DB, hvor du har følgende variabler:
    - BOOL: `Start` (start rullebånd)
    - BOOL: `Done` (PLC sætter denne til 1 når rullebåndet er færdig)
    - INT: `MotorDriftstid` (sekunder rullebåndet har kørt)
    - Rullebåndet skal køre i 10-12 sekunder (styres af PLC-programmet)

2. Python-program – byg trin for trin:

**a) Start simpelt:**
    - Skriv et program der opretter forbindelse til PLC'en (brug `try`, `except` og `finally` så forbindelsen altid lukkes korrekt).
    - Udskriv "Forbindelse oprettet" eller fejlbesked.
    - **Succeskriterie:** Programmet kan både vise "Forbindelse oprettet" og håndtere fejl, så der ikke opstår crash hvis PLC ikke kan kontaktes.


**b) Udvid programmet:**
    - Spørg brugeren om at starte rullebåndet (`input("Start rullebåndet? Tryk Enter for at starte")`).
    - Skriv `Start = 1` til PLC (DB).
    - **Succeskriterie:** Når brugeren trykker Enter, sættes Start-bit i PLC, og rullebåndet starter.


**c) Udvid igen:**
    - Sæt en løkke der overvåger `Done`-bit (læs fra DB indtil `Done = 1`).
    - Når `Done = 1`, læs værdien af `MotorDriftstid` fra DB og afslut løkken.
    - **Succeskriterie:** Programmet venter til rullebåndet er færdigt (Done=1), og kan læse driftstiden fra PLC.


**d) Udvid med logning:**
        - Tidsstempel og skriv værdien til en tekstfil med formatet:
            `2026-01-16 14:30:00 | Motor driftstid: XX sekunder` eller `tid, værdi`.
        - **Succeskriterie:** Hver gang rullebåndet har kørt, tilføjes en ny linje med tid og driftstid i logfilen.


**e) Udvid med reset og loop:**
    - Sæt `Done = 0` og `Start = 0` igen (reset).
    - Gør det muligt at starte forfra (loop).
    - **Succeskriterie:** Programmet afventer bruger input på ny.


**f) Husk:**
    - Brug `try`, `except` og `finally` til at håndtere fejl og sikre at forbindelsen til PLC altid lukkes korrekt, også hvis der opstår fejl undervejs.
    - **Succeskriterie:** Forbindelsen til PLC lukkes altid korrekt, også hvis der opstår fejl undervejs.

3. Prøv at åbne logfilen i Notepad eller Excel og se hvordan dataen ser ud.

## ✅ Tjekliste

* [ ] Jeg kan skrive til en tekstfil med `open()`
* [ ] Jeg kan logge målinger eller status
* [ ] Jeg kan formatere loglinjer med tid og flere værdier
* [ ] Jeg har prøvet at åbne og læse logfilen bagefter

---

**Tip:**
- Du kan ændre PLC_IP, DB og filnavn hvis nødvendigt.
- Stop loggeren med Ctrl+C.
