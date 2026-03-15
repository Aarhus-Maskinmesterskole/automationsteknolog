# 01 - Skriv en fil
I denne opgave skal du skrive en fil ved hjælp af Python. Vi vil bruge den indbyggede `open()` funktion til at oprette og skrive til en fil.

## Trin 1: Opret en fil
Først skal vi oprette en fil, som vi kan skrive til. Vi kan gøre dette ved at bruge `with open()` funktionen med 'a' (append) mode. Der er flere forskellige modes, du kan bruge:
- 'r' - Læse mode (standard)
- 'w' - Skrive mode (overskriver eksisterende fil)
- 'a' - Append mode (tilføjer til eksisterende fil)

```python
import csv
# Opret en fil og åbn den i append mode
with open('min_fil.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Dette er en ny linje."])
```
## Trin 2: Kør koden
Når du kører ovenstående kode, vil den oprette en fil kaldet `min_fil.csv` (hvis den ikke allerede findes) og tilføje teksten "Dette er en ny linje." til filen. Hvis du kører koden flere gange, vil den tilføje en ny linje hver gang.

## Trin 3: Læs filen
For at bekræfte, at teksten er blevet skrevet til filen, kan du åbne filen i læse mode og udskrive indholdet:

```python
# Åbn filen i læse mode og udskriv indholdet
with open('min_fil.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```
Når du kører denne kode, vil den læse indholdet af `min_fil.csv` og udskrive det til konsollen. Du bør se alle linjerne, der er blevet tilføjet til filen.