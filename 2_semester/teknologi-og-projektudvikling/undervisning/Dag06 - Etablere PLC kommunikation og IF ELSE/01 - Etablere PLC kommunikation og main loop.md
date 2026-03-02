# Dag 06 - Etablere PLC kommunikation og The Main Loop

Når vi skal skrive et program, som kontinuerligt og pålideligt interagerer med en PLC, får vi brug for at bygge et såkaldt "Main Loop" – altså et loop der kører uendeligt for at hente data og skrive data tilbage til PLC'en, så længe vores program er aktivt. 

I takt med at vores logik bliver mere kompliceret, har vi også brug for at strukturere vores kommunikation forsvarligt (f.eks. med Error Handling) og dele køreprocessen op i læs, logik og skriv.

## Etablering af PLC kommunikation 
Lige som i de forrige dage opsætter vi først vores forbindelse. Nedenfor opretter vi en klient og forbinder til vores PLC:

```python
import snap7
import time
from snap7.util import *

# Opretter variabler for PLC-forbindelsen
PLC_IP = '192.168.0.1'  # Erstat med din PLC's IP-adresse
RACK = 0 
SLOT = 1 

# Opret en Snap7 klient og forbind
client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)
```

## "Main Loop" Struktur
Et standard PLC-styringsprogram i Python kører i grove træk tre ting igen og igen:
1. **Læs (Read):** Hent alle relevante variabler fra PLC'en.
2. **Logik (Process):** Udfør betingelser som f.eks. `if / else` ud fra inputs.
3. **Skriv (Write):** Opdater og skriv nye værdier tilbage til PLC'en.

For at gøre dette, bruger vi et `while True:` loop. Det betyder "Kør dette loop for evigt", men vi pacer det lidt ved hjælp af `time.sleep()`, så vi ikke spammer PLC'en med anmodninger tusindvis af gange i sekundet.

Her er et simpelt eksempel på et Main Loop:

```python
import snap7
import time
from traceback import print_exc
from snap7.util import get_bool, set_bool

# =================== Opsætning ==================
PLC_IP = '192.168.0.1'
RACK = 0
SLOT = 1

client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

DB_NUMBER = 1 # Datablok nummer

IN_OFFSET = 0 # Indgang (f.eks. en knap - S1) på DB1.DBX0.0

OUT_OFFSET = 0 # Udgang (f.eks. en lampe - Q1) på DB1.DBX0.1

# =================== Uendeligt Main Loop ==================
try:
    print("Forbindelse oprettet. Starter main loop (Tryk Ctrl+C for at stoppe)...")
    while True:
        # ------- 1. LÆS (Read) -------
        # Læs variablens byte (1 byte for at få fat i boolean data)
        indgang_raw = client.db_read(DB_NUMBER, IN_OFFSET, 1)
        # Udtræk præcis den boolean der sidder på DB1.DBX0.0
        S1 = get_bool(indgang_raw, 0, 0)
        
        # ------- 2. LOGIK (IF/ELSE) -------
        H1 = False
        
        # Vi implementerer vores Simple betingelse
        if S1 == True:
            H1 = True
        else:
            H1 = False
            
        # ------- 3. SKRIV (Write) -------
        # For at undgå at overskrive andre bits i samme byte, læser vi byten først
        udgang_raw = client.db_read(DB_NUMBER, OUT_OFFSET, 1)
        
        # Ændre den specifikke bit (DB1.DBX0.1) baseret på vores logik
        set_bool(udgang_raw, 0, 1, H1)
        
        # Skriv det muterede bytearray tilbage til PLC'en
        client.db_write(DB_NUMBER, OUT_OFFSET, udgang_raw)
        
        # ------- 4. VENT (Sleep) -------
        # Vent i 0.1 sekunder før næste cyklus (100 ms) 
        time.sleep(0.035)

# Sikker håndtering hvis brugeren stopper programmet med f.eks. Ctrl+C (KeyboardInterrupt) i terminalen
except KeyboardInterrupt:
    print("\nProgrammet blev stoppet af brugeren.")
    
except Exception as e:
    print("Der opstod en fejl:")
    print_exc() # Printer fejlen til terminalen
    
finally:
    # Uanset hvad, sørg for at afbryde forbindelsen til PLC'en korrekt
    print("Lukker forbindelsen...")
    client.disconnect()
    client.destroy()
```

## Forklaring af "The Main Loop" Koncepter:

### Try / Except / Finally (Fejlhåndtering)
Vi pakker vores uendelige loop ind i en `try`-blok. Det gør vi for at vi kan fange fejl (exceptions), som f.eks. netværksnedbrud, eller i dette tilfælde at man trykker `Ctrl+C` for at slukke skriptet.
- **`try:`** – Selve vores loop kører herinde.
- **`except KeyboardInterrupt:`** – Fanger når du trykker Ctrl+C i terminalen for at afbryde scriptet for at lukke pænt ned i stedet for at crashe med en rød fejlbesked.
- **`finally:`** – Kører ALLTID til sidst – både hvis programmet får en fejl, hvis brugeren afbryder manuelt, eller hvis programmet skulle stoppe af andre grunde. Det er super vigtigt at tilføje `client.disconnect()` herinde, så jeres program altid frisætter forbindelsen til PLC'en, uanset hvordan programmet stopper. Hvis man ikke afbryder en snap7 forbindelse rigtigt overlever forbindelsen potentielt inde i PLC'en og resulterede i at der ikke kunne skabes flere forbindelser senere.

### Logikken (IF / ELSE)
Indefter the read og the write, ligger selve "hjernen" i jeres PLC bridge.
I eksemplet vil:
```python
        if S1 == True:
            H1 = True
        else:
            H1 = False
```
Sikre, at så længe knappen læses til *True*, udledes logikken at variablen for at tænde lampen laves til *True*, som i næste skriv bliver skrevet til udgangen. 

### Forsinkelse med `time.sleep()`
Uden forsinkelsen vil Python scriptet prøve at sende beskeder til PLC'en flere tusinde gange i sekundet. Dette kan nemt overbelaste både dit eget netværkskort og PLC'ens kommunikations-interface – derfor holder vi igen med at sove i f.eks. `0.1` eller t.o.m `1` sekund afhængigt af hvor reaktionsdygtigt scriptet skal være.