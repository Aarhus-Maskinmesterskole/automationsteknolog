# Dag04 - Read variabler fra PLC
## Etablering af PLC kommunikation
Først etablerer vi kommunikation mellem en PLC og en computer (Python). 

```python
import snap7
from snap7.util import *
# Opretter variabler for PLC-forbindelsen
PLC_IP = '192.168.0.1'  # Erstat med din PLC's IP-adresse
RACK = 0 # Dette findes i tia portal og kaldes dette for rail under Device configuration
SLOT = 1 # Dette findes i tia portal og er hvor CPU'en er placeret

# Opret en Snap7 klient
client = snap7.client.Client()

# Forbind til PLC'en
client.connect(PLC_IP, RACK, SLOT)
```

## Læs variabler fra PLC'en
Nu hvor vi har etableret forbindelse, kan vi læse variabler fra PLC'en. Her er et eksempel på hvordan man læser en BOOL, INT, REAL og WORD:

```python   
import snap7
from snap7.util import get_bool, get_int, get_real, get_word
# Opretter variabler for PLC-forbindelsen
PLC_IP = '192.168.0.1'  # Erstat med din PLC's IP-adresse
RACK = 0 # Dette findes i tia portal og kaldes dette for rail under Device configuration
SLOT = 1 # Dette findes i tia portal og er hvor CPU'en er placeret

# Opret en Snap7 klient
client = snap7.client.Client()

# Forbind til PLC'en
client.connect(PLC_IP, RACK, SLOT)

DB_NUMBER = 1
BOOL_OFFSET = 0
BOOL_SIZE = 1

# Læs en BOOL fra DB1.DBX0.0
bool_value_raw = client.db_read(DB_NUMBER, BOOL_OFFSET, BOOL_SIZE)  # DB1, BOOL_OFFSET=0, BOOL_SIZE=1 byte
bool_value = get_bool(bool_value_raw, 0, 0)  # Læs bit DBX0.0
print(f"BOOL value: {bool_value}")

INT_OFFSET = 2
INT_SIZE = 2
# Læs en INT fra DB1.DBW2
int_value_raw = client.db_read(DB_NUMBER, INT_OFFSET, INT_SIZE)  # DB1, INT_OFFSET=2, INT_SIZE=2 bytes
int_value = get_int(int_value_raw, 0)  # Læs INT fra byte 0
print(f"INT value: {int_value}")

REAL_OFFSET = 4
REAL_SIZE = 4
# Læs en REAL fra DB1.DBD4
real_value_raw = client.db_read(DB_NUMBER, REAL_OFFSET, REAL_SIZE)  # DB1, REAL_OFFSET=4, REAL_SIZE=4 bytes
real_value = get_real(real_value_raw, 0)  # Læs REAL fra byte 0
print(f"REAL value: {real_value}")

WORD_OFFSET = 8
WORD_SIZE = 2
# Læs en WORD fra DB1.DBW8
word_value_raw = client.db_read(DB_NUMBER, WORD_OFFSET, WORD_SIZE)  # DB1, WORD_OFFSET=8, WORD_SIZE=2 bytes
word_value = get_word(word_value_raw, 0)  # Læs WORD fra byte 0
print(f"WORD value: {word_value}")

# Husk at lukke forbindelsen når du er færdig
client.disconnect()
client.destroy()
```
## Forklaring på koden

### Variabler for indeksering i datablokken
```python
DB_NUMBER = 1
BOOL_OFFSET = 0
BOOL_SIZE = 1
```
- `DB_NUMBER`: Dette er det databloknummer, hvor dine variabler er placeret (f.eks. DB1).
- `BOOL_OFFSET`: Dette er byte-offset for den første variabel (f.eks. DBX0.0 starter ved byte 0).
- `BOOL_SIZE`: Dette er størrelsen i bytes for den type variabel, du vil læse (f.eks. 1 byte for BOOL).

### Bytearrays
- `client.db_read()`: Denne funktion læser rå byte-data fra PLC'en baseret på det angivne databloknummer, offset og størrelse.

### Læsning af en BOOL
```python
bool_value_raw = client.db_read(DB_NUMBER, BOOL_OFFSET, BOOL_SIZE)  # DB1, BOOL_OFFSET=0, BOOL_SIZE=1 byte
bool_value = get_bool(bool_value_raw, 0, 0)  # Læs bit DBX0.0
print(f"BOOL value: {bool_value}")
```

- `get_bool()`: Denne funktion konverterer de rå byte-data til en BOOL-værdi ved at specificere byte-indekset og bit-indekset (f.eks. bit 0 i byte 0 for DBX0.0).
- `print()`: Dette udskriver den læste BOOL-værdi.

### Læsning af en INT
```python
int_value_raw = client.db_read(DB_NUMBER, INT_OFFSET, INT_SIZE)  # DB1, INT_OFFSET=2, INT_SIZE=2 bytes
int_value = get_int(int_value_raw, 0)  # Læs INT fra byte 0
print(f"INT value: {int_value}")
```

- `get_int()`: Denne funktion konverterer de rå byte-data til en INT-værdi ved at specificere byte-indekset (f.eks. byte 0).

### Læsning af en REAL
```python
real_value_raw = client.db_read(DB_NUMBER, REAL_OFFSET, REAL_SIZE)  # DB1, REAL_OFFSET=4, REAL_SIZE=4 bytes
real_value = get_real(real_value_raw, 0)  # Læs REAL fra byte 0
print(f"REAL value: {real_value}")
```

- `get_real()`: Denne funktion konverterer de rå byte-data til en REAL-værdi ved at specificere byte-indekset (f.eks. byte 0).

### Læsning af en WORD
```python
word_value_raw = client.db_read(DB_NUMBER, WORD_OFFSET, WORD_SIZE)  # DB1, WORD_OFFSET=8, WORD_SIZE=2 bytes
word_value = get_word(word_value_raw, 0)  # Læs WORD fra byte 0
print(f"WORD value: {word_value}")
```

- `get_word()`: Denne funktion konverterer de rå byte-data til en WORD-værdi ved at specificere byte-indekset (f.eks. byte 0).

### Afslutning
Efter du har læst de ønskede variabler, er det vigtigt at lukke forbindelsen til PLC'en for at frigøre ressourcer:

```python
client.disconnect()
client.destroy()
```

- `client.disconnect()`: Dette lukker forbindelsen til PLC'en.
- `client.destroy()`: Dette frigør klientressourcerne.