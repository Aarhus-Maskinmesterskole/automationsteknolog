## Opgave 2 — Inter-VLAN routing, let og roligt

**Tænk sådan her:** Der er to rum med hver sin farve. PC1 bor i rum 10. PC2 bor i rum 20. R1 er dørmanden. Når vi tænder dørmanden, kan de to rum tale sammen.

---

### Forudsætning

Opgave 1 virker:

* PC1 ↔ R1 i **VLAN10**
* PC2 ↔ R1 i **VLAN20**
* På R1 findes **eth0.10** og **eth0.20** allerede (trunk-varianten).

---

### Trin 1 — Tænd dørmanden på R1

```bash
sysctl -w net.ipv4.ip_forward=1
ip -4 route
```

* Første linje åbner døren mellem rum 10 og 20.
* Anden linje viser, at R1 kender begge net som “connected”.

### Trin 2 — Tjek at begge børn kan snakke med dørmanden

**PC1**

```bash
ip -4 addr; ip r
ping -c2 10.10.10.1
```

**PC2**

```bash
ip -4 addr; ip r
ping -c2 10.10.20.1
```

### Trin 3 — Test PC1 ↔ PC2

**Fra PC1**

```bash
ping -c3 10.10.20.2
traceroute 10.10.20.2 || tracepath 10.10.20.2
```

* Ét hop via R1 er korrekt.

### Se trafikken (valgfrit)

* Trunk-kablet på R1:

```bash
tcpdump -ni eth0 'vlan and icmp'
```

* Eller specifikt:

```bash
tcpdump -ni eth0 'vlan 10 and icmp'
tcpdump -ni eth0 'vlan 20 and icmp'
```

### Hurtig fejlsøgning

```bash
ip -br a        # IP’er sidder på eth0.10 og eth0.20
ip r            # R1 har to connected /24
ip neigh        # ARP for PC1 og PC2
```

* Ingen svar PC1→PC2 → `ip_forward` er 0 på R1.
* PC når sin GW men ikke modpart → forkert default-gateway på PC’en.
* Stadig problemer → trunkport mod R1 mangler VLAN 10/20 eller subinterface er DOWN.

## Variant B — To kabler, ingen trunk (R1: eth0 til PC1, eth1 til PC2)

**Tænk simpelt:** Der er to rum. PC1 taler i rum A. PC2 taler i rum B. R1 står i midten og åbner døren mellem A og B.

**Tænd døren på R1**

```bash
sysctl -w net.ipv4.ip_forward=1
ip -4 route
```

* Første linje tænder “må gå mellem rum”.
* Anden linje viser, at R1 kender begge net (10.10.10.0/24 og 10.10.20.0/24 som “connected”).

**Test**

* Fra PC1:

  ```bash
  ping -c3 10.10.20.2
  traceroute 10.10.20.2 || tracepath 10.10.20.2
  ```

  Ét hop via R1 er korrekt.
* Valgfrit fra PC2:

  ```bash
  ping -c3 10.10.10.2
  ```

**Se trafikken på R1**

```bash
tcpdump -ni eth0 icmp    # PC1-siden
tcpdump -ni eth1 icmp    # PC2-siden
```

**Hurtig fejlsøgning**

```bash
ip -br a        # IP’er på de rigtige interfaces
ip r            # R1 har to connected /24
ip neigh        # ARP for PC1 og PC2 ses efter lokale pings
```

* Ingen svar PC1→PC2: `ip_forward` er 0 på R1. Tænd den.
* PC kan nå sin GW men ikke modpart: forkert default-gateway på PC’en.
* Intet på tcpdump på den ene side: forkert kabel/port eller interface-navn.

## Appendiks

* ```sh
  sysctl -w net.ipv4.ip_forward=1
  ```

  Tænder IPv4-routing i kernel. Midlertidigt til næste reboot.

* ```sh
  ip -4 route
  ```

  Viser IPv4-rutetabel (connected-net og default).

* ```sh
  ip -4 addr
  ```

  Viser kun IPv4-adresser på alle interfaces.

* ```sh
  ip r
  ```

  Alias for `ip route`.

* ```sh
  ping -c<N> <destination>
  ```

  Sender N ICMP-eko. Reachability-test og latens.

* ```sh
  traceroute <destination>
  ```

  Viser rute hop-for-hop med stigende TTL.

* ```sh
  tracepath <destination>
  ```

  `traceroute`-alternativ der ofte virker uden sudo.

* ```sh
  tcpdump -ni eth0 'vlan and icmp'
  ```

  Sniffer 802.1Q-tagget ICMP på trunk-interface `eth0`. `-n` = ingen DNS, `-i` vælger interface.

* ```sh
  tcpdump -ni eth0 'vlan 10 and icmp'
  tcpdump -ni eth0 'vlan 20 and icmp'
  ```

  Sniffer kun ICMP i hhv. VLAN 10 og VLAN 20 på trunken.

* ```sh
  ip -br a
  ```

  “Brief” visning: interface, status og IP’er pr. linje.

* ```sh
  ip neigh
  ```

  Neighbor-tabel (ARP/NDP). Bekræfter MAC-opløsning og hvem der er lært.

* ```sh
  tcpdump -ni eth0 icmp
  tcpdump -ni eth1 icmp
  ```

  Sniffer ICMP på hver side i “to kabler”-varianten.

* ```sh
  <cmd1> ; <cmd2>
  ```

  Shell-separator: kør `cmd2` efter `cmd1` uanset exit-status. (Brugt som `ip -4 addr; ip r`.)
