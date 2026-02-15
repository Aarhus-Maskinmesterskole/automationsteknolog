# 🤖 Universal Robots som Modbus TCP Client (til Siemens PLC Server) 🌐

> 🎯 **Læringsmål:** Du lærer at konfigurere **Universal Robots (UR)** som **Modbus TCP Client**, der kan **skrive til coils** på en **Siemens PLC**, som kører **Modbus TCP Server** ✅

---

## 🎥 Video-guide

👉 [https://www.youtube.com/watch?v=xu8TcCQ1nGo](https://www.youtube.com/watch?v=xu8TcCQ1nGo)

---

## ⚠️ OBS: Netværk & IP-adresser (meget vigtigt!) 🧠🔌

Når du følger videoen, så brug **dine egne IP-adresser** — ikke videoens.
Ellers kan I få IP-konflikter eller være i forkert subnet.

### 🔎 Find din PC-IP

* **Windows:** `ipconfig`
* **Linux/Mac:** `ifconfig` *(eller `ip a` på Linux)*
  📌 Kig efter IP’en på Ethernet-adapteren (typisk `192.168.x.x` eller `10.x.x.x`)

### ✅ Netværkstest (skal virke før du går videre)

* PC → Robot: `ping <robot-IP>`
* Robot → PC: `ping <pc-IP>` *(hvis muligt)*

### 🧩 Find IP på UR-simulator (Lubuntu)

1. Tryk på den **nederste knap i venstre side** (startmenu)
2. Find **Terminal / TeraTerm**
3. Skriv: `ip a`
   📌 Notér robot-simulatorens IP

---

# ✅ 1) Del A – Opsæt UR som Modbus TCP Client 🔁📤

### 🛠️ Opgave (trin-for-trin)

1. Åbn **VMware** og start **Universal Robots simulatoren** ▶️
2. Log ind, og tryk på **de tre streger** (☰) i øverste højre hjørne
3. Vælg: **System → Netværk**

   * Find robot-IP (skal være **DHCP**)
4. På din PC: ping robotten for at bekræfte forbindelsen ✅
5. På robotten: gå til
   **Installation → Fieldbus → Modbus**

   * Indtast Siemens PLC’ens IP (fx `192.168.0.2`)
6. Tryk **Add New Signal** og opret et signal:

### ➕ Signal opsætning (UR → PLC)

* **Type:** Digital Output *(skriver til coils i PLC’en)*
* **Address:** 0 *(coil 0)*
* **Name:** `Coil_0`

7. Gem installationen og start robotprogrammet ▶️

✅ **Mål:** UR kan nu sende en Modbus-kommando til PLC’en og sætte **coil 0**.

---

# ✅ 2) Del B – Opsæt Siemens PLC som Modbus TCP Server 🧠🌐

> 🎯 PLC’en skal “lytte” som server på **port 502** og tage imod skriverier fra UR-clienten.

### 🛠️ Opgave (trin-for-trin)

1. Åbn **TIA Portal** og opret et nyt projekt.
2. Tilføj en **S7-1200 eller S7-1500** (PLC_1).
3. Gå til **OB1**.
4. Indsæt blokken **MB_SERVER** i OB1.
5. Opret en ny datablok: **`mb_server_db`** med følgende:

#### 📦 Variabler i `mb_server_db`

* `disconnect` (BOOL)
* `mb_holding` : ARRAY [0..9] OF WORD
* `connection` (TCON_IP_V4)

  * **Interface:** 64
  * **ID:** 1 (unik)
  * **ConnectionType:** 11 (TCP)
  * **RemoteAddress:**

    * **IP:** tom *(accepter alle clients)*
    * **RemotePort:** tom
  * **LocalPort:** 502 *(Modbus standard)*
* `NDR` (BOOL)
* `DR` (BOOL)
* `Error` (BOOL)
* `Status` (WORD)

6. Sæt PLC’ens IP:
   **Properties → Communication → Profinet Interface → Ethernet addresses**

   * IP skal matche den IP du bruger på UR-siden (fx `192.168.0.2`)
7. Download som **Hardware download** og start PLC’en ▶️

---

# 🧪 Test & verifikation (det fede øjeblik 😄) ✅

8. Åbn **`mb_server_db`** online og overvåg fx:

* `mb_holding[0]`

9. På UR: Aktivér “value”/output for signalet `Coil_0`
   ➡️ Du bør se at PLC’en reagerer, og at data/bit bliver sat (fx `mb_holding[0]` går til 1) 🔁

✅ **Succes-kriterie:** Når UR skriver til **coil 0**, kan du se det afspejlet i PLC’ens Modbus-data.

---

## 🧯 Hurtig fejlfinding (hvis det ikke virker)

* ✅ Kan Windows pinge robotten?
* ✅ Kan robotten pinge PLC/PC? (samme subnet)
* ✅ Bruger PLC’en port **502**?
* ✅ Har du den rigtige PLC-IP i UR Modbus-menuen?
* ✅ Er MB_SERVER faktisk aktiv i OB1 (og PLC’en i RUN)?