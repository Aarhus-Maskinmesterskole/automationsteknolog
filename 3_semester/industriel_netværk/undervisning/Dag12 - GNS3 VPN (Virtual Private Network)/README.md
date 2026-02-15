# WireGuard: Windows ↔ GNS3-router ↔ Linux-PC

*(Ingen firewall — fuld guide i Markdown)*

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
