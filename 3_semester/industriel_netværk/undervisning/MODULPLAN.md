# Modulplan - Netvaerksteknologi

Denne plan er den aktuelle didaktiske plan for forlobet. Den folger website-strukturen i 12 moduler og bruger dagmapperne i `undervisning/` som materialegrundlag. Dagmapperne er derfor fortsat arbejdsmapper med opgaver og ovelser, men de er ikke laengere den primaere struktur for progressionen i faget.

## Didaktisk praemis

- Websitet er den styrende struktur for fagets progression, begreber, laboratorieforlob og studieaktiviteter.
- Dagmaterialerne bruges som kildebank og ovelsesmateriale, der organiseres ind i website-modulerne.
- Enkelte moduler samler materiale fra flere undervisningsdage eller kombinerer klasseundervisning med self-study og aflevering.

## Kursusramme

- 5 ECTS
- 12 moduler
- 2 studieaktiviteter
- Fokus pa at de studerende kan opsaette, forklare, dokumentere, fejlfinde og kvalitetssikre netvaerkslosninger i maskin- og automationsanlaeg

## Modul 01 - Industrielle netvaerk og praksiskontekst

- Fokus: OT/IT, komponentroller, serviceveje og anlaegsforstaelse som professionel ramme for resten af faget.
- Materialegrundlag: website modul 01 samt intro-case, grundbegreber og PLC-naere netvaerksforstaelse fra `Dag01 - Netværk og IP-basic`.
- Planlagte aktiviteter: kort teorioplaeg, case-draeftelse, identifikation af komponentroller og netvaerksskitse.
- Produkt og dokumentation: netvaerksskitse med komponentroller og kort begrundelse for servicevej.

## Modul 02 - IP-adressering og subnetting i GNS3

- Fokus: IPv4, subnetlogik, gateways, routing og dokumentation af adresseplan.
- Materialegrundlag: `Dag07 - GNS3 introduktion`, `Dag08 - GNS3 Ping, ARP og Traceroute` og `Dag09 - GNS3 Segmentering/01-subnetting`.
- Planlagte aktiviteter: opbygning af basal GNS3-topologi, permanent IP-konfiguration, ping, traceroute og subnetopdeling.
- Produkt og dokumentation: adresseplan, output fra `ip addr` og `ip route` samt traceroute- eller ping-evidens.

## Modul 03 - Switches og fysiske topologier

- Fokus: switchroller, MAC-tabeller, portstruktur og industrielle topologier som forberedelse til segmentering.
- Materialegrundlag: website modul 03 og den videre didaktiske opdeling af segmenteringssporet fra `Dag09 - GNS3 Segmentering` suppleret med netvaerksudstyr og grundbegreber fra `Dag01 - Netværk og IP-basic`.
- Planlagte aktiviteter: gennemgang af managed kontra unmanaged switches, fysisk topologi, portplan og analyse af switchingadfaerd.
- Produkt og dokumentation: topologiskitse, portplan og kort analyse af MAC-laering eller trafikflow.

## Modul 04 - Routing og VLAN segmentering

- Fokus: logisk zoneopdeling, VLAN, trunk-forstaelse og routing mellem segmenter.
- Materialegrundlag: `Dag09 - GNS3 Segmentering/02-vlan`, `Dag09 - GNS3 Segmentering/03-routing` og `Dag10 - GNS3 Routing og ACL`.
- Planlagte aktiviteter: VLAN-plan, router-on-a-stick eller tilsvarende segmentering, routing mellem zoner og test af isolation.
- Produkt og dokumentation: VLAN-tabel, netvaerksdiagram, routingtabeller og test af tilladt eller blokeret trafik.

## Modul 05 - Case-aflevering 1: Infrastruktur

- Fokus: samlet dokumentation af de fire forste moduler som en professionel infrastrukturopgave.
- Materialegrundlag: modul 01-04.
- Planlagte aktiviteter: projektarbejde med samlet topologi, adresseplan, zoneopdeling og test.
- Produkt og dokumentation: afleveringsmappe med tegning, adresseplan, dokumenterede valg og test-evidens.

## Modul 06 - Siemens PLC og Profinet

- Fokus: commissioning, device naming, IP-konfiguration og Profinet som industrinaer kommunikationsform.
- Materialegrundlag: PLC- og netvaerksaktiviteter fra `Dag01 - Netværk og IP-basic`, protokolintroduktion fra `Dag02 - Profinet og protokoller` og website-modulet for Siemens/Profinet.
- Planlagte aktiviteter: accessible devices, adressering, navngivning, hardwarekonfiguration og commissioning i TIA Portal.
- Produkt og dokumentation: Profinet-topologi, navngivning, IP-plan og kort commissioningnotat.

## Modul 07 - Siemens PLC-til-PLC-kommunikation

