# 🔀 Guide: Merge en branch til main

Når du arbejder med branches i Git, laver du typisk funktionalitet i en midlertidig gren (branch), som til sidst skal flettes tilbage i hovedsporet `main`. Denne guide forklarer processen trin for trin.

---

## 🧠 Hvad er et merge?

Et merge kombinerer ændringer fra én branch (f.eks. `feature-sensor`) ind i en anden (typisk `main`). Det bruges, når arbejdet i branchen er afsluttet og skal være en del af projektets hovedversion.

---

## 🔧 Hvornår bør du merge?

* Når en funktion eller dokumentation er færdig
* Når en gruppe har testet og dokumenteret sin kode
* Før aflevering, så `main` indeholder hele projektet

> Du bør **aldrig** arbejde direkte i `main` under udvikling. Brug branches og merge, når du er klar.

---

## 🪜 Hvordan gør man? (Kort version)

1. Skift til `main`:

   ```bash
   git checkout main
   git pull
   ```
2. Merge din branch:

   ```bash
   git merge feature-sensor
   ```
3. Push ændringerne:

   ```bash
   git push
   ```

Hvis der opstår konflikter, markerer Git det i filerne. Du skal da løse dem manuelt, gemme og committe:

```bash
git add .
git commit -m "Løst merge-konflikt i ..."
git push
```

---

## 🧭 Tips til god merge-praksis

* Lav **små branches** med ét klart formål
* Skriv **gode commit-beskeder**, der forklarer hvad du har lavet
* Merg **ofte** så du undgår store konflikter
* Brug `git status` og `git log` for at følge med

---

## 💼 Hvorfor bruges merge i erhvervslivet?

Fordi teams arbejder parallelt – og kode skal samles ét sted:

* Det gør det muligt at teste nye idéer uden at ødelægge eksisterende kode
* Det gør samarbejde muligt via pull requests og review
* Det er en central del af alle moderne udviklingsmetoder (Scrum, CI/CD, GitOps)

> Merge er ikke kun teknik – det handler om **samarbejde og tillid til hinandens arbejde**.
