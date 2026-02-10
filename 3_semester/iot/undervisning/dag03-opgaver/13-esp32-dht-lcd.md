# 🌡️📟 Projekt 13 – Standalone Klima-station med Display

## 📋 Projektbeskrivelse

Du skal bygge en komplet vejrstation der både viser data lokalt på et LCD display OG sender data til cloud via MQTT. Stationen måler temperatur og fugtighed med DHT11 sensor, viser det på et 16x2 LCD, og publisher til MQTT topics for remote overvågning.

**Scenario:**  
En sensor-station skal kunne fungere standalone (uden computer), men data skal også kunne ses remote via MQTT. LCD displayet viser real-time målinger så data kan aflæses lokalt, mens Node-RED eller andre enheder kan subscribe til MQTT topics.

---

## 🎯 Kravspecifikation

### Hardware
- **DHT11 sensor** (GPIO 4) - Måler temp/fugtighed
- **LCD 1602 Display** (I2C: SDA=GPIO 21, SCL=GPIO 22) - Lokal visning

### Funktionalitet

**Must-have (Minimum krav):**
1. Læs DHT11 sensor hvert 2. sekund
2. Vis data på LCD:
   - Linje 1: `Temp: XXC` (max 16 karakterer)
   - Linje 2: `Hum:  XX%` (noter double-space for alignment)
3. Publisher temperatur til: `stud/esp32/dit_navn/temp`
4. Publisher fugtighed til: `stud/esp32/dit_navn/humidity`
5. Print målinger til console
6. Vis fejlbesked på LCD hvis sensor fejler
7. Velkomstbesked ved opstart: "ESP32 Sensor" / "Starter..."

**Nice-to-have (Bonus):**
- Vis WiFi status på LCD (IP adresse på boot)
- Toggle mellem Celsius og Fahrenheit
- Vis min/max værdier for dagen
- Scrollende tekst hvis data er for lang
- Backlight control via MQTT

### MQTT Topics
```
Publisher:
  stud/esp32/dit_navn/temp → "23" (grader Celsius)
  stud/esp32/dit_navn/humidity → "55" (procent)
```

---

## 💡 Hints og Vejledning

### Relevante opgaver at kigge i:

📁 **[01-esp32-dht11.md](01-esp32-dht11.md)**
- Hvordan man læser DHT11 sensor (GPIO 4)
- `sensor.measure()`, `sensor.temperature()`, `sensor.humidity()`
- Fejlhåndtering for sensor læsning
- MQTT publish af sensor data

📁 **[09-esp32-lcd-display.md](09-esp32-lcd-display.md)**
- Komplet LCD1602 I2C driver class
- `lcd.display(line1, line2)` funktion
- I2C setup (SDA=21, SCL=22)
- I2C scanning og adresse detection (0x27 eller 0x3F)

### Tekniske hints:

**1. Kombiner DHT11 og LCD:**

```python
# Fra opgave 01: DHT11 sensor
import dht
from machine import Pin
sensor = dht.DHT11(Pin(4))

# Fra opgave 09: LCD display
from machine import I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
lcd = LCD1602(i2c, 0x27)  # Brug LCD class fra opgave 09

# Kombiner:
sensor.measure()
temp = sensor.temperature()
hum = sensor.humidity()

lcd.display(f"Temp: {temp}C", f"Hum:  {hum}%")
```

**2. Formatering til LCD (16 karakterer max pr. linje):**
```python
temp = 23
hum = 55

# String formatting:
line1 = f"Temp: {temp}C"       # "Temp: 23C" (9 chars)
line2 = f"Hum:  {hum}%"        # "Hum:  55%" (10 chars)

# Auto-truncate hvis for lang:
line1 = line1[:16]
line2 = line2[:16]

lcd.display(line1, line2)
```

**3. Dual output (LCD + MQTT):**
```python
# Samme data til begge outputs:
client.publish(b"temp", str(temp).encode())
client.publish(b"humidity", str(hum).encode())
lcd.display(f"Temp: {temp}C", f"Hum:  {hum}%")
```

**4. Fejlhåndtering med LCD feedback:**
```python
try:
    sensor.measure()
    temp = sensor.temperature()
    # ... normal kode
except Exception as e:
    print(f'Sensor fejl: {e}')
    lcd.display("Fejl!", "Tjek sensor")
```

**5. I2C address scanning (hvis usikker):**

```python
# Fra opgave 09: Scan I2C bus
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
devices = i2c.scan()
if devices:
    print(f'LCD adresse: {hex(devices[0])}')
else:
    print('Ingen I2C enheder fundet!')
```

**6. Kopier LCD1602 class:**
```python
# Du skal kopiere hele LCD1602 class fra opgave 09
# Eller gem den som separat fil og import:
# from lcd1602 import LCD1602
```

---

## ✅ Test Kriterie

### Grundlæggende test:
1. ✓ Programmet starter, LCD viser "ESP32 Sensor" / "Starter..."
2. ✓ Efter 2 sekunder: LCD viser temp og fugtighed
3. ✓ LCD opdateres hvert 2. sekund med nye værdier
4. ✓ MQTT Explorer modtager temperatur på korrekt topic
5. ✓ MQTT Explorer modtager fugtighed på korrekt topic
6. ✓ Console printer emoji og værdier
7. ✓ Hvis sensor fejler: LCD viser "Fejl!" / "Tjek sensor"

