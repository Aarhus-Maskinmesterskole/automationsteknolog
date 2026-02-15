# Opgave 3 — Router-on-a-stick over to switche

**Tænk sådan her:** To rum på hver sin switch. En trappe mellem switchene. Dørmanden (R1) står ved trappen. R1 sørger for, at rum 10 og rum 20 kan tale sammen.

## Formål

* Få inter-VLAN routing til at virke hen over to L2-switche.
* Validere, at dot1q-trunk bærer VLAN 10 og 20.
* Fejlsøge med målrettede målinger.

## Læringsmål

Du kan:

1. Planlægge portroller på flere switche.
2. Konfigurere Linux router-subinterfaces til 802.1Q.
3. Verificere tagging på trunk med `tcpdump`.

---

## Forudsætning

* GNS3 “Ethernet switch” på begge switche.
* 8021q modulet på værten.
* Ingen firewall i spil.

---

## Topologi og portplan

| Enhed   | Port | Type   | VLAN | Til        |
| ------- | ---- | ------ | ---- | ---------- |
| Switch1 | e0   | dot1q  | 1    | R1 eth0    |
| Switch1 | e1   | dot1q  | 1    | Switch2 e0 |
| Switch1 | e2   | access | 10   | PC1        |
| Switch2 | e0   | dot1q  | 1    | Switch1 e1 |
| Switch2 | e1   | access | 20   | PC2        |

Note: GNS3 “Ethernet switch” bærer alle VLAN på dot1q-porte. Feltet “VLAN” på dot1q er kun “native VLAN”.

<img width="3456" height="2160" alt="image" src="https://github.com/user-attachments/assets/35a3aec7-1921-41a0-8630-732ba4d05a72" />


---

## Adresseplan

| VLAN | Net        | Router IP       | PC IP      | Maske |
| ---: | ---------- | --------------- | ---------- | ----- |
|   10 | 10.10.10.0 | 10.10.10.1 (R1) | 10.10.10.2 | /24   |
|   20 | 10.10.20.0 | 10.10.20.1 (R1) | 10.10.20.2 | /24   |

---

## Trin 1 — Sæt switche

* Åbn **Configure** på hver switch.
* S1: e0=dot1q, e1=dot1q, e2=access VLAN 10.
* S2: e0=dot1q, e1=access VLAN 20.
* Apply/OK.

## Trin 2 — Router R1 (802.1Q-subinterfaces)

```bash
ip link add link eth0 name eth0.10 type vlan id 10
ip link add link eth0 name eth0.20 type vlan id 20
ip addr add 10.10.10.1/24 dev eth0.10
ip addr add 10.10.20.1/24 dev eth0.20
ip link set eth0.10 up; ip link set eth0.20 up
sysctl -w net.ipv4.ip_forward=1
ip -d link show eth0.10
ip -4 route
```

## Trin 3 — PC1 og PC2

```bash
# PC1 (VLAN10)
ip addr flush dev eth0
ip addr add 10.10.10.2/24 dev eth0
ip route replace default via 10.10.10.1
ping -c2 10.10.10.1

# PC2 (VLAN20)
ip addr flush dev eth0
ip addr add 10.10.20.2/24 dev eth0
ip route replace default via 10.10.20.1
ping -c2 10.10.20.1
```

## Trin 4 — End-to-end test

Fra PC1:

```bash
ping -c3 10.10.20.2
traceroute 10.10.20.2 || tracepath 10.10.20.2
```

Forvent ét hop via R1.

## Trin 5 — Se tags på trunken (valgfrit)

På R1:

```bash
tcpdump -ni eth0 'vlan 10 and icmp'
tcpdump -ni eth0 'vlan 20 and icmp'
```

Du skal se ICMP fra hver test i det tilsvarende VLAN.

---

## Hurtig fejlsøgning

* PC1 når ikke 10.10.10.1 → S1 e2 ikke access 10, eller `eth0.10` DOWN.
* PC2 når ikke 10.10.20.1 → S2 e1 ikke access 20, eller `eth0.20` DOWN.
* PC1↔PC2 fejler men GW virker → `net.ipv4.ip_forward=0`.
* Ingen ICMP i `tcpdump 'vlan 20'` under PC2-test → S1 e1 eller S2 e0 ikke sat til dot1q.
* “Operation not supported” ved oprettelse af `eth0.10` → indlæs 8021q på værten.

---

## Ekstra (valgfrit)

1. Tilføj **VLAN30** til samme trunkkæde. PC3 på S2 access VLAN30, og på R1:

   ```bash
   ip link add link eth0 name eth0.30 type vlan id 30
   ip addr add 10.10.30.1/24 dev eth0.30
   ip link set eth0.30 up
   ```

   Test PC1↔PC3.
2. Skift native VLAN på trunkene til en ubrugt VLAN og bekræft med `tcpdump -ni eth0 'not vlan'` at intet krydser untagget.
