# Dag04 - Etablere PLC kommunikation
## Etablering af PLC kommunikation
For at etablere kommunikation mellem en PLC og en computer (Python), skal vi først sikre os, at vi har de nødvendige biblioteker installeret. Vi vil bruge `Snap7` biblioteket til at kommunikere med Siemens PLC'er.

### Installation af Snap7
For at installere Snap7, kan du bruge pip:

```bash
python -m pip install python-snap7
```

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

## Forklaring af koden

### Importer Snap7 biblioteket
```python
import snap7
from snap7.util import *
```

- `import snap7`: Dette importerer hovedbiblioteket, som indeholder funktioner til at oprette forbindelse og kommunikere med PLC'en.
- `from snap7.util import *`: Dette importerer hjælpefunktioner, som gør det lettere at håndtere data, der læses fra PLC'en.

### Opret en Snap7 klient
```python
client = snap7.client.Client()
```
- `client = snap7.client.Client()`: Dette opretter en instans af Snap7 klienten, som vi vil bruge til at kommunikere med PLC'en. (OBS! til eksamen vil jeg ikke spørge til klasser og objekter, så du behøver ikke at forstå dette i dybden endnu)

### Forbind til PLC'en
```python
client.connect(PLC_IP, RACK, SLOT)
```
- `client.connect(PLC_IP, RACK, SLOT)`: Dette etablerer en forbindelse til PLC'en ved hjælp af den angivne IP-adresse, rack-nummer og slot-nummer. Hvis forbindelsen er vellykket, kan vi nu læse og skrive data til PLC'en.

### Afslutning
Efter du har læst de ønskede variabler, er det vigtigt at lukke forbindelsen til PLC'en for at frigøre ressourcer:

```python
client.disconnect()
client.destroy()
```

- `client.disconnect()`: Dette lukker forbindelsen til PLC'en.
- `client.destroy()`: Dette frigør klientressourcerne.