# 04 – Skriv til PLC-tags med pycomm3

Her er fire helt simple opgaver, hvor du skal skrive til forskellige tags på en Allen-Bradley PLC med pycomm3.

---

## Opgave 1 – Skriv til Start_PB (BOOL)

```python
from pycomm3 import LogixDriver

PLC_IP = "192.168.1.209"

with LogixDriver(PLC_IP) as plc:
    result = plc.write(("Start_PB", True))
    print(f"Skrev True til Start_PB: {result}")
```

---

## Opgave 2 – Skriv til Motor_Speed (INT)

```python
from pycomm3 import LogixDriver

PLC_IP = "192.168.1.209"

with LogixDriver(PLC_IP) as plc:
    result = plc.write(("Motor_Speed", 42))
    print(f"Skrev 42 til Motor_Speed: {result}")
```

---

## Opgave 3 – Skriv til Tank_Level (REAL)

```python
from pycomm3 import LogixDriver

PLC_IP = "192.168.1.209"

with LogixDriver(PLC_IP) as plc:
    result = plc.write(("Tank_Level", 123.4))
    print(f"Skrev 123.4 til Tank_Level: {result}")
```

---

## Opgave 4 – Skriv til Temperature (STRING)

```python
from pycomm3 import LogixDriver

PLC_IP = "192.168.1.209"

with LogixDriver(PLC_IP) as plc:
    result = plc.write(("Temperature", "74.2"))
    print(f"Skrev '74.2' til Temperature: {result}")
    
```
## Opgave 5 – Forbindelse med fejl-håndtering (try/except/finally)

Skriv et Python-program der forsøger at oprette forbindelse til PLC'en med snap7, men brug `try/except/finally` til at håndtere fejl. Programmet skal:

- Prøve at oprette forbindelse til PLC'en (prøv evt. med forkert IP først for at fremprovokere fejl)
- Udskrive en fejlbesked hvis forbindelsen fejler
- Udskrive "Forbindelse oprettet" hvis det lykkes
- Altid lukke forbindelsen korrekt i `finally`-blokken

Ekstra: Udvid programmet så det også håndterer fejl hvis PLC'en taber forbindelsen undervejs (fx under skrivning).