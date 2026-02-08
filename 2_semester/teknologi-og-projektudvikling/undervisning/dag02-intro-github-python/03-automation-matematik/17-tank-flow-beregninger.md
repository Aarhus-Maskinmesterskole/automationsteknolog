# 💧 17 – Tank og Flow Beregninger: Volumen, Fyldning og Flow

I automation arbejder vi ofte med tanke, beholdere og væskeflow. Python kan hjælpe med at beregne volumen, fyldningstid, flow rates og niveau-kontrol.

---

## 🔧 Indhold

* Volumen beregninger (cylinder, rektangel, sfære)
* Level % → Liter
* Flow rate konverteringer
* Fyldnings- og tømningstid
* Overflow detection
* Flow totalizer

---

## 📘 1. Cylindrisk tank volumen

**Formel:**
```
V = π × r² × h
```

Hvor:
- V = Volumen (m³ eller L)
- r = Radius (m)
- h = Højde (m)

```python
import math

def cylinder_volume(radius_m, height_m):
    """
    Beregn volumen af cylindrisk tank
    
    Args:
        radius_m: Radius i meter
        height_m: Højde i meter
    
    Returns:
        Volumen i liter
    """
    volume_m3 = math.pi * radius_m**2 * height_m
    volume_liters = volume_m3 * 1000  # 1 m³ = 1000 L
    return round(volume_liters, 1)

# Eksempel: Tank med diameter 2m, højde 3m
radius = 1.0  # meter (diameter 2m)
height = 3.0  # meter

volume = cylinder_volume(radius, height)
print(f"Tank volumen: {volume} L ({volume/1000} m³)")
```

---

## 📘 2. Rektangulær tank volumen

**Formel:**
```
V = L × B × H
```

```python
def rectangular_volume(length_m, width_m, height_m):
    """
    Beregn volumen af rektangulær tank
    
    Args:
        length_m: Længde i meter
        width_m: Bredde i meter
        height_m: Højde i meter
    
    Returns:
        Volumen i liter
    """
    volume_m3 = length_m * width_m * height_m
    volume_liters = volume_m3 * 1000
    return round(volume_liters, 1)

# Eksempel: 2m × 1.5m × 2m tank
volume = rectangular_volume(2, 1.5, 2)
print(f"Tank volumen: {volume} L")  # 6000 L
```

---

## 📘 3. Level % → Volumen

**Konverter niveau procent til faktisk volumen:**

```python
def level_to_volume(level_percent, total_capacity_liters):
    """
    Konverter niveau % til liter
    
    Args:
        level_percent: Niveau i procent (0-100)
        total_capacity_liters: Total kapacitet i liter
    
    Returns:
        Faktisk volumen i liter
    """
    volume = (level_percent / 100) * total_capacity_liters
    return round(volume, 1)

# Eksempel: 5000L tank ved 67% fyldt
volume = level_to_volume(67, 5000)
print(f"67% af 5000L = {volume} L")  # 3350 L
```

---

## 📘 4. Volumen → Level %

**Reverse: Fra liter til procent:**

```python
def volume_to_level(volume_liters, total_capacity_liters):
    """
    Konverter volumen til niveau %
    
    Args:
        volume_liters: Faktisk volumen i liter
        total_capacity_liters: Total kapacitet i liter
    
    Returns:
        Niveau i procent
    """
    level = (volume_liters / total_capacity_liters) * 100
    return round(level, 1)

# Eksempel: 2750L i en 5000L tank
level = volume_to_level(2750, 5000)
print(f"2750L i 5000L tank = {level}%")  # 55%
```

---

## 📘 5. Flow rate konverteringer

