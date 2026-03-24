# GNS3 Opgaver – nftables og Linux-router
Dette dokument indeholder en række opgaver, der guider dig gennem opsætning af en Linux-router i GNS3 med fokus på routing og firewall-konfiguration ved hjælp af `nftables`.
---

## Opgave 1: Aktivér routing på en Linux-router

**Mål:**
Få to virtuelle netværk til at kunne pinge hinanden via en Linux-router.
![alt text](img/image.png)
**Trin:**
1. Opret et GNS3-projekt med to LAN-segmenter og en Linux-router imellem.
2. Tilføj to linux-pc'er
    1. PC1: 192.168.1.10/24
        ```bash
        ip addr add 192.168.1.10/24 dev eth0
        ```
    2. PC2: 192.168.2.10/24
        ```bash
        ip addr add 192.168.2.10/24 dev eth1
        ```
3. Aktivere default route på PC'erne
    1. På PC1:
       ```bash
       ip route add default via 192.168.1.1
       ```
    2. På PC2:
       ```bash
       ip route add default via 192.168.2.1
       ```
3. Sæt IP-adresser på routerens interfaces (eth0: 192.168.1.1/24, eth1: 192.168.2.1/24).
4. Aktivér routing på routeren:
   ```bash
   sysctl -w net.ipv4.ip_forward=1
   ```
5. Test med ping fra PC1 til PC2.
    - Output PC1 skal vise følgende:
        ```bash
        aams-linux-pc-1:/# ping -c4 192.168.2.10
        PING 192.168.2.10 (192.168.2.10): 56 data bytes
        64 bytes from 192.168.2.10: seq=0 ttl=63 time=0.121 ms
        64 bytes from 192.168.2.10: seq=1 ttl=63 time=0.137 ms
        64 bytes from 192.168.2.10: seq=2 ttl=63 time=0.267 ms
        64 bytes from 192.168.2.10: seq=3 ttl=63 time=0.149 ms

        --- 192.168.2.10 ping statistics ---
        4 packets transmitted, 4 packets received, 0% packet loss
        round-trip min/avg/max = 0.121/0.168/0.267 ms
        aams-linux-pc-1:/#
        ```
    - Output PC2 skal vise følgende:
        ```bash
        aams-linux-pc-2:/# ping -c4 192.168.1.10
        PING 192.168.1.10 (192.168.1.10): 56 data bytes
        64 bytes from 192.168.1.10: seq=0 ttl=63 time=0.142 ms
        64 bytes from 192.168.1.10: seq=1 ttl=63 time=0.153 ms
        64 bytes from 192.168.1.10: seq=2 ttl=63 time=0.142 ms
        64 bytes from 192.168.1.10: seq=3 ttl=63 time=0.149 ms

        --- 192.168.1.10 ping statistics ---
        4 packets transmitted, 4 packets received, 0% packet loss
        round-trip min/avg/max = 0.142/0.146/0.153 ms
        aams-linux-pc-2:/#
        ```
    Der findes andre måder at teste forbindelsen på som fx ved brug af `tcpdump` kommandoen:
    - På PC1:
        ```bash
        aams-linux-pc-1:/# tcpdump -i eth0 icmp
        aams-linux-pc-1:/# tcpdump
        tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
        listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes

        19:20:40.881329 IP 192.168.2.10 > 192.168.1.10: ICMP echo request, id 307, seq 0, length 64
        19:20:40.881338 IP 192.168.1.10 > 192.168.2.10: ICMP echo reply, id 307, seq 0, length 64
        19:20:41.881422 IP 192.168.2.10 > 192.168.1.10: ICMP echo request, id 307, seq 1, length 64
        19:20:41.881431 IP 192.168.1.10 > 192.168.2.10: ICMP echo reply, id 307, seq 1, length 64
        19:20:42.881844 IP 192.168.2.10 > 192.168.1.10: ICMP echo request, id 307, seq 2, length 64
        19:20:42.881863 IP 192.168.1.10 > 192.168.2.10: ICMP echo reply, id 307, seq 2, length 64
        19:20:43.881744 IP 192.168.2.10 > 192.168.1.10: ICMP echo request, id 307, seq 3, length 64
        19:20:43.881752 IP 192.168.1.10 > 192.168.2.10: ICMP echo reply, id 307, seq 3, length 64
        19:20:45.897684 ARP, Request who-has 192.168.1.1 tell 192.168.1.10, length 28
        19:20:45.897991 ARP, Request who-has 192.168.1.10 tell 192.168.1.1, length 28
        19:20:45.897995 ARP, Reply 192.168.1.10 is-at 02:42:e9:fc:2b:00 (oui Unknown), length 28
        ```

    eller ved at bruge wireshark til at fange ICMP pakkerne på routerens interfaces. I wireshark kan du se at de bliver routet korrekt mellem de to netværk.
    ![alt text](img/image-1.png)

