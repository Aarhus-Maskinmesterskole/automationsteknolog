# Opgave 2: Multi-router topologi - Flere hop

## 🎯 Formål

Lær at konfigurere statiske routes i et netværk med flere routere, hvor pakker skal gennem flere hop for at nå destinationen.

---

## 📋 Opgavebeskrivelse

Byg en multi-site topologi der simulerer:
- **Hovedkontor** med IT-afdelingen
- **Produktionssite** med PLC'er og HMI
- **Fjerntlager** med sensorer

Alle forbundet via dedikerede routere.

```
┌────────────────┐         ┌────────────────┐         ┌────────────────┐
│  Hovedkontor   │         │  Produktion    │         │  Fjerntlager   │
│                │         │                │         │                │
│   PC-IT        │         │   HMI          │         │   PC-Lager     │
│ 192.168.10.10  │         │ 10.50.0.10     │         │ 10.60.0.10     │
│      /24       │         │    /16         │         │    /16         │
└───────┬────────┘         └───────┬────────┘         └───────┬────────┘
        │                          │                          │
   192.168.10.1                10.50.0.1                  10.60.0.1
        │                          │                          │
   ┌────┴─────┐              ┌─────┴──────┐            ┌──────┴─────┐
   │ Router-1 │              │  Router-2  │            │  Router-3  │
   │ (IT-GW)  │              │ (Prod-GW)  │            │ (Lager-GW) │
   └────┬─────┘              └─────┬──────┘            └──────┬─────┘
        │.1                        │.2                        │.3
        └──────┬───────────────────┴────────────────┬─────────┘
               │     10.100.0.0/24 (Transit Net)    │
               │                                    │
```

**Transit Network:** Et dedikeret netværk kun til router-til-router kommunikation.

---

## 🔧 Trin-for-trin implementering

### Trin 1: Opret topologi i GNS3

1. **Komponenter:**
   - 3x Alpine Linux (Router-1, Router-2, Router-3)
   - 1x Switch (for transit network)
   - 3x VPCS (PC-IT, HMI, PC-Lager)

2. **Forbindelser:**
   - Router-1 eth0 ↔ PC-IT
   - Router-2 eth0 ↔ HMI
   - Router-3 eth0 ↔ PC-Lager
   - Router-1 eth1 ↔ Switch
   - Router-2 eth1 ↔ Switch
   - Router-3 eth1 ↔ Switch

### Trin 2: Konfigurer Router-1 (IT-Gateway)

```bash
# IP på lokalt netværk (til PC-IT)
ip addr add 192.168.10.1/24 dev eth0
ip link set eth0 up

# IP på transit netværk
ip addr add 10.100.0.1/24 dev eth1
ip link set eth1 up

# Aktivér routing
sysctl -w net.ipv4.ip_forward=1

# Tilføj statiske routes til de andre sites
ip route add 10.50.0.0/16 via 10.100.0.2
ip route add 10.60.0.0/16 via 10.100.0.3

# Vis routing-tabel
ip route show
```

### Trin 3: Konfigurer Router-2 (Produktion-Gateway)

```bash
# IP på lokalt netværk (til HMI)
ip addr add 10.50.0.1/16 dev eth0
ip link set eth0 up

# IP på transit netværk
ip addr add 10.100.0.2/24 dev eth1
ip link set eth1 up

# Aktivér routing
sysctl -w net.ipv4.ip_forward=1

# Tilføj statiske routes
ip route add 192.168.10.0/24 via 10.100.0.1
ip route add 10.60.0.0/16 via 10.100.0.3

# Vis routing-tabel
ip route show
```

### Trin 4: Konfigurer Router-3 (Lager-Gateway)

```bash
# IP på lokalt netværk (til PC-Lager)
ip addr add 10.60.0.1/16 dev eth0
ip link set eth0 up

# IP på transit netværk
ip addr add 10.100.0.3/24 dev eth1
ip link set eth1 up

# Aktivér routing
sysctl -w net.ipv4.ip_forward=1

# Tilføj statiske routes
ip route add 192.168.10.0/24 via 10.100.0.1
ip route add 10.50.0.0/16 via 10.100.0.2

# Vis routing-tabel
ip route show
```

### Trin 5: Konfigurer klienter

```bash
# PC-IT (VPCS)
ip 192.168.10.10/24 192.168.10.1

# HMI (VPCS)
ip 10.50.0.10/16 10.50.0.1

# PC-Lager (VPCS)
ip 10.60.0.10/16 10.60.0.1
```

### Trin 6: Test multi-hop routing

```bash
# Fra PC-IT til HMI (2 hop)
ping 10.50.0.10

# Fra PC-IT til PC-Lager (2 hop)
ping 10.60.0.10

# Fra HMI til PC-Lager (2 hop)
ping 10.60.0.10

# Brug traceroute for at se hele ruten
traceroute 10.50.0.10
```

**Forventet traceroute output fra PC-IT til HMI:**
```
1  192.168.10.1    (Router-1)
2  10.100.0.2      (Router-2)
3  10.50.0.10      (HMI)
```

---

## 📊 Dokumentationskrav

