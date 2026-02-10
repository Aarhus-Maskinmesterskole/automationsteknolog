# 🛠️ Komplet guide: Git i terminalen

Denne guide giver dig en omfattende introduktion til Git via terminalen — fra installation, til effektivt samarbejde, versionsstyring og deling af kode på GitHub.

## 📦 Installation af Git

### Windows

1. **Download Git til Windows**:
   - Gå til [git-scm.com/download/win](https://git-scm.com/download/win)
   - Download den seneste version af Git for Windows
   - Kør installationsfilen (.exe)

2. **Installationsvejledning**:
   - Vælg **default editor** (anbefalet: Visual Studio Code hvis installeret)
   - Vælg **Git from the command line and also from 3rd-party software**
   - Vælg **Use bundled OpenSSH**
   - Vælg **Use the OpenSSL library**
   - Vælg **Checkout Windows-style, commit Unix-style line endings**
   - Vælg **Use MinTTY** (default terminal)
   - Accepter resten af standardindstillingerne

3. **Verificer installationen**:
   ```bash
   git --version
   ```

### macOS

```bash
# Via Homebrew (anbefalet)
brew install git

# Eller via Xcode Command Line Tools
xcode-select --install
```

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install git
```

## ⚙️ Grundlæggende Git-konfiguration

Efter installation skal du konfigurere Git med dit navn og email:

```bash
git config --global user.name "Dit Navn"
git config --global user.email "din.email@example.com"
```

Se din konfiguration:

```bash
git config --list
```

## 🧰 Forudsætninger

* Git er installeret på din maskine
* Du har en GitHub-konto og adgang til internettet

---

## 📁 1. Opret nyt projekt og initialisér repository

Først opretter du en mappe til dit projekt og initialiserer Git:

```bash
mkdir mit-projekt
cd mit-projekt
git init
```

Dette opretter en skjult `.git`-mappe, som Git bruger til at holde styr på ændringer.

Tilføj nogle basale projektfiler:

```bash
echo "__pycache__/\n*.csv\n.vscode/" > .gitignore
echo "# Mit Projekt" > README.md
touch main.py
```

> `.gitignore` angiver hvilke filer og mapper Git skal ignorere (fx cache, midlertidige filer og IDE-konfiguration).

---

## 📝 2. Tilføj filer og foretag første commit

Git holder styr på ændringer i såkaldte commits:

```bash
git add .          # Tilføjer alle filer til staging-området
# eller: git add filnavn.py

git commit -m "Første commit med projektfiler"
```

> Sørg for at commit-beskeder er meningsfulde og fortæller hvad du har ændret.

Du kan se filernes status med:

```bash
git status
```

---

## 🌐 3. Opret GitHub-repo og forbind det til lokalt repo

### Opret repository på GitHub

1. Gå til [github.com](https://github.com) og log ind
2. Klik på **New repository** (eller + ikonet øverst til højre)
3. Giv repoet et navn (fx `mit-projekt`)
4. Vælg **Public** eller **Private**
5. **Tilføj IKKE** README, .gitignore eller license (vi har allerede disse lokalt)
6. Klik **Create repository**

### Forbind lokalt repo til GitHub

Kopiér kommandoerne fra GitHub og kør dem i din terminal:

```bash
git remote add origin https://github.com/brugernavn/mit-projekt.git
git branch -M main
git push -u origin main
```

> Erstat `brugernavn` med dit GitHub-brugernavn

Verificer at det er forbundet:

```bash
git remote -v
```

---

## 🔄 4. Push og pull – del og hent ændringer

Når du foretager ændringer:

```bash
git add .
git commit -m "Rettet fejl i databehandling"
git push
```

Når du vil hente andres ændringer:

```bash
git pull
```

> Brug `git pull --rebase` hvis du vil undgå unødvendige merge-commits.

---

## 👯 5. Klon eksisterende projekter fra GitHub

Du kan hente andres kode til din maskine:

```bash
git clone https://github.com/brugernavn/projektnavn.git
```

Dette opretter en ny mappe med projektets navn og downloader alle filer.

Skift til projektmappen:

```bash
cd projektnavn
```

---

## 🌳 6. Arbejd med branches (grene)

Branches bruges til at arbejde med nye funktioner uden at forstyrre main:

```bash
git checkout -b ny-feature
```

Lav dine ændringer, og kør derefter:

```bash
git add .
git commit -m "Tilføjet ny feature"
git push -u origin ny-feature
```

Se dine branches:

```bash
git branch -a
```

---

## 🔁 7. Merge en branch til main

Når din feature er klar, gør du sådan:

```bash
git checkout main
git pull

git merge ny-feature
```

Løs eventuelle konflikter, og push den opdaterede main:

```bash
git push
```

> Merge-konflikter kan ses med `git status` og redigeres i en teksteditor.

---

## 👥 8. Samarbejde i teams – best practices

* Hver udvikler arbejder i sin egen branch
* Lav små commits med klare beskeder
* Brug `pull` ofte for at holde sig opdateret
* Opret Pull Requests (PRs) på GitHub og gennemgå hinandens kode
* Kommunikér klart i commit- og PR-beskeder

---

## 🧪 9. Se status, ændringer og historik

```bash
git status         # Hvad er ændret?
git log --oneline  # Kort commit-historik
git diff           # Hvad er ændret siden sidste commit?
```

Du kan også se hvem der har lavet hvilke ændringer:

```bash
git blame fil.py
```

---

## 🧹 10. Slet branches efter merge

Når en branch er merged og ikke længere bruges:

```bash
git branch -d ny-feature              # Lokalt

git push origin --delete ny-feature  # Fjerner fra GitHub
```

> Hold repoet ryddeligt – især i gruppeprojekter

---

## 📌 11. Tips og fejlfinding

* Brug `.gitignore` aktivt
* Commit små ændringer ofte
* Brug `git restore` eller `git checkout` til at gendanne filer
* Hvis du sidder fast: prøv `git status` og `git log` for overblik

> Har du lavet rod? `git reflog` kan vise tidligere HEAD-placeringer.

---

## ✅ Klar til professionelt Git-arbejde

Du er nu klar til at:

* Installere og konfigurere Git på din maskine
* Arbejde med Git i terminalen
* Oprette, versionere og dokumentere kodeprojekter
* Samarbejde effektivt i grupper
* Forstå og navigere i branches, commits og konflikter

> Brug Git som et dagligt værktøj — det giver bedre samarbejde, sikkerhed og overblik i alle udviklingsprojekter.