---

## Opgave 2: Basis-firewall med nftables

**Mål:**
Bloker al trafik til routeren undtagen fra lokalnettet `192.168.1.0/24`.

**Trin:**
1. Brug samme setup som i opgave 1.
2. Installer nftables på routeren (hvis ikke allerede installeret):
   ```bash
   apt update # Kræver internetadgang
   apt install nftables # Kræver internetadgang

   ```
3. Lav en fil `nftables.conf`
   ```bash
   vi /etc/nftables.conf
   ```
   Indsæt følgende indhold i filen:
   ```bash
   table inet filter {
       chain input {
           type filter hook input priority 0; policy drop;
           ip saddr 192.168.1.0/24 accept
       }
       chain forward {
           type filter hook forward priority 0; policy accept;
       }
      chain output {
         type filter hook output priority 0; policy accept;
      }
   }
   ```
4. Aktivér nftables-konfigurationen:
   ```bash
   nft -f /etc/nftables.conf
   ```
5. Test med ping fra PC1 til routeren og fra PC2 til routeren.
   - Ping fra PC1 (skal virke):
       ```bash
       ping -c4 192.168.1.1
       ```
   - Ping fra PC2 (skal ikke virke):
       ```bash
       ping -c4 192.168.1.1
       ```

---


## Opgave 3: Selektiv routing-firewall med nftables

**Mål:**  
Tillad kun trafik fra netværk `192.168.1.0/24` til netværk `192.168.2.0/24`. Blokér al trafik fra `192.168.2.0/24` til `192.168.1.0/24`.

**Trin:**
1. Brug samme setup som i opgave 1 og 2.
2. Opdater eller opret filen `/etc/nftables.conf` med følgende indhold:
   ```bash
   table inet filter {
   chain input {
      type filter hook input priority 0; policy drop;
      # Tillad basal trafik til routeren fra begge LAN
      ip saddr 192.168.1.0/24 counter accept
      ip saddr 192.168.2.0/24 counter accept
   }

   chain forward {
      type filter hook forward priority 0; policy drop;

      # 0) Tillad returtrafik (meget vigtig!)
      ct state established,related counter accept

      # 1) Tillad nye forbindelser fra 192.168.1.0/24 -> 192.168.2.0/24
      ip saddr 192.168.1.0/24 ip daddr 192.168.2.0/24 ct state new counter accept

      # 2) Drop nye forbindelser den anden vej
      ip saddr 192.168.2.0/24 ip daddr 192.168.1.0/24 ct state new counter drop
   }

   chain output {
      type filter hook output priority 0; policy accept;
   }
   }
   ```
3. Indlæs konfigurationen:
   ```bash
   nft -f /etc/nftables.conf
   ```
   hvis man gerne vil have permanent gemt sin konfiguration `vi /etc/network/interfaces` og tilføje:
   ```bash
   post-up nft -f /etc/nftables.conf
   ```

