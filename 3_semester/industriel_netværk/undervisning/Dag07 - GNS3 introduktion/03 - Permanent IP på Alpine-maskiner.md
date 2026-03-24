# Permanent IP-adresse på Alpine-maskiner

I denne øvelse gør du IP-konfigurationen permanent, så maskinerne beholder samme adresse efter genstart. Det er et vigtigt skridt, før du arbejder videre med routere, services og større topologier.

## Placering i forløbet

1. Forrige øvelse: [02 - Ping mellem to Alpine-maskiner](02%20-%20Ping%20mellem%20to%20Alpine-maskiner.md)
2. Denne øvelse: gør host-konfiguration stabil efter reboot.
3. Næste øvelse: [04 - Router mellem to subnet](04%20-%20Router%20mellem%20to%20subnet.md)

## Læringsmål

Når du er færdig, kan du:
1. Forklare forskellen på midlertidig og permanent IP-konfiguration.
2. Konfigurere statisk IP i Alpine Linux.
3. Verificere at konfigurationen overlever genstart.
4. Fejlsøge fejl i interface-konfiguration.

## Hvorfor permanent IP-adresse?

Hvis IP-adressen ændrer sig ved genstart, kan scripts, firewallregler, testcases og services fejle. En fast adresse gør netværket forudsigeligt og lettere at dokumentere.

## IP-plan til øvelsen

1. PC1: `10.0.0.1/24`
2. PC2: `10.0.0.2/24`
3. Netværk: `10.0.0.0/24`

## Trin 1: Klargør topologi

1. Start GNS3 og åbn et projekt med to Alpine-maskiner.
2. Forbind dem via `eth0`.
3. Start begge noder og åbn console.

## Trin 2: Konfigurer permanent IP på PC1

> ### ⌨️ `vi` Overlevelsesguide
> Bare rolig, `vi` er simpel, når man kender de 3 trin:
> 1. **Tryk `i`**: Nu kan du skrive (Insert mode).
> 2. **Skriv din tekst**: Brug piletasterne til at navigere.
> 3. **Tryk `Esc`**, skriv `:wq` og tryk **Enter**: Gemmer og lukker (Write & Quit).
> *(Hvis det går helt galt: Tryk `Esc` og skriv `:q!` for at lukke uden at gemme)*

1. Åbn netværksfilen:

```bash
vi /etc/network/interfaces
```

2. Indsæt eller opdater til:

```text
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
    address 10.0.0.1
    netmask 255.255.255.0
```

3. Gem filen og genstart netværket:

```bash
/etc/init.d/networking restart
```

## Trin 3: Konfigurer permanent IP på PC2

1. Gentag samme procedure, men brug adressen `10.0.0.2`.
2. Genstart netværket på PC2.

## Trin 4: Verificer konfigurationen

Kør på begge maskiner:

```bash
ip -br addr show eth0
```

Test forbindelse fra PC1:

```bash
ping -c 4 10.0.0.2
```

## Trin 5: Test efter genstart

1. Genstart begge noder i GNS3.
2. Kør igen:

```bash
ip -br addr show eth0
ping -c 4 10.0.0.2
```

Hvis adresserne er de samme efter reboot, er konfigurationen permanent.

## Verifikation (succeskriterier)

1. Begge noder får korrekt IP-adresse automatisk efter opstart.
2. Ping virker efter genstart.
3. Ingen manuel `ip addr add` er nødvendig.

## Fejlfinding

1. IP mangler efter reboot:
Kontroller syntaksen i `/etc/network/interfaces`.
2. Interface kommer ikke up:
Kontroller at `auto eth0` er med i filen.
3. Ping fejler:
Kontroller subnet, kabel i GNS3 og `ip -br addr` på begge noder.
4. Forkert editor-kommando:
Brug `vi` hvis `vim` ikke er installeret.

## Refleksionsspørgsmål

1. Hvornår vil DHCP være bedre end statisk IP?
2. Hvorfor er permanent IP vigtig i laboratorie- og produktionsmiljøer?
3. Hvad er risikoen ved dårlig dokumentation af IP-plan?

## Ekstraopgave

1. Tilføj en tredje node med IP `10.0.0.3/24`.
2. Verificer ping mellem alle tre noder.
3. Dokumenter resultatet med en tabel over IP-adresser og testresultater.