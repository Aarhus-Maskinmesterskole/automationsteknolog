# 📝 Guide til opgave: Lav en ændring og commit

Denne guide viser dig, hvordan du laver en mindre ændring i en fil, og hvordan du bruger Git til at gemme denne ændring lokalt og derefter sende den til GitHub.

---

## 🌟 Læringsmål

* Du kan redigere en eksisterende fil i dit projekt
* Du forstår, hvordan du arbejder med `git add`, `git commit` og `git push`
* Du kan verificere dine ændringer online i GitHub

---

## 🔧 Kompetencer

* Versionsstyring i praksis
* Arbejde med det lokale Git-repository
* Dokumentation af ændringer gennem commit-beskeder

---

## 🦻 Trin-for-trin vejledning

### 🔹 1. Redigér din README.md

Åbn filen `README.md` i din editor (fx VS Code), og tilføj følgende tekst nederst i filen:

```markdown
Dette repo bruges til Git-træning i Teknologi og Projektudvikling.
```

Gem filen.

---

### 🔹 2. Tjek status i terminalen

Kør følgende kommando for at se, hvad der er blevet ændret:

```bash
git status
```

Du bør se noget i stil med:

```text
modified:   README.md
```

---

### 🔹 3. Tilføj og commit ændringen

Føj ændringen til Git's "staging area":

```bash
git add README.md
```

Lav et commit med en meningsfuld besked:

```bash
git commit -m "Opdateret README med formål for repoet"
```

---

### 🔹 4. Push til GitHub

Send dine ændringer til det fjernlager, du klonede fra:

```bash
git push
```

---

### 🔹 5. Kontrollér på GitHub

Gå til dit repository i browseren:

* Tjek at `README.md` er opdateret med den nye tekst
* Klik på "Commits" for at se din besked og tidspunkt

---

## ✅ Tjekliste

* [ ] Du har redigeret `README.md` og gemt filen
* [ ] Du har brugt `git status` og `git add`
* [ ] Du har lavet et commit med en klar besked
* [ ] Du har pushed til GitHub og tjekket ændringen online

---

## 🧠 Hvorfor er dette vigtigt?

Det er vigtigt at kunne dokumentere og versionere dine ændringer. Hver commit er et lille snapshot af dit projekt, som du og dine gruppemedlemmer altid kan gå tilbage til.

> Hyppige og meningsfulde commits er kernen i godt samarbejde i softwareudvikling.
