# GNS3 — 2 Linux-PC’er + 1 Linux-router med /25-subnet fra Opgave 1

### Formål

* Omsætte de to **/25** fra Opgave 1 til en fungerende L3-forbindelse i GNS3.
* Træne korrekt IP-adresseting, default-gateway og routing på Linux.
* Opbygge en kort, reproducerbar fejlsøgningsrutine på L2/L3 uden firewall-indblanding.

### Læringsmål

Efter øvelsen kan du:

1. Vælge gyldige host-IP’er i to /25 uden at ramme net/broadcast.
2. Konfigurere Linux-routerens interfaces med /25 og aktivere `ip_forward`.
3. Sætte korrekt default-route på PC1 og PC2 mod hver sin router-IP.
4. Verificere reachability med `ping` og ét hop i `traceroute`/`tracepath`.
5. Bruge `ip -br a`, `ip r`, `ip neigh` og `tcpdump` til at lokalisere og rette fejl.
6. Forklare ARP→ICMP-flowet for PC1→R1→PC2 i dette design.

**Topologi:**
`PC1 —(LAN A /25)— R1 —(LAN B /25)— PC2`

---

## Del A — Notér dine /25-resultater

**Subnet #1**

* Net: `____________________`
* Broadcast: `____________________`
* Første brugbare: `____________________`
* Sidste brugbare: `____________________`

**Subnet #2**

* Net: `____________________`
* Broadcast: `____________________`
* Første brugbare: `____________________`
* Sidste brugbare: `____________________`

> Brug CIDR `/25` på alle adresser.

---

## Del B — GNS3 step-by-step

**Antag** noder: `R1` (Linux-router), `PC1`, `PC2`. Kablet: `PC1 — R1 — PC2`.
Find korrekte interface-navne med `ip -br link` og erstat `eth0/eth1`.

### IP-plan

* **LAN A (PC1↔R1-eth0) = Subnet #1**

  * R1-eth0: **første brugbare** i Subnet #1
  * PC1: vilkårlig **brugbar** i Subnet #1 (ikke R1-IP)
* **LAN B (R1-eth1↔PC2) = Subnet #2**

  * R1-eth1: **første brugbare** i Subnet #2
  * PC2: vilkårlig **brugbar** i Subnet #2 (ikke R1-IP)
 
<img width="3456" height="2160" alt="Screenshot From 2025-08-27 17-42-54" src="https://github.com/user-attachments/assets/2fb3fa73-dc63-4f18-9bcd-e7e2b5f42f3b" />


### 1) Router (R1)

```bash
# erstat <> med dine konkrete /25-adresser
ip addr flush dev eth0; ip addr flush dev eth1
ip addr replace <R1_ETH0_IP_I_SUBNET1>/25 dev eth0
ip addr replace <R1_ETH1_IP_I_SUBNET2>/25 dev eth1
ip link set eth0 up; ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1

# tjek
ip -br a
cat /proc/sys/net/ipv4/ip_forward    # skal være 1
```

### 2) PC1

```bash
ip addr flush dev eth0
ip r flush table main
ip addr replace <PC1_IP_I_SUBNET1>/25 dev eth0
ip link set eth0 up
ip route replace default via <R1_ETH0_IP_I_SUBNET1>

# tjek
ip -br a; ip r
ping -c2 <R1_ETH0_IP_I_SUBNET1>
```

### 3) PC2

```bash
ip addr flush dev eth0
ip r flush table main
ip addr replace <PC2_IP_I_SUBNET2>/25 dev eth0
ip link set eth0 up
ip route replace default via <R1_ETH1_IP_I_SUBNET2>

# tjek
ip -br a; ip r
ping -c2 <R1_ETH1_IP_I_SUBNET2>
```

### 4) Ende-til-ende test

**Fra PC1**

```bash
ping -c3 <PC2_IP_I_SUBNET2>
# hvis 'traceroute' mangler, brug tracepath
traceroute <PC2_IP_I_SUBNET2> || tracepath <PC2_IP_I_SUBNET2>
```

Valgfrit fra PC2:

```bash
ping -c3 <PC1_IP_I_SUBNET1>
```

---

## Hurtig fejlsøgning

```bash
ip -br link                      # interfaces UP
ip -br a                         # korrekte /25-adresser
ip r                             # default via R1 på PC’er
ip neigh                         # ARP entries efter lokale pings
tcpdump -ni eth0 icmp or arp     # på R1 eller PC ved tvivl
```

**Typiske fejl**

* Net- eller broadcast-adresse brugt som host-IP → vælg en brugbar.
* Forkert gateway på PC’er → skal være R1-IP i samme /25.
* Forwarding slukket på R1 → `ip_forward` skal være 1.
* Forkerte interface-navne → bekræft med `ip -br link`.

**Firewall-tjek (kun læsning)**

```bash
command -v nft >/dev/null && sudo nft list ruleset
command -v iptables >/dev/null && sudo iptables -S
# lav ingen ændringer her i øvelsen
```

---

## Referenceværdier (skjult eksempel)

<details>
<summary>Vis eksempel</summary>

* Subnet #1: 192.168.1.0/25

  * R1-eth0: 192.168.1.1/25
  * PC1: 192.168.1.10/25  · GW 192.168.1.1
* Subnet #2: 192.168.1.128/25

  * R1-eth1: 192.168.1.129/25
  * PC2: 192.168.1.130/25 · GW 192.168.1.129

</details>
