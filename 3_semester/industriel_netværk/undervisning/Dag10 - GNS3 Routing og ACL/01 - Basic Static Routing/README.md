# Opgave 1: Grundlæggende statisk routing - 3 netværkszoner

## 🎯 Formål

Opbyg et typisk 3-lags industrinetværk med statisk routing mellem IT-zone, DMZ og OT-zone.

---

## 📋 Opgavebeskrivelse

Du skal bygge følgende netværk i GNS3:

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│   IT-Zone       │         │   DMZ           │         │   OT-Zone       │
│   (Kontor)      │         │   (SCADA/HMI)   │         │   (PLC'er)      │
│                 │         │                 │         │                 │
│  PC-IT          │         │  SCADA-Server   │         │  PC-OT          │
│  192.168.1.10   │         │  10.10.0.10     │         │  10.20.0.10     │
│                 │         │                 │         │                 │
└────────┬────────┘         └────────┬────────┘         └────────┬────────┘
         │                           │                           │
    192.168.1.1                  10.10.0.1                   10.20.0.1
         │                           │                           │
         └───────────┬───────────────┴───────────┬───────────────┘
                     │                           │
                     │      Router (Alpine)      │
                     │                           │
                eth0 │        eth1               │ eth2
            192.168.1.1    10.10.0.1         10.20.0.1
```

---

## 🔧 Trin-for-trin implementering

### Trin 1: Opret topologi i GNS3

1. **Opret komponenter:**
   - 1x Alpine Linux (Router)
   - 3x VPCS (PC-IT, SCADA-Server, PC-OT)

2. **Forbind:**
   - Router eth0 ↔ PC-IT
   - Router eth1 ↔ SCADA-Server  
   - Router eth2 ↔ PC-OT

### Trin 2: Konfigurer routeren

```bash
# Start routeren og log ind
# Sæt IP-adresser på de 3 interfaces

ip addr add 192.168.1.1/24 dev eth0
ip addr add 10.10.0.1/16 dev eth1
ip addr add 10.20.0.1/16 dev eth2

ip link set eth0 up
ip link set eth1 up
ip link set eth2 up

# Aktivér IP forwarding (routing)
sysctl -w net.ipv4.ip_forward=1

# Vis routing-tabel
ip route show
```

**Spørgsmål til refleksion:**
- Hvilke routes er automatisk tilføjet? Hvorfor?
- Hvad betyder "dev eth0 proto kernel scope link"?

### Trin 3: Konfigurer PC-IT (VPCS)

```bash
# I VPCS konsollen for PC-IT
ip 192.168.1.10/24 192.168.1.1

# Test forbindelse til routeren
ping 192.168.1.1

# Vis route table
show ip
```

### Trin 4: Konfigurer SCADA-Server (VPCS)

```bash
# I VPCS konsollen for SCADA
ip 10.10.0.10/16 10.10.0.1

# Test forbindelse til routeren
ping 10.10.0.1
```

### Trin 5: Konfigurer PC-OT (VPCS)

```bash
# I VPCS konsollen for PC-OT
ip 10.20.0.10/16 10.20.0.1

# Test forbindelse til routeren
ping 10.20.0.1
```

### Trin 6: Test kommunikation mellem zoner

```bash
# På PC-IT - test til DMZ og OT
ping 10.10.0.10
ping 10.20.0.10

# På SCADA-Server - test til IT og OT
ping 192.168.1.10
ping 10.20.0.10

# På PC-OT - test til IT og DMZ
ping 192.168.1.10
ping 10.10.0.10
```

**Hvis ping fejler** - tjek på routeren:

```bash
# På routeren - se routing-tabel
ip route show

# Test ICMP forwarding
tcpdump -i eth0 icmp
# (kør ping fra PC-IT mens tcpdump kører)
```

---

## 📊 Dokumentationskrav

Lav en `.md`-fil med følgende:

### 1. Netværksdiagram
- Tegn topologien med alle IP-adresser
- Markér routing-interfaces

### 2. Routing-tabel fra routeren

Kør `ip route show` og indsæt output:

```
[Indsæt din routing-tabel her]
```

**Forklar hver linje:**
- Hvad betyder "10.10.0.0/16 dev eth1"?
- Hvad er forskellen på "proto kernel" og "proto static"?

### 3. Test-resultater

For hver kombination af ping-tests:

| Fra          | Til           | Resultat | RTT (ms) | Forklaring |
|--------------|---------------|----------|----------|------------|
| PC-IT        | SCADA-Server  | ✅/❌    |          |            |
| PC-IT        | PC-OT         | ✅/❌    |          |            |
| SCADA-Server | PC-IT         | ✅/❌    |          |            |
| SCADA-Server | PC-OT         | ✅/❌    |          |            |
| PC-OT        | PC-IT         | ✅/❌    |          |            |
| PC-OT        | SCADA-Server  | ✅/❌    |          |            |

### 4. Pakke-flow analyse

Vælg én vellykket ping (f.eks. PC-IT → PC-OT) og forklar:

1. **ICMP Echo Request:**
   - Afsender: `192.168.1.10`
   - Modtager: `10.20.0.10`
   - Pakken ankommer til routerens eth0
   - Router ser i routing-tabel: `10.20.0.0/16 dev eth2`
   - Router videresender via eth2

2. **ICMP Echo Reply:**
   - [Beskriv returvejen]

---

## 🤔 Refleksionsspørgsmål

1. **Hvorfor bruges statiske IP-adresser i stedet for DHCP i dette setup?**

2. **Hvad sker der hvis du glemmer at aktivere `ip_forward` på routeren?**

3. **Forestil dig at PC-OT er en PLC. Hvorfor er det kritisk at den har en fast IP?**

4. **Hvad betyder det at routeren er en "single point of failure" i dette netværk?**

5. **I et rigtigt industrinetværk - ville du tillade direkte kommunikation mellem IT-zone og OT-zone? Hvorfor/hvorfor ikke?**

---

## 🎯 Ekstra udfordringer

### Udfordring 1: Tilføj firewall-regler

Tillad kun:
- IT-zone → DMZ (ping)
- DMZ → OT-zone (ping)
- Bloker IT-zone → OT-zone (direkte)

```bash
# Hint: Brug nftables på routeren
nft add rule inet filter forward ip saddr 192.168.1.0/24 ip daddr 10.20.0.0/16 drop
```

### Udfordring 2: Tilføj mere OT-udstyr

Tilføj endnu en VPCS som simulerer en PLC:
- PLC: `10.20.0.20/16`
- Test kommunikation fra SCADA til PLC

### Udfordring 3: Implementér logging

Log alle ICMP-pakker der routes:

```bash
# Hint: nftables med log
nft add rule inet filter forward ip protocol icmp log prefix \"ICMP-ROUTED: \"
```

---

## ✅ Checklist før aflevering

- [ ] GNS3 topologi kører og alle enheder kan pingge hinanden
- [ ] Netværksdiagram tegnet og uploadet
- [ ] Routing-tabel fra router dokumenteret og forklaret
- [ ] Ping-test tabel udfyldt med alle resultater
- [ ] Pakke-flow analyseret for mindst én ping
- [ ] Refleksionsspørgsmål besvaret
- [ ] Screenshots af vellykket ping mellem alle zoner
- [ ] Fil uploadet til GitHub i `dag10-ditnavn/opgave1.md`

---

**Held og lykke! Dette er fundamentet for industriel netværksarkitektur! 🏭**
