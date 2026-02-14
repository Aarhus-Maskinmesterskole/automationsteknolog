# Universal Robots Modbus TCP Client
**Læringsmål:** I denne opgave lærer du at opsætte en Universal Robots som Modbus TCP klient.

---

Video kan følges her: [https://www.youtube.com/watch?v=xu8TcCQ1nGo](https://www.youtube.com/watch?v=xu8TcCQ1nGo)

OBS! Når i følger videoen så brug egen IP-adresse og ikke de i videoen, da det kan skabe konflikter hvis flere bruger samme IP-adresse eller jeres netværk ligger i et andet subnet. Hvis i er i tvivl om jeres IP-adresse så kan i finde den ved at åbne en terminal og skrive `ipconfig` (Windows) eller `ifconfig` (Linux/Mac). Kig efter den IP-adresse der er tilknyttet jeres Ethernet adapter. Den vil typisk starte med 192.168.x.x eller 10.x.x.x. Sørg for at windows kan pinge robotten og at robotten kan pinge windows for at sikre at de er på samme netværk. For at finde IP-adressen på Universal Robots simulatoren så tryk på nederste knap på venstre side i Lubuntu for at finde teraterm og skriv ip a.

---

## 1) Del A – Opsætning af Universal Robots som Modbus TCP Client
### Opgave
1. Åben VMware og start Universal Robots simulatoren.
2. Log ind på simulatoren og til de tre streger over hinanden i øverste højre hjørne.
3. Vælge "System" -> "Netværk" og find dens IP-adresse (den skal være sat til DHCP).
4. Åben en terminal på din computer og ping robotten for at sikre at den er forbundet til netværket.
5. Navigér til "Installation" -> "Fieldbus" -> "Modbus" sæt IP-adressen på Siemens PLC'en (f.eks. 192.168.0.2).
6. Tryk Add New Signal og opret et signal med følgende indstillinger:
   - Type: Digital Output (for at skrive til coils i PLC'en)
   - Address: 0 (for at skrive til coil 0 i PLC'en)
   - Name: "Coil_0"
7. Gem og start programmet på robotten.

## 2) Del B – Opret Siemens PLC program til at modtage Modbus TCP Server data
### Opgave
1. Åbn TIA Portal og opret et nyt projekt.
2. Tilføj en S7-1200 eller S7-1500 PLC til projektet.
3. Gå til OB1.
4. Indsæt blokken MB_SERVER i OB1.
5. Opret en ny datablok med navnet mb_server_db.
   - Indsæt følgende variabler i datablokken:
     - `disconnect` (BOOL)
     - `mb_holding` som array [0..9] of (WORD)
     - `connection` (TCON_IP_V4)
         - Interface: 64 (PLC interface)
         - ID: Unik ID (f.eks. 1)
         - ConnectionType: 11 (for TCP)
         - Remoteaddress:
                - IP: Blank fordi vi ønsker at acceptere alle forbindelser
                - RemotePort: blank
                - LocalPort: 502 (standard Modbus TCP port)
    - NDR: BOOL
    - DR: BOOL
    - Error: BOOL
    - Status: WORD
6. Tryk properties på PLC_1 og gå til "Communication" → "Profinet Interface" → "Ethernet addresses" og sæt en statisk IP-adresse til samme som i step 5.
7. Download programmet til PLC'en som Hardware download og start PLC'en.
8. Åben db_server_db og overvåg `mb_holding[0]` mens du starter programmet på robotten. Du skulle gerne se at `mb_holding[0]` bliver sat til 1, når robotten skriver til coil 0 i PLC'en ved at aktivere "value" i Universal Robots.