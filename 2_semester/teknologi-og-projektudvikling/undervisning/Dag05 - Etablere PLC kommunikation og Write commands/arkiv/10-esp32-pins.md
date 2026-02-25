# 📘 10 – ESP32-WROOM-32 Pins og Funktioner

#### 🎯 Oversigt

Denne fil forklarer ESP32-WROOM-32's GPIO-pins og deres anvendelser: Digital I/O, PWM, Analog (ADC), Kapacitiv Touch.

ESP32 har 34 GPIO-pins (GPIO0-GPIO39), men ikke alle er frit tilgængelige pga. strøm, boot og andre funktioner.

---

### 🔌 Digital I/O (Input/Output)

De fleste GPIO-pins kan bruges til digital I/O.

**Tilgængelige pins:** GPIO0-GPIO39 (undtagen special-pins)

**Eksempler:**
- GPIO2, GPIO4, GPIO5, GPIO18, GPIO19, GPIO21, GPIO22, GPIO23

**Bemærkninger:**
- GPIO0: Bruges til boot (hold LOW ved opstart for flash mode)
- GPIO1/GPIO3: UART0 (Serial)
- GPIO6-GPIO11: SPI flash (ikke tilgængelig)
- GPIO12: Boot strapping (hold HIGH ved opstart)
- GPIO34-GPIO39: Input only (ingen pull-up/down)

**Brug i kode:**
```python
from machine import Pin

led = Pin(2, Pin.OUT)  # Output
button = Pin(4, Pin.IN, Pin.PULL_UP)  # Input med pull-up
```

---

### ⚡ PWM (Pulse Width Modulation)

De fleste digitale pins understøtter PWM for analog output (f.eks. LED lysstyrke, motor speed).

**Tilgængelige pins:** GPIO0-GPIO33 (samme som digital I/O, undtagen input-only)

**Eksempler:**
- GPIO2, GPIO4, GPIO5, GPIO18, GPIO19

**Bemærkninger:**
- PWM frekvens: 1Hz - 40MHz
- Duty cycle: 0-1023 (10-bit resolution)

**Brug i kode:**
```python
from machine import Pin, PWM

led = PWM(Pin(2), freq=1000)
led.duty(512)  # 50% duty cycle
```

---

### 📊 Analog (ADC - Analog to Digital Converter)

ESP32 har 2 ADC-enheder: ADC1 (stabil) og ADC2 (kan konflikte med WiFi).

**ADC1 (anbefalet):**
- Pins: GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO37, GPIO38, GPIO39
- 12-bit resolution (0-4095)
- Spændingsområde: 0-3.3V (brug atten for højere)

**ADC2 (undgå hvis muligt):**
- Pins: GPIO0, GPIO2, GPIO4, GPIO12, GPIO13, GPIO14, GPIO15, GPIO25, GPIO26, GPIO27
- Samme som ADC1, men kan forstyrre WiFi

**Bemærkninger:**
- GPIO34-GPIO39: Input only
- ADC2 pins kan ikke bruges samtidig med WiFi

**Brug i kode:**
```python
from machine import ADC, Pin

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)  # 0-3.3V
value = adc.read()  # 0-4095
```

---

### 👆 Kapacitiv Touch

ESP32 har 10 indbyggede touch pins til berøringsdetektion uden eksterne komponenter.

**Touch Pins:**
- GPIO4 (T0)
- GPIO0 (T1)
- GPIO2 (T2)
- GPIO15 (T3)
- GPIO13 (T4)
- GPIO12 (T5)
- GPIO14 (T6)
- GPIO27 (T7)
- GPIO33 (T8)
- GPIO32 (T9)

**Bemærkninger:**
- Touch værdi: Typisk 0-1000 (falder ved berøring)
- Ingen eksterne komponenter nødvendig
- Kan bruges samtidig med digital I/O

**Brug i kode:**
```python
from machine import TouchPad, Pin

touch = TouchPad(Pin(4))
value = touch.read()  # Læs touch værdi
```

---

### ⚠️ Vigtige Bemærkninger

* **Strømforsyning:** Brug 3.3V til alle pins (GPIO er 3.3V tolerant)
* **Boot-problemer:** Undgå at bruge GPIO0, GPIO2, GPIO12, GPIO15 som output ved boot
* **WiFi/Bluetooth:** ADC2 pins kan forstyrre trådløs kommunikation
* **Input-only pins:** GPIO34-GPIO39 kan kun bruges som input
* **Pull-up/down:** Tilgængelig på de fleste pins undtagen GPIO34-GPIO39

---

### ✅ Tjekliste

* [ ] Jeg har identificeret de pins jeg vil bruge
* [ ] Jeg har tjekket for konflikter (boot, WiFi, etc.)
* [ ] Jeg har valgt ADC1 pins for analog læsning
* [ ] Jeg har noteret touch pins for kapacitiv sensing
* [ ] Jeg forstår begrænsningerne for hver pin-type

---
