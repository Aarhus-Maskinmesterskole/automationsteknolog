
# 01 – pycomm3‑Installation & Smoke‑test

> *Første opgave på Dag 04 – Python ⇄ Allen-Bradley PLC (EtherNet/IP)*

## 🎯 Formål

At installere **pycomm3** i et isoleret miljø på både Windows **og** Linux, bekræfte at modulet kan importeres, samt udføre en hurtig “smoke‑test”, der forbinder til en PLC og læser en tag for at verificere netværksadgang.

---

## 📂 Forudsætninger

| Krav              | Windows 11 / 10                   | Ubuntu 22.04 LTS         |
| ----------------- | --------------------------------- | ------------------------ |
| Python            | 3.7 – 3.12 (x64)                  | 3.7 – 3.12               |
| Compiler          | Ingen speciel compiler krævet      | Ingen speciel compiler   |
| pycomm3 lib       | pip installerer alt               | pip installerer alt      |
| Admin‑rettigheder | Kun til pip-installation           | Kun til `apt`            |

---

## 🔧 Trin for trin

### 1. Opret og aktiver virtuel env

```bash
# vælg mappen du arbejder i (fx dag04-python-plc-kommunikation/02-ethernet-ip/)
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

### 2. Installér pycomm3 (pip)

```bash
python -m pip install --upgrade pip
pip install pycomm3
```

Dette henter den nyeste version af pycomm3.

### 3. Verificér import

```bash
python - << "PY"
from pycomm3 import LogixDriver
import platform, sys
print("pycomm3 version:", LogixDriver.__module__)
print("OS:", platform.system(), platform.release())
print("Python:", sys.version)
PY
```

Output skal vise pycomm3‑modulet uden Tracebacks.

### 4. Smoke-test: Læs et tag fra PLC

```python
from pycomm3 import LogixDriver

# Erstat med IP-adressen på din PLC
PLC_IP = "192.168.0.10"
TAG_NAME = "MyTag"  # erstat med et tag som findes i din controller

with LogixDriver(PLC_IP) as plc:
	result = plc.read(TAG_NAME)
	print(result.value)
```

Hvis du får en værdi uden fejl, er forbindelsen OK!