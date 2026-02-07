# 🧭 Guide til opgave: Opret og klon et GitHub-repository

Denne vejledning hjælper dig gennem en typisk GitHub-opgave, hvor du opretter et repository og henter det ned lokalt med **git**. Det er den mest udbredte metode og fungerer på alle platforme.

---

## 🎯 Læringsmål

* Du kan oprette et repository i GitHub med korrekt navn og indhold
* Du kan klone et repo til din computer med `git clone`
* Du forstår sammenhængen mellem lokal og fjern versionsstyring (remote)

## 🔧 Kompetencer

* Versionsstyring med Git og GitHub
* Grundlæggende terminalkommandoer
* Strukturering og organisering af kodeprojekter

---

## 🪜 Trin-for-trin vejledning

## 🔹 1. Log ind på GitHub og opret repo

1. Gå til: [https://github.com](https://github.com)
2. Klik på **+ → New repository**
3. Indtast:

   * **Repository name:** `gruppe-XX-testrepo`
   * **Description:** “Testprojekt for GitHub intro”
   * **Visibility:** vælg **Private**
   * ⚠️ Fjern flueben i **“Add a README file”** (vi laver den selv)
4. Klik **Create repository**

Når repo’et er oprettet, bliver du vist en side med “Quick setup”.

---

## 🔹 2. Klon repo med `git clone` (anbefalet med HTTPS)

Kopiér repo’ets HTTPS-adresse fra GitHub (den ligner dette):

`https://github.com/brugernavn/gruppe-XX-testrepo.git`

Kør:

```bash
git clone https://github.com/brugernavn/gruppe-XX-testrepo.git
cd gruppe-XX-testrepo
```

> Du er nu inde i din lokale kopi af repo’et.

### Hvis du bliver bedt om login

GitHub tillader ikke længere “password login” til git over HTTPS. Du skal bruge en **Personal Access Token (PAT)**.

---

## 🔹 2A. (Kun hvis nødvendigt) Opret GitHub token til HTTPS (PAT)

1. GitHub → Settings → Developer settings → **Personal access tokens** → **Tokens (classic)**
2. Generate new token (classic)
3. Vælg:

   * Expiration: fx 30/90 dage
   * Scope: ✅ `repo`
4. Kopiér token (du ser den kun én gang)

Når git spørger:

* **Username:** din GitHub-bruger
* **Password:** indsæt token (ikke dit GitHub password)

> Tip: På Ubuntu kan Git Credential Manager gøre dette nemmere, men token virker altid.

---

## 🔹 3. Opret første fil og struktur

1. Opret en README:

```bash
echo "# GitHub Test Repo" > README.md
```

2. Opret docs-mappe + en fil (så mappen vises på GitHub):

```bash
mkdir docs
echo "Dokumentation kommer her." > docs/test.md
```

3. Gem ændringer og push:

```bash
git add .
git commit -m "Init: Tilføjet README og docs mappe"
git push
```

---

## 🔹 4. Tjek GitHub

Gå tilbage til GitHub-repo’et og verificér:

* README er synlig
* `docs/test.md` ligger i `docs/`

---

## ✅ Tjekliste

* [ ] Repo oprettet uden auto-genereret README
* [ ] Repo klonet lokalt med `git clone`
* [ ] README + `docs/` + `docs/test.md` oprettet
* [ ] Commit + push gennemført
* [ ] Verificeret på GitHub

---

## 🧠 Hvorfor er dette vigtigt?

Det er fundamentet for alt gruppens arbejde: kode, dokumentation og samarbejde.
Når I kan dette, kan I arbejde professionelt med Git i alle projekter fremover.

---

## Bonus: “Industrimåden”

I industrien ser du typisk:

* **git clone + SSH** (når det er sat op)
* eller **git clone + token** (HTTPS)
  GitHub CLI (`gh`) bruges nogle steder, men det er ikke et must og kan skabe unødig friktion i undervisning.

---

## 🔹 (Valgfrit) Klon repo med SSH (Windows + Linux)

SSH gør, at du typisk kan `git push` uden tokens/password hver gang. Du skal:

1. have en SSH-nøgle på din computer
2. tilføje den **public key** til GitHub
3. klone med `git@github.com:...`

---

### ✅ Linux (Ubuntu/Debian osv.)

**1) Tjek om du allerede har en nøgle**

```bash
ls -la ~/.ssh
```

Hvis du ser `id_ed25519` og `id_ed25519.pub`, så har du en nøgle.

**2) Opret en ny nøgle (anbefalet)**

```bash
ssh-keygen -t ed25519 -C "din-email@skole.dk"
```

**3) Start ssh-agent og tilføj nøglen**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**4) Kopiér public key**

```bash
cat ~/.ssh/id_ed25519.pub
```

**5) Tilføj nøglen på GitHub**
GitHub → **Settings** → **SSH and GPG keys** → **New SSH key** → paste → **Add**

**6) Test**

```bash
ssh -T git@github.com
```

**7) Klon med SSH**

```bash
git clone git@github.com:brugernavn/gruppe-XX-testrepo.git
cd gruppe-XX-testrepo
```

---

### ✅ Windows 10/11 (to nemme muligheder)

> Du kan gøre det i **PowerShell** eller **Git Bash** (begge virker).
> Git Bash følger Linux-kommandoer mest.

#### Mulighed A: PowerShell (anbefalet på moderne Windows)

**1) Tjek/Start ssh-agent**
Kør PowerShell som normal bruger:

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
```

**2) Opret nøgle**

```powershell
ssh-keygen -t ed25519 -C "din-email@skole.dk"
```

Tryk Enter for standard placering.

**3) Tilføj nøglen**

```powershell
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

**4) Kopiér public key**

```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub
```

**5) Tilføj nøglen på GitHub**
GitHub → **Settings** → **SSH and GPG keys** → **New SSH key** → paste → **Add**

**6) Test**

```powershell
ssh -T git@github.com
```

**7) Klon**

```powershell
git clone git@github.com:brugernavn/gruppe-XX-testrepo.git
cd gruppe-XX-testrepo
```

#### Mulighed B: Git Bash (hvis Git for Windows er installeret)

**1) Opret nøgle**

```bash
ssh-keygen -t ed25519 -C "din-email@skole.dk"
```

**2) Start agent og tilføj nøgle**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**3) Kopiér public key**

```bash
cat ~/.ssh/id_ed25519.pub
```

**4) Tilføj på GitHub + test**

```bash
ssh -T git@github.com
```

**5) Klon**

```bash
git clone git@github.com:brugernavn/gruppe-XX-testrepo.git
cd gruppe-XX-testrepo
```

---

### 🔹 Commit + push (samme for Windows og Linux)

```bash
echo "# GitHub Test Repo" > README.md
mkdir docs
echo "Dokumentation kommer her." > docs/test.md

git add .
git commit -m "Init: Tilføjet README og docs mappe"
git push
```

---

### ℹ️ Typiske fejl (hurtige fixes)

* **“Permission denied (publickey)”**
  → Nøglen er ikke tilføjet til GitHub, eller ssh-agent kører ikke.

* **“The authenticity of host 'github.com' can’t be established”**
  → Svar `yes` første gang.

* **Windows spørger om passphrase**
  → Det er din nøgles passphrase (hvis du satte en), ikke GitHub password.

Hvis du vil, kan jeg tilføje en lille “tjekliste”-boks til slut med præcis hvad de skal se, når alt virker (ssh-test + `git remote -v`).
