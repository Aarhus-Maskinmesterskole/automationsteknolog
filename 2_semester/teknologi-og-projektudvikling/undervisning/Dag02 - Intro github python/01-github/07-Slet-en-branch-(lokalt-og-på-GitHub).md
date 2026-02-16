# 🧹 Guide til opgave: Slet en branch (lokalt og på GitHub)

Når en branch er blevet merged og arbejdet er færdigt, bør den slettes for at holde projektet ryddeligt. Denne opgave viser, hvordan du sletter både lokalt og remote.

---

## 🎯 Læringsmål

* Du kan identificere hvilke branches der er færdige og kan slettes
* Du kan slette branches korrekt både lokalt og på GitHub
* Du forstår hvorfor oprydning er vigtig i versionsstyring

## 🛠️ Kompetencer

* Branch management
* Oprydning og vedligeholdelse af repository
* Arbejde med lokal og remote Git-tracking

---

## 🪜 Trin-for-trin vejledning

### 🔹 1. Tjek at du er på `main`

Du må **ikke** slette en branch du står i:

```bash
git checkout main
```

### 🔹 2. Slet branch lokalt

```bash
git branch -d feature-beskrivelse
```

> `-d` betyder "delete" og Git tjekker at branchen er merged først

Hvis branchen **ikke** er merged, og du **stadig** vil slette:

```bash
git branch -D feature-beskrivelse
```

> Brug kun `-D` hvis du er helt sikker

### 🔹 3. Slet branch på GitHub (remote)

```bash
git push origin --delete feature-beskrivelse
```

---

## ✅ Tjekliste

* [ ] Du har skiftet til `main`
* [ ] Du har slettet den lokale branch med `git branch -d`
* [ ] Du har slettet den remote branch med `git push origin --delete ...`
* [ ] Du kan bekræfte at branchen er væk på GitHub under "branches"

---

## 🧠 Hvorfor er dette vigtigt?

Ubrugte branches gør projektet rodet og sværere at navigere i – især når I arbejder i grupper. En opdateret og opryddet repo viser også professionel praksis og gør det nemmere for andre (fx underviser) at følge med i jeres proces.

> En god hovedregel: *Når en branch er merged og ikke længere skal bruges, så slet den.*
