# Dag 09 - GNS3 Segmentering

Velkommen til dag 9 af Industrielt Netværk.

> I dag går vi fra et fladt netværk til opdelte net med subnet, VLAN og routing mellem segmenter.

---

## Læringsmål for dagen

- Forklare forskellen på subnetting og VLAN-segmentering
- Opdele et netværk i mindre logiske enheder i GNS3
- Forstå hvornår en router er nødvendig mellem segmenter
- Dokumentere og teste trafik mellem segmenter
- Forberede grundlaget for Dag 10 med statisk routing

---

## Placering i forløbet

1. Forrige dag: [Dag08 - GNS3 Ping, ARP og Traceroute/README.md](./../Dag08%20-%20GNS3%20Ping%2C%20ARP%20og%20Traceroute/README.md)
2. Denne dag: opdeling og strukturering af netværket
3. Næste dag: [Dag10 - GNS3 Routing og ACL/README.md](./../Dag10%20-%20GNS3%20Routing%20og%20ACL/README.md)

---

## Dagens progression

1. Start med subnetting og adresseplanlægning
2. Arbejd videre med VLAN og isolation
3. Byg routing mellem segmenter
4. Brug ekstra øvelser til at forbinde teori og praksis

---

## Opgaver og materialer

1. [01-subnetting/README.md](./01-subnetting/README.md)
2. [02-vlan/01-opgave.md](./02-vlan/01-opgave.md)
3. [03-routing/01-opgaver.md](./03-routing/01-opgaver.md)
4. [router-subnet-routing.md](./router-subnet-routing.md)
5. [router-bridge.md](./router-bridge.md)

---

## Anbefalet gennemførelse

1. Start med subnetting for at få adresseplanen på plads
2. Gå videre til VLAN for at forstå logisk segmentering på switchniveau
3. Arbejd derefter med routing mellem adskilte net
4. Brug de ekstra router-øvelser til at forstærke forståelsen

---

## Dokumentation

Dokumenter gerne med:

- IP-plan og subnetberegninger
- skærmbillede af topologi i GNS3
- output fra `ip addr`, `ip route` og relevante switch-kommandoer
- ping-tests mellem segmenter
- kort forklaring af hvorfor trafik virker eller ikke virker

---

## Næste dag

Næste naturlige skridt er at styre trafikken mellem netværkszoner med statisk routing og adgangskontrol.
