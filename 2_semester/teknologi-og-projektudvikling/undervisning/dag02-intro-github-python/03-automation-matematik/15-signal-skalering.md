# 📊 15 – Signal Skalering: 4-20mA og 0-10V

I automation bruger vi ofte analoge signaler som 4-20mA og 0-10V til at måle temperatur, tryk, flow osv. Python kan hjælpe med at konvertere disse signaler til engineering units (°C, bar, L/min).

---

## 🔧 Indhold

* Hvad er analoge signaler?
* 4-20mA standard
* Skalering formel
* mA → Engineering units
* Engineering units → mA
* 0-10V signaler

---

## 📘 1. Hvad er analoge signaler?

I automation sender sensorer ofte analoge signaler:

* **4-20mA** = Strømsignal (mest almindeligt)
  - 4mA = minimum værdi
  - 20mA = maksimum værdi
  - Robust over lange kabler

* **0-10V** = Spændingssignal
  - 0V = minimum værdi
  - 10V = maksimum værdi
  - Kortere kabler

**Eksempel:**
- Temperatursensor: 0-100°C sendes som 4-20mA
- 4mA = 0°C
- 12mA = 50°C
- 20mA = 100°C

---

## 📘 2. Skalering formel

**Grundformel for lineær skalering:**

```
EU = ((Signal - Signal_min) / (Signal_max - Signal_min)) × (EU_max - EU_min) + EU_min
```

Hvor:
- **EU** = Engineering Units (°C, bar, L/min osv.)
- **Signal** = Målt signal (mA eller V)
- **Signal_min/max** = Signal range (4-20mA eller 0-10V)
- **EU_min/max** = Engineering units range (0-100°C osv.)

---

## 📘 3. Konverter mA → °C

Temperatursensor: 0-100°C sendes som 4-20mA

```python
def ma_to_celsius(ma):
    """Konverter 4-20mA til 0-100°C"""
    signal_min = 4    # mA
    signal_max = 20   # mA
    temp_min = 0      # °C
    temp_max = 100    # °C
    
    # Skalering
    celsius = ((ma - signal_min) / (signal_max - signal_min)) * (temp_max - temp_min) + temp_min
    
    return round(celsius, 1)

# Test
print(f"4mA = {ma_to_celsius(4)}°C")     # 0°C
print(f"12mA = {ma_to_celsius(12)}°C")   # 50°C
print(f"20mA = {ma_to_celsius(20)}°C")   # 100°C
```

---

## 📘 4. Konverter °C → mA

Reverse engineering: Hvad skal sensoren sende for at vise 25°C?

```python
def celsius_to_ma(celsius):
    """Konverter 0-100°C til 4-20mA"""
    temp_min = 0
    temp_max = 100
    signal_min = 4
    signal_max = 20
    
    # Reverse skalering
    ma = ((celsius - temp_min) / (temp_max - temp_min)) * (signal_max - signal_min) + signal_min
    
    return round(ma, 2)

# Test
print(f"0°C = {celsius_to_ma(0)}mA")     # 4mA
print(f"25°C = {celsius_to_ma(25)}mA")   # 8mA
print(f"100°C = {celsius_to_ma(100)}mA") # 20mA
```

---

## 📘 5. Generisk skaleringsfunktion

```python
def scale_signal(signal, signal_min, signal_max, eu_min, eu_max):
    """
    Generisk funktion til at skalere signaler
    
    Args:
        signal: Målt signal (mA eller V)
        signal_min: Minimum signal værdi
        signal_max: Maximum signal værdi
        eu_min: Minimum engineering unit
        eu_max: Maximum engineering unit
    
    Returns:
        Skaleret værdi i engineering units
    """
    eu = ((signal - signal_min) / (signal_max - signal_min)) * (eu_max - eu_min) + eu_min
    return round(eu, 2)

# Eksempel: Tryksensor 0-10 bar sendes som 4-20mA
ma_signal = 16
bar = scale_signal(ma_signal, 4, 20, 0, 10)
print(f"{ma_signal}mA = {bar} bar")

# Eksempel: Level sensor 0-5m sendes som 0-10V
v_signal = 7.5
meter = scale_signal(v_signal, 0, 10, 0, 5)
print(f"{v_signal}V = {meter} m")
```

---

## 📘 6. Flow sensor eksempel

Flow sensor: 0-500 L/min sendes som 4-20mA