```python
def convert_flow(value, from_unit, to_unit):
    """
    Konverter mellem flow enheder
    
    Units: L/min, L/h, m3/h, L/s
    """
    # Konverter til L/min først
    if from_unit == "L/min":
        l_per_min = value
    elif from_unit == "L/h":
        l_per_min = value / 60
    elif from_unit == "m3/h":
        l_per_min = (value * 1000) / 60
    elif from_unit == "L/s":
        l_per_min = value * 60
    else:
        return None
    
    # Konverter fra L/min til target unit
    if to_unit == "L/min":
        result = l_per_min
    elif to_unit == "L/h":
        result = l_per_min * 60
    elif to_unit == "m3/h":
        result = (l_per_min * 60) / 1000
    elif to_unit == "L/s":
        result = l_per_min / 60
    else:
        return None
    
    return round(result, 2)

# Test
print(f"100 L/min = {convert_flow(100, 'L/min', 'L/h')} L/h")      # 6000 L/h
print(f"100 L/min = {convert_flow(100, 'L/min', 'm3/h')} m³/h")   # 6 m³/h
print(f"6 m³/h = {convert_flow(6, 'm3/h', 'L/min')} L/min")       # 100 L/min
```

---

## 📘 6. Fyldningstid

**Hvor lang tid tager det at fylde en tank?**

```python
def fill_time(volume_needed_liters, flow_rate_l_per_min):
    """
    Beregn fyldningstid
    
    Args:
        volume_needed_liters: Volumen der skal fyldes (liter)
        flow_rate_l_per_min: Flow rate i L/min
    
    Returns:
        Tid i minutter
    """
    time_min = volume_needed_liters / flow_rate_l_per_min
    return round(time_min, 1)

def format_time(minutes):
    """Konverter minutter til timer:minutter"""
    hours = int(minutes // 60)
    mins = int(minutes % 60)
    return f"{hours}t {mins}m"

# Eksempel: Fyld 5000L tank med 120 L/min
time = fill_time(5000, 120)
print(f"Fyldningstid: {time} min ({format_time(time)})")  # 41.7 min (0t 41m)
```

---

## 📘 7. Tømningstid

```python
def drain_time(current_volume_liters, flow_rate_l_per_min):
    """
    Beregn tømningstid
    
    Args:
        current_volume_liters: Nuværende volumen i liter
        flow_rate_l_per_min: Flow rate i L/min
    
    Returns:
        Tid i minutter
    """
    time_min = current_volume_liters / flow_rate_l_per_min
    return round(time_min, 1)

# Eksempel: Tøm 3500L med 80 L/min
time = drain_time(3500, 80)
print(f"Tømningstid: {time} min ({format_time(time)})")  # 43.8 min
```

---

## 📘 8. Overflow/Underflow detection

```python
def check_tank_status(current_level_percent, high_alarm=90, low_alarm=10):
    """
    Tjek tank status og returner advarsler
    
    Args:
        current_level_percent: Nuværende niveau %
        high_alarm: Høj alarm grænse %
        low_alarm: Lav alarm grænse %
    
    Returns:
        Status besked
    """
    if current_level_percent >= 100:
        return "⚠️ ALARM: OVERFLOW!"
    elif current_level_percent >= high_alarm:
        return "⚠️ ADVARSEL: Højt niveau"
    elif current_level_percent <= 0:
        return "⚠️ ALARM: Tom tank!"
    elif current_level_percent <= low_alarm:
        return "⚠️ ADVARSEL: Lavt niveau"
    else:
        return "✅ OK"

# Test
print(check_tank_status(95))   # Advarsel: Højt niveau
print(check_tank_status(50))   # OK
print(check_tank_status(5))    # Advarsel: Lavt niveau
print(check_tank_status(105))  # OVERFLOW
```

---

## 📘 9. Flow totalizer

**Beregn total volumen over tid:**

```python
def flow_totalizer(flow_rate_l_per_min, time_minutes):
    """
    Beregn total volumen pumped
    
    Args:
        flow_rate_l_per_min: Flow rate i L/min
        time_minutes: Tid i minutter
    
    Returns:
        Total volumen i liter
    """
    total_liters = flow_rate_l_per_min * time_minutes
    return round(total_liters, 1)

# Eksempel: 150 L/min i 45 minutter
total = flow_totalizer(150, 45)
print(f"Total volumen pumped: {total} L ({total/1000} m³)")  # 6750 L
```

---

## 📘 10. Tank-klasse

