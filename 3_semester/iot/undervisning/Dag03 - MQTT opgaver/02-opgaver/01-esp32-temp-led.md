# 🌡️💡 Projekt 01 – Temperatur Overvågning med LED Alarm

## 📋 Projektbeskrivelse

Du skal bygge et automatisk temperatur-alarm system. Systemet skal kontinuerligt måle temperaturen og tænde en gul LED hvis temperaturen overstiger en bestemt grænse (threshold). Både temperatur og alarm-status skal sendes via MQTT så systemet kan overvåges remote.

**Scenario:**  
Et værelse skal overvåges for overophedning. Hvis temperaturen kommer over 25°C, skal en LED lyse som advarsel. Data skal også kunne ses i Node-RED eller MQTT Explorer.

---

## 🎯 Kravspecifikation

### Hardware
- **DHT11 sensor** (GPIO 4) - Måler temperatur
- **Gul LED** (GPIO 12) - Visual alarm indikator

### Funktionalitet

**Must-have (Minimum krav):**
1. Læs temperatur fra DHT11 sensor hvert 2. sekund
2. Sammenlign temperatur med threshold (25°C)
3. Tænd LED automatisk hvis `temp > 25°C`
4. Sluk LED automatisk hvis `temp ≤ 25°C`
5. Publisher temperatur til MQTT topic: `stud/esp32/dit_navn/temp`
6. Publisher LED status til MQTT topic: `stud/esp32/dit_navn/temp_alarm` ("ON" eller "OFF")
7. Print status til console med emoji indikator (🔴 eller 🟢)

**Nice-to-have (Bonus):**
- Kun publish LED status når den ændrer sig (ikke ved hver måling)
- Mulighed for at ændre threshold via MQTT
- Tilføj hysteresis (fx tænd ved 25°C, sluk først ved 23°C)
- Send email/notifikation via Node-RED når alarm aktiveres

### MQTT Topics
```
Publisher:
  stud/esp32/dit_navn/temp → "23" (temperatur i °C)
  stud/esp32/dit_navn/temp_alarm → "ON" eller "OFF"
```

---

## 💡 Hints og Vejledning

### Relevante opgaver at kigge i:

📁 **[01-esp32-dht11.md](01-esp32-dht11.md)**
- Hvordan man læser DHT11 sensor
- Publisher temperatur via MQTT
- Kode til `sensor.measure()` og `sensor.temperature()`

📁 **[07-esp32-yellow-led.md](07-esp32-yellow-led.md)**
- Hvordan man styrer LED (GPIO 12)
- `Pin.OUT` og `led.value(0/1)`
- LED on/off funktioner

### Tekniske hints:

**1. Kombiner sensor input og LED output:**
```python
# Fra opgave 01: Sensor læsning
sensor = dht.DHT11(Pin(4))
sensor.measure()
temp = sensor.temperature()

# Fra opgave 07: LED kontrol
led = Pin(12, Pin.OUT)
led.value(1)  # Tænd
led.value(0)  # Sluk
```

**2. Threshold logik:**
```python
THRESHOLD = 25.0

if temp > THRESHOLD:
    # Temperatur for høj → Tænd LED
else:
    # Temperatur OK → Sluk LED
```

**3. Undgå flicker (status tracking):**
```python
# Husk tidligere LED status
led_status = False  # Initialiser

# Kun ændre hvis status skal skifte
if temp > THRESHOLD and not led_status:
    # Tænd LED + publish
    led_status = True
elif temp <= THRESHOLD and led_status:
    # Sluk LED + publish
    led_status = False
```

**4. Publisher til 2 forskellige topics:**
```python
client.publish(b"stud/esp32/dit_navn/temp", str(temp).encode())
client.publish(b"stud/esp32/dit_navn/temp_alarm", b"ON")
```

---

## ✅ Test Kriterie

### Grundlæggende test:
1. ✓ Programmet starter uden fejl
2. ✓ Temperatur vises i console hvert 2. sekund
3. ✓ LED er slukket når temp < 25°C
4. ✓ LED tænder når temp > 25°C
5. ✓ Temperatur kan ses i MQTT Explorer
6. ✓ LED status kan ses i MQTT Explorer

### Avanceret test:
- Varm DHT11 sensor (fx med din hånd) → LED skal tænde
- Fjern varme → LED skal slukke efter temperatur falder
- LED skal IKKE flicker (tænde/slukke hurtigt)
- MQTT Explorer viser korrekt real-time data

### Test i Node-RED:
**Opret flow:**
```
[MQTT In: temp] → [Gauge 0-50°C]
[MQTT In: temp_alarm] → [Text/LED node]
```

---

## 🚀 Bonus Udfordringer

1. **Justerbar threshold:**  
   Subscribe til topic `stud/esp32/dit_navn/set_threshold` og lad brugeren ændre grænsen via MQTT

2. **Hysteresis:**  
   Tænd ved 25°C, men sluk først ved 23°C (undgå flicker omkring grænsen)

3. **RGB LED i stedet:**  
   Grøn = OK, Gul = Advarsel (23-25°C), Rød = Alarm (>25°C)

4. **Historik:**  
   Gem max/min temperatur og send med i separat topic

5. **Display:**  
   Kombiner med LCD display (se opgave 09) til lokal visning

---

## 📌 Ekstra Noter

**Typiske fejl:**
- Glemme at checke `led_status` før ændring → LED flicker
- Forkert GPIO pin nummer
- Publisher kun temperatur, men glemmer alarm status
- Threshold check uden `> THRESHOLD and not led_status` logik

**Use cases i den virkelige verden:**
- 🌡️ Server room temperatur overvågning
- 🔥 Ovn/maskine overophedning alarm
- ❄️ Frost-advarsel (inverter logik til < 2°C)
- 🏠 Smart hjem klimastyring
