# Opgave 4: Fejlfinding - Routing loops og fejlkonfiguration

## 🎯 Formål

Lær at identificere, diagnosticere og løse almindelige routing-fejl i industrielle netværk. Forstå hvordan routing loops opstår og hvordan TTL beskytter mod dem.

---

## 📋 Opgavebeskrivelse

Du får flere **fejlbehæftede** netværksscenarier. Din opgave er at:
1. Identificere fejlen
2. Diagnosticere med netværksværktøjer
3. Forklare hvad der er galt
4. Rette fejlen
5. Dokumentere løsningen

---

## 🔍 Scenarie 1: Den mystiske routing loop

### Setup

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   PC-A      │         │  Router-1   │         │  Router-2   │         │   PC-B      │
│ 10.10.0.10  │────────►│             │────────►│             │────────►│ 10.20.0.10  │
│    /16      │ eth0    │  10.10.0.1  │ eth1    │  10.20.0.1  │ eth0    │    /16      │
└─────────────┘         │  10.99.0.1  │         │  10.99.0.2  │         └─────────────┘
                        └─────────────┘         └─────────────┘
```

### Fejlbehæftet konfiguration

**Router-1:**
```bash
ip addr add 10.10.0.1/16 dev eth0
ip addr add 10.99.0.1/24 dev eth1
ip link set eth0 up
ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1

# FEJL: Default route peger tilbage mod Router-2
ip route add default via 10.99.0.2
```

**Router-2:**
```bash
ip addr add 10.20.0.1/16 dev eth0
ip addr add 10.99.0.2/24 dev eth1
ip link set eth0 up
ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1

# FEJL: Route til 10.10.0.0 peger tilbage mod Router-1
ip route add 10.10.0.0/16 via 10.99.0.1
```

### Din opgave

1. **Byg topologien** i GNS3 med ovenstående konfiguration

2. **Prøv at pinge** fra PC-A til PC-B:
   ```bash
   ping 10.20.0.10
   ```

3. **Observér fejlen:**
   - Hvad sker der?
   - Får du svar?
   - Hvad viser traceroute?

4. **Diagnosticér:**
   ```bash
   # Kør traceroute
   traceroute 10.20.0.10
   
   # På Router-1 - følg pakke-flowet
   tcpdump -i any icmp -n
   ```

5. **Besvar:**
   - Hvad er problemet?
   - Hvorfor stopper ping'en ikke med det samme?
   - Hvad er TTL's rolle?

6. **Ret fejlen** - dokumentér den korrekte konfiguration

---

## 🔍 Scenarie 2: Den manglende return-route

### Setup

```
┌─────────────┐    eth0  ┌─────────────┐  eth1   ┌─────────────┐
│   PC-IT     │─────────►│  Router-1   │────────►│  Router-2   │
│192.168.1.10 │          │192.168.1.1  │         │ 10.50.0.1   │
│    /24      │          │ 10.100.0.1  │         │ 10.50.0.1   │
└─────────────┘          └─────────────┘         │ 10.100.0.2  │
                                                  └──────┬──────┘
                                                     eth0 │
                                                          │
                                                   ┌──────┴──────┐
                                                   │    HMI      │
                                                   │  10.50.0.10 │
                                                   └─────────────┘
```

### Fejlbehæftet konfiguration

**Router-1:**
```bash
ip addr add 192.168.1.1/24 dev eth0
ip addr add 10.100.0.1/30 dev eth1
ip link set eth0 up
ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1

# Korrekt route til destinationen
ip route add 10.50.0.0/16 via 10.100.0.2
```

**Router-2:**
```bash
ip addr add 10.50.0.1/16 dev eth0
ip addr add 10.100.0.2/30 dev eth1
ip link set eth0 up
ip link set eth1 up
sysctl -w net.ipv4.ip_forward=1