```python
class Tank:
    def __init__(self, capacity_liters, current_volume_liters=0):
        self.capacity = capacity_liters
        self.current_volume = current_volume_liters
    
    def get_level_percent(self):
        """Beregn niveau %"""
        return round((self.current_volume / self.capacity) * 100, 1)
    
    def fill(self, liters):
        """Tilføj væske"""
        self.current_volume += liters
        if self.current_volume > self.capacity:
            overflow = self.current_volume - self.capacity
            self.current_volume = self.capacity
            return f"⚠️ Overflow: {overflow} L spildt"
        return f"✅ Tilføjet {liters} L"
    
    def drain(self, liters):
        """Fjern væske"""
        self.current_volume -= liters
        if self.current_volume < 0:
            shortage = abs(self.current_volume)
            self.current_volume = 0
            return f"⚠️ Tom tank: {shortage} L mangler"
        return f"✅ Fjernet {liters} L"
    
    def status(self):
        """Vis tank status"""
        level = self.get_level_percent()
        print(f"Tank: {self.current_volume:.1f} L / {self.capacity} L ({level}%)")
        print(check_tank_status(level))

# Test
tank = Tank(5000, 2500)
tank.status()
print(tank.fill(1000))
tank.status()
print(tank.drain(500))
tank.status()
```

---

## 🧪 Øvelser

1. Beregn volumen af en cylindrisk tank med diameter 3m og højde 4m.
2. En 8000L tank er 42% fyldt. Hvor mange liter er der i tanken?
3. Hvor lang tid tager det at fylde en 3000L tank med 75 L/min?

---

## For de øvede

4. Lav en funktion der beregner hvor mange tanke der skal til for at opbevare X liter.
5. En tank fyldes med 120 L/min og tømmes samtidig med 80 L/min. Hvor lang tid tager det at fylde fra 0 til 100%?
6. Implementér en funktion der advarer hvis fyldning vil medføre overflow.
7. Beregn hvor meget plads der spares ved at bruge cylindrisk tank vs. rektangulær tank med samme volumen.

---

## ✅ Tjekliste

* [ ] Jeg kan beregne volumen af cylindriske og rektangulære tanke
* [ ] Jeg kan konvertere mellem niveau % og liter
* [ ] Jeg kan beregne fyldnings- og tømningstid
* [ ] Jeg kan konvertere mellem flow enheder
* [ ] Jeg kan lave overflow/underflow detection
* [ ] Jeg kan arbejde med flow totalizers

---

## 💡 Tips

* **Enheder:**
  - 1 m³ = 1000 liter
  - 1 liter = 1 dm³
  - Flow: L/min er mest almindelig i industrien

* **Sikkerhed:**
  - Implementér altid high/low alarms
  - Overflow kan være dyrt og farligt
  - Dead band: 5-10% fra alarm til action

* **Praktisk:**
  - Tag højde for piber, ventiler og dead volume
  - Slange/rør volumen kan være betydeligt
  - Flow er ikke altid konstant

---

## 📚 Nyttige formler

**Cylinder volumen:**
```
V = π × r² × h
```

**Rektangel volumen:**
```
V = L × B × H
```

**Fyldningstid:**
```
Tid = Volumen / Flow_rate
```

**Flow konvertering:**
```
L/min → m³/h: (L/min × 60) / 1000
m³/h → L/min: (m³/h × 1000) / 60
```

**Niveau:**
```
Niveau% = (Volumen / Kapacitet) × 100
```

---

## 🔧 Praktisk eksempel: Tank system

```python
# System med 3 tanke
tank_a = Tank(10000, 8000)  # Hoved tank
tank_b = Tank(5000, 1000)   # Buffer tank
tank_c = Tank(3000, 0)      # Process tank

print("=== Initial Status ===")
tank_a.status()
tank_b.status()
tank_c.status()

# Simuler filling
print("\n=== Fylder tank C fra tank A ===")
transfer_volume = 2500
print(tank_a.drain(transfer_volume))
print(tank_c.fill(transfer_volume))

print("\n=== Efter overførsel ===")
tank_a.status()
tank_c.status()

# Beregn hvor lang tid det tog
flow_rate = 100  # L/min
time = fill_time(transfer_volume, flow_rate)
print(f"\nOverførselstid: {time} min ved {flow_rate} L/min")
```

---
