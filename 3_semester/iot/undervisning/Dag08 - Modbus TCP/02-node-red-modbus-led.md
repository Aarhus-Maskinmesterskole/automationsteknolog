# Opgave 3: Tænd/sluk LED på GPIO12 via Modbus TCP (Node-RED → ESP32)

Formålet: du skal lære at styre en LED på ESP32 fra Node-RED ved at skrive til en Modbus Coil.

---

## 1) Hent Modbus-biblioteket

Installer **brainelectronics/micropython-modbus** på ESP32:

**Metode: Thonny**
- Hent GitHub-repoet **brainelectronics/micropython-modbus**
- Kopiér mappen **`umodbus`** til **`/lib`** på ESP32

---

## 2) ESP32 serverkode

### Hardware
- ESP32 board
- LED på GPIO12 med modstand (eller brug den indbyggede LED)
- Forbindelse:
  - GPIO12 → LED → 220Ω modstand → GND

### Python kode

Gem som `main.py` på ESP32:

```python
# main.py — Modbus TCP server: Coil 12 -> LED på GPIO12
from machine import Pin
import time
from umodbus.tcp import ModbusTCP

UNIT_ID = 1
PORT = 502

# LED på GPIO12 (aktiv høj)
led = Pin(12, Pin.OUT, value=0)

# Callback: kør når en coil skrives (FC5/FC15)
def coil_set_cb(reg_type, address, val):
    if address == 12:
        led.value(1 if bool(val) else 0)
        print("LED: {}".format("ON" if val else "OFF"))

# Opret Modbus-server, bind til alle interfaces på port 502
mb = ModbusTCP(unit_id=UNIT_ID)
mb.bind(local_ip="0.0.0.0", local_port=PORT)

# Registrér coil 12 med callback
mb.setup_registers({
    "COILS": {
        "LED_YELLOW": {"register": 12, "len": 1, "val": 0, "on_set_cb": coil_set_cb}
    }
})

print("Modbus TCP kører på port {} (Unit ID {})".format(PORT, UNIT_ID))

# Hovedløkke: servér Modbus-forespørgsler
while True:
    mb.process()
    time.sleep_ms(10)
```

**Vigtigt:**
- ESP32 skal være forbundet til WiFi (brug tidligere WiFi-kode hvis nødvendigt)
- Notér ESP32's IP-adresse
- Hvis din LED er **aktiv lav**, byt logikken: `led.value(0 if bool(val) else 1)`

---

## 3) Installér Node-RED palette

Hvis ikke allerede installeret:

1. Gå til **Menu → Manage palette**
2. Vælg **Install** tab
3. Søg efter: `node-red-contrib-modbustcp`
4. Klik **Install**

---

## 4) Opret Node-RED flow

### Flow struktur

```
[Inject (ON)] → [Modbus Write] 
[Inject (OFF)] → [Modbus Write]
```

### Trin-for-trin

1. **Inject node (ON)**
   - Payload: **boolean** → `true`
   - Navn: "LED ON"

2. **Inject node (OFF)**
   - Payload: **boolean** → `false`
   - Navn: "LED OFF"

3. **Modbus Write node** (fra modbustcp-paletten)
   - **Server/IP**: ESP32's IP-adresse
   - **Port**: `502`
   - **Unit ID**: `1`
   - **Function**: **Coil (FC5)** - Write Single Coil
   - **Address**: `12`
   - **Quantity**: `1`

4. Forbind begge inject-noder til samme Modbus Write node

### Deploy og test

1. Klik **Deploy**
2. Klik på "LED ON" inject → LED'en tænder
3. Klik på "LED OFF" inject → LED'en slukker

---

## 5) Valgfri udvidelse: Læs LED status

For at verificere LED status kan du tilføje en read-funktion:

### Flow tilføjelse
```
[Inject (repeat 1s)] → [Modbus Read] → [Debug]
```

**Modbus Read node:**
- **Function**: **Read Coils (FC1)**
- **Address**: `12`
- **Quantity**: `1`
- Resten samme som Write node

Dette viser LED status i debug-outputtet hvert sekund.

---

## 6) Ekstra opgaver (valgfri)

### Opgave A: Dashboard
- Installér `node-red-dashboard`
- Tilføj en switch-widget til at tænde/slukke LED
- Tilføj en LED-indikator til at vise status

### Opgave B: Flere LED'er
- Tilslut LED'er på GPIO13 og GPIO14
- Opret coils på adresse 13 og 14 i ESP32-koden
- Lav individuelle kontrolknapper i Node-RED

### Opgave C: Blink funktion
- Lav en flow der blinker LED'en med 1 sekunders interval
- Brug en loop med delays mellem ON/OFF kommandoer

---

## Troubleshooting

**Problem: LED reagerer ikke**
- Tjek at ESP32 og Node-RED er på samme netværk
- Verificér IP-adresse er korrekt
- Tjek at port er 502 og Unit ID er 1
- Se ESP32's serial output for fejlmeddelelser

**Problem: Forkert GPIO pin**
- Bekræft at LED'en sidder på **GPIO12**
- Nogle boards har anderledes pin-layout

**Problem: LED tænder når den skal slukke**
- LED'en er sandsynligvis aktiv lav
- Ændr callback til: `led.value(0 if bool(val) else 1)`

**Problem: Modbus Write node ikke tilgængelig**
- Tjek at `node-red-contrib-modbustcp` er installeret korrekt
- Genstart Node-RED efter installation

---

## Konklusion

Du har nu lært at:
- Opsætte ESP32 som Modbus TCP server med Coils
- Bruge callbacks til at reagere på Modbus-skrivninger
- Styre hardware (LED) fra Node-RED via Modbus
- Læse status tilbage fra ESP32

Dette er grundlaget for at styre alle slags hardware fra Node-RED!
