# 💻 01 – Installation af Pandas og Matplotlib (VS Code)

Denne guide hjælper dig med at klargøre din computer til databehandling i Python via **Visual Studio Code**. Du installerer de vigtigste værktøjer og lærer, hvordan du tester, at alt virker korrekt.

---

## 🎯 Mål for modulet

* Installere `pandas` og `matplotlib`
* Køre testscript i VS Code for at bekræfte installation
* Forstå hvordan du strukturerer Python-filer i projekter

---

## 📦 Hvad er det vi installerer?

| Pakke        | Funktion                                    |
| ------------ | ------------------------------------------- |
| `pandas`     | Arbejd med datasæt og tabeller (DataFrames) |
| `matplotlib` | Lav grafer og visualiseringer               |

---

## 🧰 Installation i VS Code

1. Åbn **VS Code** og terminalen (Ctrl + \` eller Terminal → New Terminal)

2. Skriv følgende kommando:

```bash
pip install pandas matplotlib
```

> Brug evt. `python -m pip install pandas matplotlib` hvis `pip` ikke virker.

---

## ✅ Test din installation

1. Opret en ny Python-fil med navnet `test_installation.py`
2. Indsæt følgende kode:

```python
import pandas as pd
import matplotlib.pyplot as plt

print("pandas version:", pd.__version__)
data = pd.DataFrame({"x": [1, 2, 3], "y": [1, 4, 9]})
print(data)
data.plot(x="x", y="y", kind="line")
plt.show()
```

3. Kør scriptet (højreklik → Run Python File in Terminal eller brug grøn pil i øverste hjørne).

Hvis du ser:

* DataFrame udskrevet i terminalen
* En graf åbner i nyt vindue

... så er installationen OK.

---

## 🧠 Tip

* Brug `requirements.txt` til at samle pakker du bruger i projekter
* Brug virtuelle miljøer (`python -m venv env`) hvis du arbejder med flere projekter
* Gem alle Python-filer i mappen `python/` i dit GitHub-repo

---

Denne opsætning bruges i resten af forløbet til databehandling, graftegning og analyse.