4. Test:
   - Ping fra PC1 (`192.168.1.10`) til PC2 (`192.168.2.10`) skal virke ved at køre:
       ```bash
       ping -c4 192.168.2.10
       ```
   - Ping fra PC2 (`192.168.2.10`) til PC1 (`192.168.1.10`) skal ikke virke ved at køre:
       ```bash
       ping -c4 192.168.1.10
       ```
5. Test med wireshark på routerens interfaces for at se, at trafikken bliver blokeret korrekt i den ene retning.
![alt text](img/image-3.png)
*Bemærk de to markeringer i wireshark. No 3 viser ping fra PC2 til PC1. Router afviser pakken. No 7 viser ping fra PC1 til PC2. Router accepterer pakken.*

---

## Opgave 4: Selektiv routing-firewall med nftables

**Mål:**  
Målet er nu at vende tilladelser og blokeringer, dvs. tillad kun trafik fra netværk `192.168.2.0/24` til netværk `192.168.1.0/24`. Blokér al trafik fra `192.168.1.0/24` til `192.168.2.0/24`.

**Trin:**
1. Brug samme setup som i opgave 1 og 2.
2. Opdater eller opret filen `/etc/nftables.conf` med følgende indhold:
   ```bash
   table inet filter {
   chain input {
      type filter hook input priority 0; policy drop;
      # Tillad basal trafik til routeren fra begge LAN
      ip saddr 192.168.1.0/24 counter accept
      ip saddr 192.168.2.0/24 counter accept
   }

   chain forward {
      type filter hook forward priority 0; policy drop;

      # 0) Tillad returtrafik (meget vigtig!)
      ct state established,related counter accept

      # 1) Tillad nye forbindelser fra 192.168.1.0/24 -> 192.168.2.0/24
      ip saddr 192.168.2.0/24 ip daddr 192.168.1.0/24 ct state new counter accept

      # 2) Drop nye forbindelser den anden vej
      ip saddr 192.168.2.0/24 ip daddr 192.168.1.0/24 ct state new counter drop
   }

   chain output {
      type filter hook output priority 0; policy accept;
   }
   }
   ```
3. Indlæs konfigurationen:
   ```bash
   nft -f /etc/nftables.conf
   ```
   hvis man gerne vil have permanent gemt sin konfiguration `vi /etc/network/interfaces` og tilføje:
   ```bash
   post-up nft -f /etc/nftables.conf
   ```

4. Test:
   - Ping fra PC2 (`192.168.2.10`) til PC1 (`192.168.1.10`) skal virke ved at køre:
       ```bash
       ping -c4 192.168.1.10
       ```
   - Ping fra PC1 (`192.168.2.10`) til PC2 (`192.168.2.10`) skal ikke virke ved at køre:
       ```bash
       ping -c4 192.168.2.10
       ```
5. Test med `tcpdump` på routerens interfaces for at se, at trafikken bliver blokeret korrekt i den ene retning.
   - Output på routerens eth1 interface skal vise noget i stil med:
      ```bash
      nfw-1:/# tcpdump -i eth1
      tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
      listening on eth1, link-type EN10MB (Ethernet), snapshot length 262144 bytes
      10:16:16.387224 ARP, Request who-has 192.168.2.1 tell 192.168.2.10, length 28
      10:16:16.387235 ARP, Reply 192.168.2.1 is-at 02:42:7f:c7:90:01 (oui Unknown), length 28
      10:16:16.387260 IP 192.168.2.10 > 192.168.1.10: ICMP echo request, id 53, seq 0, length 64
      10:16:16.387383 IP 192.168.1.10 > 192.168.2.10: ICMP echo reply, id 53, seq 0, length 64
      10:16:21.468953 IP6 fe80::42:7fff:fec7:9001 > ip6-allrouters: ICMP6, router solicitation, length 16
      10:16:21.468964 ARP, Request who-has 192.168.2.10 tell 192.168.2.1, length 28
      10:16:21.469036 ARP, Reply 192.168.2.10 is-at 02:42:5e:38:f2:00 (oui Unknown), length 28
      ```
   - Output på routerens eth0 interface skal vise noget i stil med:
      ```bash
      nfw-1:/# tcpdump -i eth0
      tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
      listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
      10:17:53.097827 IP 192.168.1.10 > 192.168.2.10: ICMP echo request, id 55, seq 0, length 64
      ```
      *Bemærk at der ikke er nogen ICMP echo reply, da pakken er blevet droppet af firewall-reglerne.*

