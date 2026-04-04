# Standard Node-RED noder

I denne sektion vil vi gennemgå de vigtigste standard-noder i Node-RED. Disse noder er inkluderet i enhver Node-RED installation og udgør de grundlæggende byggeklodser for de fleste flows.

## Oversigt

Node-RED leveres med et omfattende sæt af standardnoder, der dækker alt fra simple inputs og outputs til avanceret datamanipulation. Vi fokuserer på følgende noder, som er de mest fundamentale:

1. [**Inject**](./01-inject.md) - Indsætter beskeder i et flow, enten manuelt eller efter en tidsplan
2. [**Debug**](./02-debug.md) - Viser beskedindhold og hjælper med at fejlfinde flows
3. [**Function**](./03-function.md) - Tillader brugerdefineret JavaScript-kode til at manipulere beskeder
4. [**Change**](./04-change.md) - Ændrer beskedegenskaber uden at skrive JavaScript
5. [**Switch**](./05-switch.md) - Router beskeder baseret på deres indhold
6. [**Delay**](./06-delay.md) - Introducerer forsinkelser eller rate-limiting i flows
7. [**Template**](./07-template.md) - Skaber formateret output ved hjælp af Mustache-skabeloner

## Hvorfor disse noder er vigtige

Disse syv noder repræsenterer de mest grundlæggende funktioner i Node-RED:

- **Input**: Inject-noden giver en måde at starte flows og teste funktionalitet
- **Output**: Debug-noden er uundværlig for at se resultater og fejlfinde
- **Datamanipulation**: Function-, Change- og Template-noderne tillader forskellige måder at transformere data
- **Flow kontrol**: Switch- og Delay-noderne styrer flowet af beskeder gennem systemet

Ved at mestre disse syv noder kan du bygge en lang række funktionelle flows, selv uden at tilføje yderligere noder.

## Forhold mellem noderne

Disse noder komplementerer hinanden og tilbyder forskellige tilgange til lignende problemer:

- **Function vs. Change**: Function-noden giver fuld JavaScript-programmering, mens Change-noden tilbyder en simpel måde at ændre beskedegenskaber uden at skrive kode.

- **Switch vs. Function**: Switch-noden tilbyder specialiseret routing baseret på beskedindhold, mens en Function-node kan implementere mere kompleks betinget logik.

- **Template vs. Function**: Template-noden er optimeret til at generere formateret tekst, mens Function-noden giver mere fleksibilitet til datamanipulation.

## Kom i gang

Klik på linkene ovenfor for at lære mere om hver node, eller gennemgå dem i rækkefølge for at få en grundig introduktion til Node-RED's kernefunktionalitet.

Hvert modul indeholder:
- Grundlæggende forklaring af nodens funktion
- Konfigurationsindstillinger
- Praktiske eksempler
- Avancerede anvendelser
- Øvelser til at teste din forståelse

## Yderligere ressourcer

- [Node-RED officiel dokumentation](https://nodered.org/docs/)
- [Node-RED bibliotek](https://flows.nodered.org/) - En samling af brugerbidrag og eksempler
- [Node-RED forum](https://discourse.nodered.org/) - Community-forum for spørgsmål og diskussion

