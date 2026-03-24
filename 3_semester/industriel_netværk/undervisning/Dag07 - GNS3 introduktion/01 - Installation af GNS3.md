# Dag 7 - Installation af GNS3 og GNS3 VM

I dette forløb installerer du GNS3 og GNS3 VM, så du kan bygge og teste netværk i et kontrolleret, virtuelt miljø.

## Forløbsoverblik (Dag 7)

1. Denne øvelse: installer og klargør miljøet.
2. Næste øvelse: [02 - Ping mellem to Alpine-maskiner](02%20-%20Ping%20mellem%20to%20Alpine-maskiner.md)
3. Derefter: [03 - Permanent IP på Alpine-maskiner](03%20-%20Permanent%20IP%20på%20Alpine-maskiner.md)
4. Afslutning: [04 - Router mellem to subnet](04%20-%20Router%20mellem%20to%20subnet.md)

## Læringsmål

Når du er færdig, kan du:
1. Installere GNS3 på Windows.
2. Starte GNS3 VM og forbinde den til GNS3.
3. Oprette et simpelt projekt med to noder.
4. Verificere at laboratoriemiljøet virker.

## Forudsætninger

1. Windows-pc med administratorrettigheder.
2. Virtualisering aktiveret i BIOS/UEFI.
3. Stabil internetforbindelse.
4. Docker installeret (hvis du bruger Docker-baserede noder).

## Tidsforbrug

Forventet tid: 30-45 minutter.

## Trin 1: Installer GNS3

1. Følg installationsguiden til Windows: [GNS3 Windows Installation](../../hardware-og-software/GNS3/gns3-windows.md)
2. Start GNS3 efter installation, og gennemfør førsteopsætningen (Setup Wizard).
3. Aktivér GNS3 VM i indstillingerne, hvis den ikke allerede er aktiv.

## Trin 2: Klargør enheder til øvelser

1. Brug denne vejledning til at hente og indsætte Docker-enheder: [GNS3 Docker devices](../../hardware-og-software/GNS3-IMAGE/README.md)
2. Opret et nyt projekt med et tydeligt navn, fx `dag07-gns3-intro`.
3. Tilføj to PC-enheder i projektet.

## Trin 3: Hurtig funktionstest

1. Se videoen og gennemfør den grundlæggende test: [Ping mellem 2 PC'er](https://www.youtube.com/watch?v=SLBe_yMNwYQ)
2. Start begge enheder og åbn console på hver.
3. Verificer at begge noder kan startes uden fejl.

## Verifikation (succeskriterier)

1. GNS3 starter uden fejl.
2. GNS3 VM vises som connected/running.
3. Projektet indeholder to aktive noder.
4. Du kan åbne console på begge noder.

## Fejlfinding

1. GNS3 VM starter ikke:
Kontroller virtualisering i BIOS/UEFI og at hypervisor/VM-platform er korrekt sat op.
2. Node kan ikke startes:
Kontroller at image er korrekt hentet, og at der er nok RAM/CPU.
3. Console åbner ikke:
Kontroller terminalindstillinger i GNS3 og genstart GNS3.

## Refleksionsspørgsmål

1. Hvorfor er det en fordel at bruge virtuelle netværk i undervisning?
2. Hvad er forskellen på GNS3 desktop og GNS3 VM?
3. Hvilke fejl kan opstå, hvis virtualisering er slået fra?

## Ekstraopgave

1. Opret et ekstra projekt med tre noder og dokumenter topologien med et skærmbillede.