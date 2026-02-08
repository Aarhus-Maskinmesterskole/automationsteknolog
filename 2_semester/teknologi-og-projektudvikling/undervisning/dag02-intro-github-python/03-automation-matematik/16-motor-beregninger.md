# ⚙️ 16 – Motor Beregninger: RPM, Effekt og Moment

Motorer er hjertet i automation. Python kan hjælpe med at beregne hastighed, effekt, moment, gear ratios og energiforbrug - alt sammen vigtige parametre når du arbejder med motorer og frekvensomformere.

---

## 🔧 Indhold

* Grundlæggende motor parametre
* RPM ↔ Hz (frekvensomformer)
* Effekt, moment og hastighed
* Gear ratio beregninger
* Energiforbrug
* Start-tid og acceleration

---

## 📘 1. Grundlæggende motor parametre

**Vigtige begreber:**
- **RPM** = Rotations Per Minut (omdrejninger per minut)
- **Hz** = Frekvens (typisk 50 Hz i Europa, 60 Hz i USA)
- **P** = Pole par (2, 4, 6, 8 poler)
- **kW** = Effekt i kilowatt
- **Nm** = Moment (Newton-meter)

**Standard motor hastigheder ved 50 Hz:**
- 2-polet motor: ~3000 RPM (2880-2940 RPM pga. slip)
- 4-polet motor: ~1500 RPM (1440-1470 RPM)
- 6-polet motor: ~1000 RPM (960-980 RPM)

---

## 📘 2. Hz → RPM (Frekvensomformer)

**Formel:**
```
RPM = (120 × Hz) / Antal_poler
```

(Teoretisk hastighed - uden slip)

```python
def hz_to_rpm(hz, poler=4):
    """
    Konverter frekvens til RPM
    
    Args:
        hz: Frekvens i Hz
        poler: Antal motor poler (2, 4, 6, 8)
    
    Returns:
        Teoretisk RPM
    """
    rpm = (120 * hz) / poler
    return round(rpm)

# Test med 4-polet motor
print(f"50 Hz = {hz_to_rpm(50, 4)} RPM")  # 1500 RPM
print(f"25 Hz = {hz_to_rpm(25, 4)} RPM")  # 750 RPM
print(f"75 Hz = {hz_to_rpm(75, 4)} RPM")  # 2250 RPM

# Test med 2-polet motor
print(f"\n50 Hz (2-polet) = {hz_to_rpm(50, 2)} RPM")  # 3000 RPM
```

---

## 📘 3. RPM → Hz

**Reverse engineering: Hvilken frekvens skal jeg indstille?**

```python
def rpm_to_hz(rpm, poler=4):
    """
    Konverter RPM til frekvens
    
    Args:
        rpm: Ønsket hastighed i RPM
        poler: Antal motor poler
    
    Returns:
        Nødvendig frekvens i Hz
    """
    hz = (rpm * poler) / 120
    return round(hz, 1)

# Hvis jeg vil have 1200 RPM på en 4-polet motor
print(f"1200 RPM = {rpm_to_hz(1200, 4)} Hz")  # 40 Hz
print(f"900 RPM = {rpm_to_hz(900, 4)} Hz")    # 30 Hz
```

---

## 📘 4. Effekt og Moment

**Sammenhæng mellem effekt (kW), moment (Nm) og hastighed (RPM):**

```
P(kW) = (M(Nm) × RPM) / 9549
```

```python
def calculate_power(torque_nm, rpm):
    """
    Beregn effekt fra moment og hastighed
    
    Args:
        torque_nm: Moment i Newton-meter
        rpm: Hastighed i RPM
    
    Returns:
        Effekt i kW
    """
    kw = (torque_nm * rpm) / 9549
    return round(kw, 2)

# Eksempel: Motor med 95 Nm ved 1450 RPM
power = calculate_power(95, 1450)
print(f"Effekt: {power} kW")  # ~14.4 kW (dvs. 15 kW motor)
```

---

## 📘 5. Beregn Moment

Hvis du kender effekt og hastighed, kan du beregne moment:

```python
def calculate_torque(kw, rpm):
    """
    Beregn moment fra effekt og hastighed
    
    Args:
        kw: Effekt i kilowatt
        rpm: Hastighed i RPM
    
    Returns:
        Moment i Nm
    """
    torque = (kw * 9549) / rpm
    return round(torque, 1)

# Eksempel: 11 kW motor ved 1450 RPM
torque = calculate_torque(11, 1450)
print(f"Moment: {torque} Nm")  # ~72.5 Nm
```

---

## 📘 6. Gear Ratio (Gearing)

**Gear ratio beregninger:**

```python
def gear_output_rpm(motor_rpm, gear_ratio):
    """
    Beregn output hastighed efter gear
    
    Args:
        motor_rpm: Motor hastighed
        gear_ratio: Gear forhold (fx 10:1 = 10)
    
    Returns:
        Output RPM
    """
    output_rpm = motor_rpm / gear_ratio
    return round(output_rpm, 1)

def gear_output_torque(motor_torque, gear_ratio, efficiency=0.95):
    """
    Beregn output moment efter gear
    
    Args:
        motor_torque: Motor moment i Nm
        gear_ratio: Gear forhold
        efficiency: Gear effektivitet (typisk 0.90-0.98)
    
    Returns:
        Output moment i Nm
    """
    output_torque = motor_torque * gear_ratio * efficiency
    return round(output_torque, 1)

# Eksempel: 1450 RPM motor med 10:1 gear
motor_rpm = 1450
motor_torque = 50
gear_ratio = 10

output_rpm = gear_output_rpm(motor_rpm, gear_ratio)
output_torque = gear_output_torque(motor_torque, gear_ratio)

print(f"Motor: {motor_rpm} RPM, {motor_torque} Nm")
print(f"Output: {output_rpm} RPM, {output_torque} Nm")
```

---

## 📘 7. Energiforbrug

**Beregn energiforbrug over tid:**

```python
def energy_consumption(kw, hours):
    """
    Beregn energiforbrug
    
    Args:
        kw: Effekt i kilowatt
        hours: Driftstimer
    
    Returns:
        Energi i kWh
    """
    kwh = kw * hours
    return round(kwh, 2)

def energy_cost(kwh, price_per_kwh=2.50):
    """
    Beregn energi omkostninger
    
    Args:
        kwh: Energi i kWh
        price_per_kwh: Pris per kWh i DKK
    
    Returns:
        Omkostning i DKK
    """
    cost = kwh * price_per_kwh
    return round(cost, 2)

# Eksempel: 15 kW motor kører 8 timer dagligt
daily_kwh = energy_consumption(15, 8)
monthly_kwh = energy_consumption(15, 8 * 22)  # 22 arbejdsdage
monthly_cost = energy_cost(monthly_kwh)

print(f"Daglig: {daily_kwh} kWh")
print(f"Månedlig: {monthly_kwh} kWh = {monthly_cost} DKK")
```

---

## 📘 8. Acceleration og Start-tid

**Beregn tid til at nå ønsket hastighed:**

```python
def acceleration_time(rpm_start, rpm_end, acceleration_rpm_per_sec):
    """
    Beregn accelerationstid
    
    Args:
        rpm_start: Start hastighed
        rpm_end: Slut hastighed
        acceleration_rpm_per_sec: Acceleration i RPM/s
    
    Returns:
        Tid i sekunder
    """
    delta_rpm = abs(rpm_end - rpm_start)
    time_sec = delta_rpm / acceleration_rpm_per_sec
    return round(time_sec, 1)

# Eksempel: 0-1450 RPM med 100 RPM/s acceleration
time = acceleration_time(0, 1450, 100)
print(f"Accelerationstid: {time} sekunder")  # 14.5 sek

# Med hurtigere acceleration
time_fast = acceleration_time(0, 1450, 200)
print(f"Hurtig acceleration: {time_fast} sekunder")  # 7.25 sek
```

---

## 📘 9. Komplet motor-klasse