- Fokus: PLC-til-PLC dataudveksling via PUT/GET, TCON, TSEND og TRCV.
- Materialegrundlag: `Dag02 - Profinet og protokoller/01-S7communication.md`, `Dag02 - Profinet og protokoller/02-Open-User-Communication.md` og `Dag03 - Arbejde videre med opgaver fra Dag02`.
- Planlagte aktiviteter: konfiguration af forbindelser, dataudveksling, test, fejlhaandtering og kort refleksion over valg af kommunikationsform.
- Produkt og dokumentation: netvaerksdiagram, blokskaermbilleder, testlog og kort forklaring af valg og resultat.

## Modul 08 - Rockwell PLC og Echo

- Fokus: commissioning og netvaerksforstaelse i et andet fabrikat end Siemens.
- Materialegrundlag: Rockwell/Kepserver-sporet i `Dag06 - KepserverEX (OPC-UA Gateway)/01-kepserver/04-rockwell.md` samt website-modulet for Rockwell og Echo.
- Planlagte aktiviteter: opsaetning af Rockwell- eller Echo-miljo, kommunikationstest og sammenligning med Siemens-sporet.
- Produkt og dokumentation: servicebeskrivelse, skaermbillede af kommunikation eller commissioning og kort sammenligning mellem platformene.

## Modul 09 - Profibus-master og decentral I/O

- Fokus: Profibus, adressering, termination, diagnostik og decentral I/O.
- Materialegrundlag: `Dag04 - Profibus og Modbus TCP/02-profibus-decentral-io.md` samt Profibus-delen af `Dag05 - Profibus, IO-Link og Modbus TCP/01-rotationsøvelse.md`.
- Planlagte aktiviteter: konfiguration af master og slave, hardwareopsaetning, adressevalg, termination og diagnostik.
- Produkt og dokumentation: Profibus-topologi, adresseoversigt, dokumenteret termination og diagnose- eller testresultat.

## Modul 10 - Firewalls, NAT og sikker fjernadgang

- Fokus: sikker segmentering, adgangskontrol, firewall-regler, RDP og VPN som begrundet servicevej.
- Materialegrundlag: `Dag10 - GNS3 Routing og ACL`, `Dag11 - GNS3 Firewall` og `Dag12 - GNS3 VPN`.
- Planlagte aktiviteter: routing mellem zoner, nftables eller tilsvarende filtrering, RDP-scenarie og WireGuard-baseret fjernadgang.
- Produkt og dokumentation: topologi med zoner, regelsaet, test af adgang eller blokering og kort beskrivelse af sikker servicevej.

## Modul 11 - Integration (Kepserver og IO-Link)

- Fokus: bro mellem OT og IT, tagstruktur, datakilder og intelligente enheder.
- Materialegrundlag: `Dag05 - Profibus, IO-Link og Modbus TCP/01-rotationsøvelse.md`, `Dag06 - KepserverEX (OPC-UA Gateway)/01-kepserver/01-siemens-s7.md`, `Dag06 - KepserverEX (OPC-UA Gateway)/01-kepserver/04-rockwell.md` og `Dag06 - KepserverEX (OPC-UA Gateway)/02-siemens-opc-ua/01-s71500-opcua-server.md`.
- Planlagte aktiviteter: opsaetning af Kepserver-kanal, tags, IO-Link-konfiguration og droeftelse af datatilgaengelighed i integrationssporet.
- Produkt og dokumentation: tagliste, oversigt over datakilder, IO-Link-portskema og kort note om integrationsvalg.

## Modul 12 - Case-aflevering 2: Sikker integration

- Fokus: samlet afsluttende case hvor netvaerk, automation, sikkerhed og integration bindes sammen.
- Materialegrundlag: modul 06-11.
- Planlagte aktiviteter: projektarbejde med begrundede tekniske valg, dokumentation og mundtlig eller skriftlig overdragelse.
- Produkt og dokumentation: samlet afleveringspakke med topologi, valgte teknologier, test, sikkerhedsbeskrivelse og overdragelsesegnet dokumentation.

## Studieaktiviteter og vurdering

- Aflevering 1 ligger efter GNS3-grundforlobet og fungerer som dokumenteret milepael for infrastrukturforstaelse.
- Aflevering 2 samler routing, firewall, sikker fjernadgang og integration i en stoerre afsluttende case.
- Den loebende vurdering er formativ og sker gennem dialog, dokumentation, fejlsoegning, korte refleksionssporgsmaal og visning af mellemresultater i undervisningen.

## Praktisk note

Den dagopdelte mappe bevares fortsat som arbejdsstruktur for konkrete opgaver, men den aktuelle kursus- og modulplan for faget er denne plan og website-strukturen, fordi det er her progression, leverancer og studieaktiviteter nu er samlet og gjort eksplicit.
