# Dag 05 - Fysisk input og output: Læsning og skrivning til PLC'en
For at læse og skrive data til en PLC, har vi brug for at forstå, hvordan vi kan interagere med de fysiske indgange og udgange, der er tilsluttet PLC'en. Dette indebærer at læse tilstanden på fysiske knapper, sensorer eller andre inputenheder og derefter skrive kommandoer tilbage til PLC'en for at styre aktuatorer som motorer, lamper eller relæer.

## Læsning af fysiske indgange
For at læse en fysisk indgang, skal vi først etablere en forbindelse til PLC'en og derefter bruge den relevante funktion til at hente data fra den specifikke adresse, hvor indgangen er tilsluttet. For eksempel, `%I0.0`, `%Q0.0` eller `%M0.0` for digitale indgange, udgange og memory bits.

```python
import snap7
from snap7.util import get_bool
from snap7.types import S7AreaPA  # PA=Output


# Opretter variabler for PLC-forbindelsen
PLC_IP = '192.168.0.1'  # Erstat med din PLC's IP-adresse
RACK = 0 
SLOT = 1

AREA = S7AreaPE  # Vi vil læse en fysisk indgang
DB_NUMBER = 1    # Datablok nummer (hvis relevant)
I_OFFSET = 0         # Indgangens byte offset
I_SIZE = 1           # Antal bytes at læse (1 byte for digitale indgange)

# Opret en Snap7 klient og forbind
client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

# Læs en digital indgang (f.eks. S1 på %I0.0)
i_bytes_raw = client.read_area(AREA, DB_NUMBER, I_OFFSET, I_SIZE)
S1 = get_bool(i_bytes_raw, 0, 0)  # Læs bit 0 i byte 0 (S1) -> I0.0
print(f"S1 status: {S1}")
client.disconnect()
client.destroy()
```
### Forklaring af koden
- `client.read_area(AREA, DB_NUMBER, I_OFFSET, I_SIZE)`: Denne funktion læser data fra PLC'ens inputområde (PE) på rack 0, slot 0, startende ved byte 0 og læser 1 byte.
- `get_bool(i_bytes_raw, 0, 0)`: Denne funktion udtrækker den specifikke bit (bit 0 i byte 0) fra det rå bytearray, som vi læste fra PLC'en, og returnerer det som en boolean værdi (True/False).

## Læsning af fysiske udgange
Ligesom vi kan læse indgange, kan vi også læse udgange for at se, hvad der aktuelt er tændt eller slukket. Dette kan være nyttigt for at verificere, at vores kommandoer har haft den ønskede effekt.

```python
import snap7
from snap7.util import get_bool
from snap7.types import S7AreaPA  # PA=Output

# Opretter variabler for PLC-forbindelsen
PLC_IP = '192.168.0.1'  # Erstat med din PLC's IP-adresse
RACK = 0 
SLOT = 1

AREA = S7AreaPA  # Vi vil læse en fysisk udgang
Q_OFFSET = 0         # Udgangens byte offset
Q_SIZE = 1           # Antal bytes at læse (1 byte for digitale udgange)
# Læs en digital udgang (f.eks. Q1 på %Q0.0)
q_bytes_raw = client.read_area(AREA, DB_NUMBER, Q_OFFSET, Q_SIZE)
Q1 = get_bool(q_bytes_raw, 0, 0)  # Læs bit 0 i byte 0 (Q1) -> Q0.0
print(f"Q1 status: {Q1}")
```

## Skrivning til fysiske udgange
For at skrive til en fysisk udgang, følger vi en lignende proces, men vi bruger en anden funktion til at skrive data til PLC'en. For eksempel, hvis vi vil sætte en udgang (f.eks. Q1 på %Q0.0), kan vi gøre det som følger:

