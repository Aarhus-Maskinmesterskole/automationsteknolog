# 04 - Router mellem to subnet

I denne øvelse bygger du et lille routed netværk. Målet er at forstå, hvordan en router fungerer som "bro" mellem to forskellige subnet, og hvorfor en default gateway er nødvendig for at forlade sit eget lokale netværk.

## 🗺️ Topologi og IP-plan

Brug denne oversigt til at konfigurere dit netværk i GNS3:

```text
      Subnet A: 10.0.1.0/24              Subnet B: 10.0.2.0/24
   [ PC1 ] .10 -------- .1 [ R1 ] .1 -------- .10 [ PC2 ]
           eth0       eth0        eth1       eth0
   (GW: 10.0.1.1)                        (GW: 10.0.2.1)
```

1. **PC1 (Subnet A):** IP `10.0.1.10/24`, Gateway `10.0.1.1`
2. **R1 (Router):** Interface eth0: `10.0.1.1/24`, Interface eth1: `10.0.2.1/24`
3. **PC2 (Subnet B):** IP `10.0.2.10/24`, Gateway `10.0.2.1`

---

## Trin 1: Opbyg topologien i GNS3
1. Opret et nyt projekt: `dag07-router`.
2. Tilføj to Alpine-maskiner (PC1, PC2) og én router (R1).
3. **VIGTIGT:** Forbind PC1 til R1's **eth0** og PC2 til R1's **eth1**.
4. Start alle noder.

---

## Trin 2: Konfigurer PC1 og PC2
Her fortæller vi computerne deres egen adresse, og hvem deres "udgang" (Default Gateway) er.

**Kør på PC1:**
```bash
ip addr add 10.0.1.10/24 dev eth0
ip link set eth0 up
ip route add default via 10.0.1.1
```

**Kør på PC2:**
```bash
ip addr add 10.0.2.10/24 dev eth0
ip link set eth0 up
ip route add default via 10.0.2.1
```

---

## Trin 3: Konfigurer Routeren (R1)
En router er i princippet blot en computer med flere netkort. For at den skal sende trafik videre fra det ene kort til det andet, skal vi aktivere "IP Forwarding".

**Kør på R1:**
```bash
# Konfigurer begge netkort
ip addr add 10.0.1.1/24 dev eth0
ip addr add 10.0.2.1/24 dev eth1
ip link set eth0 up
ip link set eth1 up

# Aktiver videresendelse af pakker (IP Forwarding)
sysctl -w net.ipv4.ip_forward=1
```

---

## Trin 4: Verificer og "Se" forbindelsen

1. **Ping-test:** Kan PC1 ramme PC2? 
   `ping -c 4 10.0.2.10`
2. **Se pakkens vej (Traceroute):**
   Kør denne kommando på PC1 for at se alle "hop" på vejen til PC2:
   ```bash
   traceroute 10.0.2.10
   ```
   *Hvilken IP-adresse er det første hop? Hvorfor?*

3. **Tjek naboer (ARP):**
   Kør `ip neigh` på PC1. Kan den se PC2's MAC-adresse? 
   *(SPOILER: Nej, den ser kun routerens MAC-adresse, da routeren agerer stedfortræder).*

---

## ❓ Refleksionsspørgsmål
1. **Hvorfor kan PC1 ikke pinge PC2, hvis du glemmer `ip route add default...` kommandoen?**
2. **Hvad sker der med forbindelsen, hvis du sætter `net.ipv4.ip_forward=0` på routeren?**
3. **Hvornår har man brug for en router i en industriel installation (f.eks. på en fabrik)?**

---

## 💾 Ekstraopgave
Gør konfigurationen permanent på alle tre noder ved at redigere `/etc/network/interfaces` som lært i opgave 03. Husk at tilføje `gateway` feltet under `iface eth0 inet static` på dine hosts.
