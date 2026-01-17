# 📘 README – Dag 03: ESP32 intro

Velkommen til tredje undervisningsdag, hvor du skal arbejde med ESP32-mikrocontrolleren. Målet i dag er at komme i gang med at programmere ESP32, tilslutte en sensor, læse måleværdier og sende dem som struktureret output via seriel kommunikation.

Dette modul er fundamentet for de kommende dage, hvor vi i Python skal hente og analysere data fra ESP32.

---

## 🎯 Formål med dagen

* Installere og opsætte ESP32 i Arduino IDE
* Skrive en simpel ESP32-sketch der læser analoge værdier
* Forstå hvordan `Serial.print()` bruges til at sende data
* Producere data i et CSV-lignende format til senere brug i Python

---

## 📚 Modulstruktur og filer

Du arbejder dig igennem følgende filer i rækkefølge:

```
dag03-esp32-intro/
├── 01-opsaetning-esp32.md         # Installer board og test med blink
├── 02-sensor-maaling.md           # analogRead() og delay()
├── 03-seriel-output.md            # Serial.begin(), print målinger
├── 04-eksperimenter.md            # Måling af fysiske fænomener
├── 05-debug-og-fejl.md            # Almindelige problemer og løsninger
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

* En fungerende ESP32 med korrekt COM-port og programmering
* En sensor, der giver måleværdier via analogRead()
* Seriel output der ligner: `1023,250` (værdi, delay)
* En forståelse af hvordan denne data senere skal læses af Python

---

> Tænk på ESP32 som "sensorens stemme" – den taler via `Serial.print()`, og Python lærer at lytte i næste modul.
