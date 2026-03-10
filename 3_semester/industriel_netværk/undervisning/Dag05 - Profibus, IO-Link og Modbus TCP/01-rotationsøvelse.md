# AAMS – Rotationsøvelser
## Industriel Kommunikation: Profibus, Modbus TCP, IO-Link og Emulate 3D

**Underviser:** Anders S. Østergaard

---

## Generelle Instruktioner

**Vigtigt:** Der er kun ét sæt Profibus- og IO-Link-udstyr tilgængeligt. Vær derfor effektive ved Profibus-stationerne og giv straks plads til næste gruppe, når I er færdige.

**Formål:** Alle øvelser fokuserer på konfiguration og opsætning. Der skal IKKE programmeres – kun konfigureres (dog skal et mindre program fremgå i **Del 4**).

**Dokumentation:** Dokumentér jeres opsætning kort efter hver øvelse.

**Rotation:** Grupper roterer mellem stationerne.

---

## Del 1: Profibus S7-1500 og Decentral IO

**Varighed:** 30 minutter  
**Udstyr:** S7-1500 PLC, Decentral IO-enhed, Profibus-kabel  
**Reference:** [YouTube – Profibus S7-1500 decentral IO](https://www.youtube.com/watch?v=oTKpon7wkMo)

### Opgave

Konfigurér Profibus-kommunikation mellem S7-1500 og en decentral IO-enhed.

### Trin

1. Åbn TIA Portal og opret nyt projekt
2. Tilføj S7-1500 PLC til projektet
3. Konfigurér Profibus DP-interface på PLC'en
4. Tilføj decentral IO-enhed til Profibus-netværket
5. Indstil Profibus-adresse for IO-enheden (TIA Portal)
6. Indstil Profibus-adresse på IO-enheden (hardware)
7. Upload konfiguration til PLC'en
8. Test forbindelsen ved at kontrollere diagnosticering
9. Verificér I/O-mapping i Online & Diagnostics

### Dokumentation

- Screenshot af Profibus-konfiguration i TIA Portal
- Notér Profibus-adresser brugt
- Diagnosticsresultater (OK/fejl)
- Eventuelle fejl og løsninger

---

## Del 2: Profibus S7-1500 til S7-1500

**Varighed:** 30 minutter  
**Udstyr:** 2 × S7-1500 PLC, Profibus-kabel  
**Reference:** [YouTube – Profibus S7-1500 til S7-1500](https://www.youtube.com/watch?v=OCbpnXw5ZGE)

### Opgave

Opsæt Profibus-kommunikation mellem to S7-1500 PLC'er.

### Trin

1. Konfigurér den første PLC som Profibus DP-master
2. Konfigurér den anden PLC som Profibus DP-slave
3. Indstil forskellige Profibus-adresser (fx Master: 2, Slave: 3)
4. Definer dataudveksling mellem PLC'erne
5. Upload konfiguration til begge PLC'er
6. Test kommunikation ved at sende data fra master til slave
7. Verificér modtagelse af data på slave-siden

### Dokumentation

- Profibus-topologi diagram
- Screenshot af konfiguration på begge PLC'er
- Test af dataudveksling
- Noter om eventuelle udfordringer

> **HUSK:** Frigør stationen når I er færdige!

---

## Del 3: Modbus TCP mellem to Siemens PLC'er

**Varighed:** 45 minutter  
**Udstyr:** 2 × S7-1500 PLC, Ethernet-kabler, switch  
**Reference:** [YouTube – Modbus TCP PLC til PLC](https://www.youtube.com/watch?v=3k7vggo7ltQ)

### Opgave

Etabler Modbus TCP-kommunikation mellem to Siemens PLC'er.

### Trin

1. Tilslut begge PLC'er til samme Ethernet-netværk
2. Indstil IP-adresser på begge PLC'er (fx 192.168.1.10 og 192.168.1.11)
3. Konfigurér den første PLC som Modbus TCP-client
4. Konfigurér den anden PLC som Modbus TCP-server
5. Opsæt Modbus TCP-instruktioner (MB_CLIENT og MB_SERVER)
6. Definer hvilke data der skal udveksles (holding registers)
7. Test kommunikationen
8. Verificér dataudveksling gennem Online & Diagnostics

### Dokumentation

- Netværksdiagram med IP-adresser
- Screenshot af Modbus TCP-konfiguration
- Dokumentation af register-mapping
- Testresultater

---

## Del 4: Modbus TCP (Emulate 3D) & S7-1500

**Varighed:** 45 minutter  
**Udstyr:** S7-1500 PLC, PC med Emulate 3D  
**Reference:** [YouTube – Modbus TCP med Emulate3D](https://www.youtube.com/watch?v=WTjcJUzEBSk)

### Opgave

Opsæt Modbus TCP-kommunikation mellem Emulate 3D og S7-1500.

### Trin

1. Start Emulate 3D på PC'en
2. Konfigurér S7-1500 som Modbus TCP-server
3. Indstil IP-adresse på PLC (fx 192.168.1.20)
4. Konfigurér Emulate 3D til at forbinde via Modbus TCP
5. Definér register-mapping mellem Emulate 3D og PLC
6. Etabler forbindelse
7. Test kommunikation ved at styre virtuelle I/O fra PLC
8. Verificér at data flows korrekt begge veje
9. Lav et lille program i PLC'en til at læse/skrive data til Emulate 3D transportbånd eller lignende

### Dokumentation

- Screenshot af Emulate 3D-opsætning
- PLC Modbus TCP-konfiguration
- Register-mapping dokumentation
- Test af I/O-styring

---

## Del 5: IO-Link AL1302 Konfiguration

**Varighed:** 30 minutter  
**Udstyr:** S7-1500 PLC, AL1302 IO-Link master, IO-Link sensorer  
**Reference:** [YouTube – IO-Link AL1302 konfiguration](https://www.youtube.com/watch?v=6METqn73cJA)

### Opgave

Konfigurér IO-Link AL1302 med S7-1500 PLC.

### Trin

1. Tilslut AL1302 IO-Link master til PLC via Profinet (fysisk)
2. Indsæt GSD-fil for AL1302 i TIA Portal
3. Konfigurér Profinet-forbindelse i TIA Portal
4. Tilføj AL1302 til hardware-konfiguration
5. Tilslut IO-Link sensorer til AL1302
6. Konfigurér IO-Link porte på AL1302 (enable og disable porte)
7. Upload konfiguration til PLC
8. Test IO-Link kommunikation
9. Læs sensordata gennem IO-Link

> **Hint:** IoT browser IP: 192.168.1.24, Profinet IP: 192.168.1.3

### Dokumentation

- Hardware-forbindelsesdiagram
- Screenshot af AL1302-konfiguration
- IO-Link port-opsætning
- Sensordata-aflæsning

---

## Afslutning og indhold af aflevering

Denne aflevering er individuel, men I kan naturligvis hjælpe hinanden undervejs.

### Hvad har I lært?

- Forskelle mellem Profibus, Ethernet-baseret Modbus TCP og IO-Link
- Konfiguration af industrielle kommunikationsprotokoller
- Praktisk erfaring med Siemens TIA Portal
- Troubleshooting af kommunikationsproblemer
- Dokumentation af tekniske opsætninger

### Refleksionsspørgsmål

1. Hvilken kommunikationstype var nemmest at konfigurere og hvorfor?
2. Hvilke udfordringer stødte I på, og hvordan løste I dem?
3. Hvilke fordele og ulemper så I ved de forskellige protokoller?
4. Hvordan ville I vælge kommunikationsprotokol til et industrielt projekt?

### Aflevering

Upload jeres dokumentation (teoretisk beskrivelse af protokol og opsætning, screenshots, diagrammer, noter).