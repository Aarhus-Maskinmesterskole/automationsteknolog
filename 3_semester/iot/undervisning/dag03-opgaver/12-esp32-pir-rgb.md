# 👁️🌈 Projekt 12 – Presence Indicator med Motion og RGB

## 📋 Projektbeskrivelse

Du skal bygge et "presence indicator" system der visuelt viser om der er aktivitet i rummet. Et PIR motion sensor detekterer bevægelse, og en RGB LED ændrer farve baseret på om der er motion eller ej. Systemet skal også rapportere motion-status via MQTT.

**Scenario:**  
Et smart hjem skal vise om der er personer i rummet. Grøn LED = motion detekteret (nogen er der). Blå LED = ingen motion (rummet er tomt). Remote overvågning via MQTT gør det muligt at se status fra andre enheder.

---

## 🎯 Kravspecifikation

### Hardware
- **PIR motion sensor** (GPIO 14) - Detekterer bevægelse
- **RGB LED / SK6812** (GPIO 26) - Visual feedback

### Funktionalitet

**Must-have (Minimum krav):**
1. Læs PIR sensor kontinuerligt (polling hver 100ms)
2. Når motion detekteres (PIR = HIGH) → Sæt RGB LED til GRØN (0, 255, 0)
3. Når ingen motion (PIR = LOW) → Sæt RGB LED til BLÅ (0, 0, 255)
4. Publisher motion status til MQTT: `stud/esp32/dit_navn/motion`
   - Send "1" ved motion
   - Send "0" ved ingen motion
5. Brug `retain=True` så nye subscribers ser seneste status
6. Kun publish når status ændrer sig (edge detection)
7. Print status-ændringer til console med emoji

**Nice-to-have (Bonus):**
- Puls-effekt: LED blinker grøn ved motion (breathing effect)
- Farve-gradient: Fade mellem blå og grøn
- Multi-LED: Forskellige LED'er i strippen viser forskellige farver
- Timeout: LED skifter til rød hvis motion i >1 time (mulig brand/alarm)

### MQTT Topics
```
Publisher:
  stud/esp32/dit_navn/motion → "1" eller "0" (retain=True)
```

---

## 💡 Hints og Vejledning

### Relevante opgaver at kigge i:

📁 **[02-esp32-pir-sensor.md](02-esp32-pir-sensor.md)**
- Hvordan man læser PIR sensor (GPIO 14)
- Edge detection (state change)
- `retain=True` parameter til MQTT publish
- Print motion events til console

📁 **[08-esp32-rgb-led.md](08-esp32-rgb-led.md)**
- Hvordan man styrer SK6812 RGB LED
- NeoPixel bibliotek setup
- `set_color(r, g, b)` funktion
- Farve-definitioner (R, G, B) tuples

### Tekniske hints:

**1. Kombiner PIR input og RGB output:**

```python
# Fra opgave 02: PIR sensor
pir = Pin(14, Pin.IN)
last_state = 0

# Fra opgave 08: RGB LED
from neopixel import NeoPixel
np = NeoPixel(Pin(26), 4)  # 4 LED'er

def set_color(r, g, b):
    for i in range(4):
        np[i] = (r, g, b)
    np.write()
```

**2. State-baseret farve mapping:**
```python
# Definer farver
COLOR_MOTION = (0, 255, 0)      # Grøn
COLOR_NO_MOTION = (0, 0, 255)   # Blå

# I main loop:
motion = pir.value()

if motion == 1:
    set_color(*COLOR_MOTION)  # Grøn LED
else:
    set_color(*COLOR_NO_MOTION)  # Blå LED
```

**3. Edge detection (kun trigger ved ændring):**
```python
if motion != last_state:
    # Status har ændret sig!
    if motion == 1:
        # 0 → 1: Motion startet
        set_color(0, 255, 0)  # Grøn
        client.publish(topic, b"1", retain=True)
    else:
        # 1 → 0: Motion stoppet
        set_color(0, 0, 255)  # Blå
        client.publish(topic, b"0", retain=True)
    
    last_state = motion  # Opdater state
```

**4. NeoPixel unpacking trick:**
```python
# * operator "unpacker" tuple
color = (255, 0, 0)
set_color(*color)  # Samme som: set_color(255, 0, 0)
```

---

## ✅ Test Kriterie

### Grundlæggende test:
1. ✓ Programmet starter, RGB LED er blå
2. ✓ Bevæg dig foran PIR → RGB skifter til grøn
3. ✓ Stå stille i 5+ sekunder → RGB skifter tilbage til blå
4. ✓ MQTT Explorer modtager "1" og "0" på motion topic
5. ✓ `retain=True` virker: Ny subscriber ser seneste status
6. ✓ LED skifter KUN ved edge (ikke konstant opdatering)

