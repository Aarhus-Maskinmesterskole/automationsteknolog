# Opgave — Routing mellem 2 subnets (ingen VLAN)

**Idé:** To adskilte L2-segmenter. Én Linux-router i midten. To Linux-PC’er i hver sit subnet.

## Topologi

PC1 ─ Switch1 ─ R1 ─ Switch2 ─ PC2
(eller kobl PC1 direkte til R1-eth0 og PC2 til R1-eth1)

## Adresseplan

| Side | Net        | Router IP  | PC IP      | Maske |
| ---: | ---------- | ---------- | ---------- | ----- |
|    A | 10.10.10.0 | 10.10.10.1 | 10.10.10.2 | /24   |
|    B | 10.10.20.0 | 10.10.20.1 | 10.10.20.2 | /24   |

## R1 (Linux-router)

```bash
ip addr add 10.10.10.1/24 dev eth0
ip addr add 10.10.20.1/24 dev eth1
ip link set eth0 up; ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1
ip -4 route
```

## PC1

```bash
ip addr flush dev eth0
ip addr add 10.10.10.2/24 dev eth0
ip route replace default via 10.10.10.1
ping -c2 10.10.10.1
```

## PC2

```bash
ip addr flush dev eth0
ip addr add 10.10.20.2/24 dev eth0
ip route replace default via 10.10.20.1
ping -c2 10.10.20.1
```

## Test (fra PC1)

```bash
ping -c3 10.10.20.2
traceroute 10.10.20.2 || tracepath 10.10.20.2
```

Forvent 1 hop via R1.

## Validering (på R1)

```bash
ip -br a
ip -4 route
ip neigh
tcpdump -ni eth0 icmp   # A-siden
tcpdump -ni eth1 icmp   # B-siden
```

## Fejlsøgning

* Ingen kryds-ping: `sysctl net.ipv4.ip_forward` skal være 1.
* PC1 når ikke 10.10.10.1: forkert kabel eller `eth0` DOWN.
* `ip r` på PC’er skal vise én default via R1.
* ARP mangler: `ip neigh` på R1 skal vise 10.10.10.2 på eth0 og 10.10.20.2 på eth1.
