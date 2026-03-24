# Dag 08 - GNS3 Ping, ARP og Traceroute

Velkommen til dag 8 af Industrielt Netværk.

> I dag arbejder vi med de vigtigste værktøjer til netværksforståelse og fejlfinding i GNS3: `ping`, ARP og `traceroute`.

---

## Læringsmål for dagen

- Forstå hvad `ping` kan og ikke kan fortælle om en forbindelse
- Forklare hvordan ARP bruges til at finde MAC-adresser på lokale netværk
- Bruge `traceroute` til at se vejen gennem et netværk
- Dokumentere og fejlfinde forbindelsesproblemer systematisk
- Koble værktøjerne til de topologier, der blev bygget på Dag 07

---

## Placering i forløbet

1. Forrige dag: [Dag07 - GNS3 Introduktion/README.md](./../Dag07%20-%20GNS3%20introduktion/README.md)
2. Denne dag: netværksanalyse og fejlfinding i de miljøer, du allerede har bygget
3. Næste dag: [Dag09 - GNS3 Segmentering/README.md](./../Dag09%20-%20GNS3%20Segmentering/README.md)

---

## Dagens progression

1. Verificér lokal forbindelse med `ping`
2. Undersøg hvordan ARP knytter IP-adresser til MAC-adresser
3. Brug `traceroute` til at se vejen mellem subnet
4. Saml resultaterne i en kort fejlsøgningsmetode

---

## Opgaver

1. Genbrug topologien fra Dag 07 med to hosts og en router
2. Test forbindelse i samme subnet og mellem to subnet
3. Brug `ip neigh` eller tilsvarende til at se ARP-tabellen
4. Brug `traceroute` eller `tracepath` til at identificere hop
5. Beskriv forskellen på lokal levering og routing via gateway

---

## Anbefalet gennemførelse

1. Start med en topologi hvor ping allerede virker
2. Slet eller ryd ARP-tabellen og observer hvad der sker ved første ping
3. Test `traceroute` fra et subnet til et andet
4. Dokumentér hvilke kommandoer du brugte, og hvad de viste

---

## Egne noter og dokumentation

Dokumenter gerne med:

- skærmbillede af GNS3-topologi
- output fra `ping`
- output fra `ip neigh`
- output fra `traceroute` eller `tracepath`
- kort forklaring af hvad hvert hop eller hver ARP-entry betyder

Inden undervisningen slutter vises dette til underviseren, og der er mulighed for at stille spørgsmål og få feedback.

---

## Næste dag

Næste naturlige skridt er at opdele netværket i segmenter med subnet og VLAN.
