# Opgave 4 — GNS3-PC ping’er fysisk PLC på andet /25-subnet

### Formål

* Split et `/24` i to `/25`. Få end-to-end forbindelse mellem virtuel PC og fysisk PLC via Linux-router.
* Træn IP-tildeling, default-gateways og basis-routing. Ingen firewall.

### Læringsmål

Efter opgaven kan du:

1. Designe to `/25` fra `192.168.0.0/24` og vælge gyldige host-IP’er.
2. Konfigurere Linux-router med to L3-interfaces og `ip_forward`.
3. Sætte korrekt default-route på PC og PLC.
4. Verificere trafik med `ping` og `traceroute/tracepath`.
5. Fejlsøge med `ip -br a`, `ip r`, `ip neigh`, `tcpdump`.

---

## Topologi

`PC1 —(Subnet A /25)— R1 —(Subnet B /25)— Cloud(PC’ens fysiske ethernet-port) ——[direkte kabel]—— PLC`

Cloud bindes til **din computers fysiske ethernet-port**. Porten går direkte i PLC.


<img width="3456" height="2160" alt="Screenshot From 2025-08-27 17-42-54" src="https://github.com/user-attachments/assets/d741ad4d-3210-4896-9e14-71855dfca660" />

---

## Adresseplan (matrix)

### Subnet-metadata

| Subnet | Prefix | Net-ID        | Broadcast     | Host-range                  |
| ------ | ------ | ------------- | ------------- | --------------------------- |
| A      | /25    | 192.168.0.0   | 192.168.0.127 | 192.168.0.1–192.168.0.126   |
| B      | /25    | 192.168.0.128 | 192.168.0.255 | 192.168.0.129–192.168.0.254 |

### Interface-adresser

| Enhed | Interface | Subnet | IP/CIDR          | Default GW    | Note                    |
| ----- | --------- | ------ | ---------------- | ------------- | ----------------------- |
| R1    | eth0      | A      | 192.168.0.1/25   | –             | Mod PC1                 |
| PC1   | eth0      | A      | 192.168.0.10/25  | 192.168.0.1   | Valgfri host i A        |
| R1    | eth1      | B      | 192.168.0.129/25 | –             | Mod PLC                 |
| PLC   | eth?      | B      | 192.168.0.130/25 | 192.168.0.129 | Direkte kabel via Cloud |

Juster host-IP’er ved behov. Bevar `/25`.

---

## Forudsætninger

* GNS3 med Linux-PC, Linux-router og **Cloud**.
* PLC kan sættes med statisk IP og gateway.
* Din computers ethernet-port er fri til Cloud.

---

## Trin A — Byg i GNS3

1. Tilføj **PC1**, **R1**, **Cloud**.
2. Cloud → **Configure** → vælg **din computers fysiske ethernet-port**.
3. Kabling i GNS3: `PC1 ↔ R1-eth0`, `R1-eth1 ↔ Cloud`.
4. Sæt fysisk kabel fra porten i din computer til **PLC**.
5. Find interfacenavne i noderne: `ip -br link`.

---

## Trin B — Konfigurer noder

### R1 (Linux-router)

```bash
ip addr flush dev eth0; ip addr flush dev eth1
ip addr add 192.168.0.1/25 dev eth0
ip addr add 192.168.0.129/25 dev eth1
ip link set eth0 up; ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1

# tjek
ip -br a
cat /proc/sys/net/ipv4/ip_forward   # skal være 1
```

### PC1

```bash
ip addr flush dev eth0
ip r flush table main
ip addr add 192.168.0.10/25 dev eth0
ip link set eth0 up
ip route replace default via 192.168.0.1

# tjek
ip -br a; ip r
ping -c2 192.168.0.1
```

### PLC (fysisk)

* IP: `192.168.0.130/25`
* Default GW: `192.168.0.129`
* Link: direkte kabel til den port du valgte i Cloud.

---

## Verificering

1. På R1:

```bash
ping -c2 192.168.0.130
```

2. På PC1:

```bash
ping -c3 192.168.0.130
traceroute 192.168.0.130 || tracepath 192.168.0.130   # ét hop via 192.168.0.1
```

Succes: PC1 når PLC. `traceroute/tracepath` viser ét hop (R1).

---

## Fejlsøgning

```bash
ip -br link                      # interfaces UP
ip -br a                         # korrekte /25
ip r                             # PC1 default via 192.168.0.1
ip neigh                         # ARP entries
tcpdump -ni eth1 icmp or arp     # på R1 mod PLC-siden
```

Typiske fejl:

* Cloud bundet til forkert port eller link DOWN.
* Forkert gateway på PLC.
* Forkerte interface-navne i noderne.

---

## Hvis PLC’s gateway ikke kan ændres (midlertidig NAT)

```bash
iptables -t nat -A POSTROUTING -s 192.168.0.0/25 -d 192.168.0.128/25 -o eth1 -j MASQUERADE
```

Fjern NAT igen når korrekt gateway er sat på PLC.
