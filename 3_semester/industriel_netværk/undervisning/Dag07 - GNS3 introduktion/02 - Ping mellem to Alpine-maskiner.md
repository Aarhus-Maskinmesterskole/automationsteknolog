# Ping mellem to Alpine-maskiner

I denne øvelse opbygger du et simpelt netværk med to Alpine-maskiner i GNS3 og verificerer forbindelsen med ping.

## Placering i forløbet

1. Forrige øvelse: [01 - Installation af GNS3](01%20-%20Installation%20af%20GNS3.md)
2. Denne øvelse: midlertidig IP-konfiguration og ping i samme subnet.
3. Næste øvelse: [03 - Permanent IP på Alpine-maskiner](03%20-%20Permanent%20IP%20på%20Alpine-maskiner.md)
4. Derefter: [04 - Router mellem to subnet](04%20-%20Router%20mellem%20to%20subnet.md)

## Læringsmål

Når du er færdig, kan du:
1. Oprette en topologi med to hosts i samme subnet.
2. Tildele IP-adresser manuelt på Linux-interface.
3. Verificere Layer 3-forbindelse med ICMP (ping).
4. Fejlsøge grundlæggende netværksfejl.

## Kort teori: Hvorfor ping?

`ping` bruger ICMP Echo Request/Echo Reply til at teste om en destination kan nås. Hvis du får svar, ved du at IP-laget fungerer mellem enhederne. Før ping lykkes, skal interface være oppe, IP-adresser være korrekte og enhederne være i samme subnet.

## IP-plan til øvelsen

1. PC1: `10.0.0.1/24`
2. PC2: `10.0.0.2/24`
3. Subnet: `10.0.0.0/24`

## Trin 1: Opret topologi

1. Start GNS3 og opret et nyt projekt, fx `dag07-ping`.
2. Tilføj to Alpine-maskiner fra enhedslisten (`itifn-pc:1.0`).
3. Forbind maskinerne direkte på `eth0`.
4. Start begge maskiner.
5. Åbn en console på hver maskine.

## Trin 2: Konfigurer IP-adresser

Kør følgende på PC1:

```bash
ip addr add 10.0.0.1/24 dev eth0
ip link set eth0 up
ip -br addr show eth0
```

Kør følgende på PC2:

```bash
ip addr add 10.0.0.2/24 dev eth0
ip link set eth0 up
ip -br addr show eth0
```

## Trin 3: Test forbindelsen

1. Fra PC1:

```bash
ping -c 4 10.0.0.2
```

2. Fra PC2:

```bash
ping -c 4 10.0.0.1
```

3. Kontrollér ARP-tabellen på en af maskinerne:

```bash
ip neigh
```

## Verifikation (succeskriterier)

1. Begge maskiner har korrekt IP på `eth0`.
2. Ping virker i begge retninger.
3. Packet loss er 0 procent.
4. `ip neigh` viser modpartens IP/MAC.

## Fejlfinding

1. Ingen ping-svar:
Kontroller at begge interfaces er up med `ip -br link`.
2. Forkert IP/subnet:
Kontroller adresser med `ip -br addr`.
3. Ingen ARP-entry:
Kontroller fysisk/virtuel forbindelse i GNS3-topologien.
4. En node starter ikke:
Genstart noden og kontroller image-konfiguration.

## Refleksionsspørgsmål

1. Hvorfor kan to hosts ikke pinge hinanden, hvis de ligger i forskellige subnet uden router?
2. Hvad fortæller ARP-tabellen dig i denne øvelse?
3. Hvilken forskel er der på link-status og IP-forbindelse?

## Ekstraopgave

1. Skift begge adresser til subnettet `192.168.10.0/24` og gentag testen.
2. Dokumenter din løsning med kommandooutput fra `ip -br addr` og `ping`.
