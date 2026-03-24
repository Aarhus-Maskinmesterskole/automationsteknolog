# 🖼️ 04 – Eksport og annotering af grafer

Når du har lavet en vellykket visualisering, er næste skridt at gemme og forbedre den, så den kan bruges i dokumentation, rapporter eller præsentationer. En flot graf bliver endnu mere effektiv, når du tilføjer forklarende elementer som tekst, pile, markeringer af maksimum eller minimum samt visuelle grænser. Disse elementer hjælper læseren med at forstå konteksten og betydningen af dine målinger – og de fremhæver tydeligt, hvilke data der er særligt vigtige.

I denne guide lærer du, hvordan du gemmer dine plots i høj opløsning og gør dem mere informative ved hjælp af Matplotlibs funktioner som `annotate()`, `axhline()` og `axvline()`.

---

## 🎯 Læringsmål – Hvad du lærer i dette modul

* At anvende `plt.savefig()` til at eksportere grafer som billedfiler i høj opløsning
* At bruge `annotate()` og `axhline()` til at tilføje forklarende elementer til dine figurer
* At klargøre grafer til dokumentation og præsentation med tydelige markeringer og etiketter
* At gemme figurer i flere formater og forstå formaternes fordele i forskellige sammenhænge

---

## 💾 Sådan gemmer du en graf som billedfil

Når du har lavet en graf, kan du gemme den ved hjælp af `savefig()`:

```python
plt.savefig("graf1.png", dpi=300)
```

* Brug `dpi=300` for høj opløsning – det sikrer, at grafen fremstår skarp i både print og digitale dokumenter
* Du kan også gemme som `.pdf` (vektorbaseret og skalerbart), `.svg` (velegnet til web), eller `.jpg` (komprimeret billede)
* Hvis du vil angive en bestemt sti, fx til dokumentationsmappen, kan du bruge: `"docs/figurer/graf1.png"`
* **Vigtigt:** Kald altid `savefig()` **før** `plt.show()`. Ellers gemmes en tom eller ufærdig figur

---

## ✏️ Sådan tilføjer du tekst og visuelle markeringer

Ved at bruge `annotate()` og `axhline()` kan du fremhæve specifikke punkter i datasættet – f.eks. et maksimum eller en kritisk grænse.

```python
import matplotlib.pyplot as plt
import pandas as pd

# Eksempeldata
data = pd.DataFrame({"tid": range(10), "værdi": [2, 3, 5, 6, 8, 9, 7, 6, 5, 4]})
plt.plot(data["tid"], data["værdi"], label="Måling", marker="o")

# Find maksimum og dets indeks
tidspunkt = data["tid"][data["værdi"].idxmax()]
værdi = data["værdi"].max()

# Tilføj en pil og tekst ved maksimum
plt.annotate("Maksimum",
             xy=(tidspunkt, værdi),
             xytext=(4, 5),
             arrowprops=dict(arrowstyle="->", color="black"),
             fontsize=9)

# Tilføj en vandret grænselinje
plt.axhline(y=7, color="red", linestyle="--", label="Tærskelværdi")

plt.xlabel("Tid (sekunder)")
plt.ylabel("Sensorværdi")
plt.title("Visualisering med annotation og tærskel")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("annoteret_plot.png", dpi=300)
plt.show()
```

> Annotationer er nyttige i dokumentation, fordi de formidler budskaber visuelt uden behov for lange forklaringer i teksten.

---

## 🧪 Øvelser – Brug annotation og eksport aktivt

1. Lav en graf over dine egne målinger og gem den som `.png` med `dpi=300`
2. Brug `annotate()` til at markere et vigtigt punkt: f.eks. et lokalt maksimum eller minimum
3. Tilføj en grænseværdi med `axhline()` – gerne farvet og med tydelig signatur
4. Gem grafen både som `.png` og `.pdf` og åbn dem i forskellige programmer (fx browser, PowerPoint, Word)
5. Indsæt grafen i din dokumentation eller præsentation
6. (Ekstra) Brug `plt.axvline()` til at markere et bestemt tidspunkt – f.eks. når et eksperiment starter

---

## ✅ Tjekliste – Har du opnået dette?

* [ ] Jeg har gemt min graf med `plt.savefig()` i korrekt opløsning og format
* [ ] Jeg har tilføjet en forklarende tekst med `annotate()`
* [ ] Jeg har markeret grænser eller tærskelværdier med `axhline()` og evt. `axvline()`
* [ ] Jeg har gemt grafen i mindst to formater og vurderet forskellen
* [ ] Jeg har anvendt grafen i en rapport, dokumentation eller præsentation

---

> En godt formateret graf med tydelige markeringer kan løfte din dokumentation markant. Det handler ikke kun om data – men om at fremhæve det væsentlige og gøre det forståeligt for andre.