---

## Opgave 4: Basics nft
**Mål:** Tillad trafik fra netværk `192.168.2.0/24` til netværk `192.168.1.0/24`. Tillad traffik fra `192.168.1.0/24` til `192.168.2.0/24`.

**Trin:**
**Trin:**
1. Brug samme setup som i opgave 1 og 2.
2. Opdater eller opret filen `/etc/nftables.conf` med følgende indhold:
   ```bash
   table inet filter {
   chain input {
      type filter hook input priority 0; policy drop;
      # Tillad basal trafik til routeren fra begge LAN
      ip saddr 192.168.1.0/24 counter accept
      ip saddr 192.168.2.0/24 counter accept
   }

   chain forward {
      type filter hook forward priority 0; policy drop;

      # 0) Tillad returtrafik (meget vigtig!)
      ct state established,related counter accept

      # 1) Tillad nye forbindelser fra 192.168.1.0/24 -> 192.168.2.0/24
      ip saddr 192.168.2.0/24 ip daddr 192.168.1.0/24 ct state new counter accept
      ip saddr 192.168.1.0/24 ip daddr 192.168.2.0/24 ct state new counter accept

      # 2) Drop nye forbindelser den anden vej
      #ip saddr 192.168.2.0/24 ip daddr 192.168.1.0/24 ct state new counter drop
   }

   chain output {
      type filter hook output priority 0; policy accept;
   }
   }
   ```
3. Indlæs konfigurationen:
   ```bash
   nft -f /etc/nftables.conf
   ```
   hvis man gerne vil have permanent gemt sin konfiguration `vi /etc/network/interfaces` og tilføje:
   ```bash
   post-up nft -f /etc/nftables.conf
   ```
4. Åben wireshark på hver af routerens interfaces for at observere trafikken.

5. Test:
   - Ping fra PC2 (`192.168.2.10`) til PC1 (`192.168.1.10`) skal virke ved at køre:
       ```bash
       ping -c4 192.168.1.10
       ```
   - Ping fra PC1 (`192.168.2.10`) til PC2 (`192.168.2.10`) skal virke ved at køre:
       ```bash
       ping -c4 192.168.2.10
       ```
   ![alt text](img/image-4.png)
   *Bemærk at der er trafik i begge retninger.*
## Opgave 4: NAT for internetdeling

**Mål:**
Giv et internt netværk adgang til “internet” via NAT.

**Trin:**
1. Tilføj et tredje interface på routeren (eth2) og tilslut det til et “internet”-segment (fx 10.0.0.1/24).
2. Opret NAT-tabel og postrouting-chain:
   ```bash
   sudo nft add table ip nat
   sudo nft add chain ip nat postrouting { type nat hook postrouting priority 100; }
   sudo nft add rule ip nat postrouting oif "eth2" masquerade
   ```
3. Test at PC1 kan pinge en “internet-server” på 10.0.0.2.

---

## Opgave 4: VLAN-router-on-a-stick

**Mål:**
Routeren skal håndtere to VLANs på ét interface. Router skal tillade trafik fra VLAN 10 til VLAN 20, men ikke den anden vej.

**Trin:**
1. Indsæt en switch mellem routeren og de to linux-pc'er.
![alt text](img/image-5.png)
2. Dobbelt klick på switch og opret VLAN-subinterfaces som vist på billede:
![alt text](img/image-6.png)
   - VLAN 10 -> PC1
   - VLAN 20 -> PC2
3. Giv PC'erne IP-adresser:
   1. PC1 (VLAN 10): 192.168.10.10/24 via `/etc/network/interfaces`
   2. PC2 (VLAN 20): 192.168.20.10/24 via `/etc/network/interfaces`
