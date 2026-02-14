## Grundlæggende ip addressing
Vis, tilføj og fjern IP-adresser, aktiver/deaktivér netværksinterfaces, og administrer routing-tabeller ved hjælp af `ip`-kommandoen:
```bash
ip addr show  # Vis netværksinterfaces og adresser
ip addr show dev eth0  # Vis detaljer for et specifikt interface
ip addr add 192.168.1.1/24 dev eth0  # Tilføj IP-adresse til interface
ip addr del 192.168.1.1/24 dev eth0  # Fjern IP-adresse fra interface
```

Sæt et interface op eller ned, og vis dets status:
```bash
ip link set dev eth0 up    # Aktivér interface
ip link set dev eth0 down  # Deaktivér interface
ip link show dev eth0     # Vis status for interface
```
Vis, tilføj og fjern ruter i routing-tabellen:
```bash
ip route show  # Vis routing tabel
ip route add default via 192.168.1.254  # Tilføj standard gateway
ip route del default via 192.168.1.254  # Fjern standard gateway
ip route add 192.168.1.0/24 dev eth0  # Tilføj statisk rute
ip route del 192.168.1.0/24 dev eth0  # Fjern statisk rute
```
Sæt permanente IP-adresser og ruter ved at redigere netværkskonfigurationsfilerne, som varierer afhængigt af distributionen (f.eks. `/etc/network/interfaces` for Debian-baserede systemer eller netplan-konfigurationsfiler).

```bash
vi /etc/network/interfaces  # Rediger netværkskonfiguration på Debian-baserede systemer
```
Brug `insert`-kommandoen i `vi` til at tilføje eller ændre IP-adresser og ruter. Den vil vise `I` istedet for `-`. Brug esc for at afslutte indsættelsestilstand, og skriv `:wq` for at gemme og afslutte filen.

for at sætte en eth interface til dhcp brug:
```bash
udhcp eth0
```

for at sætte en eth interface til permanen dhcp brug skriv i /etc/network/interfaces:
```bash
auto eth0
iface eth0 inet dhcp
```

**Eksempel på netværkskonfiguration i `/etc/network/interfaces`:**
```bash
auto eth0
iface eth0 inet static
    address 192.168.1.100
    netmask 255.255.255.0
    gateway 192.168.1.1

auto eth1
iface eth1 inet dhcp
```

---

## Grundlæggende nftables-begreber

* **Table:** En samling af chains og regler, organiseret efter formål (f.eks. *filter* eller *nat*) og protokol (ip, ip6, inet).

  * **filter:** Bruges til at bestemme, hvilken trafik der skal tillades eller blokeres (klassisk firewall).
  * **nat:** Bruges til at oversætte IP-adresser, f.eks. ved internetdeling eller overlappende netværk.
* **Chain:** En sekvens af regler, der udføres for en bestemt type trafik (*input*, *output* eller *forward*). Hver chain har et *hook*, som bestemmer, **hvornår** den aktiveres i pakkens rejse gennem systemet.
* **Rule:** En enkelt regel, der matcher trafik og udfører en handling (f.eks. *accept*, *drop*, *log* eller *masquerade*).
* **Protokolfamilier:**

  * **ip:** IPv4-trafik
  * **ip6:** IPv6-trafik
  * **inet:** Dækker både IPv4 og IPv6 (typisk brugt i moderne opsætninger)

---

### Sådan bygger du tables, chains og rules (trin for trin)

1. **Table:** Start med at oprette en table. En table fungerer som en “mappe” til dine firewall-regler.

   ```bash
   nft add table inet filter
   ```

   Her oprettes en table kaldet **filter**, der håndterer både IPv4 og IPv6-trafik.

---

2. **Chain:** Opret derefter en chain i tabellen. En chain er en “række” af regler, der udføres for en bestemt type trafik.

   ```bash
   nft add chain inet filter input { type filter hook input priority 0; policy drop; }
   ```

   Denne kommando opretter en chain kaldet **input** i tabellen **filter**, der aktiveres for indgående trafik og som **dropper alt** som udgangspunkt (bedste praksis).

**Forklaring af parametre:**

* `type filter` — Chain bruges til filtrering af trafik (firewall).
* `type nat` — Chain bruges til NAT (adresseoversættelse).
* `type route` — Chain til routing-beslutninger (sjældent anvendt).

**Hooks:**

* `hook input` — Trafik der **skal til routeren selv** (f.eks. SSH eller WireGuard).
* `hook output` — Trafik der **sendes ud fra routeren**.
* `hook forward` — Trafik der **videresendes gennem routeren** (routing mellem interfaces).
* `hook prerouting` — Bruges til NAT **før routing**.
* `hook postrouting` — Bruges til NAT **efter routing**.

**Prioritet (`priority`):**

* Bestemmer rækkefølgen, hvis flere chains bruger samme hook.
  Lavere tal betyder højere prioritet.
  `priority 0` er standard og dækker de fleste behov.

---

**Eksempler:**

```bash
# Filter-chain for indgående trafik (policy drop)
nft add chain inet filter input { type filter hook input priority 0; policy drop; }

# NAT-chain for udgående trafik
nft add chain ip nat postrouting { type nat hook postrouting priority 100; }

# Filter-chain for videresendt trafik
nft add chain inet filter forward { type filter hook forward priority 0; policy drop; }
```

---

3. **Rule:** Tilføj regler til din chain. En regel definerer, hvad der skal ske for bestemte pakker.

   ```bash
   nft add rule inet filter input ip saddr 192.168.1.0/24 accept
   nft add rule inet filter input drop
   ```

   Første regel tillader trafik fra lokalnettet (192.168.1.0/24).
   Anden regel dropper alt andet, fordi vi arbejder med “default deny”.

---

**Opsummering:**

* **Table** = “mappe” for regler
* **Chain** = “række” af regler for en bestemt trafiktype
* **Rule** = selve reglen (hvad der tillades, blokeres eller oversættes)

---

**Tip:**
Vis hele din aktive opsætning:

```bash
nft list ruleset
```

**Hint** : Gem din konfiguration i `/etc/nftables.conf` for at gøre den permanent ved opstart og indlæs den med:

```bash
vi /etc/network/interfaces

auto eth0
iface eth0 inet dhcp
    up nft -f /etc/nftables.conf

up sysctl -w net.ipv4.ip_forward=1
```
Dette eksempel viser at nftables konfigurationen bliver indlæst ved opstart af eth0 interface og ikke før, hvilket sikrer at firewall-reglerne er aktive, så snart netværksforbindelsen er oppe. Dernæst viser det at forwarding aktiveres uanset om eth0 er startet op.

