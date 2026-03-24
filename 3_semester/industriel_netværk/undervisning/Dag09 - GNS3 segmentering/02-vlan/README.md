# 02 - VLAN

I denne del arbejder du med VLAN i GNS3. Fokus er først at forstå isolation mellem VLAN og derefter at aktivere kommunikation med inter-VLAN routing.

---

## Læringsmål

- Forstå hvorfor VLAN bruges til logisk segmentering
- Konfigurere to VLAN i GNS3
- Verificere isolation mellem VLAN
- Aktivere routing mellem VLAN via en Linux-router
- Dokumentere trunk, access-porte og gateway-konfiguration

---

## Progression

1. Opret to VLAN og bekræft isolation
2. Tænd routing mellem VLAN 10 og VLAN 20
3. Udvid løsningen til flere switche med router-on-a-stick
4. Brug fejlsøgning og målinger til at validere tagging og trafikflow

---

## Opgaver

1. [01-opgave.md](./01-opgave.md)
Introduktion til to VLAN med isolation og en sovende "dørmand".

2. [02-opgave.md](./02-opgave.md)
Inter-VLAN routing mellem VLAN 10 og VLAN 20.

3. [03-opgave.md](./03-opgave.md)
Router-on-a-stick over to switche.

4. [04-opgave.md](./04-opgave.md)
Supplerende eller udvidet VLAN-øvelse.

---

## Anbefalet gennemførelse

1. Start med opgave 1 for at forstå ren VLAN-isolation.
2. Gå videre til opgave 2 for at aktivere routing mellem VLAN.
3. Brug opgave 3 til at arbejde med trunk over flere switche.
4. Brug opgave 4 som repetition eller ekstra træning.

---

## Dokumentation

Dokumenter gerne med:

- topologi i GNS3
- VLAN- og portopsætning på switch
- output fra `ip -br addr` og `ip route`
- ping-tests før og efter routing aktiveres
- `tcpdump`-output hvis du undersøger tagging på trunk

---

## Videre i forløbet

Når VLAN og isolation er forstået, er næste skridt routing mellem adskilte subnet og flere routere.

