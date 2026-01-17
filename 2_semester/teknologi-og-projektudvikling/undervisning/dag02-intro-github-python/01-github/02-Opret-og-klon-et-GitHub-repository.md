# 🧭 Guide til opgave: Opret og klon et GitHub-repository

Denne vejledning hjælper dig gennem en typisk GitHub-opgave, hvor du skal oprette et repository og hente det ned på din egen computer. Det er vigtigt for alle fremtidige projekter, at du mestrer denne proces.

---

## 🎯 Læringsmål

* Du kan oprette et repository i GitHub med korrekt navn og indhold
* Du kan bruge GitHub CLI til at klone et repo til din computer
* Du forstår, hvordan lokal og fjern version styring hænger sammen

## 🔧 Kompetencer

* Versionsstyring med Git og GitHub
* Grundlæggende terminalkommandoer
* Strukturering og organisering af kodeprojekter

---

## 🪜 Trin-for-trin vejledning

### 🔹 1. Log ind på GitHub og opret repo

1. Gå til: [https://github.com](https://github.com)
2. Klik på **+ > New repository**
3. Indtast:

   * **Repository name:** `gruppe-XX-testrepo`
   * **Description:** "Testprojekt for GitHub intro"
   * **Visibility:** vælg **Private** (kun jer og underviser kan se det)
   * ⚠️ Fjern flueben i *“Add README”* – vi laver den selv
4. Klik **Create repository**

### 🔹 2. Klon repo via GitHub CLI

Åbn din terminal og kør:

```bash
gh repo clone brugernavn/gruppe-XX-testrepo
cd gruppe-XX-testrepo
```

> Du bør nu være inde i din lokale version af projektmappen

### 🔹 3. Opret første fil og struktur

1. Opret en README:

```bash
echo "# GitHub Test Repo" > README.md
```

2. Opret eksempelmappe:

```bash
mkdir docs
```

3. Gem ændringerne:

```bash
git add .
git commit -m "Init: Tilføjet README og docs mappe"
git push
```

### 🔹 4. Tjek GitHub

Gå tilbage til din browser, åbn dit repository, og se at:

* README er oprettet
* Mappen `docs/` er synlig (kræver typisk at der er en fil i den)

> Tip: Opret evt. en tom `docs/test.md` for at sikre visning

---

## ✅ Tjekliste

* [ ] Du har oprettet repoet korrekt og uden auto-genereret README
* [ ] Du har klonet det lokalt med `gh repo clone`
* [ ] Du har oprettet og committed en README og en `docs/`-mappe
* [ ] Du har pushed og verificeret på GitHub

---

## 🧠 Hvorfor er dette vigtigt?

Det danner fundamentet for hele dit videre arbejde i faget. Du og din gruppe skal kunne arbejde i fælles GitHub-repositories, hvor både kode, dokumentation og data ligger korrekt struktureret.

Alt fremtidigt arbejde — fra Python til ESP32 og dokumentation — starter med dette skridt.
