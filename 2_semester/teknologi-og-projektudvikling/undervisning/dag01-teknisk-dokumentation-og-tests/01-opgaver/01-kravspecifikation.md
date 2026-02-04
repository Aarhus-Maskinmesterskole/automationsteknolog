# Opgave: Kravspecifikation for simpelt system

## Beskrivelse
Lav en kort kravspecifikation til et simpelt system (fx LED + knap eller temperaturmåling + blæser).
Kravene skal være **målbare** og opdeles i:
- Funktionelle krav (hvad systemet skal gøre)
- Ikke-funktionelle krav (hvordan systemet skal opføre sig: responstid, stabilitet, miljø, etc.)
- Prioritering: must-have / nice-to-have

## Acceptance criteria
- Dokumentet indeholder min. **4 funktionelle** og **3 ikke-funktionelle** krav
- Mindst **2 krav** har tydelige mål (fx “≤ 0,5 s”, “inden for 1 sekund”, “kører 24 timer uden fejl”)
- Kravene er formuleret uden tvetydighed (ingen “hurtigt”, “nemt”, osv.)
- Der er angivet hvilke krav der er must-have vs nice-to-have

## Skabelon

### Funktionelle krav
| # | Krav | Mål | Prioritet |
|---|------|-----|-----------|
| 1 |      |     |           |
| 2 |      |     |           |
| 3 |      |     |           |
| 4 |      |     |           |

### Ikke-funktionelle krav
| # | Krav | Mål | Prioritet |
|---|------|-----|-----------|
| 1 |      |     |           |
| 2 |      |     |           |
| 3 |      |     |           |

## Eksempel (temperatur + blæser)

### Funktionelle krav
| # | Krav | Mål | Prioritet |
|---|------|-----|-----------|
| 1 | Systemet skal måle temperaturen hvert sekund | 1 Hz | Must-have |
| 2 | Systemet skal tænde blæseren, hvis temperaturen overstiger 30°C | ≤ 1 sekund forsinkelse | Must-have |
| 3 | Systemet skal slukke blæseren, hvis temperaturen falder under 28°C | ≤ 1 sekund forsinkelse | Must-have |
| 4 | Systemet skal kunne vise aktuel temperatur på display | Opdatering ≤ 2 sekunder | Nice-to-have |

### Ikke-funktionelle krav
| # | Krav | Mål | Prioritet |
|---|------|-----|-----------|
| 1 | Systemet skal kunne køre uden fejl i 24 timer | 24 timer | Must-have |
| 2 | Systemet skal fungere ved temperaturer fra 0°C til 50°C | 0-50°C | Must-have |
| 3 | Systemet skal have en samlet responstid på under 2 sekunder | ≤ 2 sekunder | Nice-to-have |

## Referencer
- Kravspec: definition, funktionelle vs ikke-funktionelle, typiske fejl og testkobling
- Kravspec eksempel (temp + blæser)