---

Perfekt — her får du afsnittet **Routing** i samme klare og teknisk korrekte stil som det forrige.
Jeg har gjort sproget mere præcist, forklaret forskellen mellem *midlertidig* og *permanent* aktivering, og tilføjet små sikkerhedsnoter.

---

## Routing

For at din Linux-maskine kan fungere som router, skal **IP-forwarding** aktiveres.
Det gør, at kerne (kernel) må videresende pakker mellem interfaces — fx fra et VLAN til et andet eller mellem LAN og WAN.

---

### Midlertidig aktivering

Denne metode aktiverer routing med det samme, men ændringen forsvinder ved genstart:

```bash
sysctl -w net.ipv4.ip_forward=1
```

Eller den mere “rå” variant:

```bash
echo 1 | tee /proc/sys/net/ipv4/ip_forward
```

Begge udfører præcis samme handling — de ændrer værdien i kernelens runtime-parametre.

---

### Permanent aktivering

Vil du have routing slået til ved hver opstart, skal du gemme indstillingen i `/etc/sysctl.d/`:

```bash
echo "net.ipv4.ip_forward=1" | tee /etc/sysctl.d/99-router.conf
sysctl --system
```

**Forklaring:**

* Filer i `/etc/sysctl.d/` indlæses automatisk ved boot, i rækkefølge efter filnavn.
* `99-router.conf` er et godt navn, fordi den læses sidst og derfor overskriver eventuelle tidligere indstillinger.
* `sysctl --system` genindlæser alle systemparametre uden genstart.

---

### Verificér at routing er aktiv

Du kan tjekke status med:

```bash
sysctl net.ipv4.ip_forward
```

Et output på `net.ipv4.ip_forward = 1` betyder, at forwarding er aktiv.

---

### Bonus: IPv6-routing (valgfrit)

Vil du også tillade videresendelse af IPv6-trafik:

```bash
sysctl -w net.ipv6.conf.all.forwarding=1
```

Og permanent:

```bash
echo "net.ipv6.conf.all.forwarding=1" | tee -a /etc/sysctl.d/99-router.conf
sysctl --system
```

---

**Bemærk:**
Aktivering af IP-forwarding i sig selv åbner ikke noget for uønsket trafik.
Sikkerheden styres stadig af dine `nftables`-regler — derfor bør du altid kombinere routing med en firewall-konfiguration, hvor “policy drop” er standard.

---

Perfekt — her er afsnittet **“Eksempel: Basisopsætning af nftables”** rettet og udvidet i samme stil som de tidligere.
Jeg har bevaret dit pædagogiske flow, men gjort sproget lidt skarpere, tilføjet `policy drop` (for sikkerhed) og små tekniske præciseringer.

---

## Eksempel: Basisopsætning af nftables

Dette eksempel viser, hvordan du opsætter en helt basal firewall, som tillader trafik fra det lokale netværk og blokerer alt andet.
Strukturen kan senere udvides med flere regler og NAT.

---

### Trin for trin

```bash
# Opret tabel og chains
nft add table inet filter
nft add chain inet filter input   { type filter hook input   priority 0; policy drop; }
nft add chain inet filter forward { type filter hook forward priority 0; policy drop; }
nft add chain inet filter output  { type filter hook output  priority 0; policy accept; }

# Tillad trafik fra lokalnettet
nft add rule inet filter input ip saddr 192.168.1.0/24 accept

# Tillad etablerede forbindelser (returnerende trafik)
nft add rule inet filter input ct state established,related accept

# Drop og log alt andet
nft add rule inet filter input log prefix "DROP_INPUT: " counter drop
```
**Bemærk:** Output-kæden kører med policy accept, da firewallen normalt gerne må lave udgående forbindelser selv.
```

---

### Forklaring af konfigurationen

* **Table:** `inet filter` — håndterer både IPv4 og IPv6-trafik.
* **Chains:**

  * `input` — styrer trafik *til routeren selv*.
  * `forward` — styrer trafik *gennem routeren* (mellem interfaces).
  * `output` — styrer trafik *ud fra routeren* (routerens egne forbindelser).
* **policy drop:** betyder, at al trafik blokeres, medmindre en regel tillader den.
* **`ct state established,related`**: tillader returtrafik for allerede etablerede forbindelser (kernelens conntrack).
* **`counter`**: tæller, hvor mange gange reglen er ramt — nyttigt til fejlfinding.
* **`log prefix`**: tilføjer et prefix i systemloggen, så du kan se, hvad der bliver droppet.

---

### Gennemgang af flowet

1. Når en pakke rammer routeren, kontrolleres den i rækkefølge af reglerne i `input`.
2. Hvis pakken kommer fra 192.168.1.0/24 → **accepteres**.
3. Hvis pakken er del af en eksisterende forbindelse → **accepteres**.
4. Alt andet → **logges og droppes**.

Dette svarer til princippet *“allow known, drop the rest”*, som er standard i sikkerhedsdesign.

---

### Se eller gem opsætningen

Vis hele konfigurationen:

```bash
nft list ruleset
```

Gem den som standardopsætning:

```bash
sh -c 'nft list ruleset > /etc/nftables.conf'
systemctl enable --now nftables
```

Så vil reglerne automatisk blive indlæst ved næste opstart.

---

Perfekt — her kommer afsnittet **“NAT og netværks-til-netværks-NAT”** i samme teknisk korrekte og undervisningsvenlige stil som de forrige afsnit.
Jeg har gjort forklaringerne klarere, præciseret forskellen mellem *masquerade* og *SNAT*, og tilføjet små kommentarer, så læseren forstår, hvad der sker i hver linje.

---

## NAT og netværks-til-netværks-NAT

**NAT (Network Address Translation)** bruges til at oversætte IP-adresser mellem forskellige netværk.
Det er især nyttigt i to situationer:

1. Når flere interne enheder skal dele én offentlig IP-adresse (internetdeling).
2. Når to netværk med **overlappende subnets** skal kunne kommunikere (f.eks. ved virksomhedsfusion eller segmentering mellem IT/OT).

---

### 1. Internetdeling (klassisk masquerade-NAT)

Dette eksempel viser, hvordan du lader et internt netværk (LAN) få adgang til internettet via routerens udgående interface (WAN).

```bash
# Opret NAT-tabel og postrouting-chain
nft add table ip nat
nft add chain ip nat postrouting { type nat hook postrouting priority 100; policy accept; }

