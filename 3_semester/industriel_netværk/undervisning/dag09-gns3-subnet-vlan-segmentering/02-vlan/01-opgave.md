# Opgave 1 — To VLAN i GNS3 med isolation, let og roligt

**Tænk sådan her:** To farvede rum på samme etage. PC1 bor i rum 10. PC2 bor i rum 20. Dørmanden (R1) står i døren men sover. Når dørmanden sover, kan rummene ikke tale sammen.

---

### Forudsætning

* GNS3-projekt oprettet.
* Noder: PC1, PC2, switch, router R1.
* Ønsker du trunk: brug en switch med VLAN-understøttelse (fx IOSv-L2).
  Har du kun “Ethernet switch” i GNS3: brug Variant B uden trunk.
* På værten skal 802.1Q være mulig. Hvis du får “Operation not supported” ved `eth0.10`, indlæs modulet på værten.

---

### Adresseplan

| VLAN | Net        | Router IP  | PC IP      | Maske |
| ---: | ---------- | ---------- | ---------- | ----- |
|   10 | 10.10.10.0 | 10.10.10.1 | 10.10.10.2 | /24   |
|   20 | 10.10.20.0 | 10.10.20.1 | 10.10.20.2 | /24   |

---

## Variant A — Trunk mellem SW og R1

### Trin 1 — Byg i GNS3

* Kabler: PC1→SW e1, PC2→SW e2, R1→SW e8.

### Trin 2 — Switch

* Opret VLAN 10 og 20.
* e1: access VLAN 10.
* e2: access VLAN 20.
* e8: trunk, allowed VLANs 10,20.
* Tip (IOSv-L2):

  ```
  conf t
  vlan 10,20
  int e1
    switchport mode access
    switchport access vlan 10
  int e2
    switchport mode access
    switchport access vlan 20
  int e8
    switchport mode trunk
    switchport trunk allowed vlan 10,20
  end
  ```

<img width="3456" height="2160" alt="image" src="https://github.com/user-attachments/assets/c7bf651a-9b3c-4941-ae7b-93f05898b25c" />

### Trin 3 — Router R1 (dørmanden sover)

```bash
sysctl -w net.ipv4.ip_forward=0
ip link add link eth0 name eth0.10 type vlan id 10
ip link add link eth0 name eth0.20 type vlan id 20
ip addr add 10.10.10.1/24 dev eth0.10
ip addr add 10.10.20.1/24 dev eth0.20
ip link set eth0.10 up
ip link set eth0.20 up
ip -d link show eth0.10
ip -d link show eth0.20
```

### Trin 4 — PC1 og PC2

```bash
# PC1 i VLAN10
ip addr flush dev eth0
ip addr add 10.10.10.2/24 dev eth0
ip route replace default via 10.10.10.1
ping -c2 10.10.10.1

# PC2 i VLAN20
ip addr flush dev eth0
ip addr add 10.10.20.2/24 dev eth0
ip route replace default via 10.10.20.1
ping -c2 10.10.20.1
```

### Trin 5 — Verificér isolation

* Kryds-VLAN **skal fejle**, fordi dørmanden sover:

  ```bash
  sysctl -w net.ipv4.ip_forward=0
  ping -c3 10.10.20.2   # fra PC1
  ```
* Se tags på trunk:

  ```bash
  tcpdump -ni eth0 'vlan and icmp'   # på R1
  ```

### Hurtig fejlsøgning

* PC1 kan ikke nå 10.10.10.1 → forkert access-VLAN på e1.
* PC2 kan ikke nå 10.10.20.1 → VLAN20 ikke på e2/ eller trunken mangler VLAN 20.
* `eth0.10`/`.20` DOWN → bring interface UP.
* “Operation not supported” ved `eth0.10` → 8021q mangler på værten.

---

## Variant B — To kabler, ingen trunk

**Tænk simpelt:** Hvert rum har sit eget kabel til dørmanden. Dørmanden sover stadig.

