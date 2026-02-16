# Opgave 5: Mini testplan + testprotokol

## Beskrivelse
Lav en testsektion der knytter tests til krav.
Lav en lille tabel (Test ID, beskrivelse, acceptkriterier, resultat, signatur/dato).
Vælg mindst 3 testtyper (gerne FAT + SAT + én mere).

## Acceptance criteria
- Min. **6 testcases** i alt (fx 2 FAT, 2 SAT, 2 Performance/UAT/SIT)
- Hver testcase har **acceptkriterium** der matcher et krav (fx responstid ≤ 0,5 s / ≤ 1 s)
- Testcases har unikke Test-ID’er (FAT-001 osv.)
- Testdokumentet kan indgå direkte i teknisk dokumentation

## Skabelon eksempel

| Test ID   | Testtype   | Beskrivelse                        | Acceptkriterium         | Resultat | Signatur/dato |
|-----------|------------|------------------------------------|------------------------|----------|---------------|
| FAT-001   | FAT        | Test af temperaturmåling           | Måler korrekt temp.    |          |               |
| FAT-002   | FAT        | Test af blæser aktivering          | Tænder ved >30°C       |          |               |
| SAT-001   | SAT        | Test af blæser slukning            | Slukker ved <28°C      |          |               |
| SAT-002   | SAT        | Test af displayopdatering          | Opdatering ≤ 2 sek.    |          |               |
| PERF-001  | Performance| Test af systemets responstid       | Responstid ≤ 1 sek.    |          |               |
| UAT-001   | UAT        | Test af systemets drift 24 timer   | Ingen fejl i 24 timer  |          |               |

*Du kan tilføje flere testcases og testtyper efter behov. Husk at koble acceptkriterier til krav fra kravspecifikationen.*

## Referencer
- Testtyper og eksempler: FAT/SAT/SIT/UAT/Performance/Usability
- Kravspec → testmetoder (kobling mellem krav og test)
- Kravspec eksempel med test-tabeller (temp + blæser)
- Skabelon til teknisk dokumentation (testplan/protokol)
