# 03 - Routing

I denne del arbejder du med routing mellem subnet uden fokus på VLAN. Målet er at forstå, hvordan routere forbinder adskilte net, og hvordan statiske ruter bygges op trin for trin.

---

## Læringsmål

- Konfigurere routing mellem to subnet med én router
- Forstå default gateway på hosts
- Arbejde med statiske ruter mellem to routere
- Analysere hop og pakkevej med `traceroute` og `ip route`
- Forstå hvordan routing kan bruges til at styre, hvem der kan nå hvem

---

## Progression

1. Start med én router mellem to subnet
2. Udvid til to routere med transitnet
3. Arbejd med et mere styret routingscenarie med flere routere og begrænset reachability

---

## Opgaver

1. [01-opgaver.md](./01-opgaver.md)
Routing mellem to subnet med én Linux-router.

2. [02-opgave.md](./02-opgave.md)
To routere med /30-transit og statiske ruter.

3. [03-opgave.md](./03-opgave.md)
Tre routere og selektiv reachability mellem flere net.

---

## Anbefalet gennemførelse

1. Begynd med opgave 1 for at få basisrouting til at virke.
2. Fortsæt med opgave 2 for at forstå transitnet og flere hop.
3. Slut med opgave 3, hvor routing bruges mere målrettet til at styre trafikmønstre.

---

## Dokumentation

Dokumenter gerne med:

- IP-plan for alle interfaces
- output fra `ip route` på routere og hosts
- ping-tests og `traceroute`
- kort forklaring af hvorfor pakker tager den viste vej

---

## Videre i forløbet

Denne del peger direkte frem mod Dag 10, hvor routing bliver udbygget til flere zoner, redundans og målrettet fejlfinding.

