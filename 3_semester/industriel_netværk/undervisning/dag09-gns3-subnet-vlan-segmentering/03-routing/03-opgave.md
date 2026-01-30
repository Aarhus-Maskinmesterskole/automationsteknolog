# Opgave — 3 PC’er og 3 routere: Midter-PC må begge veje, sider må ikke krydse

## Idé

PC3 i midten kan pinge PC1 og PC2. PC1 og PC2 kan ikke pinge hinanden. Løses med statiske ruter uden firewall.

## Topologi

<img width="3456" height="2160" alt="image" src="https://github.com/user-attachments/assets/27b7e2ca-99a1-4f2a-a5ac-ae06f705701a" />


## Adresseplan

| Segment     | Enhed/IF | IP/Mask        |
| ----------- | -------- | -------------- |
| LAN-A (/24) | R1 lan   | 10.10.10.1/24  |
|             | PC1      | 10.10.10.2/24  |
| R1–R2 (/30) | R1 t1    | 10.255.10.1/30 |
|             | R2 t1    | 10.255.10.2/30 |
| LAN-M (/24) | R2 lan   | 10.10.30.1/24  |
|             | PC3      | 10.10.30.2/24  |
| R2–R3 (/30) | R2 t2    | 10.255.20.1/30 |
|             | R3 t2    | 10.255.20.2/30 |
| LAN-B (/24) | R3 lan   | 10.10.20.1/24  |
|             | PC2      | 10.10.20.2/24  |

> Antag: R1 `eth0=lan`, `eth1=t1`. R2 `eth0=t1`, `eth1=lan`, `eth2=t2`. R3 `eth0=t2`, `eth1=lan`.

---

## Konfiguration

### R1

```bash
ip addr add 10.10.10.1/24 dev eth0
ip addr add 10.255.10.1/30 dev eth1
ip link set eth0 up; ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1

# Kun PC3 må nås “på den anden side”
ip route add 10.10.30.2/32 via 10.255.10.2

# Ingen default-route på R1
ip route del default 2>/dev/null || true
ip -4 route
```

### R2

```bash
ip addr add 10.255.10.2/30 dev eth0     # mod R1
ip addr add 10.10.30.1/24 dev eth1      # LAN-M
ip addr add 10.255.20.1/30 dev eth2     # mod R3
ip link set eth0 up; ip link set eth1 up; ip link set eth2 up
sysctl -w net.ipv4.ip_forward=1

# Ruter til begge sider
ip route add 10.10.10.0/24 via 10.255.10.1
ip route add 10.10.20.0/24 via 10.255.20.2
ip -4 route
```

### R3

```bash
ip addr add 10.255.20.2/30 dev eth0
ip addr add 10.10.20.1/24 dev eth1
ip link set eth0 up; ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1

# Kun PC3 må nås “på den anden side”
ip route add 10.10.30.2/32 via 10.255.20.1

# Ingen default-route på R3
ip route del default 2>/dev/null || true
ip -4 route
```

### PC1

```bash
ip addr flush dev eth0
ip addr add 10.10.10.2/24 dev eth0
ip route replace default via 10.10.10.1
ping -c2 10.10.10.1
```

### PC2

```bash
ip addr flush dev eth0
ip addr add 10.10.20.2/24 dev eth0
ip route replace default via 10.10.20.1
ping -c2 10.10.20.1
```

### PC3

```bash
ip addr flush dev eth0
ip addr add 10.10.30.2/24 dev eth0
ip route replace default via 10.10.30.1
ping -c2 10.10.30.1
```

---

## Tests

### Skal virke (fra PC3)

```bash
ping -c3 10.10.10.2
ping -c3 10.10.20.2
traceroute 10.10.10.2 || tracepath 10.10.10.2   # går via R2→R1
traceroute 10.10.20.2 || tracepath 10.10.20.2   # går via R2→R3
```

### Skal fejle

```bash
# fra PC1
ping -c3 10.10.20.2
traceroute 10.10.20.2 || tracepath 10.10.20.2   # stopper ved R1

# fra PC2
ping -c3 10.10.10.2
traceroute 10.10.10.2 || tracepath 10.10.10.2   # stopper ved R3
```

---

## Verificering og fejlsøgning

```bash
# På alle routere
ip -br a
ip -4 route
ip neigh

# R2: se transit-trafik
tcpdump -ni eth0 icmp   # mod R1
tcpdump -ni eth2 icmp   # mod R3
```

Typiske fejl:

* PC3 kan ikke pinge PC1/PC2 → mangler ruter på R2.
* PC1↔PC2 kan pinge alligevel → du har lagt /24-rute på R1/R3; slet dem og behold kun /32 til 10.10.30.2.
* Kryds-ping stopper ikke ved R1/R3 → der ligger en default-route; fjern den.
