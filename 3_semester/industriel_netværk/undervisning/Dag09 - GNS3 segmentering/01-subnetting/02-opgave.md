
# 02 — Split 192.168.1.0/24 til 4 subnet (/26)

### Formål (forbedret)

* Træne sikker opdeling af et /24 i fire /26.
* Anvende fast metode: *prefix → blokstørrelse → net → broadcast → host-range*.
* Identificere præcis host-range for **subnet #2** uden hjælpemidler.

### Læringsmål

Efter opgaven kan du:

1. Forklare sammenhængen mellem prefix, host-bits og antal adresser for /26.
2. Beregne blokstørrelse og brugbare værter i et /26.
3. Liste de fire /26-net i 192.168.1.0/24 korrekt og finde net/broadcast for hvert.
4. Udlede første og sidste brugbare IP i **subnet #2**.
5. Validere svaret med multipla-reglen og “broadcast = næste net − 1”.
6. Tjekke om en vilkårlig IP hører til i **subnet #2**.

## Forudsætninger

* Grundlæggende IPv4. Ingen facit i filen.
* Du må bruge lommeregner.

---

## Opgave

Givet: **192.168.1.0/24**. Del i **4 subnet** af samme størrelse (**/26**).

### Trin 1 — Nyt prefix

* Skriv det nye prefix: `____ / ____`
* Antal host‑bits: `____`

### Trin 2 — Blokstørrelse og brugbare adresser

* Formel: `blokstørrelse = 2^(32 − prefix)`  → `2^(32 − ____ ) = ____`
* Brugbare værts‑IP pr. subnet: `blokstørrelse − 2 = ____`

### Trin 3 — Find de fire subnet

Start ved 192.168.1.0. Læg blokstørrelsen til for at finde næste net.

* Subnet #1 netadresse: `____________`
* Subnet #2 netadresse: `____________`
* Subnet #3 netadresse: `____________`
* Subnet #4 netadresse: `____________`

### Trin 4 — Net- og broadcast pr. subnet

* **Subnet #1**
  Net: `____________`  ·  Broadcast: `____________`
* **Subnet #2**
  Net: `____________`  ·  Broadcast: `____________`
* **Subnet #3**
  Net: `____________`  ·  Broadcast: `____________`
* **Subnet #4**
  Net: `____________`  ·  Broadcast: `____________`

### Trin 5 — IP‑range for subnet

* Første brugbare IP: `____________`
* Sidste brugbare IP: `____________`

---

## Tjekliste

* [ ] Fire korrekte /26‑net identificeret
* [ ] Net og broadcast for hvert subnet fundet
* [ ] Første og sidste brugbare for **subnet #2** angivet

## Tips

* /26 giver fire delnet ud af et /24. Springet ligger i **fjerde oktet**.
* Netadresser er multipla af blokstørrelsen. Broadcast er én adresse før næste net.
* Host‑range er alt mellem net og broadcast (ekskl.).