### Trin 1 — Byg i GNS3

* Kabler: PC1→SW e1 (access 10), PC2→SW e2 (access 20).
* R1 har to NICs: `eth0` til VLAN10-accessport, `eth1` til VLAN20-accessport.

<img width="3456" height="2160" alt="image" src="https://github.com/user-attachments/assets/adf1c6e8-d20a-43ae-af54-90908a587cc1" />



### Trin 2 — Switch

* e1: access VLAN 10.
* e2: access VLAN 20.
* Port til R1-eth0: access VLAN 10.
* Port til R1-eth1: access VLAN 20.

### Trin 3 — Router R1

```bash
sysctl -w net.ipv4.ip_forward=0
ip addr add 10.10.10.1/24 dev eth0
ip addr add 10.10.20.1/24 dev eth1
ip link set eth0 up
ip link set eth1 up
ip -4 route
```

### Trin 4 — PC1 og PC2

(Samme IP’er som i Variant A.)

### Trin 5 — Verificér isolation

```bash
ping -c3 10.10.20.2   # fra PC1, skal fejle
tcpdump -ni eth0 icmp # på R1: se PC1-trafik på “10-siden”
tcpdump -ni eth1 icmp # på R1: se PC2-trafik på “20-siden”
```

### Hurtig fejlsøgning

* PC når sin egen GW men ikke modpart → forventet, dørmanden sover.
* Kan ikke nå GW → forkert access-VLAN eller forkert kabel til R1-interface.
* Ingen ICMP i `tcpdump` på én side → tjek interface-navn og link-status.

---

## Videre til Opgave 2

Tænd dørmanden og test kryds-VLAN:

```bash
sysctl -w net.ipv4.ip_forward=1
ping -c3 10.10.20.2   # fra PC1
traceroute 10.10.20.2 || tracepath 10.10.20.2
```
## Appendiks

* ```sh
  sysctl -w net.ipv4.ip_forward=0|1
  ```

  Slår IPv4-routing fra (0) eller til (1) i kernel. Midlertidigt til næste reboot.

* ```sh
  ip link add link eth0 name eth0.<VID> type vlan id <VID>
  ```

  Opretter 802.1Q-subinterface på `eth0` med VLAN-ID `<VID>`. Kræver 8021q på værten.

* ```sh
  ip addr add <IP/CIDR> dev <interface>
  ```

  Tildeler IP-adresse til et interface. Gælder indtil reboot eller flush.

* ```sh
  ip link set <interface> up
  ```

  Aktiverer interfacet. Skal være UP før det kan sende/modtage.

* ```sh
  ip -d link show <interface>
  ```

  Viser linkdetaljer. For VLAN ses parent-link og VLAN-ID.

* ```sh
  ip addr flush dev <interface>
  ```

  Fjerner alle IP-adresser fra interfacet. God “clean state”.

* ```sh
  ip route replace default via <GW>
  ```

  Opretter eller erstatter default-route til gateway `<GW>`.

* ```sh
  ip -4 route
  ```

  Viser IPv4-rutetabellen. Bruges til at bekræfte “connected” net og default.

* ```sh
  ping -c<N> <destination>
  ```

  Sender N ICMP-eko til `<destination>`. Bruges til reachability-test.

* ```sh
  tcpdump -ni eth0 'vlan and icmp'
  ```

  Sniffer tagget ICMP på trunk-link `eth0`. `-n` = ingen DNS-opslag, `-i` vælger interface.

* ```sh
  tcpdump -ni eth0 icmp
  tcpdump -ni eth1 icmp
  ```

  Sniffer ICMP på en specifik side. Bruges i “to kabler”-varianten.

* ```sh
  traceroute <destination>
  ```

  Viser ruten hop-for-hop via TTL. Kræver ofte root/installeret pakke.

* ```sh
  tracepath <destination>
  ```

  Alternativ til `traceroute`. Virker typisk uden sudo.
