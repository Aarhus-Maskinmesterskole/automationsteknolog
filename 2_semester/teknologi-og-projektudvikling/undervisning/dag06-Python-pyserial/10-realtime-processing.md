# 📡 10 – Simuleret realtidsbehandling i Python

Denne guide lærer dig at simulere realtidsmålinger med Python – helt uden brug af ESP32 eller anden hardware. Det er særligt nyttigt, når du vil teste eller udvikle dine scripts, men ikke har fysisk adgang til sensorer, udviklingsboards eller seriel data. Ved hjælp af Python-modulerne `random`, `time`, `pandas` og `matplotlib` kan du generere en datastrøm, analysere den løbende og visualisere resultaterne grafisk – næsten som hvis du havde reelle målinger fra en fysisk sensor.

Du opbygger et datasæt trin for trin, præcis som hvis det kom ind fra en sensor. Hver måling består af en værdi og et tidspunkt. Undervejs gemmer du data, beregner glidende gennemsnit og visualiserer udviklingen over tid. Denne type simulering forbereder dig på at håndtere live-målinger i praksis – uanset om de kommer fra ESP32, en PLC, en datalogger eller noget helt tredje. Du får samtidig bygget robuste scripts, som du senere kan koble op på rigtige datakilder.

---

## 🎯 Læringsmål

* Simulere en strøm af målinger over tid ved hjælp af `random`
* Tilføje data løbende til en Pandas DataFrame og bearbejde den dynamisk
* Anvende `.rolling()` til at beregne glidende gennemsnit og forstå dets funktion
* Visualisere data og trends med `matplotlib`
* Eksportere målinger til CSV-format til videre dokumentation eller analyse
* Teste databehandlingskode i et kontrolleret miljø uden afhængighed af hardware

---

## ⏳ Simuler en datastrøm i Python

```python
import pandas as pd
import time
import random

målinger = []

for i in range(50):
    ny_værdi = random.randint(0, 1023)  # simuleret analog input
    timestamp = pd.Timestamp.now()  # nuværende tidspunkt
    målinger.append({"tid": timestamp, "værdi": ny_værdi})
    print(f"{timestamp} → {ny_værdi}")
    time.sleep(0.3)  # simuleret målefrekvens

# Konverter til DataFrame
data = pd.DataFrame(målinger)
```

> Du simulerer her en datastrøm som kunne komme fra en ESP32. Hvert datapunkt består af en måleværdi og et timestamp, hvilket giver dig et realistisk udgangspunkt for analyse, debugging og visualisering.

---

## 🧮 Beregn glidende gennemsnit

```python
data["glidende"] = data["værdi"].rolling(window=10).mean()
print(data.tail())
```

> Et glidende gennemsnit er nyttigt til at glatte svingende data og fremhæve overordnede trends. Vinduet angiver hvor mange målinger der inkluderes i gennemsnittet.

---

## 📈 Visualiser datastrøm og gennemsnit

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(data["tid"], data["værdi"], label="Rå måling", linestyle='-', color='blue')
plt.plot(data["tid"], data["glidende"], label="Glidende gns.", linestyle='--', color='orange')
plt.xlabel("Tid")
plt.ylabel("Sensorværdi")
plt.title("Simulerede målinger i realtid")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

> Brug af grafer giver dig overblik over datastrukturer og fejl. Prøv at eksperimentere med farver, stregtyper og labels for at gøre visualiseringen mere informativ.

---

## 💾 Gem datasæt som CSV

```python
data.to_csv("simuleret.csv", index=False)
```

> CSV-filer er standardformatet til at gemme måledata og kan åbnes både i Excel og Python. Filen gemmes som udgangspunkt i samme mappe som dit script.

---

## 🧪 Øvelser og eksperimenter

1. Simulér 50 målinger med `time.sleep(0.3)` og tilfældige værdier mellem 0 og 1023.
2. Skift vindue for gennemsnit til `window=5`, `10` og `20` og sammenlign graferne.
3. Tilføj en kolonne `alarm`, der er `True` hvis `værdi > 1000`:

   ```python
   data["alarm"] = data["værdi"] > 1000
   ```
4. Gem data til `simuleret.csv` og åbn filen i både Pandas og Excel.
5. Prøv at erstatte line-plot med scatter-plot:

   ```python
   plt.scatter(data["tid"], data["værdi"], label="Målinger", alpha=0.6)
   plt.grid()
   plt.legend()
   plt.show()
   ```
6. Udvid med min-/maks-analyse:

   ```python
   print("Min:", data["værdi"].min())
   print("Max:", data["værdi"].max())
   ```

---

## ✅ Tjekliste

* [ ] Jeg har simuleret en målestrøm og opbygget en DataFrame
* [ ] Jeg har anvendt `.rolling()` til at beregne glidende gennemsnit
* [ ] Jeg har visualiseret målinger med matplotlib
* [ ] Jeg har gemt mine målinger som CSV og åbnet dem igen
* [ ] Jeg har eksperimenteret med betingelser, scatter-plots og statistik

---

> Dette modul giver dig en sikker ramme for at afprøve og udvikle databehandlingsflows uden fysisk hardware. Når du mestrer dette, bliver det langt lettere at koble til ESP32 eller andre datakilder i kommende moduler.
