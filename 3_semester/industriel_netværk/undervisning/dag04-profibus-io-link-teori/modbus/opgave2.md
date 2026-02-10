# Opgave 02: Modbus TCP mellem S7-1200 og PLCsim

**AAMS - Industrielt Netværk**  
**Underviser:** Anders S. Østergaard  
**Dato:** 2. september 2025

## Mål
Etabler Modbus TCP kommunikation mellem fysisk S7-1200 (server) og PLCsim S7-1200 (client).

## Topologi
```
S7-1200 (fysisk server) - Switch - PC - PLCsim S7-1200 (virtual client)
```

## IP Adresser
| Enhed | IP Adresse | Subnet Mask |
|-------|------------|-------------|
| S7-1200 (fysisk) | 192.168.1.10 | 255.255.255.0 (/24) |
| PC | 192.168.1.11 | 255.255.255.0 (/24) |
| S7-1200 (PLCsim) | 192.168.1.12 | 255.255.255.0 (/24) |

## Fysisk S7-1200 - Server Opsætning

### TIA Portal Konfiguration
```
1. Opret projekt: "Physical_PLC_Server"
2. Tilføj S7-1200 CPU
3. Ethernet interface:
   - IP: 192.168.1.10
   - Subnet: 255.255.255.0
4. Device Configuration → Protection & Security:
   - PUT/GET communication: AKTIVER
5. Opret DB100 "ProductionData":
   - DB100.DBW0 (INT): Temperature (værdi: 25)
   - DB100.DBW2 (INT): Pressure (værdi: 1013)
   - DB100.DBW4 (INT): Status (værdi: 1)
6. Download til fysisk PLC
```

## PLCsim S7-1200 - Client Opsætning

### PLCsim Konfiguration
```
1. Start PLCsim
2. Opret virtuel S7-1200
3. Netværk konfiguration:
   - Ethernet adapter: PLCsim Virtual Ethernet Adapter
   - IP: 192.168.1.12
   - Subnet: 255.255.255.0
4. Start simulation
```

### TIA Portal Virtual PLC Projekt
```
1. Opret projekt: "PLCsim_Client"
2. Tilføj S7-1200 CPU (samme type som PLCsim)
3. Ethernet interface:
   - IP: 192.168.1.12
   - Subnet: 255.255.255.0
4. Tilføj Modbus TCP instruction
5. Opret DB200 "ReceivedData"
6. Download til PLCsim
```

### Client Program (Main OB1)
```
Network 1: Modbus TCP Client
- MB_CLIENT function block
- Konfiguration:
  * REQ := Clock_1Hz (læs hvert sekund)
  * MB_MODE := 1 (Read Holding Registers)
  * MB_DATA_ADDR := 0
  * MB_DATA_LEN := 3
  * CONNECT.RemoteAddress := '192.168.1.10'
  * CONNECT.RemotePort := 502
  * MB_DATA_PTR := P#DB200.DBX0.0 BYTE 6
```

## Modbus Register Mapping
| Modbus Address | Fysisk PLC Address | Data Type | Beskrivelse |
|----------------|-------------------|-----------|-------------|
| 40001 | DB100.DBW0 | INT | Temperature (25°C) |
| 40002 | DB100.DBW2 | INT | Pressure (1013 mbar) |
| 40003 | DB100.DBW4 | INT | Status bits |

## Test og Verifikation

### Netværks Test
```bash
# Fra PC (192.168.1.11):
ping 192.168.1.10    # Fysisk PLC
ping 192.168.1.12    # PLCsim virtual PLC

# Test Modbus connectivity
telnet 192.168.1.10 502
```

### PLCsim Test
```
1. Verificer PLCsim network adapter i Windows
2. Test at PLCsim kan ping physical PLC
3. Check at virtual PLC går online i TIA Portal
```

### Data Verifikation
```
1. Online monitor fysisk PLC:
   - DB100.DBW0 = 25
   - DB100.DBW2 = 1013
   - DB100.DBW4 = 1

2. Online monitor PLCsim:
   - DB200.DBW0 skal vise 25
   - DB200.DBW2 skal vise 1013
   - DB200.DBW4 skal vise 1

3. Ændr værdi på fysisk PLC og verificer opdatering i PLCsim
```

## Fejlsøgning
- **PLCsim kan ikke pinges:** Check virtual Ethernet adapter i Windows
- **Fysisk PLC ikke tilgængelig:** Verificer netværkskabel og switch
- **Modbus timeout:** Check Windows firewall indstillinger
- **Data ikke opdateret:** Verificer MB_CLIENT ERROR og STATUS bits

**Succes kriterie:** PLCsim læser live data fra fysisk S7-1200 via Modbus TCP.
