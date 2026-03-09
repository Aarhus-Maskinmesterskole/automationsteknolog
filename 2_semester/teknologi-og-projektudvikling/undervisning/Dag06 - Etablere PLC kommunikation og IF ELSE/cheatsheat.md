# Cheatsheat
## Hurtig opsætning af PLC kommunikation med snap7 i Python
```python
import snap7
from snap7.util import get_bool, set_bool
from snap7.type import Area
import sys

# =================== PLC Konfiguration =================
PLC_IP = '192.168.0.1'  # Erstat med din PLC's IP-adresse
RACK = 0
SLOT = 1

AREA_IN = snap7.Area.PE
AREA_OUT = snap7.Area.PA

# =================== Opret forbindelse =================

try:
    client = snap7.client.Client()
    client.connect(PLC_IP, RACK, SLOT) # husk tcp_port hvis i bruger server.py
    print("Forbindelse oprettet.")
except Exception as e:
    print("Fejl ved oprettelse af forbindelse:", e)
    sys.exit(1) # Afslut programmet hvis forbindelsen ikke kunne oprettes

try:
    while True:
        # =========== Læser Input =======================

        INPUT_RAW = client.read_area(AREA_IN, 1, 0, 1) # Læs 1 byte fra input (PE)
        OUTPUT_RAW = client.read_area(AREA_OUT, 1, 0, 1) # Læs 1 byte fra output (PA)
        # i00 = get_bool(INPUT_RAW, 0, 0) # Læs bit 0 fra input
        # q00 = get_bool(OUTPUT_RAW, 0, 0) # Læs bit 0 fra output

        # =========== Logik ============================





        # =========== Skriv Output =====================
        # set_bool(OUTPUT_RAW, 0, 0, True) # Sæt bit 0 i output til True
        # client.write_area(AREA_OUT, 1, 0, OUTPUT_RAW) # Skriv det muterede bytearray tilbage til output (PA)
        time.sleep(0.035) # Vent i 35 ms før næste cyklus
except KeyboardInterrupt:
    print("Program stoppet af bruger.")
except Exception as e:
    print("Der opstod en fejl:", e)

finally:
    client.disconnect()
    print("Forbindelse lukket.")
    client.destroy()
```

## First Scan Bit

```python
first_scan = True

while True:
    if first_scan:
        # Initialiseringskode her
        first_scan = False
    # ...resten af programmet...
```

## One shot-funktion:
```python
def one_shot(current_state, previous_state):
    return current_state and not previous_state
```

## Falling edge-funktion:
```python
def falling_edge(current_state, previous_state):
    return not current_state and previous_state
```