4. Konfigurer routerens `/etc/network/interfaces` fil til at oprette VLAN-subinterfaces:
   ```bash
   auto eth0
   iface eth0 inet manual

   auto eth0.10
   iface eth0.10 inet static
      pre-up ip link add link eth0 name eth0.10 type vlan id 10
      address 192.168.10.1
      netmask 255.255.255.0
      post-down ip link del eth0.10

   auto eth0.20
   iface eth0.20 inet static
      pre-up ip link add link eth0 name eth0.20 type vlan id 20
      address 192.168.20.1
      netmask 255.255.255.0
      post-down ip link del eth0.20
   ```
5. Genstart alle maskiner og test at ping imellem PC1 og PC2 ikke virker.

6. Aktivere routing på routeren:
   ```bash
   sysctl -w net.ipv4.ip_forward=1
   ```
7. Test med ping fra PC1 til PC2 (skal virke) og fra PC2 til PC1 (skal virke).

8. Tilføj firewall-regler til at tillade trafik fra vlan 10 til vlan 20 men ikke den anden vej i `/etc/nftables.conf`:
   ```bash
   flush ruleset

   table inet filter {
   set vlan10_subnet {
      type ipv4_addr
      flags interval,constant
      elements = { 192.168.10.0/24 }
   }

   set vlan20_subnet {
      type ipv4_addr
      flags interval,constant
      elements = { 192.168.20.0/24 }
   }

   chain input {
      type filter hook input priority 0; policy drop;

      ct state established,related accept
      iif lo accept
      ip protocol icmp accept
      tcp dport { 22 } accept
      ip daddr { 192.168.10.1, 192.168.20.1 } accept
   }

   chain forward {
      type filter hook forward priority 0; policy drop;

      ct state established,related accept

      # tillad 10 -> 20
      ip saddr @vlan10_subnet ip daddr @vlan20_subnet accept
      # blokér 20 -> 10
      ip saddr @vlan20_subnet ip daddr @vlan10_subnet drop
   }

   chain output {
      type filter hook output priority 0; policy accept;
   }
   }
   ```
   9. Test at ping:
      - ping fra PC1 til PC2 `ping -c2 192.168.20.10` 
      - ping fra PC2 til PC1 (virker ikke) `ping -c2 192.168.10.10`. 
      - Brug wireshark til at bekræfte trafikken.

   ![alt text](img/image-7.png)

---

## Opgave 5: 

**Mål:**
Routeren skal håndtere to VLANs på ét interface. Router skal tillade trafik fra VLAN 20 til VLAN 10, men ikke den anden vej.

**Trin:**
1. Indsæt en switch mellem routeren og de to linux-pc'er.
![alt text](img/image-5.png)
2. Dobbelt klick på switch og opret VLAN-subinterfaces som vist på billede:
![alt text](img/image-6.png)
   - VLAN 10 -> PC1
   - VLAN 20 -> PC2
3. Giv PC'erne IP-adresser:
   1. PC1 (VLAN 10): 192.168.10.10/24 via `/etc/network/interfaces`
   2. PC2 (VLAN 20): 192.168.20.10/24 via `/etc/network/interfaces`
4. Konfigurer routerens `/etc/network/interfaces` fil til at oprette VLAN-subinterfaces:
   ```bash
   auto eth0
   iface eth0 inet manual

   auto eth0.10
   iface eth0.10 inet static
      pre-up ip link add link eth0 name eth0.10 type vlan id 10
      address 192.168.10.1
      netmask 255.255.255.0
      post-down ip link del eth0.10

   auto eth0.20
   iface eth0.20 inet static
      pre-up ip link add link eth0 name eth0.20 type vlan id 20
      address 192.168.20.1
      netmask 255.255.255.0
      post-down ip link del eth0.20
   
   # Tillader routing
   post-up sysctl -w net.ipv4.ip_forward=1

   # Indlæs firewall regler ved opstart
   post-up nft -f /etc/nftables.conf
   ```
