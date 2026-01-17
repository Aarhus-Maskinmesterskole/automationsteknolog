# 04 – Skriv til PLC med snap7

Her er fire helt simple opgaver, hvor du skal skrive til forskellige typer i en Siemens S7-PLC med snap7.

---

## Opgave 1 – Skriv til BOOL (DBX0.0)

```python
import snap7
from snap7.util import set_bool

PLC_IP = "192.168.0.1"
RACK = 0
SLOT = 1
DB = 1

cli = snap7.client.Client()
cli.connect(PLC_IP, RACK, SLOT)

buf = bytearray(1)  # 1 byte er nok til én bool
set_bool(buf, 0, 0, True)  # DBX0.0 = True
cli.db_write(DB, 0, buf)
cli.disconnect()
print("Skrev True til DBX0.0 og lukkede forbindelsen.")
```

---

## Opgave 2 – Skriv til INT (DBW2)

```python
import snap7
from snap7.util import set_int

PLC_IP = "192.168.0.1"
RACK = 0
SLOT = 1
DB = 1

client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

buf = bytearray(2)
set_int(buf, 0, 1234)  # DBW2 = 1234
client.db_write(DB, 2, buf)
client.disconnect()
print("Skrev 1234 til DBW2 og lukkede forbindelsen.")
```

---

## Opgave 3 – Skriv til REAL (DBD4)

```python
import snap7
from snap7.util import set_real

PLC_IP = "192.168.0.1"
RACK = 0
SLOT = 1
DB = 1

client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

buf = bytearray(4)
set_real(buf, 0, 42.5)  # DBD4 = 42.5
client.db_write(DB, 4, buf)
client.disconnect()
print("Skrev 42.5 til DBD4 og lukkede forbindelsen.")
```

---

## Opgave 4 – Skriv til WORD (DBW6)

```python
import snap7
from snap7.util import set_word

PLC_IP = "192.168.0.1"
RACK = 0
SLOT = 1
DB = 1

client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

buf = bytearray(2)
set_word(buf, 0, 0xFF)  # DBW6 = 0xFF
client.db_write(DB, 6, buf)
client.disconnect()
print("Skrev 0xFF til DBW6 og lukkede forbindelsen.")
```
