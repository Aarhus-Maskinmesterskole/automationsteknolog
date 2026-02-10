# 🖥️ Installation af Visual Studio Code på Windows

Denne guide hjælper dig med at installere Visual Studio Code (VS Code) og gøre det klar til Python-udvikling på Windows.

---

## 🧰 Hvad du skal bruge

* En Windows 10 eller 11 PC
* Administratoradgang (kræves til installation)
* Internetforbindelse

---

## 1️⃣ Download VS Code

1. Gå til den officielle side:
   👉 [https://code.visualstudio.com](https://code.visualstudio.com)
2. Klik på **Download for Windows** (User Installer anbefales)
3. Gem `.exe`-filen og åbn den

---

## 2️⃣ Installer VS Code

1. Kør installationsfilen
2. Acceptér licensbetingelserne og klik **Next**
3. Vælg installationsmappe (standard er fin)
4. **Vigtigt!** Sæt flueben i:

   * ✅ "Add to PATH (requires shell restart)"
   * ✅ "Register Code as editor for supported file types"
5. Klik **Install** og vent til den er færdig

---

## 3️⃣ Start VS Code og vælg sprog

1. Start programmet (via genvej eller Start-menu)
2. Første gang vil den spørge om interface-sprog – vælg **English** eller **Danish**, afhængig af underviserens valg

---

## 4️⃣ Installer Python

Hvis Python ikke allerede er installeret:

1. Gå til: 👉 [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Vælg "Download Python 3.x.x" til Windows
3. **Vigtigt!** Sæt flueben i **"Add Python to PATH"** før du klikker "Install Now"

---

## 5️⃣ Installer nødvendige Extensions

Extensions udvider VS Code's funktionalitet. Åbn Extensions-panelet (Ctrl+Shift+X) og installer følgende:

### Nødvendige Extensions

1. **Python** (Microsoft)
   - Python-understøttelse, debugging, IntelliSense
   - Søg efter "Python" og installer den fra Microsoft

2. **Pylance** (Microsoft)
   - Forbedret Python IntelliSense og type checking
   - Installeres ofte automatisk med Python-extension

### Anbefalede Extensions

3. **Rainbow CSV**
   - Farver kolonner i CSV-filer for bedre læsbarhed
   - Søg efter "Rainbow CSV"

4. **Markdown All in One**
   - Gør det nemmere at skrive dokumentation i Markdown
   - Nyttig til README-filer og dokumentation

5. **GitLens** (valgfrit)
   - Udvidet Git-funktionalitet direkte i editoren
   - Se hvem der lavede hvilke ændringer

6. **Indent Rainbow**
   - Farver indrykning for bedre overblik i Python-kode
   - Især nyttigt i Python hvor indrykning er vigtig

7. **Error Lens**
   - Viser fejl og advarsler direkte i koden
   - Gør det lettere at spotte problemer

8. **Better Comments**
   - Farvemarkerer forskellige typer kommentarer
   - Gør kommentarer mere læsbare

9. **Material Icon Theme** (valgfrit)
   - Pænere ikoner til forskellige filtyper
   - Gør det lettere at finde filer i file explorer

### Sådan installerer du extensions:

1. Klik på Extensions-ikonet (firkant i venstre sidebar) eller tryk **Ctrl+Shift+X**
2. Søg efter extension-navnet
3. Klik **Install** på den rigtige extension
4. Genstart VS Code hvis du bliver bedt om det

---

## 6️⃣ Test din installation

1. Opret en mappe til dine projekter, fx `C:\projekter\teknologi`
2. Opret en ny fil: `hello.py`

```python
print("Hej fra VS Code!")
```

3. Højreklik i editorvinduet → **Run Python File in Terminal**
4. Du burde se: `Hej fra VS Code!`

---

## ✅ Klar til brug!

VS Code er nu installeret og konfigureret til at arbejde med Python på Windows.

> Husk også at installere Git og oprette GitHub-konto, hvis du arbejder med versionsstyring.

Kontakt underviser hvis du får fejl eller er i tvivl om noget undervejs.
