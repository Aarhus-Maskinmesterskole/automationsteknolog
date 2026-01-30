# Subnetting 101 🧠🧮

Kort intro og fælles teori til repo’et. Eksempler er generiske, så dine opgaver forbliver uden facit.

## Hvorfor subnetting? 💡

* Segmentér net for sikkerhed og orden
* Styre broadcast‑domæner
* Udnytte adresser effektivt

## Grundbegreber 🔎

* **Prefix/CIDR**: f.eks. `/24` = 24 netbits, 8 hostbits.
* **Netadresse**: første adresse i subnet. Ikke tildelbar.
* **Broadcast**: sidste adresse i subnet. Ikke tildelbar.
* **Brugbar værts‑range**: alt mellem net og broadcast.
* **Blokstørrelse**: antal adresser i subnet = `2^(32 − prefix)`.
* **Brugbare værter**: `2^(32 − prefix) − 2`.

## Arbejdsgang (metode) 🛠️

1. Notér udgangspunkt, fx `X.Y.Z.0/24`.
2. Vælg nyt prefix, fx `/25` eller `/26`.
3. Beregn blokstørrelse: `2^(32 − prefix)`.
4. Læg blokstørrelsen til for at finde næste net.
5. Net = start, Broadcast = én før næste net. Range = mellem net og broadcast.
6. Tjek: Ingen host må bruge net/broadcast. Gateways er typisk første brugbare.

## Mini‑eksempel (andre tal end i opgaverne) 📘

Udgangspunkt: `10.10.10.0/24`.

* Split til `/25` → blokstørrelse 128 → net: `10.10.10.0/25`, `10.10.10.128/25`.
* Split til `/26` → blokstørrelse 64 → net: `10.10.10.0/26`, `10.10.10.64/26`, `10.10.10.128/26`, `10.10.10.192/26`.

## Hurtige tommelfingerregler 🧠

* `/25` = to halve af et `/24` (spring på 128 i sidste oktet).
* `/26` = fire kvarte af et `/24` (spring på 64 i sidste oktet).
* Broadcast = **næste net − 1**.

## Tjekliste ✔️

* [ ] Prefix matcher opgaven (/25 eller /26)
* [ ] Net og broadcast fundet pr. subnet
* [ ] Værts‑range tjekket (ingen net/broadcast som host)

## GNS3 brug (Linux‑router + Linux‑PC’er) 🖥️🧪

**Antag** noderne er oprettet. Brug kun Linux‑kommandoer.

**Find interfaces**

```bash
ip -br link
```

**Sæt IP’er**

```bash
ip addr replace <IP/CIDR> dev <if>
ip link set <if> up
```

**Default‑route på PC**

```bash
ip route replace default via <gateway>
```

**Routing på router**

```bash
sysctl -w net.ipv4.ip_forward=1
```

**Test**

```bash
ping <mål>
traceroute <mål>    # eller tracepath
```

**Fejlsøgning**

```bash
ip -br a; ip r; ip neigh; cat /proc/sys/net/ipv4/ip_forward
```

> Opgavefilerne indeholder ingen facit. Brug README’et her som støtte, ikke som løsning.

## Quick‑ref tabel 📏

| Prefix | Adresser i subnet | Brugbare værter |
| -----: | ----------------: | --------------: |
|    /30 |                 4 |               2 |
|    /29 |                 8 |               6 |
|    /28 |                16 |              14 |
|    /27 |                32 |              30 |
|    /26 |                64 |              62 |
|    /25 |               128 |             126 |
|    /24 |               256 |             254 |

## Ordliste 🗣️

* **CIDR**: Classless Inter‑Domain Routing. Notation for prefixlængde.
* **LAN**: Local Area Network.
* **Gateway**: Typisk routerens IP i subnettet. Første eller sidste brugbare.

God arbejdslyst. Hold det simpelt, regn først, tast bagefter. 🚀
