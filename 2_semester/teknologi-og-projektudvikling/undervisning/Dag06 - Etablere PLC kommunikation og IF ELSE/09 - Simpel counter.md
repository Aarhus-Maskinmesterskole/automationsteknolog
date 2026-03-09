# Opgave: Simpel counter med transportbånd

I denne opgave skal du styre et transportbåndssystem med følgende komponenter:

- **Start-knap:** Starter transportbåndet.
- **Fotocelle:** Registrerer, når en kasse ankommer til enden af det første bånd.
- **Chain transfer:** Flytter kassen fra det første bånd til det næste.
- **Kapacitiv føler:** Registrerer, når kassen er placeret korrekt over chain transfer.

## Funktionsbeskrivelse

Systemet fungerer således:
1. Transportbåndet starter, når start-knappen aktiveres.
2. Når fotocellen registrerer en kasse ved enden af båndet, stoppes transportbåndet.
3. Chain transfer aktiveres og flytter kassen til det næste bånd.
4. Kapacitiv føler bruges til at sikre, at kassen er korrekt placeret over chain transfer, før den aktiveres.
5. Når kassen er flyttet, kan systemet genstarte cyklussen for næste kasse.

Du skal implementere logik, så hver sensor kun aktiverer én handling pr. cyklus (one shot), og sikre korrekt sekvensstyring mellem transportbånd, chain transfer og kapacitiv føler.

Lav en Match case-struktur eller IF/ELSE-logik, der styrer hele processen.

![alt text](image-7.png)

## Udvidelse: Stop ved 5 kasser

Systemet skal udvides, så hele transportbåndet stopper automatisk, når counteren for fotocellen har talt til 5. Når den femte kasse er registreret og flyttet, må transportbåndet ikke starte igen, før systemet evt. resettes.

Du skal derfor:
- Implementere en counter, der tæller hver gang fotocellen registrerer en kasse (one shot).
- Stoppe hele systemet, når counteren når 5.
- Overveje hvordan systemet kan resettes, hvis det ønskes.

## Reset-funktion

Systemet skal have en reset-knap, der nulstiller counteren og tillader transportbåndet at starte igen. Når reset-knappen aktiveres, skal counteren sættes til 0, og systemet skal kunne køre en ny cyklus med op til 5 kasser.


## Bemærkning om fotocelle

Fotocellen er placeret ved indgangen til bånd 2. Det betyder, at counteren skal tælle hver gang en kasse passerer fotocellen og kommer over på bånd 2. Når den femte kasse er talt, stopper hele systemet.

## Ekstra udfordring:
Lav en falling edge for fotocellen, så den kun tæller, når kassen passerer fra bånd 1 til bånd 2, og ikke tæller flere gange, hvis kassen bliver stående ved fotocellen.