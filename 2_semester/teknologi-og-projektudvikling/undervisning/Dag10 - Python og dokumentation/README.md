# 🏗️ Python, Dokumentation og V-modellen

Velkommen! I dag skal vi binde alt det, vi har lært, sammen. Vi går fra at skrive små kodestumper til at udvikle en samlet **prototype** ved hjælp af en professionel udviklingsmodel: **V-modellen**.

## 🎯 Formål
- At forstå og anvende **V-modellen** i et praktisk projekt.
- At kunne dokumentere sin kode professionelt (Docstrings & kommentarer).
- At oprette teknisk dokumentation (Kravspecifikation, Blokdiagrammer, Flowcharts).
- At validere sin løsning gennem systematiske tests.

---

## 📐 V-modellen som rammeværk
V-modellen hjælper os med at sikre, at det vi bygger, rent faktisk er det, vi har lovet i vores kravspecifikation. Den forbinder designfasen (venstre side) direkte med testfasen (højre side).

1. **Kravspecifikation** ↔️ **Accepttest** (Virker systemet som kunden ville have det?)
2. **System Design (Blokdiagram)** ↔️ **Systemtest** (Spiller alle delene sammen?)
3. **Logisk Design (Flowchart/STM)** ↔️ **Enhedstest** (Virker de enkelte funktioner?)
4. **Implementering (Kodning)** (Bunden af V'et)

---

## 👥 Gruppearbejde
Dagens projekt udføres i grupper af **op til 3 personer**. Alle i gruppen skal have kendskab til hele processen fra kravspecifikation til test og visualisering.

## 🚀 Projektet: "Den Intelligente Produktionscelle"
I skal i dag designe og bygge en prototype på et system, der:
1. **Kommunikerer med en PLC** (Læser sensorer og styrer aktuatorer).
2. **Logger data** til en fil.
3. **Behandler data** med Pandas.
4. **Visualiserer resultatet** med Matplotlib.

---

## 📂 Opgaver
Følg filerne i rækkefølge for at komme igennem V-modellen:

0. [**Teori - V-modellen**](./00-teori-v-model.md)
1. [**01 - Kravspecifikation og Design**](./01-ide-og-kravspecifikation.md)
2. [**02 - Implementering og Kode-dokumentation**](./02-logik-og-kodning.md)
3. [**03 - Test og Validering**](./03-test-og-aflevering.md)

---

## 🛠️ Værktøjer
- **Python** (Snap7, Pandas, Matplotlib)
- **Diagrammer:** [Draw.io](https://app.diagrams.net/) eller tavlen + billede.
- **Dokumentation:** Markdown (.md) filer i jeres Github-repo.

---

> "En prototype uden dokumentation er bare kode, der tilfældigvis virker lige nu." 💡