# Aktiver NAT (masquerade) på udgående interface (f.eks. eth1)
nft add rule ip nat postrouting oif "eth1" masquerade
```

**Forklaring:**

* **`table ip nat`**: NAT-tabellen arbejder kun med IPv4 (IPv6 bruger ikke masquerade på samme måde).
* **`hook postrouting`**: NAT udføres **efter** routing — når pakken er på vej ud af systemet.
* **`priority 100`**: standardværdi for postrouting-NAT.
* **`oif "eth1"`**: matcher det udgående interface (her WAN).
* **`masquerade`**: erstatter kildens IP med routerens egen udgående IP-adresse automatisk.

Denne metode bruges typisk, når din offentlige IP tildeles dynamisk (som ved mange internetforbindelser).

---

### 2. Fast NAT (SNAT og DNAT)

Hvis du har faste IP-adresser, eller du skal forbinde to interne netværk, kan du bruge **SNAT** (Source NAT) og **DNAT** (Destination NAT).

**Eksempel: Fast SNAT mellem interne netværk**

```bash
# Ændr kildens adresse fra 192.168.10.0/24 til 10.0.0.1, når den går ud af eth1
nft add rule ip nat postrouting ip saddr 192.168.10.0/24 oif "eth1" snat to 10.0.0.1
```

**Forklaring:**

* **SNAT (Source NAT)** ændrer **afsenderadressen** på udgående pakker.
* Bruges typisk mellem interne zoner, når adresser overlapper.

**Eksempel: DNAT til server i DMZ**

```bash
# Trafik til offentlig IP 203.0.113.5 oversættes til DMZ-server 192.168.20.10
nft add chain ip nat prerouting { type nat hook prerouting priority -100; policy accept; }
nft add rule ip nat prerouting iif "eth1" ip daddr 203.0.113.5 dnat to 192.168.20.10
```

**Forklaring:**

* **DNAT (Destination NAT)** ændrer **modtageradressen** på indgående pakker, så de videresendes til en intern host.
* `prerouting`-hook betyder, at oversættelsen sker **før** kernel beslutter, hvilket interface pakken skal sendes ud af.

---

### 3. NAT mellem overlappende netværk

Når to netværk har samme IP-område (f.eks. to 192.168.1.0/24-subnets), kan du bruge **1:1 NAT** for at skabe et “oversættelseslag”.

**Eksempel:**

```bash
# Oversæt hele subnet 192.168.1.0/24 til 10.10.1.0/24
nft add rule ip nat postrouting ip saddr 192.168.1.0/24 snat to 10.10.1.0/24
nft add rule ip nat prerouting  ip daddr 10.10.1.0/24 dnat to 192.168.1.0/24
```
**Note:** Når du skriver `snat to 10.10.1.0/24` og `dnat to 192.168.1.0/24`, bruges netmap-funktionen, som giver 1:1-mapping adresse for adresse. På ældre kerner kræves eksplicit 'netmap'-syntaks; tjek `nft list ruleset` for den faktiske ekspansion.
```

Dette gør, at to ellers identiske netværk kan kommunikere uden adressekonflikter.

---

### 4. Tjek og gem din NAT-konfiguration

Vis dine NAT-regler:

```bash
nft list table ip nat
```

Gem dem permanent:

```bash
sh -c 'nft list ruleset > /etc/nftables.conf'
systemctl enable --now nftables
```

---

### Bemærk

* NAT ændrer **ikke** i sig selv, hvem der *må* kommunikere — det håndteres i **filter-tabellen** (din firewall).
* Kombinér altid NAT-regler med tilsvarende `forward`-regler i **filter-tabellen**, så du bevarer kontrol over trafikken.
* Logregler bør stå sidst i kæden (lige før implicit/eksplicit drop), så du undgår at logge trafik, som alligevel blev accepteret af tidligere regler.

---

Klar — her er afsnittet **“Interface-match: oif/iif (og *name*-varianter)”** i samme stil som resten, med præcision og små, nyttige eksempler (inkl. VLAN og WireGuard).

---

## Interface-match: `iif` og `oif` (samt `iifname`/`oifname`)

`nftables` kan matche på hvilket interface en pakke **kommer ind** på og **går ud** af:

* **`iif`**: *indgående* interface (ingress)
* **`oif`**: *udgående* interface (egress)

De tilsvarende *name*-felter (**`iifname`** og **`oifname`**) matcher også på interfacenavn.
I moderne opsætninger kan du blot bruge **`iif`/`oif`** med navne — det er kort og klart.

> Husk: At matche på interface er en stærk sikkerhedsfaktor, fordi det fastlåser retningen/zonerne.

---

### Basale eksempler

Tillad trafik **der kommer ind** på WAN (`eth0`) **til routeren selv**:

```bash
nft add rule inet filter input iif "eth0" accept
```

Masquerade (NAT) **når trafik går ud** via WAN (`eth1`):

```bash
nft add rule ip nat postrouting oif "eth1" masquerade
```

Drop alt som **kommer ind** på et bestemt interface:

```bash
nft add rule inet filter input iif "eth2" drop
```

---

### Match på *sæt* af interfaces

Du kan matche flere interfaces i samme regel:

```bash
# Tillad fra både DMZ og VPN til routeren
nft add rule inet filter input iif { "eth0.20", "wg0" } accept
```

Negation (alt undtagen disse):

```bash
nft add rule inet filter forward oif != "eth0.30" drop
```

---

### VLAN / router-on-a-stick

VLAN-subinterfaces opfører sig som egne interfaces, fx `eth0.20` (DMZ) og `eth0.30` (OT):

```bash
# VPN (wg0) -> DMZ (RDP/3389)
nft add rule inet filter forward iif "wg0"   oif "eth0.20" tcp dport 3389 accept

# DMZ -> OT (S7/TCP 102) kun fra jump host
nft add rule inet filter forward iif "eth0.20" oif "eth0.30" \
  ip saddr 192.168.20.10 ip daddr 10.0.0.0/24 tcp dport 102 accept
```

---

### WireGuard / andre tunnelinterfaces

Tunnelinterfaces som **`wg0`** kan matches helt normalt:

```bash
# Tillad VPN-klienter at nå routerens tjenester (fx SSH på 22)
nft add rule inet filter input iif "wg0" tcp dport 22 accept
```

---

### Praktiske tips

* **Vær eksplicit**: Kombinér `iif` og `oif` hvor det giver mening, så trafikken både har den rigtige kilde- og destinationszone.
* **Sæt-match først**: Start med en smal interface-match, og tilføj derefter IP/port-kriterier. Det gør reglerne hurtigere og nemmere at læse.
* **Navngivning**: Hold dine interfacenavne konsistente (fx `eth0`=WAN, `eth0.20`=DMZ, `eth0.30`=OT, `wg0`=VPN).

