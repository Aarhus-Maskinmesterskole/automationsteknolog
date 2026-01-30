# 🔗 Dag 09 – VLAN-lab: Inter-VLAN routing med Linux-router (VLAN 110, 120, 130)

## 1. Formål

Formålet med denne øvelse er, at du får praktisk erfaring med:

* Segmentering af et LAN ved hjælp af VLAN.
* Konfiguration af access- og trunk-porte på en switch.
* Opsætning af inter-VLAN routing på en Linux-baseret router (router-on-a-stick).
* Test og fejlsøgning af forbindelse mellem Linux-klienter i forskellige VLAN.

Efter øvelsen skal du kunne forklare, hvordan en enkelt fysisk forbindelse mellem switch og router kan håndtere trafik fra flere VLAN ved hjælp af 802.1Q-tags.

---

## 2. Scenarie

En virksomhed ønsker at adskille deres interne netværk i tre logiske segmenter:

* **VLAN 110 – PRODUKTION**
* **VLAN 120 – ADMINISTRATION**
* **VLAN 130 – GÆSTER**

Alle tre VLAN er forbundet til den samme switch. En Linux-router sørger for routing mellem VLAN’ene.

Der er kun **ét fysisk kabel** mellem routeren og switchen. For at kunne føre trafik fra alle tre VLAN over dette kabel, benyttes en **trunk-port** på switchen og **VLAN-subinterfaces** på routeren.

---

## 3. Topologi

Logisk topologi:

<img width="1917" height="1030" alt="image" src="https://github.com/user-attachments/assets/715fa470-3f39-41b9-ba0c-dab6c66461f0" />

* **Linux-router**

  * Ét interface mod switchen: `eth0` (trunk)
  * VLAN-subinterfaces:

    * `eth0.110` → VLAN 110
    * `eth0.120` → VLAN 120
    * `eth0.130` → VLAN 130

* **L2-switch**

  * Port til Host1 → Access, VLAN 110
  * Port til Host2 → Access, VLAN 120
  * Port til Host3 → Access, VLAN 130
  * Port til router → Trunk, tilladt VLAN 110, 120, 130

* **3 Linux-klienter (Alpine)**

  * Host1 tilhører VLAN 110
  * Host2 tilhører VLAN 120
  * Host3 tilhører VLAN 130

---

## 4. IP-plan

| VLAN | Beskrivelse | Netværk          | Gateway (Linux-router) | Host-IP        |
| ---: | ----------- | ---------------- | ---------------------- | -------------- |
|  110 | PRODUKTION  | 192.168.110.0/24 | 192.168.110.1          | 192.168.110.10 |
|  120 | ADMIN       | 192.168.120.0/24 | 192.168.120.1          | 192.168.120.10 |
|  130 | GÆSTER      | 192.168.130.0/24 | 192.168.130.1          | 192.168.130.10 |

Routeren fungerer som default gateway for alle VLAN.

---

## 5. Krav

* Alle hosts skal kunne:

  * Pinge deres egen gateway (samme VLAN).
  * Pinge de andre hosts i de andre VLAN via routeren.

* VLAN-segmentering skal ske på switchen (access/trunk).

* Inter-VLAN routing skal ske på Linux-routeren (router-on-a-stick).

---

# Opgave: Step-by-step konfiguration

Nedenstående trin skal følges i rækkefølge.
Dokumentér undervejs med relevante screenshots eller kommandoudskrifter efter lærerens anvisning.

---

## Trin 1 – Opret GNS3-projekt og topologi

1. Opret et nyt projekt i GNS3, fx:
   `VLAN_LAB_110_120_130`.
2. Tilføj følgende noder:

   * 1 × Linux-router (Debian/Ubuntu VM eller anden generisk Linux).
   * 1 × L2-switch (Cisco IOS/IOU eller tilsvarende).
   * 3 × **Alpine Linux-VM’er** som klienter.