```python
class Motor:
    def __init__(self, power_kw, rpm_nominal, poles=4):
        self.power_kw = power_kw
        self.rpm_nominal = rpm_nominal
        self.poles = poles
        self.torque_nm = calculate_torque(power_kw, rpm_nominal)
    
    def get_hz(self):
        """Beregn nominel frekvens"""
        return rpm_to_hz(self.rpm_nominal, self.poles)
    
    def rpm_at_hz(self, hz):
        """Beregn RPM ved given frekvens"""
        return hz_to_rpm(hz, self.poles)
    
    def energy_per_hour(self):
        """Energiforbrug per time"""
        return self.power_kw
    
    def info(self):
        """Vis motor information"""
        print(f"Motor: {self.power_kw} kW, {self.rpm_nominal} RPM")
        print(f"Poler: {self.poles}, Moment: {self.torque_nm} Nm")
        print(f"Nominel frekvens: {self.get_hz()} Hz")

# Opret motor objekt
motor = Motor(11, 1450, 4)
motor.info()
print(f"\nVed 25 Hz: {motor.rpm_at_hz(25)} RPM")
print(f"Energi per time: {motor.energy_per_hour()} kWh")
```

---

## 🧪 Øvelser

1. Beregn RPM for en 4-polet motor ved 30 Hz, 40 Hz og 60 Hz.
2. Du har en 7.5 kW motor ved 1450 RPM. Beregn momentet.
3. Beregn omkostning for at køre en 22 kW motor 24/7 i en måned (pris: 2 DKK/kWh).

---

## For de øvede

4. Lav en funktion der beregner hvor lang tid det tager at spare X DKK ved at skifte til en mere effektiv motor.
5. En motor med 100 Nm kører gennem et 15:1 gear. Beregn output moment og hastighed.
6. Lav et program der sammenligner 2-polet vs 4-polet motor ved forskellige frekvenser.
7. Implementér slip-beregning: Reel RPM = Teoretisk RPM × (1 - slip%), hvor slip typisk er 2-4%.

---

## ✅ Tjekliste

* [ ] Jeg kan konvertere mellem Hz og RPM
* [ ] Jeg forstår sammenhængen mellem effekt, moment og hastighed
* [ ] Jeg kan beregne gear output
* [ ] Jeg kan beregne energiforbrug og omkostninger
* [ ] Jeg kan beregne accelerationstid
* [ ] Jeg kan lave motor-beregninger i praksis

---

## 💡 Tips

* **Slip:** Motorer kører typisk 2-4% langsommere end teoretisk RPM pga. slip
* **Overload:** Motorer kan typisk levere 150-200% moment kortvarigt
* **Frekvensområde:** Typisk 0-100 Hz, nogle VFD'er kan op til 400 Hz
* **Energibesparelse:** At reducere hastighed med 20% kan spare ~50% energi (kubisk forhold for pumper/ventilation)

---

## 📚 Nyttige formler

**RPM fra frekvens:**
```
RPM = (120 × Hz) / Antal_poler
```

**Effekt fra moment:**
```
P(kW) = (M(Nm) × RPM) / 9549
```

**Moment fra effekt:**
```
M(Nm) = (P(kW) × 9549) / RPM
```

**Gear output:**
```
Output_RPM = Input_RPM / Gear_ratio
Output_Moment = Input_Moment × Gear_ratio × Efficiency
```

---

## 🔧 Praktisk eksempel: Motor selektion

```python
# Krav: Transportsystem skal køre 100 RPM med 500 Nm
required_rpm = 100
required_torque = 500

# Vælg standard 1450 RPM motor
motor_rpm = 1450

# Beregn gear ratio
gear_ratio = motor_rpm / required_rpm
print(f"Nødvendig gear ratio: {gear_ratio}:1")  # 14.5:1

# Beregn nødvendig motor moment
motor_torque = required_torque / (gear_ratio * 0.95)  # 95% efficiency
print(f"Motor moment behov: {round(motor_torque, 1)} Nm")

# Beregn motor effekt
motor_power = calculate_power(motor_torque, motor_rpm)
print(f"Motor effekt behov: {motor_power} kW")

# Vælg nærmeste standard størrelse (7.5, 11, 15, 18.5, 22 kW)
print(f"Anbefalet motor: 15 kW")
```

---