5. Genstart alle maskiner og test at ping imellem PC1 og PC2 ikke virker.

6. Aktivere routing på routeren:
   ```bash
   sysctl -w net.ipv4.ip_forward=1
   ```   
7. Test med ping fra PC1 til PC2 (skal virke) og fra PC2 til PC1 (skal virke).

8. Tilføj firewall-regler til at tillade trafik fra vlan 10 til vlan 20 men ikke den anden vej i `/etc/nftables.conf`:
   ```bash
   flush ruleset

   table inet filter {
   set vlan10_subnet {
      type ipv4_addr
      flags interval,constant
      elements = { 192.168.10.0/24 }
   }

   set vlan20_subnet {
      type ipv4_addr
      flags interval,constant
      elements = { 192.168.20.0/24 }
   }

   chain input {
      type filter hook input priority 0; policy drop;

      ct state established,related accept
      iif lo accept
      ip protocol icmp accept
      tcp dport { 22 } accept
      ip daddr { 192.168.10.1, 192.168.20.1 } accept
   }

   chain forward {
      type filter hook forward priority 0; policy drop;

      ct state established,related accept

      # blokér 10 -> 20
      ip saddr @vlan10_subnet ip daddr @vlan20_subnet drop
      # tillad 20 -> 10
      ip saddr @vlan20_subnet ip daddr @vlan10_subnet accept
   }

   chain output {
      type filter hook output priority 0; policy accept;
   }
   }
   ```
   9. Test at ping:
      - ping fra PC1 til PC2 `ping -c2 192.168.20.10` (virker ikke)
      - ping fra PC2 til PC1 (virker) `ping -c2 192.168.10.10`. 
      - Brug wireshark til at bekræfte trafikken.

   ![alt text](img/image-8.png)
---

## Opgave 6: Specifik host adgang mellem VLANs
**Mål:**
Routeren skal tillade al trafik fra VLAN 10 til VLAN 20. Fra VLAN 20 til VLAN 10 må kun én bestemt host (fx 192.168.20.50) komme igennem; alle andre i VLAN 20 blokeres mod VLAN 10.

**Trin:**
1. Indsæt en switch mellem routeren og de to linux-pc'er.
![alt text](img/image-5.png)
2. Dobbelt klick på switch og opret VLAN-subinterfaces som vist på billede:
![alt text](img/image-6.png)
   - VLAN 10 -> PC1
   - VLAN 20 -> PC2
   - VLAN 20 -> PC3 (den specielle host)
3. Giv PC'erne IP-adresser:
   1. PC1 (VLAN 10): 192.168.10.10/24 via `/etc/network/interfaces`
      Eksempel på `/etc/network/interfaces` for PC1:
      ```bash
      auto eth0
      iface eth0 inet static
         address 192.168.10.10
         netmask 255.255.255.0
         gateway 192.168.10.1
      ```
   2. PC2 (VLAN 20): 192.168.20.10/24 via `/etc/network/interfaces`
      Eksempel på `/etc/network/interfaces` for PC2:
      ```bash
      auto eth0
      iface eth0 inet static
         address 192.168.20.20
         netmask 255.255.255.0
         gateway 192.168.20.1
      ```
   3. PC3 (VLAN 20): 192.168.20.50/24 via `/etc/network/interfaces`
      Eksempel på `/etc/network/interfaces` for PC3:
      ```bash
      auto eth0
      iface eth0 inet static
         address 192.168.20.50
         netmask 255.255.255.0
         gateway 192.168.20.1
      ```

