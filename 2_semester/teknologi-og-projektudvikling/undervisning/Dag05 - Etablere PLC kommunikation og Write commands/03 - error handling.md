# Dag 5 - Etablere PLC kommunikation og error handling 🐍🤖
Når man arbejder med PLC-kommunikation, er det vigtigt at håndtere fejl korrekt. Dette kan være alt fra netværksfejl, PLC-fejl eller fejl i dataformatet. Her er nogle tips til at håndtere fejl i din PLC-kommunikation:
1. **Brug try-except blokke**: Dette er en grundlæggende måde at fange og håndtere fejl på i Python. Du kan fange specifikke undtagelser, såsom `snap7.exceptions.Snap7Exception`, for at håndtere fejl relateret til PLC-kommunikation.

```python
try:
    client.connect(PLC_IP, RACK, SLOT)
except snap7.exceptions.Snap7Exception as e:
    print(f"Fejl ved forbindelse til PLC: {e}")
```

#### Forklaring af koden
- `try`: Dette er blokken, hvor du placerer den kode, der kan forårsage en fejl. I dette tilfælde er det forbindelsen til PLC'en.

- `except snap7.exceptions.Snap7Exception as e`: Dette fanger specifikke fejl relateret til Snap7 biblioteket. Hvis der opstår en fejl under forbindelsen, vil denne blok blive udført, og du kan håndtere fejlen, f.eks. ved at vise en besked til brugeren.

2. **finally blok**: Brug en `finally` blok til at sikre, at du altid lukker forbindelsen til PLC'en, selv hvis der opstår en fejl. Dette er vigtigt for at undgå at efterlade åbne forbindelser, som kan forårsage problemer senere.

```python
try:
    client.connect(PLC_IP, RACK, SLOT)
    # Din kode til at læse eller skrive til PLC'en
except snap7.exceptions.Snap7Exception as e:
    print(f"Fejl ved forbindelse til PLC: {e}")
    # gør et eller andet for at håndtere fejlen, f.eks. vise en besked til brugeren eller lav retry mekanisme
finally:
    if client.get_connected():
        client.disconnect()
        print("Forbindelse til PLC lukket.")
    client.destroy()
    print("Ressourcer frigivet.")
```

#### Forklaring af koden
- `finally`: Denne blok vil altid blive udført, uanset om der opstår en fejl eller ej. Det er et godt sted at placere kode, der skal køre uanset udfaldet, såsom at lukke forbindelsen til PLC'en.
- `if client.get_connected()`: Dette tjekker, om klienten stadig er forbundet til PLC'en, før den forsøger at lukke forbindelsen. Dette hjælper med at undgå yderligere fejl, hvis forbindelsen allerede er brudt.

- `client.destroy()`: Dette frigiver ressourcer, der er tildelt til klienten, og sikrer, at der ikke er nogen hukommelseslækager. Hukommelseslækager kan opstå, hvis du ikke frigiver ressourcer korrekt, især når du arbejder med netværksforbindelser, hvilket kan føre til, at din applikation bruger mere og mere hukommelse over tid, indtil den til sidst går ned. Ved at bruge `client.destroy()`, sikrer du, at alle ressourcer frigives korrekt, selv hvis der opstår en fejl under kommunikationen med PLC'en.