# 03 – Real‑time Logger til TXT (pycomm3, uden pandas)

>  *Anden del af Dag 04 – Python ⇄ Allen-Bradley PLC med pycomm3*

---

## Introduktion

Du skal lave et Python-program, der cyklisk læser udvalgte PLC-tags (fx hvert sekund) og gemmer dem i en tekstfil (.txt eller .csv) med tidsstempel. Loggeren skal kunne genforbinde automatisk, hvis forbindelsen til PLC'en ryger.

---

## Formål

- Læse flere tags fra Allen-Bradley PLC med pycomm3
- Gemme data i tekstfil med tidsstempel (uden pandas)
- Loggeren skal kunne køre stabilt og genforbinde ved fejl

---

## Eksempel: Enkel PLC-logger med pycomm3 og open()

```python
import time
from datetime import datetime
from pycomm3 import LogixDriver

PLC_IP = "192.168.0.10"
TAGS   = ["Start_PB", "Motor_Speed", "Tank_Level"]
PERIOD = 1.0  # sekunder
LOGFILE = "log.txt"

header = "timestamp;" + ";".join(TAGS) + "\n"

while True:
    try:
        with LogixDriver(PLC_IP) as plc:
            # Skriv header hvis filen er tom
            try:
                with open(LOGFILE, 'x') as f:
                    f.write(header)
            except FileExistsError:
                pass
            while True:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                result = plc.read(*TAGS)
                values = [str(r.value) for r in result]
                line = f"{timestamp};" + ";".join(values) + "\n"
                with open(LOGFILE, 'a') as f:
                    f.write(line)
                print(line.strip())
                time.sleep(PERIOD)
    except Exception as e:
        print(f"Fejl: {e}. Prøver igen om 5 sek...")
        time.sleep(5)
```

---

**Tip:**
- Du kan ændre PLC_IP, PERIOD, LOGFILE og TAGS i koden eller som environment-variabler.
- Stop loggeren med Ctrl+C.

---

#### Signal-håndtering (pæn nedlukning)

Når operatøren trykker `Ctrl+C`, kaster Python et `KeyboardInterrupt`. Luk PLC-forbindelsen pænt, så du undgår hængende TCP-sessioner.

```python
try:
    main_loop()
except KeyboardInterrupt:
    print("Stopper logger...")
finally:
    # Her kan du lukke forbindelser hvis nødvendigt
    pass
```

---

### Kort opsummeret

* **Hold sample-tiden stabil**, men mål altid den faktiske loop-tid.
* **Append og flush** regelmæssigt for at minimere datatab.
* **Genforbind** automatisk, så et netværksglimt ikke stopper loggeren.
* **Ryd ordentligt op** på `Ctrl+C`, så både fil og PLC har det godt bagefter.

---

## 🧪 Øvelser

1. Tilpas loggeren så den også logger et ekstra tag, fx "Tank_Status".
2. Udskriv kun linjen til terminalen hvis "Start_PB" er True.
3. Tilføj dato til filnavnet, fx `log-2026-01-16.txt`.
4. Ekstra: Log også fejlbeskeder til en separat fil `error_log.txt`.

---

## ✅ Tjekliste

* [ ] Jeg kan skrive PLC-data til en tekstfil med open()
* [ ] Jeg kan logge flere tags og tidsstempel
* [ ] Jeg kan håndtere fejl og genforbinde
* [ ] Jeg har prøvet at åbne og læse logfilen bagefter

---

---

**Tip:**
- Du kan ændre PLC_IP, LOG_PERIOD, LOGFILE og TAGS i koden eller som environment-variabler.
- Stop loggeren med Ctrl+C.

```python
try:
    raw = cli.read_area(...)
except snap7.Snap7Exception as e:
    print("PLC-fejl:", e)
    time.sleep(2)
    cli = connect_plc()   # genopretter client-objektet
```

---

#### 5. Signal-håndtering (pæn nedlukning)

*Situation*
Når operatøren trykker `Ctrl+C`, kaster Python et `KeyboardInterrupt`. Lukker du ikke PLC-forbindelsen og fil-handle’en pænt, kan du ende med en korrupt CSV-fil og en hængende TCP-session i PLC’en.

*Løsning*

* Brug `try/except KeyboardInterrupt` **eller** et `with`-statement, hvor filen automatisk lukkes.
* Placer `cli.disconnect()` i en `finally:`-blok, så den altid køres – også ved andre exceptions.

```python
try:
    main_loop()
except KeyboardInterrupt:
    print("Stopper logger...")
finally:
    f.close()
    cli.disconnect()
```

Det er ikke blot god stil – nogle PLC-er nægter næste log-in, hvis den gamle ses­sion aldrig blev lukket.

---

### Kort opsummeret

* **Hold sample-tiden stabil**, men mål altid den faktiske loop-tid.
* **Overvåg jitter** hvis du senere skal lave fin-tids-analyse.
* **Append og flush** regelmæssigt for at minimere datatab.
* **Genforbind** automatisk, så et netværksglimt ikke stopper loggeren.
* **Ryd ordentligt op** på `Ctrl+C`, så både fil og PLC har det godt bagefter.

Med disse principper er din logger ikke blot en øvelsesopgave, men et værktøj, du faktisk tør lade køre natten over i et rigtigt procesanlæg.

---

## 🛠️ Kompetencer

Når du er færdig, kan du:

* måle faktisk loop‑frekvens og justere sleep‑tid,
* buffe data i RAM og dumpe batch‑vist, hvis disk‑IO er en flaskehals,
* bruge **ISO‑8601** tidsstempel eller Unix‑epoch afhængigt af downstream‑system,
* skrive *unit‑tests* (fx via `pytest`) for functions `connect_plc()` og `read_values()`.

---
