# Statisk Routing - Kommando Reference

Quick reference guide til statisk routing kommandoer i Linux.

---

## 🔧 Grundlæggende IP Konfiguration

### Interface opsætning

```bash
# Tilføj IP-adresse til interface
ip addr add 192.168.1.1/24 dev eth0

# Aktivér interface
ip link set eth0 up

# Deaktivér interface
ip link set eth0 down

# Vis alle interfaces
ip link show

# Vis alle IP-adresser
ip addr show

# Vis specifik interface
ip addr show dev eth0
```

### Fjern IP-adresser

```bash
# Fjern specifik IP
ip addr del 192.168.1.1/24 dev eth0

# Flush alle IP'er på interface
ip addr flush dev eth0
```

---

## 🛤️ Routing Kommandoer

### Vis routing-tabel

```bash
# Moderne kommando
ip route show

# Ældre kommando (samme resultat)
route -n

# Vis routing-tabel i tabel-format
netstat -rn

# Find route til specifik destination
ip route get 10.20.0.10
```

### Tilføj routes

```bash
# Tilføj route til netværk via gateway
ip route add 10.20.0.0/16 via 192.168.1.1

# Tilføj route via specifik interface
ip route add 10.20.0.0/16 dev eth1

# Tilføj default route
ip route add default via 192.168.1.1

# Tilføj route med metric (prioritet)
ip route add 10.20.0.0/16 via 192.168.1.1 metric 100

# Tilføj route til enkelt host
ip route add 10.20.0.50/32 via 192.168.1.1
```

### Slet routes

```bash
# Slet specifik route
ip route del 10.20.0.0/16

# Slet default route
ip route del default

# Slet default route via specifik gateway
ip route del default via 192.168.1.1
```

### Erstat route

```bash
# Erstat eksisterende route
ip route replace 10.20.0.0/16 via 192.168.1.2
```

---

## 🔄 IP Forwarding (Routing aktivering)

### Aktivér routing

```bash
# Aktivér midlertidigt (forsvinder ved reboot)
sysctl -w net.ipv4.ip_forward=1

# Eller via proc filesystem
echo 1 > /proc/sys/net/ipv4/ip_forward

# Tjek om aktiveret (skal returnere 1)
cat /proc/sys/net/ipv4/ip_forward

# Aktivér permanent (Alpine/Debian/Ubuntu)
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
sysctl -p
```

### Deaktivér routing

```bash
sysctl -w net.ipv4.ip_forward=0
```

---

## 🔍 Diagnosticering

### Ping

```bash
# Basis ping
ping 10.20.0.10

# Ping X antal gange
ping -c 4 10.20.0.10

# Ping med interval (0.2 sekunder)
ping -i 0.2 10.20.0.10

# Ping med specifik packet size
ping -s 1400 10.20.0.10

# Ping fra specifik interface
ping -I eth0 10.20.0.10

# Ping med Don't Fragment flag
ping -M do -s 1400 10.20.0.10
```

### Traceroute

```bash
# Trace ruten til destination
traceroute 10.20.0.10

# Med ICMP i stedet for UDP
traceroute -I 10.20.0.10

# Max antal hops
traceroute -m 10 10.20.0.10

# Ingen DNS opslag
traceroute -n 10.20.0.10
```

### Tcpdump

```bash
# Lyt på ICMP på alle interfaces
tcpdump -i any icmp

# Lyt på specifik interface
tcpdump -i eth0

# Vis ICMP uden hostname opslag
tcpdump -i any icmp -n

# Vis med mere detail
tcpdump -i any icmp -v

# Gem til fil
tcpdump -i any icmp -w capture.pcap

# Læs fra fil
tcpdump -r capture.pcap

# Filtrer på IP
tcpdump -i any host 10.20.0.10

# Filtrer på netværk
tcpdump -i any net 10.20.0.0/16
```

### ARP

```bash
# Vis ARP cache
arp -n

# Moderne kommando
ip neigh show

# Vis ARP for specifik interface
ip neigh show dev eth0

# Slet ARP entry
ip neigh del 10.20.0.10 dev eth0

# Flush alle ARP entries
ip neigh flush all
```

---

## 📊 Nyttige Kombinationer

### Komplet router setup (3 zones)

```bash
#!/bin/sh
# Router mellem 3 netværk

# Interfaces
ip addr add 192.168.1.1/24 dev eth0
ip addr add 10.10.0.1/16 dev eth1
ip addr add 10.20.0.1/16 dev eth2

ip link set eth0 up
ip link set eth1 up
ip link set eth2 up

# Aktivér routing
sysctl -w net.ipv4.ip_forward=1

# Routing-tabellen opdateres automatisk med direkte tilkoblede netværk
# Ingen yderligere routes nødvendige for denne simple topologi

# Vis resultat
echo "=== Interfaces ==="
ip addr show

echo "=== Routing table ==="
ip route show
```

### Multi-hop routing setup

```bash
#!/bin/sh
# Router-1: Gateway mellem lokalt netværk og remote sites

# Lokalt interface
ip addr add 192.168.10.1/24 dev eth0
ip link set eth0 up

# Transit interface
ip addr add 10.100.0.1/24 dev eth1
ip link set eth1 up

# Aktivér routing
sysctl -w net.ipv4.ip_forward=1

# Routes til remote sites (via andre routere)
ip route add 10.50.0.0/16 via 10.100.0.2
ip route add 10.60.0.0/16 via 10.100.0.3

# Vis configuration
ip addr show
ip route show
```

