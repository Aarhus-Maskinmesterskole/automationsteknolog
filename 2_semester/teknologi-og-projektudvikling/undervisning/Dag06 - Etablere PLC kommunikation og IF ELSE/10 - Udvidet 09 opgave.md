# 10 - Udvidet 09 opgave
I denne opgave skal du selv finde ud af hvordan man skriver ned i enden en csv eller txt fil hver gang en kasse er talt.

```python
from datetime import datetime
import csv

# Hvor skal denne indsættes i koden?
filename = f"{datetime.today().strftime('%Y-%m-%d')}.csv"
with open(filename, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

# Hvor skal denne indsættes i koden?
writer.writerow([datetime.now().isoformat(), ct])
f.flush()
```
**obs:** Det er vigtigt at bruge "a" (append) mode, så vi ikke overskriver tidligere data i filen. Hver gang en kasse tælles, vil en ny række blive tilføjet med tidsstemplet og den aktuelle count (ct). Ved "x" mode vil filen blive oprettet, men hvis den allerede eksisterer, vil det kaste en fejl. Derfor er "a" mere passende for dette formål, da det tillader os at tilføje data uden at slette tidligere optællinger.

f.flush() sikrer, at dataene skrives til filen med det samme, hvilket er vigtigt for at undgå datatab i tilfælde af en uventet nedlukning af programmet.