# Opgave 1: Node-RED + ModRSSIM v2 via `node-red-contrib-modbustcp`

Formålet: du skal lære at **sætte coils og registre** i ModRSSIM (server) fra Node-RED (client) — med den simple modbustcp-palette.

---

## 1) Forbered ModRSSIM v2

1. Start **ModRSSIM v2**.
2. Vælg **TCP Server**.
3. Indstil:

   * **IP:** `127.0.0.1` (eller din lokale LAN-adresse)
   * **Port:** `502` (standard Modbus TCP-port) 
   * **Slave ID:** `1` (typisk standard)
4. Opret lidt testdata:

   * **Coils**: adresser `0–7` sat til `0`.
   * **Holding Registers**: adresser `0–3` sat til `0`.
5. Husk at ModRSSIM viser "menneskeadresser" (00001, 40001).
   I Node-RED skriver vi dem 0-baseret (altså coil 0 ↔ 00001).

---

## 2) Installer og forbered Node-RED

1. Åbn Node-RED.
2. Menu → *Manage palette* → *Install* → søg efter
   `node-red-contrib-modbustcp` → **Install**.
3. Du får nu noder som:

   * **modbus read**
   * **modbus write**
   * **modbus response**

---

## 3) Skriv til en coil

1. Træk en **Inject**-node ind.
2. Træk en **modbus write**-node ind.
3. Forbind dem sammen.
4. Dobbeltklik på **modbus write**:

   * **Server**: `127.0.0.1`
   * **Port**: `502`
   * **Slave ID**: `1`
   * **Function**: `Coil (FC5)`
   * **Address**: `0`
   * **Quantity**: `1`
5. Dobbeltklik på **Inject**:

   * Payload-type: **boolean**
   * Payload: `true`
6. Tryk **Deploy** og klik på Inject.
7. I ModRSSIM skal coil 0 nu vise **ON (1)**.
   Prøv at skifte payload til `false` og tjek, at den går OFF igen.

---

## 4) Skriv flere coils på én gang

1. Lav en ny **modbus write**-node.
2. Vælg:

   * **Function**: `Multiple Coils (FC15)`
   * **Address**: `0`
   * **Quantity**: `4`
3. Lav en Inject-node med payload-type **array** og indsæt fx:

   ```
   [true, false, true, true]
   ```
4. Forbind og Deploy.
   ModRSSIM viser nu coil 0 = 1, 1 = 0, 2 = 1, 3 = 1.

---

## 5) Skriv til holding registers

1. Træk ny **modbus write**-node ind.
2. Indstil:

   * **Function:** `Holding Register (FC6)`
   * **Address:** `0`
   * **Quantity:** `1`
3. Tilføj en **Inject** med payload-type **number**, fx `1234`.
4. Deploy, klik, og adresse 40001 i ModRSSIM skal nu vise `1234`.

Vil du skrive flere ad gangen:

* Funktion: `Multiple Registers (FC16)`
* Quantity: `3`
* Inject payload som array:

  ```
  [10, 20, 30]
  ```

---

## 6) Læs værdier (coils og registre)

1. Træk en **modbus read**-node ind.
2. Dobbeltklik:

   * **Server:** samme IP/port/slave
   * **Function:** `Read Coils (FC1)`
   * **Address:** `0`
   * **Quantity:** `8`
   * **Interval:** `2` sekunder (for automatisk polling).
3. Tilføj en **debug**-node til output.
4. Deploy – du ser nu coil-tilstandene som array af `true/false`.

Gentag med en anden modbus read-node:

* **Function:** `Read Holding Registers (FC3)`
* **Quantity:** `3`
* Debug viser 16-bit heltal som `[1234, 0, 0]` fx.

---

## 7) Fejlfinding

* **Ingen forbindelse:**
  Tjek at ModRSSIM er startet og port 1502 er åben.
* **Forkert adresse:**
  Husk at Node-RED bruger 0-baseret adressering.
* **Unit ID mismatch:**
  Skal være samme i begge programmer (1).
* **Typefejl:**
  Brug boolean til coils, tal/array til registre.

---

## 8) Refleksion

Med denne palette får du et **klart én-til-én forhold** mellem Modbus-funktion og node.
Du har nu lært at:

* Skrive enkelt bits (FC5) og flere (FC15).
* Skrive enkelt registre (FC6) og flere (FC16).
* Læse coils (FC1) og holding registers (FC3).