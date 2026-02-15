# 🌐 Profibus DP: Decentral I/O med Siemens S7-1200 (ET 200SP) ⚙️

> 🎯 **Læringsmål:** Du lærer at opsætte en **Profibus DP decentral I/O station** (fx ET 200SP) og få PLC’en til at **læse/skrive digitale signaler** via Profibus.

---

## 🎥 Video-guide

👉 [https://www.youtube.com/watch?v=oTKpon7wkMo](https://www.youtube.com/watch?v=oTKpon7wkMo)

---

## ⚠️ OBS: IP-adresser (kun relevant for TIA/PLC-netværk) 🧠

Når du følger videoen, så brug **din egen IP-adresse** — ikke videoens.
Det mindsker risiko for konflikter og forkert subnet.

🔎 Find IP:

* **Windows:** `ipconfig`
* **Linux/Mac:** `ifconfig` *(eller `ip a` på Linux)*
  📌 Kig efter Ethernet-adapterens IP (typisk `192.168.x.x` eller `10.x.x.x`)

---

## 🧩 Profibus DP: Hvem er hvem? (Master/Slave) 👑➡️🤝

I denne opgave er:

* **S7-1200 + CM 1243-5 = Master** 🧠
* **ET 200SP DP station = Slave** 🧷

🎯 Målet er at konfigurere forbindelsen og derefter **styre/læse I/O** på ET 200SP.

---

## 🔥 VIGTIGT: Terminering på Profibus 🔌

✅ Termineringskontakten i Profibus-stikket skal stå på **`ON`** på:

* **første enhed** i netværket
* **sidste enhed** i netværket

Hvis terminering er forkert, får du ofte ustabil kommunikation eller ingen kommunikation 😅

---

# ✅ 1) Del A – Opsæt Profibus DP i TIA Portal 🛠️

### Opgave (trin-for-trin)

1. Åbn **TIA Portal** og opret et nyt projekt.

2. Tilføj en **S7-1215 (AC/DC/RLY)** til projektet.

3. Gå til **Device Configuration**.

4. Tilføj **CM 1243-5** (Profibus modul) til PLC’en.

5. Tilføj en **ET 200SP DP station**:
   (6ES7-151-1AA05-0AB0)

6. Tilføj digitale moduler til ET 200SP stationen:

   * Digitalt modul: **6ES7-138-4CA01-0AA0**
   * Digitalt modul: **6ES7-132-4BB01-0AB0**
   * Digitalt modul: **6ES7-134-4NB51-0AB0**

7. Sæt ET 200SP som **slave adresse 3** på Profibus-netværket:

   * 📌 **Profibus Address = 3**

✅ **Mål:** TIA Portal viser nu et Profibus-netværk hvor Master (S7-1200) kan “se” slaven (ET 200SP).

---

# ✅ 2) Del B – OB1-program: Læs/skriv og test logik i praksis 🧪

### Opgave

1. Gå til **OB1**.
2. Lav et simpelt program der demonstrerer styring og selvhold:

🔹 Opret 2 memory bits, fx:

* `M0.0` = **Start** (NO) ▶️
* `M0.1` = **Stop** (NC) ⛔
* `Q2.0` = **Coil + selvhold** 🔁

Logik (princip):

* `M0.0` (NO) starter
* `M0.1` (NC) stopper
* `Q2.0` holder sig selv (selvhold) via NO kontakt

3. Download programmet til PLC’en som **Hardware download** og start PLC’en ▶️
4. Brug en **Watch Table** til at overvåge:

   * `M0.0`, `M0.1`, `Q2.0`
   * og se hvordan signalerne påvirker hinanden 🔄

✅ **Mål:** Du kan aktivere/deaktivere og se at Q2.0 opfører sig som forventet (start/stop + selvhold).

---

## 📝 Hurtig tjekliste hvis det driller 🧯

* ✅ Er CM 1243-5 korrekt monteret/tilføjet i Device Configuration?
* ✅ Matcher Profibus-adresser? (slave = 3)
* ✅ Terminering ON på første + sidste enhed?
* ✅ Er Profibus-kablet korrekt og stik ordentligt i?
* ✅ Viser TIA “grøn” kommunikation/ingen fejl?