# FEJL: Ingen return-route til 192.168.1.0/24!
# (routing-entry mangler)
```

### Din opgave

1. **Byg og konfigurer** topologien

2. **Test ping** fra PC-IT til HMI:
   ```bash
   ping 10.50.0.10
   ```

3. **Observér:**
   - Får du svar?
   - Hvad viser `ping -c 4 10.50.0.10`?

4. **Diagnosticér på Router-2:**
   ```bash
   # Lyt efter ICMP pakker
   tcpdump -i any icmp -n
   
   # Ser du Echo Request? Ser du Echo Reply?
   ```

5. **Diagnosticér routing-tabeller:**
   ```bash
   # På Router-2
   ip route show
   ip route get 192.168.1.10
   ```

6. **Besvar:**
   - Når pakkerne frem til HMI?
   - Når reply-pakkerne tilbage?
   - Hvad mangler i Router-2's routing-tabel?

7. **Ret fejlen** og dokumentér løsningen

---

## 🔍 Scenarie 3: Forkert subnet mask

### Setup

```
┌─────────────┐         ┌─────────────┐
│   PC-A      │         │  Router     │         │   PC-B      │
│ 10.0.1.10   │────────►│ 10.0.1.1    │────────►│ 10.0.2.10   │
│  /24 <FEJL  │         │ eth0: /16   │         │  /16        │
└─────────────┘         │ 10.0.2.1    │         └─────────────┘
                        │ eth1: /16   │
                        └─────────────┘
```

### Fejlbehæftet konfiguration

**PC-A:** (FEJL!)
```bash
ip 10.0.1.10/24 10.0.1.1
```

**Router:**
```bash
ip addr add 10.0.1.1/16 dev eth0
ip addr add 10.0.2.1/16 dev eth1
# ... osv
```

**PC-B:**
```bash
ip 10.0.2.10/16 10.0.2.1
```

### Din opgave

1. **Konfigurer** med ovenstående (med fejlen!)

2. **Test ping:**
   ```bash
   # Fra PC-A
   ping 10.0.2.10
   ```

3. **Observér:**
   - Virker ping fra PC-A til routeren (10.0.1.1)?
   - Virker ping fra PC-A til PC-B (10.0.2.10)?
   - Hvorfor/hvorfor ikke?

4. **Besvar:**
   - PC-A tror den er i 10.0.1.0/24 subnet
   - Router tror der er et 10.0.0.0/16 subnet
   - Hvad sker der når PC-A skal sende til 10.0.2.10?
   - Tror PC-A at destination er på samme subnet?

5. **Ret fejlen:**
   ```bash
   # Korrekt konfiguration for PC-A
   ip 10.0.1.10/16 10.0.1.1
   ```

6. **Dokumentér** hvorfor subnet mask skal matche

---

## 🔍 Scenarie 4: Duplicate IP address

### Setup

To enheder har samme IP-adresse i netværket!

```
┌─────────────┐         
│   PC-A      │         
│ 10.0.1.10   │◄────┐
└─────────────┘     │
                    │   
       Switch ──────┤
                    │
┌─────────────┐     │
│   PC-B      │     │
│ 10.0.1.10   │◄────┘  <── FEJL: Samme IP!
└─────────────┘
```

### Din opgave

1. **Opsæt** to VPCS med samme IP

2. **Prøv at pinge** fra en 3. PC til 10.0.1.10:
   ```bash
   ping 10.0.1.10
   ```

3. **Observér:**
   - Varierer RTT (round-trip time)?
   - Får du svar fra to forskellige MAC-adresser?

4. **Diagnosticér med ARP:**
   ```bash
   # På routeren eller en anden PC
   arp -n
   
   # Eller
   ip neigh show
   ```

5. **Besvar:**
   - Hvordan opdager du at to enheder har samme IP?
   - Hvad er symptomerne?
   - Hvorfor er dette katastrofalt i industrien?

6. **Dokumentér** hvordan man undgår dette (IP-planlægning!)

---

## 🔍 Scenarie 5: MTU mismatch og fragmentering

### Setup

Router med lav MTU:

```bash
# På router eth1 - reducer MTU
ip link set eth1 mtu 500
```

### Din opgave

1. **Opsæt** netværk med router hvor eth1 har MTU=500

2. **Test med forskellige pakke-størrelser:**
   ```bash
   # Små pakker (OK)
   ping -s 100 10.20.0.10
   
   # Store pakker (problem?)
   ping -s 1400 10.20.0.10
   
   # Med Don't Fragment flag
   ping -s 1400 -M do 10.20.0.10
   ```

3. **Observér:**
   - Hvilke pings virker?
   - Hvad sker der med store pakker?

4. **Diagnosticér med tcpdump:**
   ```bash
   tcpdump -i eth1 -n
   ```

5. **Besvar:**
   - Hvad er MTU?
   - Hvordan håndterer Linux store pakker på små MTU-links?
   - Hvad betyder "Frag needed" ICMP-beskeder?

---

## 📊 Dokumentationskrav

For **hvert scenarie**, dokumentér:

### 1. Problemdiagnose

```markdown
## Scenarie X: [Navn]