```python
import snap7
from snap7.util import set_bool
# Opretter variabler for PLC-forbindelsen
PLC_IP = '192.168.0.1'  # Erstat med din PLC's IP-adresse
RACK = 0 
SLOT = 1

AREA = S7AreaPA  # Vi vil skrive til en fysisk udgang
DB_NUMBER = 1    # Datablok nummer (hvis relevant)
Q_OFFSET = 0         # Udgangens byte offset
Q_SIZE = 1           # Antal bytes at skrive (1 byte for digitale udgange)

# Opret en Snap7 klient og forbind
client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)
# Skriv en digital udgang (f.eks. Q1 på %Q0.0)
q_bytes_raw = client.read_area(AREA, DB_NUMBER, Q_OFFSET, Q_SIZE)  # Læs det nuværende byte for at undgå at overskrive andre bits
set_bool(q_bytes_raw, 0, 0, True)  # Sæt bit 0 i byte 0 (Q1) til True
client.write_area(AREA, DB_NUMBER, Q_OFFSET, q_bytes_raw)  # Skriv det muterede bytearray tilbage til PLC'en
print("Q1 er sat til True")
client.disconnect()
client.destroy()
```
### Forklaring af koden
- `client.read_area(AREA, DB_NUMBER, Q_OFFSET, Q_SIZE)`: Før vi skriver til udgangen, læser vi det nuværende byte for at sikre, at vi ikke overskriver andre bits i samme byte, som måske styrer andre udgange.
- `set_bool(q_bytes_raw, 0, 0, True)`: Denne funktion sætter den specifikke bit (bit 0 i byte 0) i det rå bytearray til True, hvilket vil tænde udgangen Q1.
- `client.write_area(AREA, DB_NUMBER, Q_OFFSET, q_bytes_raw)`: Denne funktion skriver det muterede bytearray tilbage til PLC'en, hvilket opdaterer udgangen baseret på vores logik.

## Læsning af memory bits
Memory bits (M-bits) bruges ofte til at holde midlertidige værdier eller statusinformation, der ikke er direkte knyttet til fysiske indgange eller udgange. For at læse en memory bit, kan vi bruge følgende kode:

```python
import snap7
from snap7.util import get_bool
from snap7.types import S7AreaMK  # MK=Memory
# Opretter variabler for PLC-forbindelsen
PLC_IP = '192.168.0.1'  # Erstat med din PLC's IP-adresse
RACK = 0
SLOT = 1
AREA = S7AreaMK  # Vi vil læse en memory bit
DB_NUMBER = 1    # Datablok nummer (hvis relevant)
M_OFFSET = 0         # Memory bit offset
M_SIZE = 1           # Antal bytes at læse (1 byte for 8 bits)
# Opret en Snap7 klient og forbind
client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)
# Læs en memory bit (f.eks. M0.0)
m_bytes_raw = client.read_area(AREA, DB_NUMBER, M_OFFSET, M_SIZE)
M0 = get_bool(m_bytes_raw, 0, 0)  # Læs bit 0 i byte 0 (M0.0)
print(f"M0 status: {M0}")
client.disconnect()
client.destroy()
```

### Forklaring af koden
- `client.read_area(AREA, DB_NUMBER, M_OFFSET, M_SIZE)`: Denne funktion læser data fra PLC'ens memory område (MK) på rack 0, slot 0, startende ved byte 0 og læser 1 byte.
- `get_bool(m_bytes_raw, 0, 0)`: Denne funktion udtrækker den specifikke bit (bit 0 i byte 0) fra det rå bytearray, som vi læste fra PLC'en, og returnerer det som en boolean værdi (True/False).

## Skrivning til memory bits
For at skrive til en memory bit, kan vi bruge følgende kode:

```python
import snap7
from snap7.util import set_bool
from snap7.types import S7AreaMK  # MK=Memory
# Opretter variabler for PLC-forbindelsen
PLC_IP = '192.168.0.1'
RACK = 0
SLOT = 1
AREA = S7AreaMK  # Vi vil skrive til en memory bit
DB_NUMBER = 1    # Datablok nummer (hvis relevant)
M_OFFSET = 0         # Memory bit offset
M_SIZE = 1           # Antal bytes at skrive (1 byte for 8 bits)
# Opret en Snap7 klient og forbind
client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)
# Skriv en memory bit (f.eks. M0.0)
m_bytes_raw = client.read_area(AREA, DB_NUMBER, M_OFFSET, M_SIZE)  # Læs det nuværende byte for at undgå at overskrive andre bits
set_bool(m_bytes_raw, 0, 0, True)  # Sæt bit 0 i byte 0 (M0) til True
client.write_area(AREA, DB_NUMBER, M_OFFSET, m_bytes_raw)  # Skriv det muterede bytearray tilbage til PLC'en
print("M0 er sat til True")
client.disconnect()
client.destroy()
```
### Forklaring af koden
- `client.read_area(AREA, DB_NUMBER, M_OFFSET, M_SIZE)`: Før vi skriver til memory bit, læser vi det nuværende byte for at sikre, at vi ikke overskriver andre bits i samme byte.
- `set_bool(m_bytes_raw, 0, 0, True)`: Denne funktion sætter den specifikke bit (bit 0 i byte 0) i det rå bytearray til True, hvilket vil opdatere memory bit M0.
- `client.write_area(AREA, DB_NUMBER, M_OFFSET, m_bytes_raw)`: Denne funktion skriver det muterede bytearray tilbage til PLC'en, hvilket opdaterer memory bit baseret på vores logik.

