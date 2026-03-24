# Dag 08 - GNS3 Ping, ARP og Traceroute

Velkommen til dag 8 af Industrielt Netværk.

> I dag arbejder vi med de vigtigste værktøjer til netværksforståelse og fejlfinding i GNS3: `ping`, ARP og `traceroute`.

---

## Læringsmål for dagen

- Forstå hvad `ping` kan og ikke kan fortælle om en forbindelse
- Forklare hvordan ARP bruges til at finde MAC-adresser på lokale netværk
- Bruge `traceroute` til at se vejen gennem et netværk
- Dokumentere og fejlfinde forbindelsesproblemer systematisk
- Koble værktøjerne til de topologier, der blev bygget på Dag 07

---

## Placering i forløbet

1. Forrige dag: [Dag07 - GNS3 Introduktion/README.md](./../Dag07%20-%20GNS3%20introduktion/README.md)
2. Denne dag: netværksanalyse og fejlfinding i de miljøer, du allerede har bygget
3. Næste dag: [Dag09 - GNS3 Segmentering/README.md](./../Dag09%20-%20GNS3%20Segmentering/README.md)

---

## Dagens progression

1. Verificér lokal forbindelse med `ping`
2. Undersøg hvordan ARP knytter IP-adresser til MAC-adresser
3. Brug `traceroute` til at se vejen mellem subnet
4. Saml resultaterne i en kort fejlsøgningsmetode

---

## Hovedaktiviteter

1. Genbrug topologien fra Dag 07 med to hosts og en router
2. Test forbindelse i samme subnet og mellem to subnet
3. Brug `ip neigh` eller tilsvarende til at se ARP-tabellen
4. Brug `traceroute` eller `tracepath` til at identificere hop
5. Beskriv forskellen på lokal levering og routing via gateway

---

## Anbefalet gennemførelse

1. Start med en topologi hvor ping allerede virker
2. Slet eller ryd ARP-tabellen og observer hvad der sker ved første ping
3. Test `traceroute` fra et subnet til et andet
4. Dokumentér hvilke kommandoer du brugte, og hvad de viste

---

## Dokumentation

Dokumenter gerne med:

- skærmbillede af GNS3-topologi
- output fra `ping`
- output fra `ip neigh`
- output fra `traceroute` eller `tracepath`
- kort forklaring af hvad hvert hop eller hver ARP-entry betyder

---

## Næste dag

Næste naturlige skridt er at opdele netværket i segmenter med subnet og VLAN.


---

### 5.3 Host2 (VLAN 120)

På Alpine-Host2:

1. Sæt IP-adresse:

```bash
ip addr add 192.168.120.10/24 dev eth0
```

2. Sæt interface op:

```bash
ip link set eth0 up
```

3. Sæt default gateway:

```bash
ip route add default via 192.168.120.1
```

4. Kontrol:

```bash
ip addr show dev eth0
ip route show dev eth0
```

<img width="1916" height="1028" alt="image" src="https://github.com/user-attachments/assets/ec162f2a-cecf-45bf-91dc-3eaeaff58b70" />


---

### 5.4 Host3 (VLAN 130)

På Alpine-Host3:

1. Sæt IP-adresse:

```bash
ip addr add 192.168.130.10/24 dev eth0
```

2. Sæt interface op:

```bash
ip link set eth0 up
```

3. Sæt default gateway:

```bash
ip route add default via 192.168.130.1
```

4. Kontrol:

```bash
ip addr show dev eth0
ip route show dev eth0
```

<img width="1918" height="1029" alt="image" src="https://github.com/user-attachments/assets/9666237b-fd51-434c-8b22-b1e7bbab83b2" />

---

## Trin 6 – Test af forbindelse

### 6.1 Test lokal gateway

Fra **Host1** (Alpine):

```bash
ping -c4 192.168.110.1
```

<img width="1917" height="1029" alt="image" src="https://github.com/user-attachments/assets/faa61391-1a87-41f0-9b11-d69c3bae611a" />

Fra **Host2**:

```bash
ping -c4 192.168.120.1
```

<img width="1917" height="1028" alt="image" src="https://github.com/user-attachments/assets/47879e49-dec3-41cc-a11e-0688b1b155ae" />

Fra **Host3**:

```bash
ping -c4 192.168.130.1
```

<img width="1915" height="1027" alt="image" src="https://github.com/user-attachments/assets/dda3b888-9781-4198-95a1-edaa880bce3b" />

Alle tre tests skal lykkes. Hvis ikke: tjek IP-adresser, gateway og om `eth0` er `UP`.

---

### 6.2 Test inter-VLAN routing

Fra **Host1 (VLAN 110)**:

```bash
ping 192.168.120.10
ping 192.168.130.10
```

<img width="1916" height="1028" alt="image" src="https://github.com/user-attachments/assets/425dba6e-5014-4aff-9ac7-9b66c1dd4dae" />


Fra **Host2 (VLAN 120)**:

```bash
ping 192.168.110.10
ping 192.168.130.10
```

Fra **Host3 (VLAN 130)**:

```bash
ping 192.168.110.10
ping 192.168.120.10
```

Hvis pings lykkes, fungerer inter-VLAN routing via Linux-routeren.

---

## Trin 7 – Fejlsøgning (hvis noget fejler)

På **routeren**:

```bash
ip addr show
ip -d link show
ip route
ping 192.168.110.10
ping 192.168.120.10
ping 192.168.130.10
```

På **switchen**:

```text
show vlan brief
show interfaces trunk
show running-config
```

På **Alpine-hosts**:

```bash
ip addr show dev eth0
ip route show
ping <egen gateway>
```

Typiske fejl:

* Forkert IP/netmaske eller gateway på Alpine-host.
* Forkert VLAN på switch-port.
* Trunk-port ikke korrekt konfigureret.
* VLAN-subinterface på router ikke aktivt (`DOWN`).

---

## Ekstra (frivilligt)

Hvis du bliver hurtigt færdig:

1. Tilføj et ekstra VLAN (140) med tilsvarende opsætning (subinterface på router, VLAN på switch, Alpine-host).
2. Brug `tcpdump` på routeren til at se trafik:

```bash
tcpdump -i eth0
tcpdump -i eth0.110
```
