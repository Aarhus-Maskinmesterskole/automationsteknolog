Her er en version, hvor “forklaringen” er koblet direkte ind i **opgaven** (titel, læringsmål og trin-for-trin), så det bliver én samlet opgave med både *hvad* og *hvorfor*.

---

# 📁 Guide til opgave: Tilføj struktur og filer til GitHub-repo

Denne guide hjælper dig med at oprette en professionel mappestruktur til dit projekt, lave en `.gitignore` og en README – og committe/pushe det hele korrekt til GitHub.

---

## 🎯 Læringsmål

Efter opgaven kan du:

* Oprette en **standard projektstruktur** der kan bruges i undervisning og i virksomhedscases
* Forklare formålet med `docs/`, `python/`, `data/` og `deliverables/`
* Forstå formålet med `.gitignore` og `README.md`
* Committe og pushe ændringer til GitHub

## 🛠️ Kompetencer

* Arbejde i terminalen med filstruktur og versionering
* Versionsstyring af dokumentation og kodefiler
* Strukturere dokumentation: kravspec, teknisk dok, test og mødenoter
* Bevidsthed om hvilke filer man **ikke** skal dele med andre

---

## 🪜 Trin-for-trin vejledning

### 🔹 1. Navigér til dit repository

```bash
cd gruppe-XX-testrepo
```

> Du skal stå i mappen hvor `.git` findes (ellers virker `git add` ikke).

---

### 🔹 2. Opret den anbefalede mappestruktur

Kør:

```bash
mkdir -p docs/01_kravspecifikation
mkdir -p docs/02_teknisk-dokumentation/diagrammer
mkdir -p docs/03_test
mkdir -p docs/04_moedereferater
mkdir -p python/src python/notebooks
mkdir -p data/raw data/processed data/sample
mkdir -p deliverables
```

---

### 🔹 3. Opret standardfiler (så mapperne vises på GitHub)

```bash
echo "# Teknologi og Projektudvikling – Gruppe XX" > README.md

echo "## Kravspecifikation\n\nSkriv jeres krav her..." > docs/01_kravspecifikation/kravspec.md
echo "## Acceptkriterier\n\nHvordan beviser vi at kravene er opfyldt?" > docs/01_kravspecifikation/acceptkriterier.md

echo "## Teknisk dokumentation\n\nBeskriv systemet her..." > docs/02_teknisk-dokumentation/teknisk-dok.md
echo "## Installation\n\nSådan opsætter og starter man projektet..." > docs/02_teknisk-dokumentation/installation.md

echo "## Testplan\n\nHvilke tests køres (FAT/SAT/SIT/UAT)?" > docs/03_test/testplan.md
echo "## Testresultater\n\nResultater og observationer..." > docs/03_test/testresultater.md

echo "## Mødereferat (Kickoff)\n\nBeslutninger og action points..." > docs/04_moedereferater/2026-02-07_kickoff.md

echo "print('Hello from Node-RED/Python project')" > python/src/main.py
echo "# Skriv Python-pakker her, fx:\n# requests\n# pymodbus\n" > python/requirements.txt

echo "# Data\n\nraw: rå data (må ikke ændres)\nprocessed: bearbejdet data\nsample: lille demo-data til repo\n" > data/README.md
```

---

### 🔹 4. Opret en `.gitignore`

```bash
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.vscode/
.env
data/raw/*
data/processed/*
EOF
```

**Forklaring:**

* `__pycache__/` og `*.pyc` er midlertidige Python-filer
* `.vscode/` er lokale editor-indstillinger
* `.env` kan indeholde hemmelige nøgler
* `data/raw` og `data/processed` kan blive store eller indeholde “rigtige” data
  → derfor deler vi kun `data/sample` i repo’et

---

### 🔹 5. Commit og push ændringer

```bash
git add .
git commit -m "Opgave: Tilføjet professionel struktur, README og .gitignore"
git push
```

---

## 📁 Overblik: Anbefalet struktur (skole + virksomhed)

```text
gruppe-XX-testrepo/
├── README.md
├── .gitignore
├── docs/
│   ├── 01_kravspecifikation/
│   │   ├── kravspec.md
│   │   └── acceptkriterier.md
│   ├── 02_teknisk-dokumentation/
│   │   ├── teknisk-dok.md
│   │   ├── diagrammer/
│   │   │   ├── blokdiagram.png
│   │   │   ├── flowchart.png
│   │   │   └── state-machine.png
│   │   └── installation.md
│   ├── 03_test/
│   │   ├── testplan.md
│   │   └── testresultater.md
│   └── 04_moedereferater/
│       └── 2026-02-07_kickoff.md
├── python/
│   ├── src/
│   │   └── main.py
│   ├── notebooks/
│   └── requirements.txt
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
└── deliverables/
    ├── rapport.pdf
    └── præsentation.pdf
```

---

## 🧠 Hvad skal der være under mapperne?

* **docs/** = alt dokumentation (kravspec, teknisk dokumentation, test, møder)
* **python/src/** = projektets “rigtige kode”
* **python/requirements.txt** = de Python-pakker man skal installere (`pip install -r ...`)
* **data/raw/** = rå data (ændres ikke)
* **data/processed/** = bearbejdet data (kan genskabes)
* **data/sample/** = lille demo-data der må deles i GitHub (så andre kan teste projektet)
* **deliverables/** = rapport/præsentation (færdige afleveringer)

---

## 🧪 Tjekliste

* [ ] Mapperne er oprettet og vises på GitHub
* [ ] README beskriver projektet
* [ ] `.gitignore` ignorerer cache, editorfiler og store data
* [ ] Du har committed og pushed ændringerne
