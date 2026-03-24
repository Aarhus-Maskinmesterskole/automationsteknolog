# Dag 12 - GNS3 VPN

Velkommen til dag 12 af Industrielt Netværk.

> I dag arbejder vi med sikker fjernadgang til et GNS3-netværk ved hjælp af VPN. Fokus er på WireGuard som en enkel og moderne metode til at nå ind i et afgrænset laboratorienetværk.

---

## Læringsmål for dagen

- Forstå hvorfor VPN er relevant i industrielle netværk
- Konfigurere en WireGuard-tunnel mellem Windows og en Linux-router i GNS3
- Route trafik fra VPN-klienten ind i et internt laboratorienetværk
- Teste og dokumentere sikker fjernadgang
- Koble VPN sammen med det segmenterede og beskyttede netværk fra Dag 10 og 11

---

## Placering i forløbet

1. Forrige dag: [Dag11 - GNS3 Firewall/README.md](./../Dag11%20-%20GNS3%20Firewall/README.md)
2. Denne dag: sikker adgang ind i et eksisterende GNS3-miljø
3. Supplerende materiale: [RDP.md](./RDP.md)

---

## Dagens progression

1. Klargør router og intern Linux-PC
2. Installer og konfigurer WireGuard på Windows
3. Opret tunnel og aktiver IP-forwarding på routeren
4. Test adgang til både tunnel-interface og LAN bag routeren

---

## Opgaver

1. Konfigurér router, LAN og VPN-interface
2. Installer og opsæt WireGuard-klienten på Windows
3. Verificér tunnel og adgang til LAN bag routeren
4. Brug [RDP.md](./RDP.md) som supplerende materiale til fjernadgang

---

## Hovedøvelse: WireGuard mellem Windows, GNS3-router og Linux-PC

### WireGuard: Windows ↔ GNS3-router ↔ Linux-PC

*(Ingen firewall — fuld guide i Markdown)*

---

## Anbefalet gennemførelse

1. Start med at klargøre router og intern Linux-PC
2. Konfigurér derefter WireGuard på routeren
3. Opsæt klienten på Windows og test tunnelen
4. Afslut med at verificere adgang til LAN bag routeren

---

## Egne noter og dokumentation

Dokumenter gerne med:

- IP-plan for WAN, LAN og VPN-net
- skærmbillede af tunnelkonfiguration
- output fra `wg`, `ip route` og ping-tests
- kort forklaring af hvordan trafikken bevæger sig gennem tunnelen

Inden undervisningen slutter vises dette til underviseren, og der er mulighed for at stille spørgsmål og få feedback.

---

## Næste dag

Efter Dag 12 kan forløbet samles i større scenarier, hvor segmentering, routing, firewall og VPN kombineres i samme topologi.

---

### IP-adresser:

| Enhed    | Interface  | IP                         |
| -------- | ---------- | -------------------------- |
| Windows  | VMnet1     | 192.168.2.1/24             |
| Router   | eth0 (WAN) | 192.168.2.2/24             |
| Router   | eth1 (LAN) | 10.0.0.1/24                |
| Linux-PC | eth0       | 10.0.0.10/24 (GW 10.0.0.1) |

### WireGuard-net:

* Router wg0: **10.10.10.1/24**
* Windows wg0: **10.10.10.2/32**

---

# 🛠 1. Opsæt IP-adresser (router og Linux-PC)

## 1.1 Router (“router-nfw-1”)

```sh
# WAN mod Windows / Cloud
ip addr add 192.168.2.2/24 dev eth0
ip link set eth0 up

# LAN mod Linux-PC
ip addr add 10.0.0.1/24 dev eth1
ip link set eth1 up
```

Tjek:

```sh
ip addr show eth0
ip addr show eth1
```

---

## 1.2 Linux-PC (“aams-linux-pc-1”)

```sh
ip addr add 10.0.0.10/24 dev eth0
ip link set eth0 up

# Default route ind mod routeren
ip route add default via 10.0.0.1
```

Tjek:

```sh
ip addr show eth0
ip route
```

Test LAN:

* Fra Linux-PC → `ping 10.0.0.1`
* Fra router → `ping 10.0.0.10`

---

# 💾 2. Installer WireGuard på Windows

1. Gå til: [https://www.wireguard.com/install](https://www.wireguard.com/install)
2. Download **WireGuard for Windows**
3. Installér
4. Start programmet → "Add Tunnel" → **Add empty tunnel**

Windows genererer automatisk:

* **PrivateKey**
* **PublicKey**

*Gem Windows PublicKey – den skal ind på routeren.*

---

# 🔐 3. Generér nøgler på routeren

```sh
wg genkey | tee /etc/wireguard/router_private.key | wg pubkey > /etc/wireguard/router_public.key
```

### Vis (cat) nøglerne:

```sh
cat /etc/wireguard/router_private.key
cat /etc/wireguard/router_public.key
```

Gem:

* Router **private key**
* Router **public key**

---

# 📄 4. Opret `/etc/wireguard/wg0.conf` på routeren

```ini
[Interface]
Address = 10.10.10.1/24
ListenPort = 51820
PrivateKey = <ROUTER_PRIVATE_KEY>

[Peer]
# Windows-klient
PublicKey = <WINDOWS_PUBLIC_KEY>
AllowedIPs = 10.10.10.2/32
```

Erstat:

* `<ROUTER_PRIVATE_KEY>` → fra `router_private.key`
* `<WINDOWS_PUBLIC_KEY>` → fra Windows GUI

---

# 🔁 5. Slå IP-forwarding til (nødvendigt for at nå LAN)

### Midlertidigt:

```sh
sysctl -w net.ipv4.ip_forward=1
```

### Permanent i `/etc/sysctl.conf`:

```
net.ipv4.ip_forward = 1
```

Indlæs igen:

```sh
sysctl -p
```

---

# 🚀 6. Start WireGuard på routeren

```sh
wg-quick up wg0
```

Tjek status:

```sh
wg
```

Du skal se:

```
interface: wg0
  public key: <router_public_key>
  listening port: 51820
  ...
```

Peer står som “(not connected)” indtil Windows forbinder.

---

# 🪟 7. Konfigurer WireGuard på Windows

Åbn WireGuard → vælg din tomme tunnel → indsæt:

```ini
[Interface]
PrivateKey = <WINDOWS_PRIVATE_KEY>
Address = 10.10.10.2/32

[Peer]
PublicKey = <ROUTER_PUBLIC_KEY>
Endpoint = 192.168.2.2:51820
AllowedIPs = 10.0.0.0/24, 10.10.10.1/32
PersistentKeepalive = 25
```

Erstat:

* `<WINDOWS_PRIVATE_KEY>` → Windows’ private key
* `<ROUTER_PUBLIC_KEY>` → router_public.key

Klik **Activate**.

---

# 🧪 8. Test tunnelen

Fra Windows:

```powershell
ping 10.10.10.1
```

Hvis du får svar, er WireGuard-tunnelen aktiv.

---

# 🧭 9. Test adgang til LAN bag routeren

Fra Windows:

```powershell
ping 10.0.0.1
ping 10.0.0.10
```

Hvis begge svarer:

```
Windows → WireGuard → Router → LAN → Linux-PC
```

… virker.

---

# 🎉 Resultat

Når alle trin er fulgt:

* Windows har en WireGuard-tunnel ind i GNS3
* Routeren rout’er trafik ind i LAN
* Linux-PC’en kan nås **direkte** via VPN
* Ingen firewall eller NAT er nødvendige
