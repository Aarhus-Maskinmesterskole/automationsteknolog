# Dag05 - Etablere PLC kommunikation og Write commands
## Etablering af PLC kommunikation
For at etablere kommunikation mellem en PLC og en computer (Python), skal vi først sikre os, at vi har de nødvendige biblioteker installeret. Vi vil bruge `Snap7` biblioteket til at kommunikere med Siemens PLC'er.

### Oprettelse af forbindelse
For at oprette en forbindelse til PLC'en, skal du kende IP-adressen, rack-nummeret og slot-nummeret på PLC'en.

- **IP-adresse**: Dette er den adresse, som PLC'en bruger på netværket.
- **Rack-nummer**: Dette er det rack, hvor CPU'en er placeret (normalt 0).
- **Slot-nummer**: Dette er det slot, hvor CPU'en er placeret (normalt 1) for Siemens S7-1200 og S7-1500.

### Step by step
1. Importer Snap7 biblioteket.
2. Opret en klient og forbind til PLC'en.

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
client.disconnect()
client.destroy()
```

## Skriv variabler til PLC'en
Nu hvor vi har etableret forbindelse, kan vi skrive variabler til PLC'en. Her er et eksempel på hvordan man skriver en BOOL, INT, REAL og WORD:

```python
import snap7
from snap7.util import set_bool, set_int, set_real, set_word

# =================== Opretter variabler for PLC-forbindelsen ==================
PLC_IP = '192.168.0.1'  
RACK = 0
SLOT = 1 

# =================== Opret en Snap7 klient og forbind til PLC'en ==============
client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

# =================== Variabler for DB og offsets ==================
DB_NUMBER = 1
BOOL_OFFSET = 0
BOOL_SIZE = 1

INT_OFFSET = 2
INT_SIZE = 2

REAL_OFFSET = 4
REAL_SIZE = 4

# =================== Læser DB1 for at få den nuværende værdi ==================
bool_value_raw = client.db_read(DB_NUMBER, BOOL_OFFSET, BOOL_SIZE)

# =================== Skriv en BOOL til DB1.DBX0.0 ==================
set_bool(bool_value_raw, 0, 0, True)  # Sæt bit DBX0.0 til True
client.db_write(DB_NUMBER, BOOL_OFFSET, bool_value_raw)  # Skriv tilbage til PLC'en
print("BOOL value skrevet til PLC")

# =================== Skriv en INT til DB1.DBW2 ==================
int_value_raw = client.db_read(DB_NUMBER, INT_OFFSET, INT_SIZE)
set_int(int_value_raw, 0, 123)  # Sæt INT til 123
client.db_write(DB_NUMBER, INT_OFFSET, int_value_raw)  # Skriv tilbage til PLC'en
print("INT value skrevet til PLC")

# =================== Skriv en REAL til DB1.DBD4 ==================
real_value_raw = client.db_read(DB_NUMBER, REAL_OFFSET, REAL_SIZE)
set_real(real_value_raw, 0, 123.45)  # Sæt REAL til 123.45
client.db_write(DB_NUMBER, REAL_OFFSET, real_value_raw)  # Skriv tilbage til PLC'en
print("REAL value skrevet til PLC")

# =================== Skriv en WORD til DB1.DBW8 ==================
word_value_raw = client.db_read(DB_NUMBER, WORD_OFFSET, WORD_SIZE)
set_word(word_value_raw, 0, 123)  # Sæt WORD til 123
client.db_write(DB_NUMBER, WORD_OFFSET, word_value_raw)  # Skriv tilbage til PLC'en
print("WORD value skrevet til PLC")

# =================== Afslut forbindelsen ==================
client.disconnect()
client.destroy()
```

### Forklaring af koden:
- `set_bool(bytearray, byte_index, bit_index, value)`: Bruges til at sætte en BOOL værdi i det rå bytearray, som vi læser fra PLC'en. 
- `set_int(bytearray, byte_index, value)`: Bruges til at sætte en INT værdi i det rå bytearray, som vi læser fra PLC'en.
- `set_real(bytearray, byte_index, value)`: Bruges til at sætte en REAL værdi i det rå bytearray, som vi læser fra PLC'en.
- `set_word(bytearray, byte_index, value)`: Bruges til at sætte en WORD værdi i det rå bytearray, som vi læser fra PLC'en.

Husk at altid læse den nuværende værdi fra PLC'en, før du skriver en ny værdi, da du ellers kan risikere at overskrive data, som du ikke ønsker at ændre.

Det er muligt at oprette et bytearray uden at skulle læse først men ved at læse først, sikrer du dig at du ikke overskriver data som du ikke ønsker at ændre.