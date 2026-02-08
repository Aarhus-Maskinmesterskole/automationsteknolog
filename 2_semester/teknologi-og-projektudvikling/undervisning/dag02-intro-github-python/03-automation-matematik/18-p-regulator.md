# 🎯 18 – P-Regulator: Proportional Controller

I automation bruger vi regulatorer til at holde processer stabile - fx temperatur, niveau eller tryk. Den simpleste type er P-regulatoren (Proportional), som justerer output proportionalt med afvigelsen fra setpoint.

---

## 🔧 Indhold

* Hvad er en regulator?
* P-regulator princip
* Error beregning
* Proportional gain (Kp)
* Output beregning og skalering
* Praktiske eksempler

---

## 📘 1. Hvad er en regulator?

En regulator sammenligner den **ønskede værdi** (Setpoint) med den **faktiske værdi** (Process Value) og justerer output for at minimere forskellen.

**Terminologi:**
- **SP** = Setpoint (ønsket værdi, fx 50°C)
- **PV** = Process Value (målt værdi, fx 48°C)
- **Error** = SP - PV (afvigelsen, fx 2°C)
- **Output** = Styresignal til ventil, varmer osv. (typisk 0-100%)

**Eksempler:**
- Temperatur kontrol: Juster varme for at holde 50°C
- Niveau kontrol: Juster pumpe for at holde tank ved 60%
- Tryk kontrol: Juster ventil for at holde 5 bar

---

## 📘 2. P-regulator princip

**P-regulatoren virker sådan:**
1. Mål afvigelsen (Error = SP - PV)
2. Gang med en forstærkningsfaktor (Kp)
3. Output = Error × Kp

**Formel:**
```
Output = Kp × Error
Output = Kp × (SP - PV)
```

**Kp (Proportional Gain):**
- Lille Kp = Langsom reaktion
- Stor Kp = Hurtig reaktion (men kan oscillere)

---

## 📘 3. Simpel P-regulator

```python
def p_controller(setpoint, process_value, kp):
    """
    Simpel P-regulator
    
    Args:
        setpoint: Ønsket værdi (SP)
        process_value: Målt værdi (PV)
        kp: Proportional gain
    
    Returns:
        Control output (kan være negativ!)
    """
    error = setpoint - process_value
    output = kp * error
    return round(output, 2)

# Eksempel: Temperatur kontrol
SP = 50  # Ønsket temperatur: 50°C
PV = 45  # Målt temperatur: 45°C
Kp = 2   # Gain faktor

output = p_controller(SP, PV, Kp)
print(f"SP: {SP}°C, PV: {PV}°C")
print(f"Error: {SP - PV}°C")
print(f"Output: {output}")  # 10 (2 × 5)
```

---

## 📘 4. Output skalering (0-100%)

I praksis skal output begrænses til et gyldigt område (fx 0-100%):

```python
def p_controller_scaled(setpoint, process_value, kp, output_min=0, output_max=100):
    """
    P-regulator med output skalering
    
    Args:
        setpoint: Ønsket værdi
        process_value: Målt værdi
        kp: Proportional gain
        output_min: Minimum output (fx 0%)
        output_max: Maximum output (fx 100%)
    
    Returns:
        Skaleret output mellem min og max
    """
    error = setpoint - process_value
    output = kp * error
    
    # Begræns output
    if output > output_max:
        output = output_max
    elif output < output_min:
        output = output_min
    
    return round(output, 1)

# Test
SP = 60
PV = 40
Kp = 5

output = p_controller_scaled(SP, PV, Kp)
print(f"Error: {SP - PV}, Output: {output}%")  # Error: 20, Output: 100%
```

---

## 📘 5. Temperatur kontrol eksempel

```python
def temperature_controller(target_temp, current_temp, kp=3):
    """
    P-regulator til temperatur kontrol
    
    Returnerer varme output 0-100%
    """
    error = target_temp - current_temp
    output = kp * error
    
    # Begræns til 0-100%
    output = max(0, min(100, output))
    
    return round(output, 1)

# Simuler forskellige temperaturer
target = 50  # °C
temps = [30, 40, 45, 48, 50, 52, 55]

print(f"Target temperatur: {target}°C\n")
for temp in temps:
    output = temperature_controller(target, temp)
    error = target - temp
    print(f"PV: {temp}°C | Error: {error:+3d}°C | Output: {output:5.1f}%")
```

**Output:**
```
Target temperatur: 50°C

PV: 30°C | Error: +20°C | Output: 100.0%
PV: 40°C | Error: +10°C | Output:  30.0%
PV: 45°C | Error:  +5°C | Output:  15.0%
PV: 48°C | Error:  +2°C | Output:   6.0%
PV: 50°C | Error:  +0°C | Output:   0.0%
PV: 52°C | Error:  -2°C | Output:   0.0%
PV: 55°C | Error:  -5°C | Output:   0.0%
```

---

## 📘 6. Tank niveau kontrol

```python
def level_controller(target_level_percent, current_level_percent, kp=2):
    """
    P-regulator til tank niveau
    
    Returnerer pumpe hastighed 0-100%
    """
    error = target_level_percent - current_level_percent
    output = kp * error
    
    # Begræns til 0-100%
    output = max(0, min(100, output))
    
    return round(output, 1)

# Test: Hold tank på 60%
target = 60
levels = [20, 40, 55, 58, 60, 62, 70]

print(f"Target niveau: {target}%\n")
for level in levels:
    output = level_controller(target, level)
    error = target - level
    print(f"PV: {level}% | Error: {error:+3d}% | Pumpe: {output:5.1f}%")
```

---

## 📘 7. P-regulator klasse

