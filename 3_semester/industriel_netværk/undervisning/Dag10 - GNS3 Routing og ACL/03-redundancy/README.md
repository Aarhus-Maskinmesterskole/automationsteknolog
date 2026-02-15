# Opgave 3: Redundante ruter og failover

## 🎯 Formål

I industrielle netværk er oppetid kritisk. Lær at konfigurere redundante routes med forskellige prioriteter, så netværket automatisk failover til backup-forbindelser.

---

## 📋 Opgavebeskrivelse

Byg et netværk med **to parallelle forbindelser** mellem sites, hvor den ene er primary (hurtig) og den anden er backup (langsom, men pålidelig).

```
                        ┌──────────────┐
                        │  Produktion  │
                        │              │
                        │    HMI       │
                        │  10.50.0.10  │
                        └──────┬───────┘
                               │ 10.50.0.1
                               │
                         ┌─────┴──────┐
     Primary (100Mbit)   │  Router-2  │  Backup (10Mbit)
     Metric 10          /│ (Prod-GW)  │\  Metric 100
                       / └────────────┘ \
                      /                  \
            10.100.0.2                    10.200.0.2
                    /                      \
                   /                        \
         10.100.0.1                          10.200.0.1
                 /                              \
                /                                \
        ┌──────┴────────┐                ┌──────┴────────┐
        │   Router-1    │                │   Router-1    │
        │   (IT-GW)     │                │   (IT-GW)     │
        │   eth1        │                │   eth2        │
        └──────┬────────┘                └───────────────┘
               │ 192.168.10.1
               │
        ┌──────┴──────┐
        │ Hovedkontor │
        │             │
        │   PC-IT     │
        │192.168.10.10│
        └─────────────┘
```

**Koncept:**
- Primary route (metric 10): Hurtig forbindelse
- Backup route (metric 100): Langsom backup
- Hvis primary fejler, tager Linux automatisk backup-routen

---

## 🔧 Trin-for-trin implementering

### Trin 1: Opret topologi i GNS3

1. **Komponenter:**
   - 2x Alpine Linux (Router-1, Router-2)
   - 2x VPCS (PC-IT, HMI)

2. **Forbindelser:**
   - Router-1 eth0 ↔ PC-IT
   - Router-2 eth0 ↔ HMI
   - Router-1 eth1 ↔ Router-2 eth1 (Primary link)
   - Router-1 eth2 ↔ Router-2 eth2 (Backup link)

### Trin 2: Konfigurer Router-1 (IT-Gateway)

```bash
# Lokalt netværk
ip addr add 192.168.10.1/24 dev eth0
ip link set eth0 up

# Primary link
ip addr add 10.100.0.1/30 dev eth1
ip link set eth1 up

# Backup link
ip addr add 10.200.0.1/30 dev eth2
ip link set eth2 up

# Aktivér routing
sysctl -w net.ipv4.ip_forward=1

# Tilføj routes med forskellige metrics
# Primary route (lav metric = høj prioritet)
ip route add 10.50.0.0/16 via 10.100.0.2 metric 10

# Backup route (høj metric = lav prioritet)
ip route add 10.50.0.0/16 via 10.200.0.2 metric 100

# Vis routing-tabel
ip route show
```

**Forventet output:**
```
192.168.10.0/24 dev eth0 proto kernel scope link src 192.168.10.1
10.100.0.0/30 dev eth1 proto kernel scope link src 10.100.0.1
10.200.0.0/30 dev eth2 proto kernel scope link src 10.200.0.1
10.50.0.0/16 via 10.100.0.2 dev eth1 metric 10
10.50.0.0/16 via 10.200.0.2 dev eth2 metric 100
```

> **Bemærk:** Begge routes til 10.50.0.0/16 er i tabellen! Linux vælger den med laveste metric.

### Trin 3: Konfigurer Router-2 (Produktion-Gateway)

```bash
# Lokalt netværk
ip addr add 10.50.0.1/16 dev eth0
ip link set eth0 up

# Primary link
ip addr add 10.100.0.2/30 dev eth1
ip link set eth1 up

# Backup link
ip addr add 10.200.0.2/30 dev eth2
ip link set eth2 up

# Aktivér routing
sysctl -w net.ipv4.ip_forward=1

# Tilføj redundante routes
ip route add 192.168.10.0/24 via 10.100.0.1 metric 10
ip route add 192.168.10.0/24 via 10.200.0.1 metric 100

# Vis routing-tabel
ip route show
```

### Trin 4: Konfigurer klienter

```bash
# PC-IT (VPCS)
ip 192.168.10.10/24 192.168.10.1

# HMI (VPCS)
ip 10.50.0.10/16 10.50.0.1
```

### Trin 5: Test normal drift (primary route)

```bash
# På PC-IT
ping 10.50.0.10

# På Router-1 - se hvilken route der bruges
ip route get 10.50.0.10

# Forventet output:
# 10.50.0.10 via 10.100.0.2 dev eth1 src 192.168.10.1
```

### Trin 6: Simuler link failure - test failover

```bash
# På Router-1 - sluk for primary link
ip link set eth1 down

# STRAKS derefter - ping fra PC-IT
ping 10.50.0.10

# På Router-1 - se at backup route nu bruges
ip route get 10.50.0.10

# Forventet output:
# 10.50.0.10 via 10.200.0.2 dev eth2 src 192.168.10.1
```

