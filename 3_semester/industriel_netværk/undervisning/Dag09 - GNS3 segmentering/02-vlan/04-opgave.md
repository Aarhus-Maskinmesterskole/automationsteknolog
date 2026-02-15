# Opgave 4 — Linux-PC pinger “PLC” via Cloud (to NICs, ingen trunk)

## Idé

VLAN10 på Switch1 til PC. VLAN20 på Switch2 til “PLC”. Router R1 har to NICs og ruter mellem VLAN10↔VLAN20. “PLC” simuleres som værts-NIC bag en GNS3 **Cloud**.

## Portplan

| Enhed   | Port | Type   | VLAN | Til               |
| ------- | ---- | ------ | ---- | ----------------- |
| Switch1 | e0   | access | 10   | R1 eth0           |
| Switch1 | e2   | access | 10   | linux-pc          |
| Switch2 | e0   | access | 20   | R1 eth1           |
| Switch2 | e1   | access | 20   | Cloud (værts-NIC) |

Ingen link mellem S1 og S2. Ingen trunk.

## Adresseplan

|         Siden | IP/maske                      | Bemærkning          |
| ------------: | ----------------------------- | ------------------- |
|       R1 eth0 | 10.10.10.1/24                 | VLAN10-gateway      |
|       R1 eth1 | 10.10.20.1/24                 | VLAN20-gateway      |
|      linux-pc | 10.10.10.2/24, GW 10.10.10.1  | PC på VLAN10        |
| “PLC” (Cloud) | 10.10.20.50/24, GW 10.10.20.1 | Sættes på værts-NIC |

## Trin 1 — Switche

* Switch1: sæt **e0** og **e2** til **access VLAN 10**.
* Switch2: sæt **e0** og **e1** til **access VLAN 20**. Apply/OK.

## Trin 2 — Router R1

```bash
ip addr add 10.10.10.1/24 dev eth0
ip addr add 10.10.20.1/24 dev eth1
ip link set eth0 up; ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1
ip -4 route
```

## Trin 3 — Linux-PC (VLAN10)

```bash
ip addr flush dev eth0
ip addr add 10.10.10.2/24 dev eth0
ip route replace default via 10.10.10.1
ping -c2 10.10.10.1
```

## Trin 4 — Cloud = “PLC”

1. Træk **Cloud** ind → **Configure** → vælg din værts-NIC som skal fungere som PLC-port (fx `enp3s0` eller en ekstra VM-NIC).
2. Forbind Cloud til **Switch2 e1**.
3. Sæt IP på værts-NIC’en, som om det var PLC’en:

Linux-værtsmaskine:

```bash
sudo ip addr flush dev <HOST_NIC>
sudo ip addr add 10.10.20.50/24 dev <HOST_NIC>
sudo ip link set <HOST_NIC> up
# valgfrit: default route behøves ikke på værten for ping-testen
```

Windows-værtsmaskine: Sæt statisk IPv4 10.10.20.50/24 i Netværksindstillinger.

4. Tillad ICMP på værten, hvis firewall blokerer.

> Hvis du har en fysisk Siemens PLC: brug samme Cloud-forbindelse, men sæt IP på PLC’en i stedet: 10.10.20.60/24, GW 10.10.20.1.

## Trin 5 — Test fra linux-pc

```bash
ping -c3 10.10.20.50
traceroute 10.10.20.50 || tracepath 10.10.20.50
```

Forvent ét hop via R1.

## Trin 6 — Observationer (valgfrit)

På R1:

```bash
tcpdump -ni eth0 icmp      # PC-siden
tcpdump -ni eth1 icmp      # “PLC”-siden
```

## Fejlsøgning

* PC når ikke 10.10.10.1 → Switch1 e2 ikke access 10, eller R1 eth0 DOWN.
* PC når 10.10.20.1 men ikke 10.10.20.50 → forkert Cloud-NIC valgt, værts-NIC uden IP, eller værts-firewall blokerer ICMP.
* Kryds-ping fejler helt → `net.ipv4.ip_forward=0` på R1.
* ARP: `ip neigh` på R1 skal vise 10.10.20.50 på eth1 og 10.10.10.2 på eth0.