---

### Mini-tjekliste (interface-fokuseret)

* Inbound til routeren: brug `input` + `iif "WAN"` (og evt. portmatch).
* Transit gennem routeren: brug `forward` + **både** `iif "ZONE_A"` og `oif "ZONE_B"`.
* NAT: brug `postrouting` + `oif "WAN"` (masquerade/SNAT).

---

Fremragende — her får du afsnittet **“Chain hooks og prioritet”** i samme klare og teknisk præcise stil som de foregående.
Jeg har gjort det mere forklarende og tilføjet et lille “flow-billede” i tekstform, så man forstår rækkefølgen af hooks, og hvorfor prioritet betyder noget.

---

## Chain hooks og prioritet

Når du opretter en **chain** i `nftables`, skal du definere tre nøgleparametre:

1. **type** – hvad kæden bruges til (*filter*, *nat* eller *route*)
2. **hook** – *hvor i netværksstakken* kæden kobles på
3. **priority** – rækkefølgen, hvis flere chains har samme hook

Disse parametre fortæller Linux, *hvornår* dine regler skal udføres i forhold til kernelens egen behandling af pakker.

---

### 🔗 Hooks – hvornår kæden aktiveres

Hooks repræsenterer de vigtigste “punkter” i pakkens rejse gennem systemet.

| Hook-navn       | Hvornår den rammes                                     | Typisk brug                              |
| --------------- | ------------------------------------------------------ | ---------------------------------------- |
| **prerouting**  | Før routingbeslutning (lige når pakken ankommer)       | DNAT, QoS                                |
| **input**       | Efter routingbeslutning, før levering til lokal proces | Firewall for trafik *til routeren selv*  |
| **forward**     | Trafik der skal *videresendes gennem routeren*         | Routing og segmentering                  |
| **output**      | Pakker der *sendes ud* fra routeren selv               | Firewall for routerens egne forbindelser |
| **postrouting** | Lige før pakken forlader systemet                      | SNAT, masquerade                         |

---

### 🧭 Pakkens rejse (for IPv4)

En hurtig mental model:

```
[prerouting] → (routing decision)
    ├─> [input]    → (routeren selv)
    └─> [forward]  → (videresendes)
[postrouting] → ud af systemet
```

Hvis routeren selv laver en udgående forbindelse (fx ping):

```
[output] → [postrouting]
```

---

### ⚙️ Prioritet

Prioritet afgør rækkefølgen, hvis flere chains har samme *hook*.

* Lavere tal → højere prioritet (kører først).
* Standardværdier:

  * **filter-chains:** `priority 0`
  * **nat prerouting:** `priority -100`
  * **nat postrouting:** `priority 100`

Eksempel:

```bash
# Kører før kernelens routing (tidligt i flowet)
nft add chain ip nat prerouting { type nat hook prerouting priority -100; }

# Normal filtrering (efter routingbeslutning)
nft add chain inet filter forward { type filter hook forward priority 0; }

# NAT på vej ud af systemet (sidst)
nft add chain ip nat postrouting { type nat hook postrouting priority 100; }
```

---

### 🧠 Hvad det betyder i praksis

* **DNAT** sker i *prerouting* (før routing), så kernel ved, hvor pakken skal sendes hen.
* **SNAT/masquerade** sker i *postrouting* (efter routing), så kernel ved, hvilken udgangsadresse den skal bruge.
* **Firewall-regler** kører typisk i *input* og *forward* med `priority 0`.

Det er netop prioritet og hooks, der afgør, *hvornår* en ændring (som NAT) slår igennem — og hvordan den kombineres med dine filter-regler.

---

Perfekt — her er afsnittet **“VLAN-opsætning”** rettet og udbygget, så det matcher resten af dokumentets stil: pædagogisk, teknisk præcist og med forklarende kommentarer til hver kommando.
Jeg har også tilføjet et lille afsnit om *router-on-a-stick*, fordi det næsten altid hænger sammen med VLAN-routing i praksis.

---

## VLAN-opsætning

**VLAN (Virtual LAN)** bruges til at opdele ét fysisk netværk i flere logiske segmenter.
Det giver bedre sikkerhed, isolering og mulighed for at bruge én fysisk port til flere netværk.

I Linux håndteres VLAN-tags (802.1Q) som *subinterfaces* på et fysisk interface.
Et VLAN-interface opfører sig som et almindeligt netkort — du kan tildele IP-adresse, firewall-regler og NAT separat.

---

### 🧩 Eksempel: Opret VLAN-interfaces på Linux

Antag at du har ét fysisk interface, `eth0`, og du vil opdele det i tre VLANs:

| VLAN | Formål          | Subinterface | IP-adresse      |
| ---- | --------------- | ------------ | --------------- |
| 10   | WAN / Internet  | eth0.10      | 192.168.10.1/24 |
| 20   | DMZ / Jump Host | eth0.20      | 192.168.20.1/24 |
| 30   | OT / PLC-net    | eth0.30      | 10.0.0.1/24     |

**Kommandoer:**

```bash
# Sørg for at 8021q-modulet er aktivt
modprobe 8021q

# Opret VLAN-interfaces
ip link add link eth0 name eth0.10 type vlan id 10
ip link add link eth0 name eth0.20 type vlan id 20
ip link add link eth0 name eth0.30 type vlan id 30

# Tildel IP-adresser
ip addr add 192.168.10.1/24 dev eth0.10
ip addr add 192.168.20.1/24 dev eth0.20
ip addr add 10.0.0.1/24      dev eth0.30

# Aktiver interfaces
ip link set eth0 up
ip link set eth0.10 up
ip link set eth0.20 up
ip link set eth0.30 up
```

---

### 🧠 Forklaring

* **`link eth0`**: Angiver, at VLAN-interfacet bygges ovenpå det fysiske interface `eth0`.
* **`type vlan id <nummer>`**: Definerer VLAN-ID’et (skal matche ID’et på switchen).
* **`ip addr add ...`**: Tildeler routerens IP-adresse i hvert VLAN.
* **`ip link set ... up`**: Aktiverer interfacet, så det bliver synligt i kernelens routing-tabel.

Når dette er gjort, har du tre virtuelle netkort, som `nftables` ser som uafhængige interfaces.
Du kan derfor bruge dem i regler, præcis som hvis de var fysiske:

```bash
nft add rule inet filter forward iif "eth0.20" oif "eth0.30" tcp dport 102 accept
```

---

### 🧱 Router-on-a-stick