**Observation:**
- Ping fortsætter (måske nogle pakker tabes under failover)
- Netværket er stadig operationelt
- Automatisk failover uden manuel indgriben!

### Trin 7: Test failback

```bash
# På Router-1 - genaktiver primary link
ip link set eth1 up

# Vent 2-3 sekunder

# Tjek hvilken route der nu bruges
ip route get 10.50.0.10

# Forventet: Tilbage til primary route
# 10.50.0.10 via 10.100.0.2 dev eth1 src 192.168.10.1
```

---

## 📊 Dokumentationskrav

### 1. Netværksdiagram

Tegn topologien med:
- Begge links markeret (primary og backup)
- Metrics angivet på hver route
- Test-scenarierne illustreret

### 2. Routing-tabel analyse

#### Normal drift (begge links oppe):

Router-1 routing table:
```
[Indsæt output fra: ip route show]
```

**Spørgsmål:**
- Kan du se begge routes til 10.50.0.0/16?
- Hvilken bruges ved `ip route get 10.50.0.10`?

#### Under primary link failure:

Router-1 routing table efter `ip link set eth1 down`:
```
[Indsæt output fra: ip route show]
```

**Spørgsmål:**
- Er primary routen forsvundet fra tabellen?
- Hvilken route bruges nu?

### 3. Failover test-resultater

| Test fase          | Primary link | Backup link | Ping resultat | Route used | Packet loss |
|--------------------|--------------|-------------|---------------|------------|-------------|
| Normal drift       | UP           | UP          | ✅/❌         | via .2 eth1 |             |
| Primary ned        | DOWN         | UP          | ✅/❌         | via .2 eth2 |             |
| Genaktiver primary | UP           | UP          | ✅/❌         | via .2 eth1 |             |
| Backup ned         | UP           | DOWN        | ✅/❌         | via .2 eth1 |             |
| Begge ned          | DOWN         | DOWN        | ✅/❌         | N/A        | 100%        |

### 4. Failover timing

Kør kontinuerlig ping under failover:
```bash
ping -i 0.2 10.50.0.10
```

Mens den kører, sluk for eth1.

**Dokumenter:**
- Hvor mange pakker går tabt under failover?
- Hvor lang tid tager failover? (tæl tabet)
- Er det acceptabelt for industriel kommunikation?

---

## 🤔 Refleksionsspørgsmål

1. **Hvorfor ikke bare bruge to routes med samme metric?**
   - Hvad ville Linux gøre i det tilfælde? (søg: ECMP - Equal Cost Multi-Path)

2. **I et rigtigt setup med PLC-kommunikation - kan du miste data under failover?**
   - Hvad afhænger det af? (TCP vs. UDP)

3. **Hvad er forskellen på redundans på:**
   - **Layer 2** (to switches med STP)
   - **Layer 3** (to routes med metric)

4. **I Purdue-modellen - hvor ville du placere redundans?**
   - Mellem hvilke zoner er redundans mest kritisk?

5. **Hvad er "split-brain" problemet ved redundans?**
   - Kan det ske med statisk routing?

---

## 🎯 Ekstra udfordringer

### Udfordring 1: Tre parallelle forbindelser

Tilføj en 3. forbindelse (eth3 ↔ eth3) mellem routerne:
- Metric 200 (tertiary backup)
- Test failover gennem alle tre niveauer

```bash
# Primary down
ip link set eth1 down
# → Failover til backup

# Backup down
ip link set eth2 down
# → Failover til tertiary

# Genaktivér primary
ip link set eth1 up
# → Failback til primary
```

### Udfordring 2: Asymmetrisk routing

Konfigurer:
- Router-1: Primary via eth1 (metric 10), Backup via eth2 (metric 100)
- Router-2: Primary via eth2 (metric 10), Backup via eth1 (metric 100)

**Resultat:** Traffik frem går via ét link, traffik retur via et andet!

- Hvordan ser traceroute ud?
- Er det et problem i industrien?

### Udfordring 3: Bandwidth simulation

GNS3 doesn't natively simulate bandwidth, but document:
- Hvordan ville du måle om primary er hurtigere?
- Hvad er RTT på primary vs. backup?
- Kunne du bruge `tc` (traffic control) til at simulere delay?

```bash
# Simuler 100ms delay på backup link
tc qdisc add dev eth2 root netem delay 100ms
```

### Udfordring 4: Monitoring script

Skriv et bash-script der:
1. Kører kontinuerlig ping
2. Logger hvilken route der bruges
3. Logger tidspunkt for failover
4. Beregner failover-tid

```bash
#!/bin/sh
while true; do
    ROUTE=$(ip route get 10.50.0.10 | head -n1)
    echo "$(date +%T) - $ROUTE"
    sleep 1
done
```

---

## ✅ Checklist før aflevering

- [ ] Topologi oprettet med to parallelle links
- [ ] Routing konfigureret med forskellige metrics
- [ ] Normal drift testet og dokumenteret
- [ ] Failover testet ved at slukke primary link
- [ ] Failback testet ved at genaktivere primary link
- [ ] Routing-tabeller før og efter failover dokumenteret
- [ ] Packet loss under failover målt
- [ ] Refleksionsspørgsmål besvaret
- [ ] Screenshots af `ip route show` i alle faser
- [ ] Screenshots af vellykket ping under alle scenarier
- [ ] Fil uploadet til GitHub i `dag10-ditnavn/opgave3.md`

---

**Redundans er nøglen til high-availability industrinetværk! 🔄🏭**
