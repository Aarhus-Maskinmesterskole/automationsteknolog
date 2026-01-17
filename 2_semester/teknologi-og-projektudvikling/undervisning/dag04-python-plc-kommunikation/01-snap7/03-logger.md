csv_file = "log.csv"
# 📝 03 – Logger til .txt

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

## 📘 3. Eksempel: Log sensorværdier

```python
import time

for i in range(5):
    temperatur = 20 + i  # Simuleret måling
    with open('log.txt', 'a') as f:
        f.write(f'Temperatur: {temperatur} C\n')
    time.sleep(1)
```

---

## 📘 4. Eksempel: Log PLC-data (simuleret)

```python
from datetime import datetime

status = 'KØRER'
for i in range(3):
    tid = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    niveau = 75 + i
    with open('plc_log.txt', 'a') as f:
        f.write(f'{tid} | Motor status: {status} | Tank niveau: {niveau}\n')
```

---

## 📘 5. Tips til filnavne og formatering

- Brug dato/tid i filnavnet for at holde styr på logs, fx `log-2026-01-16.txt`
- Brug altid `with open(...)` så filen lukkes korrekt
- Skriv én måling pr. linje
- Brug evt. `,` eller `;` som separator hvis du vil importere i Excel senere

---

## 🧪 Øvelser

1. Skriv et program der logger 10 tilfældige tal til en fil (én pr. linje)
2. Log brugerens input (fx status eller måling) til en fil
3. Udvid PLC-eksemplet så der logges både temperatur og tryk
4. Ekstra: Tilføj dato/tid til hver loglinje

---

## ✅ Tjekliste

* [ ] Jeg kan skrive til en tekstfil med `open()`
* [ ] Jeg kan logge målinger eller status
* [ ] Jeg kan formatere loglinjer med tid og flere værdier
* [ ] Jeg har prøvet at åbne og læse logfilen bagefter

---
```

---

**Tip:**
- Du kan ændre PLC_IP, DB og filnavn hvis nødvendigt.
- Stop loggeren med Ctrl+C.
