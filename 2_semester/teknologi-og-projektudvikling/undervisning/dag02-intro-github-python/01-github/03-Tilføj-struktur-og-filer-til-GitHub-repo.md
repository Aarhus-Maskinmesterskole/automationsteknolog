# 📁 Guide til opgave: Tilføj struktur og filer til GitHub-repo

Denne guide hjælper dig med at oprette den basale mappestruktur til dit projekt, oprette en `.gitignore` og en README – og committe det hele korrekt til GitHub.

---

## 🎯 Læringsmål

* Du kan oprette mapper og filer til et Git-styret projekt
* Du forstår formålet med `.gitignore` og `README.md`
* Du kan committe og pushe ændringer til GitHub

## 🛠️ Kompetencer

* Arbejde i terminalen med filstruktur og versionering
* Versionsstyring af dokumentation og kodefiler
* Bevidsthed om hvilke filer man **ikke** skal dele med andre

---

## 🪜 Trin-for-trin vejledning

### 🔹 1. Navigér til dit repository

Hvis du lige har lavet et repo:

```bash
cd gruppe-XX-testrepo
```

### 🔹 2. Opret mapper

```bash
mkdir docs
mkdir python
mkdir data
```

> Dette er den grundstruktur vi anvender i Teknologi og Projektudvikling.

### 🔹 3. Opret og redigér README

```bash
echo "# Teknologi og Projektudvikling – Gruppe XX" > README.md
```

> Dette er projektets forside og skal løbende opdateres.

### 🔹 4. Opret en `.gitignore`

```bash
echo "__pycache__/
*.csv
.vscode/" > .gitignore
```

> `.gitignore` sikrer at midlertidige og lokale filer ikke bliver tracket af Git.

### 🔹 5. Commit og push ændringer

```bash
git add .
git commit -m "Opgave 2: Struktur og ignore-fil"
git push
```

---

## 🧪 Tjekliste

* [ ] `docs/`, `python/`, `data/` er oprettet
* [ ] `README.md` findes og indeholder en overskrift
* [ ] `.gitignore` ignorerer relevante filer
* [ ] Ændringerne er pushed og ses på GitHub

---

## 🧠 Hvorfor er dette vigtigt?

Et professionelt projekt starter med en god struktur. Det gør det lettere at samarbejde, forstå koden og aflevere korrekt. `README.md` og `.gitignore` er centrale dele af ethvert teknologiprojekt.

> Spørg underviser hvis du er i tvivl om navngivning eller struktur.
