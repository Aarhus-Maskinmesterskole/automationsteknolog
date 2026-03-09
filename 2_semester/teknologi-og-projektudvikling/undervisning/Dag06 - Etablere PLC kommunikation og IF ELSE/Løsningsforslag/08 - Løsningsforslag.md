# 07 - Løsningsforslag

![image-6.png](image-6.png)


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

AREA_IN = Area.PE
AREA_OUT = Area.PA

i00 = False # S1 - Start knap
i01 = False # S2 - Fotocelle
q00 = False # Q1
step = 0 # Variabel til at holde styr på vores logiske trin i Match/Case strukturen

previous_i00 = False # Variabel til at holde styr på tidligere tilstand af S1
previous_i01 = False # Variabel til at holde styr på tidligere tilstand af S2

first_scan = True
# =================== One shot funktion =================

def one_shot(input_signal, previous_state):
    return input_signal and not previous_state

# =================== Falling edge detektion ============
def falling_edge(input_signal, previous_state):
    return not input_signal and previous_state

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
        q00 = get_bool(OUTPUT_RAW, 0, 0) # Læs bit 0 fra output

        # =========== Logik ============================
        match step:
            case 0: # Vent på start knap
                q00 = False # Transportbåndet er stoppet
                if one_shot(i00, previous_i00) and not i01: # Hvis start knappen trykkes og fotocellen ikke er aktiv
                    step = 1 # Gå til næste trin
            case 1: # Transportbåndet kører, vent på fotocelle
                q00 = True # Transportbåndet kører
                if one_shot(i01, previous_i01): # Hvis fotocellen registrerer en kasse
                    step = 2 # Gå til næste trin
            case 2: # Fotocelle har registreret kasse, stop bånd og reset logik
                q00 = False # Stop transportbåndet
                if falling_edge(i01, previous_i01): # Vent på at kassen fjerner sig fra fotocellen
                    step = 0 # Gå tilbage til start

        # =========== Skriv Output =====================
        set_bool(OUTPUT_RAW, 0, 0, q00) # Sæt bit 0 i output til True
        client.write_area(AREA_OUT, 1, 0, OUTPUT_RAW) # Skriv det muterede bytearray tilbage til output (PA)

        previous_i00 = i00 # Opdater tidligere tilstand for S1
        previous_i01 = i01 # Opdater tidligere tilstand for S2

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