En **router-on-a-stick** betyder, at routeren kun har ét fysisk netkort (f.eks. `eth0`), men flere VLAN-subinterfaces.
Det bruges typisk sammen med en **trunk-port** på switchen, hvor alle VLANs er tilladt (taggede).
Switchen leverer så VLAN-tags, og Linux routerer mellem dem.

**Kort opsummeret flow:**

```
[eth0.10]  (WAN)
     │
[eth0.20]  (DMZ)
     │
[eth0.30]  (OT)
```

Routeren videresender pakker mellem VLAN-interfaces via dine `nftables`-regler.

---

### ⚙️ Tips og best practices

* Sørg for, at switch-porten mod routeren er sat til **trunk-mode**, og at VLAN-ID’er matcher præcist.
* Sæt `MTU 1496`, hvis du oplever fragmenteringsproblemer (VLAN-tag tilføjer 4 bytes).
* Du kan se VLAN-status med:

  ```bash
  ip -d link show eth0.20
  ```
* Tilføj VLAN-interfaces permanent i din netværkskonfiguration (fx `/etc/network/interfaces`, Netplan, eller NetworkManager, afhængigt af distribution).

---

Perfekt — her får du afsnittet **“Subnetting og sikkerhed”** skrevet i samme gennemarbejdede stil som resten: kort, teknisk præcist, og med fokus på hvordan subnetting bruges aktivt i sikkerhed og `nftables`-regler.

---

## Subnetting og sikkerhed

**Subnetting** handler om at opdele et større netværk i mindre, logisk adskilte dele (subnets).
Det forbedrer både **sikkerhed**, **ydelse** og **administration**, fordi hver del af netværket kan have sine egne adgangsregler og overvågning.

I en sikkerhedsarkitektur bruges subnetting til at skabe **zoner** – f.eks.:

| Zone | Eksempel på netværk | Formål                             |
| ---- | ------------------- | ---------------------------------- |
| WAN  | 192.168.10.0/24     | Internet / ekstern adgang          |
| DMZ  | 192.168.20.0/24     | Jump hosts / servere               |
| OT   | 10.0.0.0/24         | Produktionsudstyr (PLC’er, HMI’er) |

Ved at kombinere subnetting med `nftables`-filtrering kan du præcist styre, hvilke zoner der må kommunikere.

---

### 🧱 Eksempel: Adgangskontrol mellem subnets

I dette eksempel tillader vi kun trafik fra et bestemt subnet til én host i et andet subnet — alt andet blokeres.

```bash
# Tillad kun trafik fra 192.168.1.0/26 til serveren 192.168.2.10
nft add rule inet filter forward ip saddr 192.168.1.0/26 ip daddr 192.168.2.10 accept

# Drop alt andet transit-trafik
nft add rule inet filter forward counter drop
```

**Forklaring:**

* `ip saddr` = kildeadresse (hvilket subnet trafikken kommer fra)
* `ip daddr` = destinationsadresse (hvilken host/subnet trafikken må nå)
* `forward`-chain styrer trafik *gennem* routeren — altså mellem netværk.

Denne tilgang implementerer princippet om **“least privilege”**:
Kun de forbindelser, der er absolut nødvendige, er åbne — alt andet lukkes af.

---

### 🔐 Netværkszoner og isolation

En god sikkerhedsstruktur adskiller netværk efter funktion og risiko.
Typisk opdeles de sådan:

* **WAN** – usikre eller offentlige forbindelser (Internet, fjernadgang)
* **DMZ** – mellemzone til kontrolleret adgang (f.eks. jump host eller servere)
* **OT** – kritiske systemer, hvor stabilitet og driftssikkerhed vægtes højt

Med `nftables` kan du opbygge *firewall-zoner* baseret på interface og subnet, f.eks.:

```bash
# Eksempel: VPN (wg0) -> DMZ -> OT
nft add rule inet filter forward iif "wg0" oif "eth0.20" tcp dport 3389 accept
nft add rule inet filter forward iif "eth0.20" oif "eth0.30" tcp dport 102 accept
```

Her kan du tydeligt se, hvordan subnettene bruges til at definere adgangsstier mellem zonerne.

---

### 🧠 Tips til sikker subnetdesign

* Hold **OT-udstyr** adskilt fra **IT-netværk** — ingen direkte routing.
* Brug **små subnets** (f.eks. /27 eller /28) i følsomme zoner for at begrænse broadcast og angrebsflade.
* Log al trafik, der **forsøger at bryde segmenteringen**:

  ```bash
  nft add rule inet filter forward log prefix "DROP_INTERZONE: " counter drop
  ```
* Dokumentér altid, *hvilke* subnets der må kommunikere, og *hvorfor* — det gør fejlfinding og audits langt nemmere.

---

Perfekt — her får du afsnittet **“Avancerede nftables-regler”** skrevet i samme stil som resten af dokumentet:
klar struktur, præcis sprogbrug og med små, pædagogiske forklaringer, der viser *hvad reglen gør, hvorfor man bruger den, og hvordan man kan tilpasse den i praksis*.

---

## Avancerede nftables-regler

Når du først har styr på de grundlæggende begreber (table, chain og rule), kan du begynde at udnytte nogle af de **avancerede funktioner** i `nftables`.
De gør det muligt at bygge mere præcise og effektive sikkerhedsregler — ofte med færre linjer og bedre performance.

---

### 🎯 Eksempel 1: Tillad kun specifik trafik fra en bestemt host

Tillad kun **SSH (TCP port 22)** fra en bestemt IP-adresse:

```bash
nft add rule inet filter input ip saddr 192.168.1.100 tcp dport 22 accept
```

**Forklaring:**

* `ip saddr` = kildeadresse (her kun én bestemt host).
* `tcp dport` = destinationsporten (SSH).
* God praksis, når du kun vil give administrative værter adgang til routeren.

> Tip: Kombinér denne regel med “default drop”-policy, så alle andre forsøg afvises.

---

### 🧱 Eksempel 2: Bloker bestemte protokoller

Bloker **UDP-trafik til port 53 (DNS)** fra hele subnettet 192.168.1.0/24:

```bash
nft add rule inet filter input ip saddr 192.168.1.0/24 udp dport 53 drop
```

**Forklaring:**

* Bruges typisk til at forhindre klienter i at omgå interne DNS-politikker.
* Du kan også logge forsøget før du dropper det (se næste eksempel).

---

### 🪵 Eksempel 3: Log og drop trafik

Log og drop al indgående trafik, der ikke matcher tilladte regler:

```bash
nft add rule inet filter input log prefix "DROP_INPUT: " counter drop
```

**Forklaring:**

