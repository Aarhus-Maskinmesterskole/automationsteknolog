# Opgave 04: Node-RED som Modbus Client til S7-1200 og S7-1500

**AAMS - Industrielt Netværk**  
**Underviser:** Anders S. Østergaard  
**Dato:** 2. september 2025

## Mål
Node-RED læser data fra to PLC servere og viser det i et simpelt dashboard.

## Topologi
```
S7-1200 (Server) - Switch - PC (Node-RED Client) - S7-1500 (Server)
```

## IP Adresser
| Enhed | IP Adresse |
|-------|------------|
| S7-1200 | 192.168.1.10 |
| PC (Node-RED) | 192.168.1.11 |
| S7-1500 PLCsim | 192.168.1.12 |

Alle bruger subnet mask: 255.255.255.0

## S7-1200 Opsætning (Modbus Server)

### TIA Portal Konfiguration
```
1. Opret projekt: "PLC1200_Server"
2. Tilføj S7-1200 CPU
3. Ethernet interface:
   - IP: 192.168.1.10
   - Subnet: 255.255.255.0
4. Device Configuration → Protection & Security:
   - PUT/GET communication: AKTIVER
5. Opret DB100 "StationData":
   - DB100.DBW0 (INT): Temperatur (værdi: 25)
   - DB100.DBW2 (INT): Tryk (værdi: 1013)
   - DB100.DBX4.0 (BOOL): Pumpe status (værdi: TRUE)
6. Download til fysisk PLC
```

## S7-1500 Opsætning (Modbus Server)

### PLCsim Advanced
```
1. Start PLCsim Advanced
2. Opret virtuel S7-1500
3. IP: 192.168.1.12
4. Start virtuel PLC
```

### TIA Portal S7-1500 Projekt
```
1. Opret projekt: "PLC1500_Server"
2. Ethernet interface:
   - IP: 192.168.1.12
   - Subnet: 255.255.255.0
3. Device Configuration → Protection & Security:
   - PUT/GET communication: AKTIVER
4. Opret DB200 "ProcessData":
   - DB200.DBW0 (INT): Flow rate (værdi: 150)
   - DB200.DBW2 (INT): Level (værdi: 75)
   - DB200.DBX4.0 (BOOL): Alarm (værdi: FALSE)
5. Download til PLCsim Advanced
```

## Node-RED Installation

### Installation på PC
```bash
1. Download og installer Node.js fra nodejs.org
2. Åbn Command Prompt som Administrator
3. Installer Node-RED:
   npm install -g node-red
4. Installer Modbus palette:
   npm install -g node-red-contrib-modbus
5. Start Node-RED:
   node-red
6. Åbn browser: http://localhost:1880
```

## Node-RED Flow Konfiguration

### Modbus Read Nodes
```
Flow 1: Læs S7-1200 data
1. Træk "Modbus Read" node til workspace
2. Dobbeltklik for konfiguration:
   - Name: "Read PLC1200"
   - Server: Opret ny server
     * Host: 192.168.1.10
     * Port: 502
     * Unit ID: 1
   - FC: Read Holding Registers (3)
   - Address: 0
   - Quantity: 3
3. Tilføj "Debug" node og forbind

Flow 2: Læs S7-1500 data
1. Træk ny "Modbus Read" node
2. Konfiguration:
   - Name: "Read PLC1500"
   - Server: Opret ny server
     * Host: 192.168.1.12
     * Port: 502
     * Unit ID: 1
   - FC: Read Holding Registers (3)
   - Address: 0
   - Quantity: 3
3. Tilføj "Debug" node og forbind
```

### Timer Trigger
```
1. Træk "Inject" node til workspace
2. Konfiguration:
   - Repeat: interval
   - Every: 5 seconds
3. Forbind til begge Modbus Read nodes
```

### Data Processing
```javascript
1. Træk "Function