### Avanceret test:
- Varm DHT11 sensor → LCD og MQTT viser stigning
- Disconnect WiFi → Program håndterer reconnect
- Forkert I2C adresse → Program detekterer fejl ved opstart
- Data i MQTT matcher data på LCD (samme værdier)

### Test i Node-RED:
**Opret dashboard:**
```
[MQTT In: temp] → [Gauge 0-50°C] → [Chart: historik]
[MQTT In: humidity] → [Gauge 0-100%] → [Chart: historik]
```

**Kombiner data:**
```
[Function: combine] → [Text: "23°C, 55%"]
```
Function node:
```javascript
var temp = flow.get('temp') || 0;
var hum = flow.get('hum') || 0;
if (msg.topic.includes('temp')) {
    flow.set('temp', msg.payload);
} else {
    flow.set('hum', msg.payload);
}
msg.payload = `${flow.get('temp')}°C, ${flow.get('hum')}%`;
return msg;
```

---

## 🚀 Bonus Udfordringer

1. **WiFi status på LCD:**  
   Vis IP adresse på boot:
   ```python
   ip = wlan.ifconfig()[0]
   lcd.display("WiFi OK", ip)
   time.sleep(2)
   ```

2. **Min/Max tracking:**  
   Gem dagens min/max temp, vis ved knaptryk eller på linje 2

3. **Celsius/Fahrenheit toggle:**  
   Subscribe til topic `set_unit` → Switch mellem C og F

4. **Backlight control:**  
   Subscribe til `lcd_backlight` → ON/OFF via MQTT

5. **Multi-page display:**  
   Roter mellem: Temp/Hum → Min/Max → WiFi info (hver 5. sek)

6. **SD card logging:**  
   Gem målinger til SD kort hver time (timestamp + data)

---

## 📌 Ekstra Noter

**Typiske fejl:**
- **LCD ikke fundet:** Tjek SDA/SCL forbindelser, power (5V/3.3V), I2C adresse
- **DHT11 fejl:** Sensor skal have 1-2 sek mellem målinger, tjek VCC/GND/Data pin
- **Forkert formatering:** Husk max 16 karakterer per linje
- **MQTT publish fejler:** Tjek WiFi forbindelse, broker tilgængelighed
- **LCD flicker:** Clear() kun når nødvendigt, ikke i loop

**LCD1602 I2C adresse:**
- Almindelig: `0x27` (standard)
- Alternativ: `0x3F` (nogle moduler)
- Find via: `i2c.scan()` i REPL

**Standalone mode (uden MQTT):**
Systemet kan køre offline hvis du:
```python
# Kommentér MQTT kode ud:
# client = MQTTClient(...)
# client.connect()
# client.publish(...)

# Kun LCD virker
lcd.display(f"Temp: {temp}C", f"Hum:  {hum}%")
```

**Use cases i den virkelige verden:**
- 🏠 Home weather station
- 🌡️ Room climate monitor
- 🔬 Lab environmental tracking
- 🌿 Greenhouse monitoring
- 💾 Data logger med lokal display

---

## 🧪 Test systemet

### Metode 1: MQTT Explorer
1. Åbn MQTT Explorer og forbind til `test.mosquitto.org`
2. Abonnér på:
   - `stud/esp32/dit_navn/temp` - Temperatur
   - `stud/esp32/dit_navn/humidity` - Fugtighed
3. Se data opdateres hvert 2. sekund

### Metode 2: Node-RED

**Opret dashboard med gauges:**
```
[MQTT In: temp] → [Gauge: 0-50°C]
[MQTT In: humidity] → [Gauge: 0-100%]
[Both] → [Chart: historisk graf]
```

**Bonus - Kombiner data:**
```javascript
// Function node: Kombiner temp + humidity
var temp = flow.get('temp') || 0;
var hum = flow.get('hum') || 0;

if (msg.topic.includes('temp')) {
    flow.set('temp', msg.payload);
} else {
    flow.set('hum', msg.payload);
}

msg.payload = `${temp}°C, ${hum}%`;
return msg;
```

---

## 📝 Forklaring

**Sådan virker sensor-display system:**

1. **Lokal display**:
   - LCD viser data direkte fra ESP32
   - Ingen internet påkrævet for at se data
   - Real-time opdatering (2 sekunder)

2. **Remote overvågning**:
   - MQTT publisher data til cloud
   - Andre enheder kan subscribe
   - Data logging og visualisering mulig

3. **Dual output**:
   - `lcd.display()` - Lokal visning
   - `client.publish()` - Remote data
   - Begge opdateres samtidig

4. **LCD formatering**:
   - Linje 1: `"Temp: 23C"` (max 16 karakterer)
   - Linje 2: `"Hum:  55%"` (to spaces for alignment)
   - Celsius symbol (°) kan erstatte med "C"

**I2C fordele:**
- Kun 2 wires (SDA/SCL) + power
- Multiple enheder på samme bus
- Standard protocol, nem at bruge

**Standalone mode:**
ESP32 kan køre uden MQTT hvis WiFi ikke tilgængeligt:
```python
# Kommentér MQTT kode ud for offline brug
# client.publish(...)
# Kun LCD display virker
```

**Use cases:**
- 🏠 Værelses-klimastation
- 🌡️ Temperatur-overvågning med lokal display
- 📊 Data logger med real-time visning
- 🔬 Lab sensor station

**Udvidelser:**
- Tilføj alarm hvis temp > threshold
- Vis dato/tid på LCD
- Tilføj flere sensorer
- Battery backup for standalone brug