* `log prefix` gør det nemt at finde hændelser i systemloggen (`/var/log/syslog` eller `journalctl -k`).
* `counter` viser, hvor mange gange reglen er ramt.
* Log kun det nødvendige — for meget logging kan fylde disken.

---

### ⚙️ Eksempel 4: Brug af sæt (sets)

Et **set** lader dig samle flere værdier (IP’er, porte, interfaces) i én regel.
Det gør konfigurationen både kortere og hurtigere at evaluere.

Tillad SSH fra flere godkendte IP-adresser:

```bash
nft add rule inet filter input ip saddr {192.168.1.10, 192.168.1.11, 10.0.0.5} tcp dport 22 accept
```

Eller tillad bestemte porte:

```bash
nft add rule inet filter input tcp dport {22, 443, 3389} accept
```

**Fordele ved sets:**

* Én regel kan erstatte mange.
* Du kan opdatere sets “on the fly” uden at genindlæse hele ruleset’et.

---

### 🧩 Eksempel 5: Stateful filtrering med connection tracking

Linux kernen holder styr på aktive forbindelser via *conntrack*.
Du kan bruge det til at tillade kun “etablerede” svarpakker:

```bash
nft add rule inet filter forward ct state established,related accept
nft add rule inet filter forward ct state invalid drop
```

**Forklaring:**

* `established,related` → tillader kun pakker, der hører til eksisterende forbindelser.
* `invalid drop` → beskytter mod ukorrekt formede pakker og misbrug af sessions.
* Disse regler hører altid hjemme tidligt i din `forward`-chain.

---

### 🧠 Best practices for avancerede regler

* Brug **kommentarer** (`comment "forklaring"`) til hver regel – det hjælper både dig og andre.
* Tilføj **`counter`** til alle vigtige regler; det giver dig statistik under drift.
* Hold **reglerne så specifikke som muligt** (brug `iif`, `oif`, `ip saddr`, `ip daddr`, `tcp dport`).
* Brug **`log prefix`** på kritiske drop-regler for at opdage fejlkonfigurationer.
* Test nye regler med `nft --check` før du loader dem permanent.

---

**Eksempel på velkommenteret regel:**

```bash
nft add rule inet filter forward iif "wg0" oif "eth0.20" tcp dport 3389 counter comment "VPN -> DMZ (RDP)" accept
```

---

Perfekt — her får du afsnittet **“Typiske kommandoer”** i samme konsistente og professionelle stil som resten af dit dokument.
Jeg har tilføjet forklaringer på, *hvorfor* og *hvornår* man bruger hver kommando, samt små praktiske tips og fejlfri syntaks.

---

## Typiske kommandoer

Når du arbejder med `nftables`, er der en række basale kommandoer, du ofte bruger til at **styre, gemme og inspicere** dine regler.
Nedenfor ser du de vigtigste — med korte forklaringer til hver.

---

### 🧱 Starte og stoppe `nftables`-tjenesten

```bash
systemctl start nftables
systemctl stop nftables
systemctl restart nftables
```

* `start` indlæser reglerne fra `/etc/nftables.conf` og aktiverer firewall’en.
* `restart` genindlæser filen — nyttigt efter ændringer.
* `stop` deaktiverer midlertidigt firewall’en (brug med forsigtighed).

---

### 💾 Gemme og gendanne din konfiguration

Gem hele det aktive regelsæt til konfigurationsfilen:

```bash
sh -c 'nft list ruleset > /etc/nftables.conf'
```

Når systemet starter, indlæses denne fil automatisk af tjenesten:

```bash
systemctl enable --now nftables
```

**Bemærk:**
Du kan altid indlæse en ny konfiguration manuelt:

```bash
nft -f /etc/nftables.conf
```

for at gøre det permanent brug .

---

### 🔍 Inspektion og fejlfinding

**Se hele regelsættet:**

```bash
nft list ruleset
```

**Se regler i en bestemt tabel eller chain:**

```bash
nft list table inet filter
nft list chain inet filter forward
```

**Overvåg ændringer i realtid:**

```bash
nft monitor
```

Viser pakker, der matcher regler, og ændringer i `nft`-konfigurationen, mens systemet kører.

---

### 🧠 Validering og test

**Tjek syntaksen for en konfigurationsfil, uden at loade den:**

```bash
nft -c -f /etc/nftables.conf
```

(`-c` betyder *check only*.)

**Test en enkelt regel før du tilføjer den permanent:**

```bash
nft --check add rule inet filter input tcp dport 22 accept
```

Det sikrer, at du ikke får syntaksfejl i et aktivt system.

---

### 🔄 Nulstilling af alle regler (bruges med omtanke)

```bash
nft flush ruleset
```

Sletter hele det aktive regelsæt — brug det kun, hvis du starter forfra.

> Tip: Lav altid en backup af din nuværende konfiguration, før du flusher:
>
> ```bash
> nft list ruleset > ~/backup-nft-$(date +%F).conf
> ```

---

### 🧩 Hjælpekommandoer

* **Se aktive tabeller:**

  ```bash
  nft list tables
  ```
* **Se statistik for regler:**

  ```bash
  nft list ruleset -a
  ```

  (flaget `-a` viser handles og counters)
* **Slet en specifik regel (via handle):**

  ```bash
  nft delete rule inet filter forward handle 25
  ```

---

### 🛠 Kort opsummering

| Formål                | Kommando                                |
| --------------------- | --------------------------------------- |
| Starte firewall       | `systemctl start nftables`              |
| Gemme konfiguration   | `nft list ruleset > /etc/nftables.conf` |
| Indlæse konfiguration | `nft -f /etc/nftables.conf`             |
| Se aktivt regelsæt    | `nft list ruleset`                      |
| Overvåge i realtid    | `nft monitor`                           |
| Tjekke syntaks        | `nft -c -f /etc/nftables.conf`          |

---

Perfekt — her er afsnittet **“Sikkerhedsprincipper”** skrevet i samme klare og konsistente stil som resten af dokumentet.
Jeg har udbygget det en smule, så det både dækker *grundlæggende firewall-principper* og *konkrete nftables-praksisser*, som du ville bruge i et sikkert netværksdesign (fx IT/OT-segmentering).

---

## Sikkerhedsprincipper

En god `nftables`-konfiguration handler ikke kun om at få trafikken til at flyde —
den handler om **kontrol**, **begrænsning** og **gennemsigtighed**.

De grundlæggende principper kan opsummeres i tre ord:
**tillad det nødvendige – bloker alt andet – log det usædvanlige.**

---

### 🔒 1. Default deny – alt er lukket som udgangspunkt

En firewall skal altid starte med en *“default drop”*-politik.
Det betyder, at ingen trafik tillades, før du aktivt åbner for den.

