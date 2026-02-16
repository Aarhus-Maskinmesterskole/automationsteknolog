# Opgave 2: Node-RED + ESP32 (python) dht22 `node-red-contrib-modbustcp`

Formålet: du skal lære at læse data fra en ESP32 (Modbus TCP server) i Node-RED (client) — med den simple modbustcp-palette.

---

## 1) Forbered ESP32 med DHT22 og Modbus TCP

### Hardware
- ESP32 board
- DHT22 sensor
- Forbind DHT22 til ESP32:
  - VCC → 3.3V
  - GND → GND
  - DATA → GPIO 4

### Python kode til ESP32

Opret en fil `main.py` på ESP32:

```python
from machine import Pin
import dht, network, time
from umodbus.tcp import ModbusTCP  # fra brainelectronics/micropython-modbus

# --- WiFi forbindelse ---
SSID = "DIT_WIFI_NAVN"
PASS = "DIT_WIFI_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(SSID, PASS)
    t0 = time.ticks_ms()
    while not wlan.isconnected():
        if time.ticks_diff(time.ticks_ms(), t0) > 15000:
            raise RuntimeError("WiFi timeout")
        time.sleep_ms(200)

ip = wlan.ifconfig()[0]
print("WiFi OK:", ip)

# --- DHT22 på GPIO 4 ---
sensor = dht.DHT22(Pin(4))

# --- Modbus TCP server ---
UNIT_ID = 1
PORT = 502  # Standard Modbus TCP port

mb = ModbusTCP(unit_id=UNIT_ID)
mb.bind(local_ip=ip, local_port=PORT)  # VIGTIGT: bind til IP og port

# Definér Holding Registers
mb.setup_registers({
    "HREGS": {
        "TEMP_X10": {"register": 0, "len": 1, "val": 0},  # Register 0 = temp * 10
        "HUM_X10":  {"register": 1, "len": 1, "val": 0},  # Register 1 = fugt * 10
    }
})

print("Modbus TCP server klar på {}:{}".format(ip, PORT))

# Timing
MEASURE_MS = 2000  # Mål hver 2. sekund
next_ms = 0

while True:
    # Mål sensor ca. hver 2. sekund
    now = time.ticks_ms()
    if time.ticks_diff(now, next_ms) >= 0:
        try:
            sensor.measure()
            temp = int(sensor.temperature() * 10)
            hum = int(sensor.humidity() * 10)
            
            mb.set_hreg(0, temp)  # Register 0 = temperatur
            mb.set_hreg(1, hum)   # Register 1 = fugtighed
            
            print("Temp: {}°C, Fugt: {}%".format(temp/10, hum/10))
        except Exception as e:
            print("Sensor fejl:", e)
        
        next_ms = time.ticks_add(now, MEASURE_MS)
    
    # VIGTIGT: Håndter Modbus-forespørgsler fra Node-RED
    mb.process()
    time.sleep_ms(25)  # Kort sleep for at ikke blokere
```

**Vigtigt:**
- Installer `micropython-modbus` biblioteket først (brainelectronics/micropython-modbus)
- Notér ESP32's IP-adresse fra output
- `mb.bind()` binder socketen til IP og port
- `mb.setup_registers()` definerer registertabellen
- `mb.process()` håndterer forespørgsler fra Node-RED - skal kaldes løbende!

---

## 2) Installér Node-RED palette

I Node-RED, installér paletten:

1. Gå til **Menu → Manage palette**
2. Vælg **Install** tab
3. Søg efter: `node-red-contrib-modbustcp`
4. Klik **Install**

---

## 3) Opret Node-RED flow

### Flow struktur

```
[Inject] → [Modbus Read] → [Function] → [Debug]
```

### Trin-for-trin

1. **Inject node**
   - Sæt til at gentage hvert 5. sekund
   - Payload: timestamp

2. **Modbus Read node** (fra modbustcp-paletten)
   - **Server**: ESP32's IP-adresse
   - **Port**: 502
   - **Unit ID**: 1
   - **FC**: 3 (Read Holding Registers)
   - **Address**: 0
   - **Quantity**: 2 (læs 2 registre)

3. **Function node** - konvertér data:
   ```javascript
   // Data er i msg.payload som array
   let temp = msg.payload[0] / 10;
   let hum = msg.payload[1] / 10;
   
   msg.payload = {
       temperatur: temp + "°C",
       fugtighed: hum + "%"
   };
   
   return msg;
   ```

4. **Debug node**
   - Vis `msg.payload`

### Deploy og test

1. Klik **Deploy**
2. Se debug output i højre panel
3. Du skulle nu se temperatur og fugtighed hvert 5. sekund

---

## 4) Ekstra opgaver (valgfri)

### Opgave A: Dashboard
- Installér `node-red-dashboard`
- Tilføj gauge-noder til at vise temperatur og fugtighed visuelt

### Opgave B: Database
- Gem data i Firebase
- Brug til historisk data og grafer

### Opgave C: Alarm
- Lav en flow der sender besked hvis temperaturen er over 30°C

---

## Troubleshooting

**Problem: Kan ikke forbinde til ESP32**
- Tjek at ESP32 og Node-RED er på samme netværk
- Verificér IP-adresse med `wlan.ifconfig()`
- Tjek at Modbus server kører på ESP32

**Problem: Får ingen data**
- Tjek at DHT22 er forbundet korrekt
- Se ESP32's serial output for fejl
- Verificér Modbus register adresser (start fra 0)

**Problem: Forkerte værdier**
- Husk at dividere med 10 i Function node
- Tjek at sensor.measure() kører uden fejl

---

## Konklusion

Du har nu lært at:
- Opsætte ESP32 som Modbus TCP server
- Læse DHT22 sensor data
- Bruge Node-RED til at læse Modbus data
- Konvertere og vise data