```python
class PController:
    def __init__(self, kp, output_min=0, output_max=100):
        self.kp = kp
        self.output_min = output_min
        self.output_max = output_max
        self.last_error = 0
    
    def calculate(self, setpoint, process_value):
        """Beregn control output"""
        error = setpoint - process_value
        output = self.kp * error
        
        # Begræns output
        output = max(self.output_min, min(self.output_max, output))
        
        self.last_error = error
        return round(output, 2)
    
    def get_error(self):
        """Hent sidste error"""
        return self.last_error

# Brug
controller = PController(kp=3, output_min=0, output_max=100)

SP = 50
PV = 45

output = controller.calculate(SP, PV)
print(f"Output: {output}%")
print(f"Error: {controller.get_error()}")
```

---

## 📘 8. Simpel simulator

**Simuler temperatur over tid:**

```python
import time

def simulate_heating():
    """Simuler opvarmning med P-regulator"""
    target_temp = 50  # °C
    current_temp = 20  # Start temperatur
    kp = 3
    
    print(f"Opvarmer til {target_temp}°C\n")
    print("Tid | Temp  | Error | Output")
    print("----|-------|-------|-------")
    
    for t in range(20):  # 20 iterationer
        # Beregn controller output
        output = temperature_controller(target_temp, current_temp, kp)
        error = target_temp - current_temp
        
        # Simuler temperatur ændring baseret på output
        temp_change = output / 50  # Simplificeret: output påvirker temp
        current_temp += temp_change
        
        print(f"{t:3d} | {current_temp:5.1f} | {error:+5.1f} | {output:5.1f}%")
        
        # Stop hvis meget tæt på target
        if abs(error) < 0.5:
            print("\n✅ Target nået!")
            break

# Kør simulation
simulate_heating()
```

---

## 🧪 Øvelser

1. Lav en P-regulator der holder tryk på 5 bar. Test med forskellige Kp værdier (1, 2, 5).
2. Beregn output for temperatur kontrol: SP=75°C, PV=68°C, Kp=4.
3. Hvilken Kp værdi giver output=50% når error=10?

---

## For de øvede

4. Lav en simulator der plotter temperatur over tid (brug lists til at gemme værdier).
5. Implementér en funktion der automatisk finder optimal Kp ved at teste forskellige værdier.
6. Tilføj dead band: Hvis error < 1°C, sæt output til 0 (undgå oscillation).
7. Kombiner med tank-klassen fra opgave 17: Regulér pumpe for at holde konstant niveau.

---

## For de advanced

8. Lav en manuel tuning guide der viser hvordan man finder god Kp værdi.
9. Implementér reverse acting controller (for køling i stedet for varmning).
10. Kombiner med Flask API: Send SP og PV → returner optimal output.
11. Sammenlign P-regulator med on/off kontrol - vis forskellen grafisk.

---

## ✅ Tjekliste

* [ ] Jeg forstår hvad SP, PV og Error betyder
* [ ] Jeg kan beregne P-regulator output
* [ ] Jeg forstår hvordan Kp påvirker responsen
* [ ] Jeg kan implementere output skalering (0-100%)
* [ ] Jeg kan lave en simpel P-regulator klasse
* [ ] Jeg kan bruge P-regulatorer i praksis

---

## 💡 Tips

* **Kp tuning:**
  - Start med lav Kp (fx 1-2)
  - Øg gradvist indtil god respons
  - For høj Kp → oscillation (svinger frem og tilbage)
  - For lav Kp → langsom respons

* **Offset problem:**
  - P-regulator alene når sjældent præcist setpoint
  - Der vil ofte være en lille permanent afvigelse (offset)
  - Dette kan løses med en I-term (kommer i avanceret kursus)

* **Dead band:**
  - Implementér dead band (fx ±1°C) for at undgå konstant justering
  - Sparer energi og slitage på udstyr

---

## 📚 Vigtige formler

**Error beregning:**
```
Error = SP - PV
```

**P-regulator output:**
```
Output = Kp × Error
Output = Kp × (SP - PV)
```

**Output begrænsning:**
```
Output = max(min_output, min(max_output, calculated_output))
```

---

## 🔧 Praktisk eksempel: Varmesystem

```python
class HeatingSystem:
    def __init__(self, target_temp, kp=3):
        self.target_temp = target_temp
        self.current_temp = 20  # Start temperatur
        self.controller = PController(kp, 0, 100)
        self.heater_output = 0
    
    def update(self):
        """Opdater system for én iteration"""
        # Beregn controller output
        self.heater_output = self.controller.calculate(
            self.target_temp, 
            self.current_temp
        )
        
        # Simuler temperatur ændring
        heating = self.heater_output / 50
        cooling = (self.current_temp - 20) * 0.1  # Heat loss
        self.current_temp += heating - cooling
    
    def status(self):
        """Vis system status"""
        error = self.target_temp - self.current_temp
        print(f"Target: {self.target_temp}°C | "
              f"Current: {self.current_temp:.1f}°C | "
              f"Error: {error:+.1f}°C | "
              f"Heater: {self.heater_output:.1f}%")

# Simuler varmesystem
system = HeatingSystem(target_temp=50, kp=3)

print("Opvarmnings simulation:\n")
for i in range(15):
    system.status()
    system.update()

print("\n✅ Simulation færdig")
```

---

## ⚙️ Real-world anvendelser

**P-regulatorer bruges til:**
- Temperatur kontrol i ovne og reaktorer
- Niveau kontrol i tanke
- Tryk kontrol i pneumatiske systemer
- Hastigheds kontrol på motorer (enkle cases)
- Flow kontrol med reguléringsventiler

**Begrænsninger:**
- Kan ikke eliminere steady-state error fuldstændigt
- Kan oscillere ved høj Kp
- Reagerer kun på nuværende error (ikke historik eller trends)

---