### Avanceret test:
- PIR sensor delay: 2-5 sekunder før reset (forventet adfærd)
- Multiple bevægelser: LED skal følge med konsekvent
- MQTT retained message: Disconnect og reconnect MQTT Explorer → Skal stadig se seneste status

### Test i Node-RED:
**Opret presence tracker:**
```
[MQTT In: motion] → [Switch: 0/1] → [Text: "Room Occupied" / "Room Empty"]
                  → [Function: timestamp] → [Chart: activity log]
```

---

## 🚀 Bonus Udfordringer

1. **Breathing effect:**  
   Lav pulserende grøn LED ved motion (fade in/out)
   ```python
   for brightness in range(50, 256, 10):
       set_color(0, brightness, 0)
       time.sleep_ms(50)
   ```

2. **Color gradient fade:**  
   Smooth transition mellem blå og grøn over 1 sekund

3. **Security mode:**  
   Tredje farve (rød) hvis motion detekteret om natten (kl. 22:00-06:00)

4. **Multi-zone LED:**  
   Brug 4 LED'er individuelt - vis "moving wave" effect ved motion

5. **Activity counter:**  
   Tæl antal motion events, send til separat topic

---

## 📌 Ekstra Noter

**Typiske fejl:**
- Glemme edge detection → LED opdateres konstant (ineffektivt)
- Forkert NeoPixel antal → IndexError
- Glemme `np.write()` → LED opdateres ikke
- Forkert RGB tuple → Forkerte farver (fx (255, 0, 0) = rød, ikke grøn)

**PIR karakteristika:**
- Delay: PIR output forbliver HIGH i 2-5 sek efter motion
- Range: 3-7 meter
- Angle: ~120° detection cone
- Warm-up: 30-60 sekunder efter power-on

**Use cases i den virkelige verden:**
- 🏠 Home occupancy indicator
- 🚨 Security presence alarm
- 💡 Auto-light trigger system
- 📊 Room utilization tracking

---

## 🧪 Test systemet

### Metode 1: MQTT Explorer
1. Åbn MQTT Explorer og forbind til `test.mosquitto.org`
2. Abonnér på `stud/esp32/dit_navn/motion`
3. Bevæg dig foran PIR sensor
4. Se motion status: `1` (motion) / `0` (ingen motion)

### Metode 2: Node-RED

**Opret visualisering:**
```
[MQTT In: motion] → [Switch node] → [Text: "Motion" eller "Ingen motion"]
                  → [LED indikator rød/grøn]
```

**Bonus - Counter:**
Tæl hvor mange gange motion er detekteret:
```
[MQTT In: motion] → [Function: count detections] → [Text: vis antal]
```

Function node:
```javascript
context.count = context.count || 0;
if (msg.payload === "1") {
    context.count++;
}
msg.payload = `Motion detekteret: ${context.count} gange`;
return msg;
```

---

## 📝 Forklaring

**Sådan virker motion-feedback:**

1. **PIR sensor**:
   - Passiv Infra-Rød sensor detekterer bevægelse
   - Output: HIGH (1) = motion, LOW (0) = no motion
   - Sensor har indbygget delay (typisk 2-5 sekunder)

2. **State tracking**:
   - `last_state` husker forrige PIR værdi
   - Kun reagerer når state ændres (undgår spam)
   - Edge detection: Trigger på 0→1 og 1→0

3. **Visual feedback**:
   - Motion = Grøn LED (alert/opmærksomhed)
   - No motion = Blå LED (idle/standby)
   - Omgående respons når motion detekteres

4. **RGB LED kontroling**:
   - `set_color()` opdaterer alle LED'er samtidig
   - `*COLOR_MOTION` unpacker (R, G, B) tuple
   - NeoPixel `write()` sender farver til LED strip

**PIR karakteristika:**
- 🕐 Delay: 2-5 sek før reset efter motion
- 📏 Range: 3-7 meter
- 👀 Vinkel: ~120° detektion

**Use cases:**
- 🏠 Presence indicator (hjemme/ude)
- 💡 Auto-lys system (motion = tænd)
- 🚨 Sikkerhedsalarm (rød LED ved motion)
- 📊 Aktivitets-monitorering

**Farve tilpasninger:**
- Rød LED = Warning/Alert mode
- Gul LED = Standby/Ready
- Hvid LED = Normal operation
- Off = Power save

**Kombiner med andre:**
- Tilføj buzzer for lyd-alarm
- Send notifikation via MQTT
- Log motion events med timestamp
