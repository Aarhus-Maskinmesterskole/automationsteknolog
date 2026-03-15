# 02 - Skriv tidsstempel til txt fil
I denne opgave skal du skrive et tidsstempel til en tekstfil ved hjælp af Python. Vi vil bruge `datetime` modulet til at få det aktuelle tidspunkt og derefter skrive det til en fil.

## Trin 1: Importer datetime modulet
Først skal vi importere `datetime` modulet, som giver os mulighed for at arbejde med dato og tid i Python.
```python
from datetime import datetime
```

## Trin 2: Få det aktuelle tidspunkt
Nu kan vi få det aktuelle tidspunkt ved hjælp af `datetime.now()` funktionen. Vi kan også formatere tidsstemplet, så det er mere læsbart.

```python
# Få det aktuelle tidspunkt
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
```
## Trin 3: Skriv tidsstemplet til en fil
Nu kan vi skrive det formaterede tidsstempel til en tekstfil ved hjælp af `with open()` funktionen i append mode.

```python
# Skriv tidsstemplet til en fil
with open('tidsstempel.txt', 'a') as file:
    file.write(formatted_time + '\n')
```
## Trin 4: Kør koden
Når du kører ovenstående kode, vil den oprette en fil kaldet `tidsstempel.txt` (hvis den ikke allerede findes) og tilføje det aktuelle tidsstempel til filen. Hvis du kører koden flere gange, vil den tilføje et nyt tidsstempel hver gang.

## Trin 5: Læs filen
For at bekræfte, at tidsstemplerne er blevet skrevet til filen,kan du åbne filen i læse mode og udskrive indholdet:
```python
# Åbn filen i læse mode og udskriv indholdet
with open('tidsstempel.txt', 'r') as file:
    content = file.read()
    print(content)
```
Når du kører denne kode, vil den læse indholdet af `tidsstempel.txt` og udskrive det til konsollen. Du bør se alle tidsstemplerne, der er blevet tilføjet til filen.