### Redundant routing setup

```bash
#!/bin/sh
# Router med primary og backup route

# Interfaces
ip addr add 192.168.10.1/24 dev eth0  # LAN
ip addr add 10.100.0.1/30 dev eth1    # Primary WAN
ip addr add 10.200.0.1/30 dev eth2    # Backup WAN

ip link set eth0 up
ip link set eth1 up
ip link set eth2 up

# Aktivér routing
sysctl -w net.ipv4.ip_forward=1

# Redundante routes (laveste metric vinder)
ip route add 10.50.0.0/16 via 10.100.0.2 metric 10   # Primary
ip route add 10.50.0.0/16 via 10.200.0.2 metric 100  # Backup

# Vis som route bruges
ip route get 10.50.0.10
```

---

## 🧪 Test Scripts

### Kontinuerlig connectivity test

```bash
#!/bin/sh
# Test forbindelse kontinuerligt og log status

TARGET="10.20.0.10"
while true; do
    if ping -c 1 -W 1 $TARGET > /dev/null 2>&1; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') - OK: $TARGET reachable"
    else
        echo "$(date '+%Y-%m-%d %H:%M:%S') - FAIL: $TARGET unreachable"
    fi
    sleep 2
done
```

### Route monitoring

```bash
#!/bin/sh
# Monitor hvilken route der bruges til destination

TARGET="10.50.0.10"
LAST_ROUTE=""

while true; do
    CURRENT_ROUTE=$(ip route get $TARGET | head -n1)
    
    if [ "$CURRENT_ROUTE" != "$LAST_ROUTE" ]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') - ROUTE CHANGED:"
        echo "  $CURRENT_ROUTE"
        LAST_ROUTE="$CURRENT_ROUTE"
    fi
    
    sleep 1
done
```

### Failover test

```bash
#!/bin/sh
# Test failover ved at slukke primary link

PRIMARY_IF="eth1"
BACKUP_IF="eth2"
TARGET="10.50.0.10"

echo "Testing primary route..."
ping -c 3 $TARGET

echo "Disabling primary interface: $PRIMARY_IF"
ip link set $PRIMARY_IF down

echo "Testing backup route..."
ping -c 3 $TARGET

echo "Re-enabling primary interface: $PRIMARY_IF"
ip link set $PRIMARY_IF up

sleep 3

echo "Testing failback to primary..."
ping -c 3 $TARGET

echo "Current route:"
ip route get $TARGET
```

---

## 🚨 Almindelige Fejl og Fixes

### Problem: Ping virker ikke mellem netværk

```bash
# Tjek 1: Er IP forwarding aktiveret?
cat /proc/sys/net/ipv4/ip_forward
# Hvis 0, aktiver det:
sysctl -w net.ipv4.ip_forward=1

# Tjek 2: Er routerne konfigureret?
ip route show

# Tjek 3: Er der firewall regler?
nft list ruleset
```

### Problem: Routing loop

```bash
# Diagnosticer med traceroute
traceroute -n 10.20.0.10

# Tjek routing-tabeller på alle routere
ip route show

# Find cirkulære routes
# Router-1: 10.20.0.0 via Router-2
# Router-2: 10.20.0.0 via Router-1  <-- LOOP!
```

### Problem: Asymmetrisk routing

```bash
# Tjek route frem
ip route get 10.20.0.10

# Tjek route tilbage (på remote router)
ip route get 192.168.1.10

# Hvis forskellige veje: asymmetrisk routing
```

### Problem: MTU issues

```bash
# Tjek MTU på interfaces
ip link show

# Test med forskellige packet sizes
ping -s 100 10.20.0.10   # Lille pakke
ping -s 1400 10.20.0.10  # Stor pakke

# Test med Don't Fragment
ping -M do -s 1400 10.20.0.10
```

---

## 💾 Permanent Konfiguration

### Alpine Linux

```bash
# /etc/network/interfaces
auto eth0
iface eth0 inet static
    address 192.168.1.1
    netmask 255.255.255.0
    
    # Post-up scripts
    post-up ip route add 10.20.0.0/16 via 192.168.1.254
    post-up sysctl -w net.ipv4.ip_forward=1
```

### Debian/Ubuntu

```bash
# /etc/network/interfaces
auto eth0
iface eth0 inet static
    address 192.168.1.1/24
    
    # Routes
    up ip route add 10.20.0.0/16 via 192.168.1.254

# /etc/sysctl.conf
net.ipv4.ip_forward=1
```

---

## 📋 Troubleshooting Checklist

```
[ ] Layer 1: Kabel tilsluttet? Link up?
    → ip link show

[ ] Layer 2: ARP working?
    → ip neigh show
    → ping til gateway

[ ] Layer 3: Routing konfigureret?
    → ip route show
    → ip route get <destination>

[ ] Layer 3: IP forwarding aktiveret (på routere)?
    → cat /proc/sys/net/ipv4/ip_forward

[ ] Layer 3: Return route konfigureret?
    → Tjek routing på remote router

[ ] Layer 4+: Firewall blokeringer?
    → nft list ruleset

[ ] Pakke-flow: Kommer pakker frem?
    → tcpdump på destination

[ ] Pakke-flow: Kommer reply tilbage?
    → tcpdump på source
```

---

**God routing! 🛤️**
