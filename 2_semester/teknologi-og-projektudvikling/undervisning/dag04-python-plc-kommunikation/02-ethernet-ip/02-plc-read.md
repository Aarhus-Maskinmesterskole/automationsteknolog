<!-- File: dag09-pycomm3/02-plc-read.md -->

# 02 – PLC‑Connect & Read BOOL/INT/REAL (pycomm3)

## 1. Opgave 1 – Læs en **BOOL** tag

> Forudsætninger i Studio 5000/RSLogix:
>
> * PLC'en har et BOOL-tag, fx `Start_PB`.
> * PLC'en er på netværket og tillader EtherNet/IP adgang.

```python
# save as opg1_read_bool.py
# pip install pycomm3

from pycomm3 import LogixDriver

# ── UDFYLD DISSE ─────────────────────────────
PLC_IP   = "192.168.0.10"   # PLC'ens IP
TAG_NAME = "Start_PB"      # Navnet på BOOL-tagget
# ─────────────────────────────────────────────

with LogixDriver(f'{PLC_IP}') as plc:
  result = plc.read(TAG_NAME)
  print(f"BOOL tag '{TAG_NAME}' = {result.value}")
```

Kør i terminalen:

```bash
python opg1_read_bool.py
```

**Hvorfor er det så kort?**
Du læser direkte tag-navnet, og får værdien som Python bool. Ingen byte/bit-adressering.

**Fejlfinding på 30 sekunder**

* Tjek IP og tag-navn.
* Tjek at PLC'en er online og tillader adgang.
* Tjek at tagget er af typen BOOL.

Når denne virker, er mønsteret identisk for INT/REAL i de næste opgaver—du læser bare et andet tag og får værdien direkte.

---

## 2. Opgave 2 – Læs en **INT** tag

> **Forudsætning:** PLC'en har et INT-tag, fx `Motor_Speed`.

```python

from pycomm3 import LogixDriver

PLC_IP   = "192.168.0.10"
TAG_NAME = "Motor_Speed"

with LogixDriver(f'{PLC_IP}') as plc:
  result = plc.read(TAG_NAME)
  print(f"INT tag '{TAG_NAME}' = {result.value}")
```

Kør:

```bash
python opg2_read_int.py
```

---

## 3. Opgave 3 – Læs en **REAL** tag

> **Forudsætning:** PLC'en har et REAL-tag, fx `Tank_Level`.

```python
# save as opg3_read_real.py
from pycomm3 import LogixDriver

PLC_IP   = "192.168.0.10"
TAG_NAME = "Tank_Level"

with LogixDriver(f'{PLC_IP}') as plc:
  result = plc.read(TAG_NAME)
  print(f"REAL tag '{TAG_NAME}' = {result.value}")
```

Kør:

```bash
python opg3_read_real.py
```

---

## 4. Opgave 4 – Læs en **String** tag

> **Forudsætning:** PLC'en har et String-tag, fx `Tank_Status`.

```python
# save as opg4_read_string.py
from pycomm3 import LogixDriver

PLC_IP   = "192.168.0.10"
TAG_NAME = "Tank_Status"

with LogixDriver(f'{PLC_IP}') as plc:
  result = plc.read(TAG_NAME)
  print(f"String tag '{TAG_NAME}' = {result.value}")

```

Kør:

```bash
python opg4_read_string.py
```

---

**Fejlfinding for alle opgaver**

* Tjek IP-adresse og tag-navn
* Tjek at PLC'en er online
* Tjek at tagget findes og har korrekt datatype
* Tjek netværksforbindelse og firewall
