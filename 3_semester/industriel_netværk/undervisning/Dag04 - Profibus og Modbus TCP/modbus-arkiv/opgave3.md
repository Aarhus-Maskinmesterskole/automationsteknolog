# Opgave 03: Simpel Modbus TCP - S7-1200 og PLCsim Advanced

**AAMS - Industrielt Netværk**  
**Underviser:** Anders S. Østergaard  
**Dato:** 2. september 2025

## Mål
Få en fysisk S7-1200 til at kommunikere med PLCsim Advanced S7-1500 via Modbus TCP.

## Hardware Setup
```
S7-1200 (fysisk) - Switch - PC - PLCsim Advanced S7-1500
```

## IP Adresser
| Enhed | IP Adresse |
|-------|------------|
| S7-1200 | 192.168.1.10 |
| PC | 192.168.1.11 |
| S7-1500 (PLCsim) | 192.168.1.12 |

Alle bruger subnet mask: 255.255.255.0

## S7-1200 Opsætning (Server)

### TIA Portal
```
1. Opret nyt projekt
2. Tilføj S7-1200 CPU
3. Ethernet interface:
   - IP: 192.168.1.10
   - Subnet: 255.255.255.0
4. Device Configuration → Protection & Security:
   - PUT/GET communication: AKTIVER
5. Opret DB10:
   - DB10.DBW0 (INT): Værdi 1234
   - DB10.DBW2 (INT): Værdi 5678
6. Download til PLC
```

## PLCsim Advanced Opsætning

### Start PLCsim Advanced
```
1. Start PLCsim Advanced
2. Opret ny virtuel PLC
3. Vælg S7-1500 CPU
4. Netværk:
   - IP: 192.168.1.12
   - Subnet: 255.255.255.0
5. Start virtuel PLC
```

### TIA Portal S7-1500 Projekt
```
1. Opret nyt projekt for S7-1500
2. Ethernet interface:
   - IP: 192.168.1.12
   - Subnet: 255.255.255.0
3. Tilføj Modbus TCP instruction
4. Opret DB20 til modtagne data
5. Download til PLCsim Advanced
```

## Modbus Konfiguration

### S7-1500 Program (Main OB1)
```
Network 1: Modbus Client
- MB_CLIENT function block
- IP: '192.168.1.10'
- Port: 502
- Læs 2 holding registers fra adresse 0
- Gem data i DB20
```

## Test

### Ping Test
```bash
# Fra PC:
ping 192.168.1.10    # S7-1200
ping 192.168.1.12    # S7-1500 PLCsim
```

### Verifikation
```
1. Online monitor på S7-1200: DB10.DBW0 = 1234
2. Online monitor på S7-1500: DB20 skal vise samme værdier
3. Ændr værdi i S7-1200 DB10
4. Verificer opdatering i S7-1500 DB20
```

## Fejlsøgning
- Ping virker ikke: Check kabler og IP adresser
- Modbus fejl: Verificer PUT/GET er aktiveret på S7-1200
- PLCsim kan ikke pinges: Check Windows firewall

**Succes kriterie:** S7-1500 læser data fra S7-1200 via Modbus TCP.
