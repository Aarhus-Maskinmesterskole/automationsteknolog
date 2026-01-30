# Opgave — To routere med /30-transit og statisk routing

**Idé:** PC1 og PC2 ligger i hver sit /24. R1 og R2 forbindes via et /30 transitlink. Statiske ruter på begge routere.

## Topologi

```
PC1 ── SwitchA ── R1 (eth0 | eth1) ── R2 (eth0 | eth1) ── SwitchB ── PC2
                  LAN-A   TRANSIT     TRANSIT   LAN-B
```

(Brug evt. direkte kabel i stedet for switches. Ingen trunk.)

## Adresser

| Segment       | Enhed/Interface | IP/Mask         |
| ------------- | --------------- | --------------- |
| LAN-A (/24)   | R1 eth0         | 10.10.10.1/24   |
|               | PC1             | 10.10.10.2/24   |
| Transit (/30) | R1 eth1         | 10.255.255.1/30 |
|               | R2 eth0         | 10.255.255.2/30 |
| LAN-B (/24)   | R2 eth1         | 10.10.20.1/24   |
|               | PC2             | 10.10.20.2/24   |

---

## Trin 1 — R1

```bash
ip addr add 10.10.10.1/24 dev eth0
ip addr add 10.255.255.1/30 dev eth1
ip link set eth0 up; ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1
ip route add 10.10.20.0/24 via 10.255.255.2
ip -4 route
```

## Trin 2 — R2

```bash
ip addr add 10.255.255.2/30 dev eth0
ip addr add 10.10.20.1/24 dev eth1
ip link set eth0 up; ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1
ip route add 10.10.10.0/24 via 10.255.255.1
ip -4 route
```

## Trin 3 — PC1

```bash
ip addr flush dev eth0
ip addr add 10.10.10.2/24 dev eth0
ip route replace default via 10.10.10.1
ping -c2 10.10.10.1
```

## Trin 4 — PC2

```bash
ip addr flush dev eth0
ip addr add 10.10.20.2/24 dev eth0
ip route replace default via 10.10.20.1
ping -c2 10.10.20.1
```

## Trin 5 — Test

Fra **PC1**:

```bash
ping -c3 10.10.20.1
ping -c3 10.10.20.2
traceroute 10.10.20.2 || tracepath 10.10.20.2   # to hop: R1 → R2
```

## Trin 6 — Verificér på routere

```bash
# R1
ip -br a
ip -4 route
ip neigh
tcpdump -ni eth1 'host 10.10.20.2 and icmp'

# R2
ip -br a
ip -4 route
ip neigh
tcpdump -ni eth0 'host 10.10.10.2 and icmp'
```

---

## Hurtig fejlsøgning

* PC1 når ikke 10.10.10.1 → kabel/port/eth0 DOWN på R1.
* `ping` PC1→10.10.20.1 fejler → transit ikke oppe eller rute mangler på R1.
* `ping` PC1→PC2 fejler men PC1→10.10.20.1 virker → ruten på **R2** til 10.10.10.0/24 mangler.
* `traceroute` viser ét hop → du tester mod R2’s IP, ikke PC2, eller der er en utilsigtet direkte vej.
* `ip neigh` mangler entries på transit → ARP når ikke frem; tjek link, IP/masker på eth1/eth0.

---

## Ekstra (valgfrit)

* Brug `ip route replace` og ændr next-hop for at se LPM-effekt.
* Tilføj en “floating static” default på R1 med højere metric som backup.
