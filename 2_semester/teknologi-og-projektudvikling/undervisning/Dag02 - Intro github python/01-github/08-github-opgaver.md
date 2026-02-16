# ✅ GitHub – Øvelsesopgaver (Dag 01)

Herunder finder du 6 konkrete opgaver, som træner dine færdigheder i Git og GitHub via terminal og GitHub CLI.

---

## 🧪 Opgave 1 – Opret og klon repository

**Formål:** Lære at oprette og hente et GitHub-repository.

1. Gå til [https://github.com](https://github.com)
2. Opret et nyt **privat** repository med navnet:

   ```
   gruppe-XX-træning
   ```
3. Klon repository til din computer:

   ```bash
   gh repo clone brugernavn/gruppe-XX-træning
   cd gruppe-XX-træning
   ```

---

## 📁 Opgave 2 – Tilføj struktur og filer

**Formål:** Få styr på mappestruktur og filhåndtering.

1. Opret følgende mapper:

   ```bash
   mkdir docs python data
   ```
2. Opret en `README.md` og `.gitignore`:

   ```bash
   echo "# GitHub træning" > README.md
   echo "__pycache__/\n*.csv" > .gitignore
   ```
3. Tilføj og commit:

   ```bash
   git add .
   git commit -m "Opgave 2: Mappestruktur og ignore-filer"
   git push
   ```

---

## ✍️ Opgave 3 – Lav en ændring og commit

**Formål:** Træn add → commit → push-flowet.

1. Tilføj følgende til din `README.md`:

   ```
   Dette repo bruges til Git-træning i Teknologi og Projektudvikling.
   ```
2. Gem, commit og push ændringen.
3. Tjek at ændringen er synlig på GitHub.

---

## 🌿 Opgave 4 – Opret og arbejd i en ny branch

**Formål:** Lær at bruge branches til nye funktioner.

1. Opret en ny branch:

   ```bash
   git checkout -b feature-beskrivelse
   ```
2. Tilføj filen `docs/beskrivelse.md` med kort tekst.
3. Commit og push branchen:

   ```bash
   git add .
   git commit -m "Tilføjet beskrivelse.md"
   git push -u origin feature-beskrivelse
   ```

---

## 🔀 Opgave 5 – Merge din branch til main

**Formål:** Forstå hvordan man integrerer arbejde i hovedgrenen.

1. Skift til `main` og hent nyeste:

   ```bash
   git checkout main
   git pull
   ```
2. Merge:

   ```bash
   git merge feature-beskrivelse
   ```
3. Push opdateret main:

   ```bash
   git push
   ```

---

## 🧹 Opgave 6 – Ryd op og slet branch

**Formål:** Lær at slette en feature-branch lokalt og på GitHub.

1. Slet lokalt:

   ```bash
   git branch -d feature-beskrivelse
   ```
2. Slet på GitHub:

   ```bash
   git push origin --delete feature-beskrivelse
   ```

---

> Disse opgaver skal løses **individuelt** eller i par. Brug terminalen og dine noter. Spørg undervis
