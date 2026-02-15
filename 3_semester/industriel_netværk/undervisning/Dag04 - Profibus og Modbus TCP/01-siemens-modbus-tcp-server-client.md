# 🔁 Modbus TCP: Server & Client med Siemens S7-1200/1500 (kan simuleres) 🤖🌐

> 🎯 **Læringsmål:** Du træner at opsætte **Modbus TCP Server og Modbus TCP Client** mellem **to Siemens PLC’er** (S7-1200/1500) — og at teste at data flyder korrekt ✅

---

## 🎥 Video-guide

👉 [https://www.youtube.com/watch?v=vc45YuAlQBc](https://www.youtube.com/watch?v=vc45YuAlQBc)

---

## ⚠️ VIGTIGT: IP-adresser (undgå konflikter!) 🧠💥

Når du følger videoen, så brug **dine egne IP-adresser** — ikke dem fra videoen.
Ellers risikerer I konflikter (samme IP) eller at jeres netværk ligger i et andet subnet.

### 🔎 Find din IP-adresse

* **Windows:** `ipconfig`
* **Linux/Mac:** `ifconfig` *(eller `ip a` på Linux)*

📌 Kig efter IP’en på din **Ethernet-adapter**. Den starter typisk med:

* `192.168.x.x` eller
* `10.x.x.x`

---

# ✅ 1) Del A – Opret Modbus TCP Server (PLC_1) 🖥️➡️🌐

### 🛠️ Opgave (trin-for-trin)

1. Åbn **TIA Portal** og opret et **nyt projekt**.
2. Tilføj en **S7-1200 eller S7-1500** (PLC_1).
3. Gå til **OB1**.
4. Indsæt funktionsblokken **MB_SERVER** i OB1.
5. Opret en ny datablok: **`mb_server_db`** og indsæt variabler:

#### 📦 Variabler i `mb_server_db`

* `disconnect` (BOOL)
* `mb_holding` : ARRAY [0..9] OF WORD
* `connection` (TCON_IP_V4)

  * **Interface:** 64 (PLC interface)
  * **ID:** Unik ID (fx 1)
  * **ConnectionType:** 11 (TCP)
  * **RemoteAddress:**

    * **IP:** tom (så serveren accepterer *alle* forbindelser)
    * **RemotePort:** tom
  * **LocalPort:** 502 (standard Modbus TCP port)
* `NDR` (BOOL)
* `DR` (BOOL)
* `Error` (BOOL)
* `Status` (WORD)

6. Sæt IP på PLC_1:
   **Properties → Communication → Profinet Interface → Ethernet addresses**
   fx: `192.168.0.2`
7. Download som **Hardware download** og start PLC’en ▶️

✅ **Mål:** PLC_1 står nu som Modbus TCP server og “udstiller” `mb_holding`.

---

# ✅ 2) Del B – Opret Modbus TCP Client (PLC_2) 🔄📥

### 🛠️ Opgave (trin-for-trin)

1. Opret en ekstra PLC i samme projekt (PLC_2).
2. Gå til **OB1**.
3. Indsæt funktionsblokken **MB_CLIENT** i OB1.
4. Opret datablok: **`mb_client_db`** og indsæt variabler:

#### 📦 Variabler i `mb_client_db`

* `req` (BOOL)
* `disconnect` (BOOL)
* `mb_mode` (USINT) → **0 = read**
* `mb_data_addr` (UDINT) → startadresse (fx `400001` for holding registers)
* `mb_data_len` (UINT)
* `mb_data_ptr` : ARRAY [0..9] OF WORD
* `connect` (BOOL)
* `mb_holding` : ARRAY [0..9] OF WORD

  * `connection` (TCON_IP_V4)

    * **Interface:** 64
    * **ID:** Unik ID (fx 2)
    * **ConnectionType:** 11 (TCP)
    * **RemoteAddress:**

      * **IP:** `192.168.0.2` (serverens IP)
      * **RemotePort:** 502
      * **LocalPort:** tom
* `DONE` (BOOL)
* `BUSY` (BOOL)
* `Error` (BOOL)
* `Status` (WORD)

5. Sæt IP på PLC_2:
   **Properties → Communication → Profinet Interface → Ethernet addresses**
   fx: `192.168.0.3`
6. Download som **Hardware download** og start PLC’en ▶️

✅ **Mål:** PLC_2 læser nu serverens `mb_holding` og placerer data i `mb_data_ptr`.

---

# 🧪 Test & verifikation (skal virke!) ✅🔍

7. Åbn online view og se at **PLC_2 opdaterer `mb_data_ptr`** fra PLC_1.
8. Test ved at ændre værdier i **PLC_1 → `mb_holding`**
   ➜ se at **PLC_2 → `mb_data_ptr`** ændrer sig tilsvarende 🔁

---

## 📝 Mini-tjekliste (hurtig fejlfinding) 🧯

Hvis det ikke virker:

* ✅ Kan du pinge PLC_1 fra netværket?
* ✅ Er begge PLC’er i samme subnet? (fx 192.168.0.xxx/24)
* ✅ Bruger du **port 502**?
* ✅ Er ID’er unikke? (server fx 1, client fx 2)
* ✅ Er `connect/req` sat rigtigt i MB_CLIENT?