### 1. Netværksdiagram

Tegn topologien og inkluder:
- Alle routere med interface-numre
- Alle IP-adresser og subnet masks
- Transit netværk markeret tydeligt
- Pile der viser routing-retninger

### 2. Routing-tabeller fra alle routere

#### Router-1 routing table:
```
[Indsæt output fra: ip route show]
```

**Analyser:**
- Hvilke routes er direkte tilkoblede (proto kernel)?
- Hvilke er statisk konfigurerede (proto static)?
- Hvad er next-hop for at nå 10.50.0.0/16?

#### Router-2 routing table:
```
[Indsæt output]
```

#### Router-3 routing table:
```
[Indsæt output]
```

### 3. Traceroute analyse

Kør traceroute fra hver klient til de andre:

| Fra      | Til         | Hop 1        | Hop 2        | Hop 3       | Total hops |
|----------|-------------|--------------|--------------|-------------|------------|
| PC-IT    | HMI         |              |              |             |            |
| PC-IT    | PC-Lager    |              |              |             |            |
| HMI      | PC-IT       |              |              |             |            |
| HMI      | PC-Lager    |              |              |             |            |
| PC-Lager | PC-IT       |              |              |             |            |
| PC-Lager | HMI         |              |              |             |            |

### 4. Pakke-flow detaljeret

Vælg én kommunikation (f.eks. PC-IT → HMI) og beskriv:

**ICMP Echo Request:**
```
1. PC-IT (192.168.10.10) sender til HMI (10.50.0.10)
2. PC-IT ser at destination ikke er på lokalt netværk
3. PC-IT sender til default gateway: 192.168.10.1
4. Router-1 modtager på eth0
5. Router-1 konsulterer routing-tabel:
   - 10.50.0.0/16 via 10.100.0.2
6. Router-1 sender via eth1 til 10.100.0.2
7. Router-2 modtager på eth1
8. Router-2 konsulterer routing-tabel:
   - 10.50.0.0/16 dev eth0 (direkte tilkoblet)
9. Router-2 sender via eth0 til 10.50.0.10
10. HMI modtager ICMP Echo Request
```

**ICMP Echo Reply:**
```
[Beskriv returvejen]
```

---

## 🤔 Refleksionsspørgsmål

1. **Hvad er formålet med transit netværket (10.100.0.0/24)?**
   - Hvorfor ikke bare forbinde alle routere direkte til hinanden?

2. **Hvad sker der hvis Router-2 ikke har en route til 192.168.10.0/24?**
   - Test det! Slet routen og prøv at pinge. Hvad returnerer Router-2?

3. **Hvor mange routing-entries skal der til i dette netværk?**
   - Router-1: _____ routes
   - Router-2: _____ routes
   - Router-3: _____ routes

4. **I et rigtigt industrinetværk med 50 sites - er statisk routing stadig praktisk?**
   - Hvad er fordele/ulemper?

5. **Hvad betyder "asymmetrisk routing"?**
   - Kan pakker tage én vej frem og en anden vej retur?

---

## 🎯 Ekstra udfordringer

### Udfordring 1: Tilføj en 4. router og site

Tilføj "Vedligeholdelses-site" (10.70.0.0/16) med Router-4:
- Opdater ALLE routing-tabeller
- Test kommunikation
- Dokumentér hvor mange routes hver router nu har

### Udfordring 2: Default route experiment

Fjern alle specifikke routes fra Router-1 og tilføj kun:
```bash
ip route add default via 10.100.0.2
```

- Hvad virker? Hvad virker ikke?
- Hvorfor er default routes problematiske i multi-router setups?

### Udfordring 3: Route metrics

Tilføj en ekstra forbindelse mellem Router-1 og Router-2:
```
Router-1 eth2 (10.101.0.1) ↔ Router-2 eth2 (10.101.0.2)
```

Konfigurer to routes til samme destination med forskellige metrics:
```bash
# På Router-1
ip route add 10.50.0.0/16 via 10.100.0.2 metric 10
ip route add 10.50.0.0/16 via 10.101.0.2 metric 20
```

- Hvilken route bruges?
- Hvad sker der hvis du slukker for eth1?

### Udfordring 4: Simulate link failure

Sluk for en router-interface:
```bash
ip link set eth1 down
```

- Kan netværket stadig kommunikere?
- Hvordan ville du designe netværket for redundans?

---

## ✅ Checklist før aflevering

- [ ] Alle 3 routere kører og er konfigureret
- [ ] Alle klienter kan pingge alle andre klienter
- [ ] Netværksdiagram inkluderer transit netværk
- [ ] Routing-tabeller fra alle routere dokumenteret
- [ ] Traceroute kørt mellem alle kombinationer
- [ ] Pakke-flow analyseret i begge retninger
- [ ] Refleksionsspørgsmål besvaret
- [ ] Screenshots af vellykket multi-hop ping
- [ ] Screenshots af traceroute output
- [ ] Fil uploadet til GitHub i `dag10-ditnavn/opgave2.md`

---

**Dette er sådan virkelige industri-netværk fungerer! 🏭🛤️**