4. Konfigurer routerens `/etc/network/interfaces` fil til at oprette VLAN-subinterfaces:
   ```bash
   auto eth0
   iface eth0 inet manual

   auto eth0.10
   iface eth0.10 inet static
      pre-up ip link add link eth0 name eth0.10 type vlan id 10
      address 192.168.10.1
      netmask 255.255.255.0
      post-down ip link del eth0.10

   auto eth0.20
   iface eth0.20 inet static
      pre-up ip link add link eth0 name eth0.20 type vlan id 20
      address 192.168.20.1
      netmask 255.255.255.0
      post-down ip link del eth0.20
   
   # Tillader routing
   post-up sysctl -w net.ipv4.ip_forward=1

   # Indlæs firewall regler ved opstart
   post-up nft -f /etc/nftables.conf
   ```
   *Når du starter routeren vil den melde fejl på nftables men det er fordi den ikke er oprettet i nu.*

5. Genstart alle maskiner og test at ping imellem alle PC'erne virker.

6. Tilføj firewall-regler til at tillade trafik fra vlan 10 til vlan 20 men kun imellem vlan 10 og PC3 i vlan 20. Lav regler i `/etc/nftables.conf`:
   ```bash
   vi /etc/nftables.conf
   ```
   Indsæt følgende indhold i filen:
   ```bash
   flush ruleset

   table inet filter {
   chain input {
      type filter hook input priority 0; policy drop;
      ct state established,related accept
      iif lo accept
      ip protocol icmp accept
      tcp dport { 22 } accept
      ip daddr { 192.168.10.1, 192.168.20.1 } accept
   }

   chain forward {
      type filter hook forward priority 0; policy drop;
      ct state established,related accept

      # Tillad ALT fra VLAN 10 -> VLAN 20
      ip saddr 192.168.10.0/24 ip daddr 192.168.20.0/24 accept

      # Whitelist: kun denne ene host i VLAN 20 må til VLAN 10
      ip saddr 192.168.20.50 ip daddr 192.168.10.0/24 accept

      # Blokér al øvrig VLAN 20 -> VLAN 10
      ip saddr 192.168.20.0/24 ip daddr 192.168.10.0/24 drop
   }

   chain output {
      type filter hook output priority 0; policy accept;
   }
   }
   ```
7. Genstart alle 4 maskiner for at indlæse de nye regler.
8. Test at ping:
   - ping fra PC1 til PC2 `ping -c2 192.168.20.20` (virker ikke)
   - ping fra PC1 til PC3 `ping -c2 192.168.20.50` (virker)
   - ping fra PC2 til PC1 `ping -c2 192.168.10.10` (virker ikke)
9. Verificer med wireshark på routerens interfaces at trafikken bliver håndteret korrekt.
   ![alt text](img/image-9.png)
   *Bemærk at ping fra PC2 til PC1 bliver droppet af firewall-reglerne, mens ping fra PC3 til PC1 bliver accepteret.*

---

## Opgave 7: 
**Mål:**
Routeren skal tillade trafik mellem `192.168.10.20` i VLAN 10 og `192.168.20.50` i VLAN 20. Al trafik mellem VLAN 10 og VLAN 20 blokeres.

**Trin:**
1. Indsæt en switch mellem routeren og de 4 linux-pc'er.
![alt text](img/image-10.png)
2. Dobbelt klick på switch og opret VLAN-subinterfaces som vist på billede:
![alt text](img/image-11.png)
   - VLAN 10 -> PC1 `192.168.10.10`
   - VLAN 10 -> PC2 `192.168.10.20` (den specielle host)
   - VLAN 20 -> PC3 `192.168.20.50` (den specielle host)
   - VLAN 20 -> PC4 `192.168.20.20`
