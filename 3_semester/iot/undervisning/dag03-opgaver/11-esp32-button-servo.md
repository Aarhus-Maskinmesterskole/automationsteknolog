# 🔘🚪 Projekt 11 – Manuel Dør-styring med Knap

## 📋 Projektbeskrivelse

Du skal bygge et manuelt dør-åbningssystem. En fysisk knap skal styre en servo motor (dør) med toggle-funktion: Første tryk åbner døren, andet tryk lukker den. Systemet skal også sende dør-status via MQTT så andre kan se om døren er åben eller lukket.

**Scenario:**  
En automatisk dør skal kunne åbnes/lukkes med en simpel knap. Hver gang der trykkes, skal døren skifte position. Status skal kunne overvåges remote via MQTT.

---

## 🎯 Kravspecifikation

### Hardware
- **Knap** (GPIO 16) - Manuel kontrol
- **Servo motor** (GPIO 13) - Dør mekanisme

### Funktionalitet

**Must-have (Minimum krav):**
1. Detekter knap-tryk (GPIO 16, active LOW med PULL_UP)
2. Første tryk → Servo til 90° (ÅBEN) + publish "OPEN"
3. Andet tryk → Servo til 0° (LUKKET) + publish "CLOSED"
4. Tredje tryk → Toggle tilbage til ÅBEN, osv.
5. Debouncing: Ignorer tryk som kommer hurtigere end 200ms
6. Vent på knap slip før næste trigger accepteres
7. Publisher status til MQTT: `stud/esp32/dit_navn/door_status`
8. Print dør-status til console

**Nice-to-have (Bonus):**
- Tæl antal åbninger og send til separat topic
- Lang-tryk (>2 sek) = Luk trins-vis (slow motion)
- LED indikator: Grøn = åben, Rød = lukket
- Triple-click = Midter-position (45°)

### MQTT Topics
```
Publisher:
  stud/esp32/dit_navn/door_status → "OPEN" eller "CLOSED"
```

---

## 💡 Hints og Vejledning

### Relevante opgaver at kigge i:

📁 **[04-esp32-button.md](04-esp32-button.md)**
- Hvordan man læser knap med debouncing
- `Pin.IN` med `PULL_UP` konfiguration
- `time.ticks_ms()` til debounce logik
- Active LOW detection (`button.value() == 0`)

📁 **[06-esp32-door-servo.md](06-esp32-door-servo.md)**
- Hvordan man styrer servo motor
- PWM setup og `angle_to_duty()` funktion
- Servo positioner: 0° (lukket), 90° (åben)

### Tekniske hints:

**1. Kombiner button input og servo output:**

```python
# Fra opgave 04: Button setup
button = Pin(16, Pin.IN, Pin.PULL_UP)
last_press_time = 0
DEBOUNCE_MS = 200

# Fra opgave 06: Servo setup
servo = PWM(Pin(13), freq=50)

def angle_to_duty(angle):
    min_duty = 26
    max_duty = 123
    duty = int(min_duty + (angle / 180.0) * (max_duty - min_duty))
    return duty
```

**2. Toggle logik (boolean state tracking):**
```python
door_open = False  # Start tilstand

# Når knap trykkes:
if door_open:
    # Dør er åben → Luk den
    servo_move(0)  # 0°
    door_open = False
    client.publish(topic, b"CLOSED")
else:
    # Dør er lukket → Åbn den
    servo_move(90)  # 90°
    door_open = True
    client.publish(topic, b"OPEN")
```

**3. Debouncing (fra opgave 04):**
```python
if button.value() == 0:  # Knap trykket
    current_time = time.ticks_ms()
    
    if time.ticks_diff(current_time, last_press_time) > DEBOUNCE_MS:
        # Gyldigt tryk → Udfør toggle
        last_press_time = current_time
```

**4. Wait for button release:**
```python
# Efter toggle, vent på slip
while button.value() == 0:
    time.sleep_ms(10)
```

---

## ✅ Test Kriterie

### Grundlæggende test:
1. ✓ Programmet starter, servo flytter til lukket position (0°)
2. ✓ Første knap-tryk → Servo åbner til 90°
3. ✓ Andet knap-tryk → Servo lukker til 0°
4. ✓ Tredje knap-tryk → Servo åbner igen (toggle virker)
5. ✓ MQTT Explorer modtager "OPEN" og "CLOSED" beskeder
6. ✓ Hurtigt dobbeltklik ignoreres (debouncing virker)

### Avanceret test:
- Hold knappen nede i 2 sekunder → Skal kun toggle én gang
- Tryk meget hurtigt 5 gange → Max 2-3 toggles registreres
- MQTT status matcher fysisk servo position

### Test i Node-RED:
**Opret flow:**
```
[MQTT In: door_status] → [Text node]
                       → [Function: count] → [Text: "Åbnet X gange"]
```

---

## 🚀 Bonus Udfordringer

1. **Åbnings-tæller:**  
   Tæl hvor mange gange døren åbnes, send til `stud/esp32/dit_navn/door_count`

2. **Tre positioner:**  
   1. tryk = 45° (halvt åben)  
   2. tryk = 90° (fuldt åben)  
   3. tryk = 0° (lukket)

3. **Lang-tryk detection:**  
   Hvis knap holdes >2 sekunder, flyt servoen langsomt (smooth motion)

4. **Dual servo:**  
   Tilføj vindue-servo (GPIO 5), brug 2 forskellige knapper

5. **RGB status:**  
   Kombiner med RGB LED - Rød=lukket, Grøn=åben

---

## 📌 Ekstra Noter

**Typiske fejl:**
- Glemme debouncing → Servo toggle hurtigt flere gange per tryk
- Glemme "wait for release" → Multiple triggers fra ét tryk
- Forkert `door_open` tracking → Toggle virker kun hver anden gang
- Active HIGH i stedet for LOW → Knap fungerer omvendt

**Use cases i den virkelige verden:**
- 🚪 Automatisk dør-åbner (handicapvenlig)
- 🪟 Smart vindue styring
- 🔒 Electronic lock system
- 🎛️ Generic on/off toggle mekanisme
