# 03 - Løsningsforslag
## Løsning: Konvertering af Nøgleskema til Python
![alt text](../image-3.png)

```python
import snap7
from snap7.util import get_bool, set_bool
from snap7.type import Area
import sys
import time

# =================== PLC Konfiguration =================
PLC_IP = '192.168.0.1'  # Erstat med din PLC's IP-adresse
RACK = 0
SLOT = 1

AREA_IN = snap7.Area.PE
AREA_OUT = snap7.Area.PA

i00 = False # S1
i01 = False # S2
i02 = False # S3
i03 = False # S4
i04 = False # S5
i05 = False # S6
q00 = False # Q1

first_scan = True
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
        # =========== First scan ========================
        if first_scan:
            print("First scan - Initialisering")
            q00 = False # Sørg for at transportbåndet starter i slukket tilstand
            first_scan = False

        # =========== Læser Input =======================
        
        INPUT_RAW = client.read_area(AREA_IN, 1, 0, 1) # Læs 1 byte fra input (PE)
        OUTPUT_RAW = client.read_area(AREA_OUT, 1, 0, 1) # Læs 1 byte fra output (PA)
        i00 = get_bool(INPUT_RAW, 0, 0) # Læs bit 0 fra input
        i01 = get_bool(INPUT_RAW, 0, 1) # Læs bit 1 fra input
        i02 = get_bool(INPUT_RAW, 0, 2) # Læs bit 2 fra input
        i03 = get_bool(INPUT_RAW, 0, 3) # Læs bit 3 fra input
        i04 = get_bool(INPUT_RAW, 0, 4) # Læs bit 4 fra input
        i05 = get_bool(INPUT_RAW, 0, 5) # Læs bit 5 fra input
        q00 = get_bool(OUTPUT_RAW, 0, 0) # Læs bit 0 fra output

        # =========== Logik ============================
        q00 = ((i00 and i01) or (i02 and i03) or (i04 and i05))

        # =========== Skriv Output =====================
        set_bool(OUTPUT_RAW, 0, 0, q00) # Sæt bit 0 i output til True
        client.write_area(AREA_OUT, 1, 0, OUTPUT_RAW) # Skriv det muterede bytearray tilbage til output (PA)
        time.sleep(0.035) # Vent i 35 ms før næste cyklus
except KeyboardInterrupt:
    print("Program stoppet af bruger.")
    print(f"Q1 state: {q00}")
except Exception as e:
    print("Der opstod en fejl:", e)

finally:
    client.disconnect()
    print("Forbindelse lukket.")
    client.destroy()
```