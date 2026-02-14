# Modbus TCP Server og Client med Siemens S7-1200/1500 (kan simuleres)
**Læringsmål:** I denne opgave træner du at oprette en Modbus TCP Server og client imellem 2 Siemens PLC'er.

---

Video kan følges her: [https://www.youtube.com/watch?v=vc45YuAlQBc](https://www.youtube.com/watch?v=vc45YuAlQBc)

OBS! Når i følger videoen så brug egen IP-adresse og ikke de i videoen, da det kan skabe konflikter hvis flere bruger samme IP-adresse eller jeres netværk ligger i et andet subnet. Hvis i er i tvivl om jeres IP-adresse så kan i finde den ved at åbne en terminal og skrive `ipconfig` (Windows) eller `ifconfig` (Linux/Mac). Kig efter den IP-adresse der er tilknyttet jeres Ethernet adapter. Den vil typisk starte med 192.168.x.x eller 10.x.x.x.

---

## 1) Del A – Opret Modbus TCP Server i Siemens PLC
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

6. Tryk properties på PLC_1 og gå til "Communication" → "Profinet Interface" → "Ethernet addresses" og sæt en statisk IP-adresse (f.eks. 192.168.0.2).
7. Download programmet til PLC'en som Hardware download og start PLC'en.

---

## 2) Del B – Opret Modbus TCP Client i Siemens PLC
### Opgave
1. Opret en ny S7-1200 eller S7-1500 PLC i samme projekt.
2. Gå til OB1.
3. Indsæt blokken MB_CLIENT i OB1.
4. Opret en ny datablok med navnet mb_client_db.
   - Indsæt følgende variabler i datablokken:
     - `req` (BOOL)
     - `disconnect` (BOOL)
     - `mb_mode` (USINT) -> 0 for read
     - `mb_data_addr` (UDINT) -> Startadresse for Modbus data (f.eks. 400001 for holding registers)
     - `mb_data_len` (UINT)
     - `mb_data_ptr` som array [0..9] of (WORD)
     - `connect` (BOOL)
     - `mb_holding` som array [0..9] (WORD)
        - `connection` (TCON_IP_V4)
            - Interface: 64 (PLC interface)
            - ID: Unik ID (f.eks. 2)
            - ConnectionType: 11 (for TCP)
            - Remoteaddress:
                - IP: 192.168.0.2 (IP-adressen på server PLC'en)
                - RemotePort: 502
                - LocalPort: blank
     - DONE: BOOL
     - BUSY: BOOL
     - Error: BOOL
     - Status: WORD
5. Tryk properties på PLC_2 og gå til "Communication" → "Profinet Interface" → "Ethernet addresses" og sæt en statisk IP-adresse (f.eks. 192.168.0.3).
6. Download programmet til PLC'en som Hardware download og start PLC'en.
7. Nu skulle PLC_2 kunne læse data fra PLC_1's mb_holding array og vise det i PLC_2's `mb_data_ptr` array.
8. Test ved at ændre værdier i PLC_1's `mb_holding` array og se ændringerne i PLC_2's `mb_data_ptr` array.
