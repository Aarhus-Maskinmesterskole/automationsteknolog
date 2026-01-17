# ⚠️ 08 – Error Handling (Fejlhåndtering)

Fejlhåndtering er vigtig i alle programmer – især når du arbejder med input, sensorer, kommunikation eller funktioner, hvor der kan opstå fejl. I Python bruges `try`, `except` og evt. `finally` til at fange og håndtere fejl, så dit program ikke crasher.

---

## 🔧 Indhold

* Hvorfor fejlhåndtering?
* `try` og `except`
* Håndtering af flere fejltyper
* `else` og `finally`
* Eksempler fra automation/PLC

---

## 📘 1. Hvorfor fejlhåndtering?

Når du fx læser data fra brugeren, en sensor eller en fil, kan der ske fejl (forkert datatype, ingen forbindelse, osv.). Uden fejlhåndtering stopper programmet med en fejlmeddelelse.

---

## 📘 2. Grundlæggende `try` og `except`

```python
try:
    temperatur = float(input("Indtast temperatur: "))
    print("Temperatur er:", temperatur)
except ValueError:
    print("Fejl: Du skal indtaste et tal!")
```

---

## 📘 3. Flere fejltyper

Du kan fange flere typer fejl:

```python
try:
    fil = open("data.txt")
    data = fil.read()
    fil.close()
except FileNotFoundError:
    print("Filen blev ikke fundet!")
except Exception as e:
    print("En anden fejl opstod:", e)
```

---

## 📘 4. Brug af `else` og `finally`

- `else` køres kun hvis der ikke opstår fejl.
- `finally` køres altid, uanset om der opstår fejl eller ej (fx til at lukke forbindelser).

```python
try:
    værdi = int(input("Indtast et heltal: "))
except ValueError:
    print("Det var ikke et heltal!")
else:
    print("Du indtastede:", værdi)
finally:
    print("Programmet er færdigt.")
```

---

## 📘 5. Eksempel fra automation/PLC

```python
try:
    from pycomm3 import LogixDriver
    PLC_IP = "192.168.0.10"  # eksempel-IP (ret til din PLC)
    with LogixDriver(PLC_IP) as plc:
        status = plc.read("Motor_Status")
        print("Motor status:", status.value)
except Exception as e:
    print("Fejl ved kommunikation med PLC:", e)
```

---

## 🧪 Øvelser

1. Lav et program der spørger brugeren om et tal og håndterer hvis input ikke er et tal.
2. Skriv kode der forsøger at åbne en fil og fanger FileNotFoundError.
3. Lav en funktion der læser en værdi fra en liste og håndterer IndexError hvis brugeren vælger et ugyldigt indeks.
4. Ekstra: Simulér kommunikation med en PLC og håndter generelle fejl med `except Exception`.

---

## ✅ Tjekliste

* [ ] Jeg kan bruge `try` og `except` til at fange fejl
* [ ] Jeg kan håndtere flere fejltyper
* [ ] Jeg kan bruge `else` og `finally`
* [ ] Jeg har prøvet fejlhåndtering i praksis

---
