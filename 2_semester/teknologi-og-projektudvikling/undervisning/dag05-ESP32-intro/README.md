# 📘 README – Dag 05: ESP32 intro (MicroPython)

Velkommen til dag 5, hvor du skal arbejde med ESP32-mikrocontrolleren. Målet i dag er at komme i gang med **MicroPython** og bruge ESP32 som en lille “sensor-/I/O-enhed”, der kan sende data videre til en PC.

Det her bliver fundamentet for de kommende dage, hvor vi i Python skal hente og analysere data fra ESP32 via seriel kommunikation (pyserial).

---

## 🎯 Formål med dagen

* Installere og opsætte MicroPython på ESP32 (via Thonny)
* Køre dit første script og få stabilt output
* Sende måledata i et simpelt CSV-lignende format
* Tilslutte og afprøve udvalgte sensorer/inputs

---

## 📚 Modulstruktur og filer

Du arbejder dig igennem følgende filer i rækkefølge:

```
dag05-ESP32-intro/
├── 01-opsaetning-esp32.md         # Flash MicroPython og test med blink i Thonny
├── 02-seriel-output-csv.md        # Stabilt output i CSV-format (til Python senere)
├── 03-dht22-simple.md             # Temperatur/fugt (DHT22)
├── 04-mq2-gas.md                  # Gas/smoke sensor (MQ-2)
├── 05-ldr.md                      # Lysmåling (LDR)
├── 06-pir.md                      # Bevægelse (PIR)
├── 07-distance.md                 # Afstand (typisk ultralyd)
├── 08-pwm-led.md                  # PWM (fx LED-dæmpning)
├── 09-capacitive-touch.md         # Kapacitiv touch
└── 10-esp32-pins.md               # Pinout/overblik
```

---

## 💼 Relevans for praksis

ESP32 bruges i både industri og hobbyprojekter til:

* Indsamling af data fra fysiske systemer
* Kommunikation med PC, sky eller cloud-platforme
* Prototyper til IoT, måling og regulering

Når du kan strukturere måledata i ESP32, bliver det meget lettere at analysere og dokumentere systemer i Python og GitHub.

---

## ✅ Output for dagen

* En fungerende ESP32 med MicroPython og Thonny-forbindelse
* Seriel output i et stabilt format (fx `SENSOR,23.5,41.2` eller `23.5,41.2`)
* Mindst én sensor der kan aflæses og printes stabilt
* En forståelse af hvorfor format og stabilitet betyder noget for efterfølgende Python-logning

---

> Tænk på ESP32 som "sensorens stemme" – den taler via `print()`, og Python lærer at lytte i næste modul.