3. Giv PC'erne IP-adresser:
   1. PC1 (VLAN 10): 192.168.10.10/24 via `/etc/network/interfaces`
      Eksempel på `/etc/network/interfaces` for PC1:
      ```bash
      auto eth0
      iface eth0 inet static
         address 192.168.10.10
         netmask 255.255.255.0
         gateway 192.168.10.1
      ```
   2. PC2 (VLAN 10): 192.168.10.20/24 via `/etc/network/interfaces`
      Eksempel på `/etc/network/interfaces` for PC2:
      ```bash
      auto eth0
      iface eth0 inet static
         address 192.168.10.20
         netmask 255.255.255.0
         gateway 192.168.10.1
      ```
   3. PC3 (VLAN 20): 192.168.20.50/24 via `/etc/network/interfaces`
      Eksempel på `/etc/network/interfaces` for PC3:
      ```bash
      auto eth0
      iface eth0 inet static
         address 192.168.20.50
         netmask 255.255.255.0
         gateway 192.168.20.1
      ```
   4. PC4 (VLAN 20): 192.168.20.20/24 via `/etc/network/interfaces`
      Eksempel på `/etc/network/interfaces` for PC4:
      ```bash
      auto eth0
      iface eth0 inet static
         address 192.168.20.20
         netmask 255.255.255.0
         gateway 192.168.20.1
      ```

4. Konfigurer routerens `/etc/network/interfaces` fil til at oprette VLAN-subinterfaces:
   ```bash
   auto eth0
   iface eth0 inet manual

   auto eth0.10
   iface eth0.10 inet static
      pre-up ip link add link eth0 name eth0.10 type vlan id 10
      address 192.168.10.1
      netmask 255.255.255.0
      post-down ip link del eth0.10

   auto eth0.20
   iface eth0.20 inet static
      pre-up ip link add link eth0 name eth0.20 type vlan id 20
      address 192.168.20.1
      netmask 255.255.255.0
      post-down ip link del eth0.20
   
   # Tillader routing
   post-up sysctl -w net.ipv4.ip_forward=1

   # Indlæs firewall regler ved opstart
   post-up nft -f /etc/nftables.conf
   ```
   *Når du starter routeren vil den melde fejl på nftables men det er fordi den ikke er oprettet i nu.*

5. Genstart alle maskiner og test at ping imellem alle PC'erne virker.

6. Tilføj firewall-regler til at tillade trafik mellem IP'er fra white liste {`192.168.10.20`, `192.168.20.50`}. Lav regler i `/etc/nftables.conf`:
   ```bash
   vi /etc/nftables.conf
   ```
   Indsæt følgende indhold i filen:
   ```bash
   flush ruleset

   table inet filter {
   chain input {
      type filter hook input priority 0; policy drop;
      ct state established,related accept
      iif lo accept
      ip protocol icmp accept
      tcp dport { 22 } accept
      ip daddr { 192.168.10.1, 192.168.20.1 } accept
   }

   chain forward {
      type filter hook forward priority 0; policy drop;
      ct state established,related accept

      # Tillad ALT fra VLAN 10 -> VLAN 20
      ip saddr 192.168.10.0/24 ip daddr 192.168.20.0/24 accept

      # Whitelist: kun disse to hosts må kommunikere mellem VLANs
      ip saddr 192.168.20.50 ip daddr 192.168.10.0/24 accept
      ip saddr 192.168.10.20 ip daddr 192.168.20.0/24 accept

      # Blokér al øvrig VLAN 20 -> VLAN 10
      ip saddr 192.168.20.0/24 ip daddr 192.168.10.0/24 drop
      ip saddr 192.168.10.0/24 ip daddr 192.168.20.0/24 drop
   }

   chain output {
      type filter hook output priority 0; policy accept;
   }
   }
   ```
7. Genstart alle 4 maskiner for at indlæse de nye regler.
8. Test at ping:
   - ping fra PC1 til PC3 `ping -c2 192.168.20.50` (virker ikke)
   - ping fra PC1 til PC4 `ping -c2 192.168.20.20` (virker ikke)
   - ping fra PC2 til PC3 `ping -c2 192.168.20.50` (virker)
   - ping fra PC2 til PC4 `ping -c2 192.168.20.20` (virker ikke)
9. Verificer med wireshark på routerens interfaces at trafikken bliver håndteret korrekt.
   ![alt text](img/image-9.png)
   *Bemærk at ping fra PC2 til PC1 bliver droppet af firewall-reglerne, mens ping fra PC3 til PC1 bliver accepteret.*

---