Eksempel:

```bash
nft add chain inet filter input { type filter hook input priority 0; policy drop; }
nft add chain inet filter forward { type filter hook forward priority 0; policy drop; }
```

Når du arbejder med zoner (f.eks. WAN, DMZ, OT), skal hver zone have sin egen adgangspunkt — kun nødvendige forbindelser åbnes med **specifikke regler**.

---

### ✅ 2. Tillad kun kendt og nødvendig trafik

Brug whitelist-princippet:
Definér præcist, *hvilke* IP’er, porte og protokoller der må bruges.

Eksempler:

```bash
# Kun RDP fra VPN til DMZ-jump host
nft add rule inet filter forward iif "wg0" oif "eth0.20" ip daddr 192.168.20.10 tcp dport 3389 accept

# Kun S7-trafik fra jump host til OT
nft add rule inet filter forward iif "eth0.20" oif "eth0.30" ip saddr 192.168.20.10 tcp dport 102 accept
```

Alt andet bør afvises eller logges.
På den måde ved du præcis, hvem der må tale med hvem.

---

### 🧠 3. Brug stateful filtrering (conntrack)

Tillad kun etablerede forbindelser — og afvis alle pakker, der ikke passer til et kendt flow.

```bash
nft add rule inet filter forward ct state established,related accept
nft add rule inet filter forward ct state invalid drop
```

**Hvorfor:**
Det forhindrer, at angribere sender vilkårlige pakker, der forsøger at omgå dine åbne porte.

---

### 🪵 4. Logning og overvågning

Logning gør det muligt at opdage uventet eller mistænkelig trafik.
Brug logning på *drop*-regler, men med omtanke — for meget logning kan støje.

```bash
nft add rule inet filter input log prefix "DROP_INPUT: " counter drop
nft add rule inet filter forward log prefix "DROP_FORWARD: " counter drop
```

> Tip: Brug et dedikeret logværktøj (fx `rsyslog`, `journalctl -k`, eller Zeek/Suricata) til at analysere mønstre i logfilerne.

---

### 🧱 5. Segmentering og zoner

Del netværket op i **zoner** (IT, DMZ, OT, VPN, WAN) og styr kommunikationen imellem dem stramt.
Fx:

* IT ↔ DMZ: Tillad kun RDP, HTTPS, SSH efter behov.
* DMZ ↔ OT: Tillad kun S7, Modbus, eller nødvendige protokoller.
* OT ↔ Internet: *ingen direkte forbindelse.*

> Tænk på routeren som en “grænsecontroller” mellem zoner, ikke bare som et trafikrør.

---

### ⚙️ 6. Regelhygiejne og dokumentation

* Tilføj **kommentarer** (`comment "forklaring"`) på alle vigtige regler.
* Brug **`counter`** til at holde øje med trafikmængder.
* Gem altid en **versioneret backup** af din konfiguration:

  ```bash
  nft list ruleset > /etc/nftables-$(date +%F).conf
  ```
* Gennemgå konfigurationen jævnligt — især efter ændringer i netværket.

---

### 🧩 7. Test og validering

Test nye regler med:

```bash
nft --check add rule inet filter forward ...
```

Så opdager du fejl, før du låser dig selv ude.
Kør altid `nft list ruleset` efter ændringer, og overvåg counters for at se, om reglerne bliver ramt som forventet.

---

### Samlet tankegang

En firewall er ikke et enkelt sæt regler — det er et **sikkerhedslag** omkring din infrastruktur.
Med `nftables` har du værktøjerne til at håndhæve det på kernel-niveau med høj præcision.

> Et sikkert system er et simpelt system: få åbninger, klar dokumentation, og alt andet lukket.

---

Perfekt — her er afsnittet **“Fejlfinding”** rettet og udbygget i samme pædagogiske og teknisk klare stil som resten af dokumentet.
Det indeholder både praktiske kommandoer og små forklaringer på, *hvordan du tolker outputtet*, så det kan bruges i undervisning eller drift.

---

## Fejlfinding

Selv den bedste firewall-konfiguration kræver løbende kontrol og fejlfinding.
Her er de vigtigste metoder til at analysere, teste og forstå, hvordan `nftables` og routing opfører sig på din Linux-router.

---

### 🔍 1. Tjek aktive regler

Vis alle tabeller, chains og regler i det nuværende regelsæt:

```bash
nft list ruleset
```

**Forklaring:**

* Viser hele firewall-strukturen — inkl. tables, chains, hooks, policies og regler.
* Brug `-a` for at se **handles** (regelnumre) og **counters** (trafikstatistik):

  ```bash
  nft list ruleset -a
  ```

> Tip: Counters er gode til at bekræfte, at dine regler faktisk bliver ramt.

---

### 🧱 2. Se en specifik tabel eller chain

```bash
nft list table inet filter
nft list chain inet filter forward
```

Brug dette, når du kun vil kontrollere én del af konfigurationen — fx `forward`-kæden for routingtrafik.

---

### 🧩 3. Overvåg ændringer i realtid

```bash
nft monitor
```

Denne kommando viser, når regler aktiveres, matches eller ændres.
Den er særlig nyttig, mens du tester nye regler, eller når du vil se, hvordan trafik rammer dine drop- og accept-regler.

---

### 📈 4. Se trafikstatistik pr. regel

For hver regel kan du se, hvor mange pakker og bytes der har matchet:

```bash
nft list chain inet filter forward
```

Du ser output som:

```
counter packets 154 bytes 12032
```

Hvis tælleren står stille, betyder det, at reglen **ikke bliver ramt** — måske matcher den forkert interface, port eller IP.

---

### 🧠 5. Tjek om routing er aktiveret

```bash
sysctl net.ipv4.ip_forward
```

Et output på:

```
net.ipv4.ip_forward = 1
```

betyder, at routing er slået til.
Hvis værdien er 0, skal du aktivere forwarding (se afsnittet *Routing*).

---

### 🧰 6. Brug ping og traceroute mellem zoner

Test kommunikation mellem zoner for at bekræfte, at routing og firewall-regler virker:

**Fra en klient i DMZ:**

```bash
ping 10.0.0.1       # routerens OT-gateway
traceroute 10.0.0.10 # PLC eller enhed i OT-nettet
```

**Hvis ping ikke virker:**

* Tjek om `icmp`-trafik er blokeret (mange regler tillader kun TCP/UDP).
* Brug evt. en midlertidig regel:

  ```bash
  nft add rule inet filter forward ip protocol icmp accept
  nft add rule inet filter forward meta l4proto ipv6-icmp accept
  ```
