# 🔄 Rotationsøvelse 1: Modbus TCP, IO-Link & Profibus 🚀

> 🎯 **Formål:** I denne rotationsøvelse får I hands-on erfaring med **tre centrale industrielle kommunikationsprotokoller**, som I møder igen og igen i moderne OT/automation.

> 🧠 **Output:** I skal **både få det til at virke** *og* kunne **forklare og dokumentere hvordan** I gjorde.

---

## 📡 Del A: Modbus TCP – Siemens S7-1200/S7-1500 som Server + Emulate3D som Client

### 🛠️ Øvelsesbeskrivelse

I skal konfigurere en **Modbus TCP server** på en Siemens **S7-1200/S7-1500**.
Herefter bruger I **Emulate3D som Modbus TCP client** til at læse/skrive data til PLC’en.

### ✅ Opgaver

1. 🎥 Følg videoen og få styr på opsætningen i TIA Portal
2. 🟩 Byg et **transportbånd i Emulate3D** med **Start/Stop-knapper**
3. 📦 Når en kasse når enden af båndet:

   * PLC’en skal **tælle +1**
   * Tællingen skal ske via **skrivning til et holding register** (fra client → PLC)

### 🎥 Video

👉 [Modbus TCP med Emulate3D](https://www.youtube.com/watch?v=WTjcJUzEBSk)

---

## 🔌 Del B: IO-Link – S7-1200 + IFM IO-Link Master + sensorer 📟

### 🛠️ Øvelsesbeskrivelse

I skal opsætte en **IFM IO-Link Master** med forskellige sensorer og koble det til en **Siemens S7-1200**.

### ✅ Fokus (det I skal kunne bagefter)

* 🔁 Skelne mellem **procesdata vs. parametre**
* 🧩 Forstå **master/device roller**
* 🧪 Teste at data faktisk opdaterer korrekt

### 🎥 Video

👉 [IO-Link Master konfiguration](https://www.youtube.com/watch?v=6METqn73cJA)

---

## 🌐 Del C: Profibus DP – S7-1200 + ET 200SP (decentral I/O) ⚙️

### 🛠️ Øvelsesbeskrivelse

I skal etablere en **Profibus DP forbindelse** mellem en **S7-1200** og en **ET 200SP station**.
Målet er at I kan **konfigurere, mappe og teste** data til/fra de digitale moduler.

### ✅ Opgave (dokumentation)

📌 Dokumentér trin-for-trin hvordan man konfigurerer Profibus DP i TIA Portal
— svarende til opgaven i:
`dag03-profibus-modbus-tcp/02-profibus-decentral-io.md`

### 📝 Fokuspunkter

* 👑 Master/Slave-konfiguration
* 🔢 Adresseopsætning (Profibus adresse + I/O mapping)
* 🔌 Digital I/O moduler (læse/skrive)
* ✅ Test af kommunikation + kort fejlsøgning (hvad tjekker du først?)

---

## 📌 VIGTIGT: Rapportkrav 🧾✨

⚠️ Rapporten skal indeholde:

* 🧠 Gode forklaringer i egne ord (ikke kun screenshots)
* 🖼️ Billeder med **figur-tekst** (fx “Figur 3: Profibus konfiguration i TIA Portal”)
* 🧭 Netværks-/topologi-overblik (gerne et simpelt diagram)