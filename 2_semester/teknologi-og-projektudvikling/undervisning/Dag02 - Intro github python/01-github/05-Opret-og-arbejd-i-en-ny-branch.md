# 🌿 Guide til opgave: Opret og arbejd i en ny branch

Branches er en vigtig del af versionsstyring med Git. De giver dig mulighed for at arbejde på nye funktioner uden at forstyrre hovedprojektet, indtil ændringerne er klar. I denne opgave lærer du at oprette og arbejde i en ny branch.

---

## 🌟 Læringsmål

* Du kan oprette en ny branch i dit Git-repository
* Du kan arbejde med filer i en branch og versionere dine ændringer
* Du forstår hvordan branches bruges til udvikling

---

## 🔧 Kompetencer

* Parallel udvikling uden konflikter
* Versionsstyring med branches
* Push af branches til GitHub

---

## 🦻 Trin-for-trin vejledning

### 🔹 1. Opret en ny branch

Sørg for at være i roden af dit projekt og kør:

```bash
git checkout -b feature-beskrivelse
```

> Dette skifter dig samtidig over til den nye branch.

Du kan bekræfte, hvilken branch du er på med:

```bash
git branch
```

Den aktive branch vil være markeret med `*`.

---

### 🔹 2. Tilføj en ny fil

Opret en ny fil med beskrivelse:

```bash
echo "Dette er en testfil til Git branch øvelse." > docs/beskrivelse.md
```

---

### 🔹 3. Gem og commit dine ændringer

Tilføj og commit filen som normalt:

```bash
git add .
git commit -m "Tilføjet beskrivelse.md"
```

---

### 🔹 4. Push branchen til GitHub

Brug `-u` for at koble din lokale branch til den på GitHub:

```bash
git push -u origin feature-beskrivelse
```

> Nu kan du finde din branch på GitHub og evt. lave en Pull Request, hvis du vil merge den senere.

---

## ✅ Tjekliste

* [ ] Du har oprettet en ny branch med `git checkout -b`
* [ ] Du har tilføjet og committed en ny fil
* [ ] Du har pushed branchen til GitHub med `-u`
* [ ] Du kan se branchen online i dit repo

---

## 🧠 Hvorfor er dette vigtigt?

Branches bruges i **alle professionelle Git workflows**. De gør det muligt at udvikle nye funktioner, rette fejl og samarbejde uden at forstyrre den stabile `main` branch.

> En god udvikler arbejder aldrig direkte i `main`, men laver altid en branch til nye opgaver.
