# Profibus Decentral I/O med Siemens S7-1200
**Læringsmål:** I denne opgave lærer du at opsætte en Profibus DP decentral I/O station med Siemens S7-1200 PLC.

---

Video kan følges her: [https://www.youtube.com/watch?v=oTKpon7wkMo](https://www.youtube.com/watch?v=oTKpon7wkMo)

OBS! Når i følger videoen så brug egen IP-adresse og ikke de i videoen, da det kan skabe konflikter hvis flere bruger samme IP-adresse eller jeres netværk ligger i et andet subnet. Hvis i er i tvivl om jeres IP-adresse så kan i finde den ved at åbne en terminal og skrive `ipconfig` (Windows) eller `ifconfig` (Linux/Mac). Kig efter den IP-adresse der er tilknyttet jeres Ethernet adapter. Den vil typisk starte med 192.168.x.x eller 10.x.x.x.

Ved profibus DP er det vigtigt at have styr på master/slave konfigurationen. I denne opgave vil S7-1200 fungere som master og en decentral I/O station (f.eks. ET 200SP) vil fungere som slave. Vi vil konfigurere kommunikationen mellem disse enheder og læse/skrivere data til de digitale moduler i den decentrale I/O station.

Husk terminering i Profibus connector skal stå til `ON` på den sidste og første enhed i netværket.

---

## 1) Del A – Opsætning af Profibus DP i TIA Portal
### Opgave
1. Åbn TIA Portal og opret et nyt projekt.
2. Tilføj en S7-1215 (AC/DC/RLY) PLC til projektet.
3. Gå til Device Configuration.
4. Tilføj CM 1243-5 til projektet.
5. Tilføj en ET 200SP DP station (6ES7-151-1AA05-0AB0) til projektet.
    - Tilføj et digitalt modul (6ES7-138-4CA01-0AA0) til ET 200SP stationen.
    - Tilføj et digitalt modul (6ES7-132-4bb01-0ab0) til ET 200SP stationen.
    - Tilføj et digitalt modul (6ES7-134-4nb51-0ab0) til ET 200SP stationen.
6. Konfigurer ET 200SP stationen til at have slave adresse 3 på Profibus netværket.

### 2) Del B – Opret OB1 program til at læse/skrivere data
1. Gå til OB1.
2. Opret et simpelt program der gør som følger:
    - Opret 2 memory bits (f.eks. M0.0 og M0.1) i PLC'en.
    - Skriv et program der sætter M0.0 (`NO`), M0.1 (`NC`), Q2.0 som coil og Q2.0 som selvhold (`NO`) over M0.0
      M0.0    M0.1    Q2.0
      ---||------|/|------( )---
      ---||---|
3. Download programmet til PLC'en og start PLC'en.
4. Brug Watch Table til at overvåge M0.0, M0.1 og Q2.0 og se hvordan de ændrer sig i forhold til hinanden.