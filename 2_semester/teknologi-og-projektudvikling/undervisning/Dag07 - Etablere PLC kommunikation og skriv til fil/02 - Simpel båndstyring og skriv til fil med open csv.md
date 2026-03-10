# Simpel transportbåndsstyring med one shot og tæller

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

## Tæller og filskrivning
Derudover skal du implementere en tæller, der tæller antallet af gange, at S2 har registreret et objekt (dvs. hvor mange gange transportbåndet er blevet stoppet). Denne tæller skal skrives til en fil hver gang den opdateres, så du kan holde styr på antallet af stoppede objekter over tid.

Der skal laves tidsstempling for hver opdatering af tælleren, så du kan se, hvornår hvert stop skete. For at kunne lave tidsstempling og filskrivning, kan du bruge Python's `datetime`-modul til at generere tidsstempler.

```python
import datetime

filename = datetime.datetime.now().strftime("tæller_log_%Y-%m-%d_%H-%M-%S.csv")
with open(filename, 'a') as file:
    file.write("Date,Count\n")
```

Hver gang at tælleren opdateres, skal du tilføje en linje til filen med det aktuelle tidspunkt og tællerens værdi:

```python
import my_function # Indeholder one_shot-funktionerne
# ================ Initialisering ================
count = 0
S2_prev = False

# ================ Resten af koden ===============
if my_function.one_shot(S2,S2_prev):
    count += 1
    file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{count}\n")
```