### Symptomer observeret:
- Hvad virkede ikke?
- Hvad returnerede ping/traceroute?

### Diagnosticeringsværktøjer brugt:
- tcpdump output
- ip route show output
- traceroute output
- arp-tabel

### Root cause analyse:
- Hvad var fejlen?
- Hvorfor opstod problemet?
- Hvilken networking-regel blev brudt?
```

### 2. Løsning

```markdown
### Løsning implementeret:

**Før (fejl):**
\```bash
[fejlbehæftet kommando]
\```

**Efter (rettet):**
\```bash
[korrekt kommando]
\```

### Verifikation:
- Ping resultat efter fix
- Routing-tabel efter fix
- Screenshot af vellykket kommunikation
```

### 3. Lektier lært

```markdown
### Hvad lærte jeg?

1. [Vigtig indsigt fra dette scenarie]
2. [Hvordan undgår jeg dette i praksis]
3. [Hvilke værktøjer hjælper med at diagnosticere dette]
```

---

## 🤔 Generelle refleksionsspørgsmål

1. **Hvad er de 3 mest almindelige routing-fejl i industrien?**
   - Baseret på dine tests

2. **Hvordan forebygger man routing loops?**
   - Dokumentation?
   - Naming conventions?
   - Automated verification?

3. **Hvad er forskellen på:**
   - **Black hole routing** (pakker forsvinder)
   - **Routing loop** (pakker cirkulerer)
   - **Asymmetrisk routing** (forskellige veje frem/tilbage)

4. **Hvordan ville du dokumentere routing i et produktionsnetværk?**
   - Excel ark?
   - Network diagram tool?
   - Automated discovery?

5. **I en nødsituation hvor produktionen er stoppet - hvilken værktøj bruger du først?**
   - ping? traceroute? tcpdump? ip route show?

---

## 🎯 Ekstra udfordring: "Fix the broken network"

### Mystery network

Du får denne GNS3-topologi (byg den):

```
PC-A ─── R1 ─── R2 ─── R3 ─── PC-B
        (???)(???)(???)
```

**Konfigurationen er mystisk og fejlbehæftet!**

Routerne er allerede konfigureret (men forkert). Din opgave:
1. Ping fra PC-A til PC-B fejler
2. Diagnosticér systematisk
3. Find ALLE fejl
4. Ret dem én ad gangen
5. Dokumentér hver fejl og fix

**Mulige fejl indbygget:**
- Routing loop mellem R2 og R3
- Manglende return-route i R1
- Forkert subnet mask på PC-A
- ip_forward ikke aktiveret på R2
- Duplicate IP mellem R2 og R3

---

## ✅ Checklist før aflevering

- [ ] Alle 5 scenarier gennemført og dokumenteret
- [ ] For hver scenarie: symptomer, diagnose, root cause, løsning
- [ ] Screenshots af fejl og vellykket fix
- [ ] tcpdump/traceroute output inkluderet hvor relevant
- [ ] Refleksionsspørgsmål besvaret
- [ ] "Lektier lært" sektion for hvert scenarie
- [ ] Fil uploadet til GitHub i `dag10-ditnavn/opgave4.md`

---

## 💡 Pro tips til fejlfinding

### Systematisk tilgang:

1. **Verificér layer 1-2:**
   - Er links up? (`ip link show`)
   - Kan du ping gateway lokalt?

2. **Verificér layer 3:**
   - Er IP-adresser korrekte? (`ip addr show`)
   - Er subnet masks korrekte?
   - Er routing-tabeller komplette? (`ip route show`)

3. **Trace pakke-flowet:**
   - Hvorfra til hvortil?
   - Gennem hvilke routere?
   - Kommer pakker frem? (`tcpdump`)
   - Kommer reply tilbage?

4. **Check for almindelige fejl:**
   - Manglende routes
   - Routing loops
   - ip_forward ikke aktiveret
   - Firewall blokeringer
   - Forkerte subnet masks

### Værktøjskasse:

```bash
# Basis connectivity
ping -c 4 <destination>

# Se rutevej
traceroute <destination>

# Tjek routing
ip route show
ip route get <destination>

# Lyt på traffik
tcpdump -i <interface> icmp -n

# Tjek interfaces
ip link show
ip addr show

# Tjek ARP
ip neigh show

# Test specifik source
ping -I <interface> <destination>
```

---

**Fejlfinding er en kunst - øv dig! 🔍🛠️**
