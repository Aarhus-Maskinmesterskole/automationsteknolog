# Simpel transportbåndsstyring med one shot

I dette eksempel skal du lave en transportbåndsstyring, hvor transportbåndet starter, når en knap (S1) trykkes, og stopper, når fotocellen (S2) registrerer et objekt. For at undgå gentagne aktiveringer skal du bruge one shot-funktioner på både S1 og S2.

## Funktionsbeskrivelse

Transportbåndet styres af to sensorer:
- **S1 (knap):** Starter transportbåndet, når den trykkes (one shot).
- **S2 (fotocelle):** Stopper transportbåndet, når et objekt registreres (one shot).

Systemet fungerer således:
- Når S1 aktiveres (rising edge), sættes udgangen Q1, så transportbåndet starter.
- Når S2 aktiveres (rising edge), slukkes Q1, og transportbåndet stopper.
- Hvis S1 trykkes igen, starter transportbåndet på ny.

Logikken implementeres med en Match case-struktur, hvor udgangen Q1 styres af one shot-funktioner for S1 og S2.

## One shot-funktioner

Du skal selv udvikle en one shot-funktion for både S1 og S2. Overvej hvordan du kan detektere, når input går fra inaktiv til aktiv (stigende kant).