```python
def ma_to_flow(ma):
    """Konverter 4-20mA til 0-500 L/min"""
    return scale_signal(ma, 4, 20, 0, 500)

def flow_to_ma(flow):
    """Konverter 0-500 L/min til 4-20mA"""
    return scale_signal(flow, 0, 500, 4, 20)

# Test
print(f"4mA = {ma_to_flow(4)} L/min")
print(f"12mA = {ma_to_flow(12)} L/min")
print(f"20mA = {ma_to_flow(20)} L/min")

print(f"\n250 L/min = {flow_to_ma(250)}mA")
```

---

## 📘 7. 0-10V signaler

Samme princip, bare med 0-10V i stedet for 4-20mA:

```python
def volt_to_pressure(volt):
    """Konverter 0-10V til 0-16 bar"""
    return scale_signal(volt, 0, 10, 0, 16)

# Test
print(f"0V = {volt_to_pressure(0)} bar")
print(f"5V = {volt_to_pressure(5)} bar")
print(f"10V = {volt_to_pressure(10)} bar")
```

---

## 📘 8. Fejldetektering

4-20mA har en fordel: Vi kan detektere fejl!

```python
def check_signal_status(ma):
    """Tjek signal status"""
    if ma < 3.5:
        return "FEJL: Signal for lavt - kabelbrud?"
    elif ma > 20.5:
        return "FEJL: Signal for højt - kortslutning?"
    elif 3.5 <= ma < 4:
        return "ADVARSEL: Signal tæt på minimum"
    elif 20 < ma <= 20.5:
        return "ADVARSEL: Signal tæt på maksimum"
    else:
        return "OK"

# Test
print(check_signal_status(2))    # Fejl
print(check_signal_status(12))   # OK
print(check_signal_status(21))   # Fejl
```

---

## 🧪 Øvelser

1. Lav en funktion der konverterer 4-20mA til 0-200°C (højtemperatur sensor).
2. En tryksensor sender 0-25 bar som 4-20mA. Hvad er trykket ved 14.4mA?
3. Lav reverse: Hvad skal signalet være for at vise 15 bar?

---

## For de øvede

4. Lav en funktion der konverterer mellem forskellige enheder (bar → PSI, L/min → m³/h).
5. Implementér en alarm-funktion: Hvis temperatur > 80°C, return advarsel.
6. Lav et program der simulerer 5 sensorer og viser alle værdier i en tabel.
7. Læs sensor-konfiguration fra en dictionary og skalér automatisk.

---

## ✅ Tjekliste

* [ ] Jeg forstår hvad 4-20mA og 0-10V signaler er
* [ ] Jeg kan bruge skalering formlen
* [ ] Jeg kan konvertere mA til engineering units
* [ ] Jeg kan lave reverse engineering (EU → mA)
* [ ] Jeg kan detektere signal-fejl
* [ ] Jeg kan lave generiske skaleringsfunktioner

---

## 💡 Tips

* **Hvorfor 4-20mA og ikke 0-20mA?**
  - 0mA kan betyde "ingen signal" eller "kabelbrud"
  - 4mA som minimum gør det muligt at detektere fejl
  
* **Dead band:**
  - 3.5-4mA = under-range (sensor under minimum)
  - 20-20.5mA = over-range (sensor over maksimum)

* **Præcision:**
  - Brug `round()` til at undgå mange decimaler
  - Sensorer har typisk 0.1-1% nøjagtighed

---

## 📚 Nyttige formler

**Lineær skalering:**
```
y = (x - x_min) / (x_max - x_min) × (y_max - y_min) + y_min
```

**Procent:**
```
Procent = (Signal - Signal_min) / (Signal_max - Signal_min) × 100
```

**Engineering units til procent:**
```
Procent = (EU - EU_min) / (EU_max - EU_min) × 100
```

---

## 🔧 Praktisk eksempel

```python
# Sensor konfiguration
sensors = {
    "temp_01": {"type": "temperature", "min": 0, "max": 100, "unit": "°C"},
    "press_01": {"type": "pressure", "min": 0, "max": 10, "unit": "bar"},
    "flow_01": {"type": "flow", "min": 0, "max": 500, "unit": "L/min"}
}

def read_sensor(sensor_id, ma_signal):
    """Læs og skalér sensor"""
    config = sensors[sensor_id]
    value = scale_signal(ma_signal, 4, 20, config["min"], config["max"])
    return f"{sensor_id}: {value} {config['unit']}"

# Simuler sensor aflæsninger
print(read_sensor("temp_01", 12))    # 50°C
print(read_sensor("press_01", 16))   # 7.5 bar
print(read_sensor("flow_01", 8))     # 125 L/min
```

---