---

## Minimal fuldt eksempel

Her er et samlet, minimalt eksempel, du kan kopiere direkte og få en fungerende router/firewall med NAT:

```bash
# Aktiver forwarding
sysctl -w net.ipv4.ip_forward=1

# Opret tabel og chains
nft add table inet filter
nft add chain inet filter input   { type filter hook input   priority 0; policy drop; }
nft add chain inet filter forward { type filter hook forward priority 0; policy drop; }
nft add chain inet filter output  { type filter hook output  priority 0; policy accept; }

# Tillad trafik fra lokalnettet
nft add rule inet filter input ip saddr 192.168.1.0/24 accept

# Tillad etablerede forbindelser
nft add rule inet filter input ct state established,related accept
nft add rule inet filter forward ct state established,related accept

# Log og drop alt andet
nft add rule inet filter input log prefix "DROP_INPUT: " counter drop
nft add rule inet filter forward log prefix "DROP_FORWARD: " counter drop

# NAT (masquerade) for udgående trafik
nft add table ip nat
nft add chain ip nat postrouting { type nat hook postrouting priority 100; }
nft add rule ip nat postrouting oif "eth1" masquerade
```

---

### 🪵 7. Analyser logfiler

Loggede drop-regler kan findes i:

```bash
journalctl -k | grep DROP
```

Eller, hvis du bruger `rsyslog`:

```bash
tail -f /var/log/syslog | grep DROP
```

Du kan genkende reglerne på dine `log prefix`-mærker, f.eks.:

```
DROP_FORWARD: IN=eth0.20 OUT=eth0.30 SRC=192.168.20.10 DST=10.0.0.15 PROTO=TCP SPT=54213 DPT=102
```

---

### 🧩 8. Kontrollér netværksinterfaces

Bekræft, at alle interfaces (fysiske og VLAN) er aktive og har korrekte IP’er:

```bash
ip addr show
```

Tjek routingtabellen:

```bash
ip route show
```

Hvis pakker ikke videresendes, kan årsagen være manglende rute eller forkert interfacebinding.

---

### ⚙️ 9. Genindlæsning og test af regler

Når du ændrer filer, kan du indlæse dem igen uden genstart:

```bash
nft -f /etc/nftables.conf
```

Valider først:

```bash
nft -c -f /etc/nftables.conf
```

(`-c` betyder “check only” – ingen ændringer udføres.)

---

### 🧱 10. Nulstil og start forfra

Hvis systemet er låst ned af fejlkonfiguration:

```bash
nft flush ruleset
```

Dette fjerner alle regler midlertidigt (trafikken flyder frit igen).
Husk derefter at gendanne din gemte konfiguration:

```bash
nft -f /etc/nftables.conf
```

---

### 🧩 Hurtig tjekliste til fejlfinding

| Problem                   | Typisk årsag                                  | Løsning                                       |
| ------------------------- | --------------------------------------------- | --------------------------------------------- |
| Ingen routing mellem net  | `ip_forward` = 0                              | Aktivér med `sysctl -w net.ipv4.ip_forward=1` |
| Trafik rammer ikke regler | Forkert `iif`/`oif` eller IP                  | Tjek med `nft list ruleset -a`                |
| Ingen NAT ud af WAN       | Manglende `masquerade`-regel                  | Se afsnittet “NAT”                            |
| Ingen log-output          | Manglende `log`-regel eller forkert logniveau | Brug `journalctl -k` og kontroller syslog     |
| Ingen tællere stiger      | Trafik rammer ikke chain                      | Kontroller `policy drop` og chain hooks       |

---

### 🧠 Afsluttende note

Når du fejlfinder `nftables`, tænk altid i **flow**:

1. Kommer pakken ind på det forventede interface?
2. Matcher den en regel i den rigtige chain og hook?
3. Hvad sker der efter reglen — bliver den accepteret, oversat (NAT), eller droppet?

Hvis du kan svare på de tre spørgsmål, kan du løse næsten enhver firewall-fejl.

---

Fremragende — her er en afrunding, der passer perfekt som afslutning på din vejledning.
Den samler hele materialet, genopfrisker de vigtigste pointer, og gør det egnet som afsluttende afsnit i et undervisnings- eller praksisdokument.

---

## Konklusion

`nftables` er mere end bare et værktøj til at filtrere pakker — det er selve fundamentet for en moderne, fleksibel og sikker Linux-router.

Ved at forstå **tables**, **chains**, **rules** og **hooks** kan du bygge et regelsæt, der præcist styrer, hvordan trafik flyder gennem systemet.
Når du kombinerer det med god **netværkssegmentering** og **stramme sikkerhedsprincipper**, får du et robust setup, der kan bruges både i IT- og OT-miljøer.

---

### 🔑 Nøglepointer fra dokumentet

* **Aktivér routing** (`ip_forward=1`) for at gøre Linux til router.
* **Brug policy drop** i alle kæder — åbn kun det, der skal bruges.
* **Segmentér netværket** med VLANs og subnet for at isolere zoner (WAN, DMZ, OT).
* **Tillad kun nødvendig trafik** og vær eksplicit med `iif`/`oif`, IP og port.
* **Brug NAT** (masquerade, SNAT, DNAT) til at forbinde interne og eksterne netværk sikkert.
* **Overvåg med counters og logs**, så du kan se, hvad der faktisk sker i realtid.
* **Dokumentér dine regler** og test altid ændringer, før de bliver permanente.

---

### 🧱 Helhedsbilledet

En sikker Linux-router består af flere lag, der arbejder sammen:

```
[ Interface / VLAN ]
        ↓
[ nftables (filter + nat) ]
        ↓
[ Routing og forwarding ]
        ↓
[ Logning, overvågning og vedligeholdelse ]
```

Når alle lagene spiller sammen, har du et system, der både **beskytter, styrer og dokumenterer** netværkstrafikken.

---

### 🧭 Videre læring

For at bygge videre på denne viden kan du:

* Udforske **`nft sets`**, **maps** og **flowtables** for højere performance.
* Integrere **IDS/IPS-systemer** (som Suricata eller Zeek) til overvågning.
* Arbejde med **IPv6** og blandede miljøer i `inet`-tabeller.
* Automatisere din opsætning med **Ansible** eller **systemd-nftables**-scripts.

---

### ✨ Afsluttende tanke

En god firewall er ikke bare en liste af regler —
det er et **sæt bevidste valg** om, hvem der må tale med hvem, hvornår og hvordan.

`nftables` giver dig fuld kontrol over det valg, med et system, der er både **transparent, effektivt og fremtidssikret**.

---

