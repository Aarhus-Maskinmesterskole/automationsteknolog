# Dag 07 - GNS3 Introduktion

Velkommen til dag 7 af Industrielt Netværk.

> I dag bygger vi fundamentet for resten af GNS3-forløbet: installation, basal IP-konfiguration, forbindelse mellem hosts og routing mellem to subnet.

---

## Læringsmål for dagen

- Installere og klargøre GNS3 og GNS3 VM
- Oprette simple topologier i GNS3
- Konfigurere midlertidige og permanente IP-adresser på Alpine-maskiner
- Forstå forskellen på kommunikation i samme subnet og mellem forskellige subnet
- Verificere forbindelser med ping og grundlæggende routing

---

## Dagens progression

1. Miljøet gøres klar
2. To hosts forbindes i samme subnet
3. IP-konfigurationen gøres permanent
4. En router forbinder to subnet

Dag 7 er dermed fundamentet for de efterfølgende dage med ARP, traceroute, segmentering, routing, firewall og VPN.

---

## Opgaver

1. [01 - Installation af GNS3](01%20-%20Installation%20af%20GNS3.md)
2. [02 - Ping mellem to Alpine-maskiner](02%20-%20Ping%20mellem%20to%20Alpine-maskiner.md)
3. [03 - Permanent IP på Alpine-maskiner](03%20-%20Permanent%20IP%20på%20Alpine-maskiner.md)
4. [04 - Router mellem to subnet](04%20-%20Router%20mellem%20to%20subnet.md)

---

## Anbefalet gennemførelse

1. Start med installation og verifikation af miljøet.
2. Gennemfør ping-øvelsen, så basal host-til-host kommunikation virker.
3. Gør IP-adresserne permanente, så konfigurationen overlever genstart.
4. Afslut med routing mellem to subnet.

---

## Egne noter og dokumentation

Dokumenter gerne undervejs med:

- skærmbillede af topologi i GNS3
- output fra `ip -br addr`
- output fra `ip route`
- resultat af ping-tests

Inden undervisningen slutter vises dette til underviseren, og der er mulighed for at stille spørgsmål og få feedback.

---

## Næste dag

Næste naturlige skridt er at arbejde videre med fejlfinding og værktøjer som ping, ARP og traceroute i GNS3.