# 01 — Split net op i 2 subnets

## Formål (forbedret)
- Træne sikker og hurtig opdeling af et /24 i to /25 uden værktøj.
- Indøve fast metode: prefix → blokstørrelse → net → broadcast → host-range.
- Klargøre adressering til efterfølgende VLAN- og routing-øvelser.

## Læringsmål
- Efter opgaven kan du:
- Forklare relationen mellem prefix, host-bits og antal adresser.
- Beregne blokstørrelse for /25 og udlede brugbare værter.
- Udpege net- og broadcast-adresser for begge /25 i 192.168.1.0/24.
- Angive første og sidste brugbare IP pr. subnet.
- Validere løsningen med multipla-reglen og “broadcast = næste net − 1”.

## Forudsætninger

* IPv4 basis. Ingen lommeregnerkrav, men du må gerne bruge en.
* Brug kun **/25** som nyt prefix. Ingen VLSM her.

---

## Opgave

Givet: **192.168.1.0/24**. Del i **2 subnet** af samme størrelse (**/25**).

### Trin 1 — Nyt prefix

* Skriv det nye prefix: `____ / ____`
* Antal host‑bits: `____`

### Trin 2 — Blokstørrelse og antal adresser

* Formel: `blokstørrelse = 2^(32 − prefix)`  → `2^(32 − ____ ) = ____`
* Brugbare værts‑IP pr. subnet: `blokstørrelse − 2 = ____`

### Trin 3 — Find de to subnet

Start fra 192.168.1.0 og læg blokstørrelsen til for at finde næste net.

* Subnet #1 netadresse: `____________`
* Subnet #2 netadresse: `____________`

### Trin 4 — Net- og broadcast pr. subnet

For hvert subnet:

* **Subnet #1**

  * Net: `____________`
  * Broadcast: `____________`
* **Subnet #2**

  * Net: `____________`
  * Broadcast: `____________`

### Trin 5 — (valgfrit) Første og sidste brugbare IP

* **Subnet #1**: `første ____`  `sidste ____`
* **Subnet #2**: `første ____`  `sidste ____`

---

## Tjekliste

* [ ] To net identificeret korrekt med /25 maske
* [ ] To broadcast‑adresser er korrekt fundet
* [ ] (Valgfrit) Første og sidste brugbare er korrekt

## Tips

* /25 betyder at den sidste **bit** i tredje oktet er delt, så springet ligger i **fjerde oktet**.
* Brug mental tommelfingerregel for /25: *to halvdeles af /24*.
* Hurtig kontrol: Netadresser ligger på multipla af blokstørrelsen. Broadcast er én adresse før næste net.

> **Bemærk:** Ingen facit her. Vi retter sammen i klassen.