3. Forbind noderne:

   * Router `eth0` → Switch port `f0/0`.
   * Alpine-Host1 → Switch `f0/1`.
   * Alpine-Host2 → Switch `f0/2`.
   * Alpine-Host3 → Switch `f0/3`.

Kontrollér at alle links er “up” i GNS3, når noderne er startet.

---

## Trin 2 – Forbered Linux-routeren

Antagelse: Nødvendige pakker (vlan, iproute2) er allerede installeret.


1. Verificér at interfacet `eth0` findes (eller find det rigtige navn):

```bash
ip link show
```

<img width="1917" height="1028" alt="image" src="https://github.com/user-attachments/assets/a60ee12d-b4ab-42ad-b16e-92ff873c0856" />


Notér navnet på interfacet mod switchen (forudsat `eth0` – hvis det hedder noget andet, brug det navn i resten af øvelsen).

---

## Trin 3 – Opret VLAN-subinterfaces på Linux-routeren

Opret et subinterface pr. VLAN:

```bash
# VLAN 110
ip link add link eth0 name eth0.110 type vlan id 110

# VLAN 120
ip link add link eth0 name eth0.120 type vlan id 120

# VLAN 130
ip link add link eth0 name eth0.130 type vlan id 130
```

Kontrol: 

```bash
ip -d -link show
```

<img width="1917" height="1028" alt="image" src="https://github.com/user-attachments/assets/8ddfeee3-f780-4cae-b059-3a8235745864" />


Tildel IP-adresser iht. IP-planen:

```bash
ip addr add 192.168.110.1/24 dev eth0.110
ip addr add 192.168.120.1/24 dev eth0.120
ip addr add 192.168.130.1/24 dev eth0.130
```

Aktivér interfaces og routing:

```bash
ip link set eth0 up
ip link set eth0.110 up
ip link set eth0.120 up
ip link set eth0.130 up

sysctl -w net.ipv4.ip_forward=1
```

Brug `clear` til at ryde console

Kontrol:

```bash
ip -d link show eth0.110
```

Tjek at der står, at det er et VLAN-interface med `vlan id 110`.
Gentag evt. for `eth0.120` og `eth0.130`.

<img width="1917" height="1030" alt="image" src="https://github.com/user-attachments/assets/852d0090-a19c-4274-8a22-b37a74198e12" />

---

## Trin 4 – Konfigurer switchen (VLAN og porte)

Gå på switchens konsol og udfør følgende.

1. Opret VLAN 110, 120 og 130 på port 1,2 og 3 (port 1 forbeholdt til dotq):

<img width="1917" height="1028" alt="image" src="https://github.com/user-attachments/assets/b98ca9f3-9810-43c8-a89d-e1a17876e26e" />

Sikr dig, at:

* VLAN 110, 120 og 130 findes `ip -d link show`

---

## Trin 5 – Konfigurer Alpine Linux-klienter (midlertidig/running config)

På hver Alpine-VM arbejdes **som root** (ingen `sudo`, ingen rc/persistenskonfiguration).
Vi laver kun runtime-konfiguration med `ip`-kommandoerne.

### 5.1 Find interface-navn

På hver Alpine-host:

```bash
ip link
```

Find navnet på det interface, der er forbundet til switchen – her antager vi `eth0`.
Hvis det hedder noget andet (fx `ens3`), bruger du det navn i stedet for `eth0` i resten af kommandoerne.

---

### 5.2 Host1 (VLAN 110)

På Alpine-Host1:

1. Sæt IP-adresse:

```bash
ip addr add 192.168.110.10/24 dev eth0
```

2. Sæt interface op:

```bash
ip link set eth0 up
```

3. Sæt default gateway:

```bash
ip route add default via 192.168.110.1
```

4. Kontrol:

```bash
ip addr show dev eth0
ip route show dev eth0
```

<img width="1918" height="1029" alt="image" src="https://github.com/user-attachments/assets/73615690-68f0-404c-bcd5-cfffb72e067d" />


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
