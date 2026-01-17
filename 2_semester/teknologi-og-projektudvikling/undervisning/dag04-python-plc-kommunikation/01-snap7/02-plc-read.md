<!-- File: dag09-snap7/02-plc-read.md -->

# 02 – PLC‑Connect & Read BOOL/INT/REAL

### 1. Opgave 1 – Læs en **BOOL** fra et DB (DBX)

> Forudsætninger i TIA Portal:
>
> * CPU tillader **PUT/GET** (”Permit access with PUT/GET…”).
> * Det pågældende **DB er uden “Optimized block access”**, så byte-/bit-adresser matcher.

```python
# save as opg1_read_bool.py
# pip install python-snap7

import snap7
from snap7.util import get_bool

# ── UDFYLD DISSE ───────────────────────────────────────────────
PLC_IP     = "192.168.0.1"  # PLC'ens IP
RACK       = 0              # S7-1200/1500 = rack 0
SLOT       = 1              # S7-1200: slot 1  |  S7-1500: slot 0
DB_NUMBER  = 1              # DB-nummer i TIA Portal
BOOL_BYTE  = 0              # DBX<BYTE>.<BIT>  -> byte-del (0..n)
BOOL_BIT   = 1              # DBX<byte>.<BIT>  -> bit-del  (0..7)
# ───────────────────────────────────────────────────────────────

# Opret klient og forbind
client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

# Læs netop den ene byte, som rummer vores bit
raw = client.db_read(DB_NUMBER, BOOL_BYTE, 1)

# Pak bit'en ud fra den læste bytebuffer (offset 0 i bufferen)
my_bool = get_bool(raw, 0, BOOL_BIT)

print(f"BOOL @ DB{DB_NUMBER}.DBX{BOOL_BYTE}.{BOOL_BIT} = {my_bool}")

# Oprydning
client.disconnect()
client.destroy()
```

Kør i terminalen:

```bash
python opg1_read_bool.py
```

**Hvorfor er det så kort?**
Vi læser kun den **ene byte**, der indeholder bit’en, og bruger `get_bool` til at plukke den specifikke **bit** ud. Det minimerer både trafik og risikoen for at overskrive/fejllæse andre data.

**Fejlfinding på 30 sekunder**

* Tjek IP, rack/slot (1200: 0/1, 1500: 0/0).
* Tjek at DB **ikke** er “optimized”.
* Tjek at CPU **tillader PUT/GET**.

Når denne virker, er mønsteret identisk for INT/REAL/WORD i de næste opgaver—du læser bare 2 eller 4 bytes og bruger den rigtige `get_*`-funktion.


## 2. Opgave 2 – Læs en **INT** (DBW)

> **Forudsætning:** DB’et er **uden** “Optimized block access”, og CPU tillader **PUT/GET**.

```python
# save as opg2_read_int.py
import snap7
from snap7.util import get_int

IP   = "192.168.0.1"  # PLC IP
RACK = 0              # S7-1200/1500 = rack 0
SLOT = 1              # S7-1200 = slot 1, S7-1500 = slot 0
DB   = 1              # DB-nummer i TIA Portal

INT_START_BYTE = 2    # DBW2  -> starter ved byte 2
BYTES_TO_READ  = 2    # INT er 2 bytes

client = snap7.client.Client()
client.connect(IP, RACK, SLOT)

data    = client.db_read(DB, INT_START_BYTE, BYTES_TO_READ)
my_int  = get_int(data, 0)  # offset 0 i den buffer vi lige læste

print("my_int:", my_int)

client.disconnect()
```

Kør:

```bash
python opg2_read_int.py
```

---

## 3. Opgave 3 – Læs en **REAL** (DBD)

```python
# save as opg3_read_real.py
import snap7
from snap7.util import get_real

IP   = "192.168.0.1"
RACK = 0
SLOT = 1
DB   = 1

REAL_START_BYTE = 4   # DBD4 -> starter ved byte 4
BYTES_TO_READ   = 4   # REAL er 4 bytes (float32)

client = snap7.client.Client()
client.connect(IP, RACK, SLOT)

data     = client.db_read(DB, REAL_START_BYTE, BYTES_TO_READ)
my_real  = get_real(data, 0)

print("my_real:", my_real)

client.disconnect()
```

Kør:

```bash
python opg3_read_real.py
```

---

## 4. Opgave 4 – Læs en **WORD** (DBW)

```python
# save as opg4_read_word.py
import snap7
from snap7.util import get_word

IP   = "192.168.0.1"
RACK = 0
SLOT = 1
DB   = 1

WORD_START_BYTE = 8   # DBW8 -> starter ved byte 8
BYTES_TO_READ   = 2   # WORD er 2 bytes (uint16)

client = snap7.client.Client()
client.connect(IP, RACK, SLOT)

data     = client.db_read(DB, WORD_START_BYTE, BYTES_TO_READ)
my_word  = get_word(data, 0)

print("my_word:", my_word)

client.disconnect()
```

Kør:

```bash
python opg4_read_word.py
```

---

#### Små noter (samme for alle opgaver)

* **Adresser:**

  * BOOL: `DBX<byte>.<bit>`
  * INT/WORD: `DBW<byte>` (2 bytes)
  * REAL/DINT: `DBD<byte>` (4 bytes)
* Brug samme **IP, rack og slot** som i TIA Portal.
* Hvis læsning fejler: tjek at DB **ikke** er “optimized” og at PLC’en tillader **PUT/GET**.
