# 🏁 Dit første Node-RED flow

## 🎯 Formål

I denne øvelse skal du oprette dit første Node-RED flow. Du vil lære de grundlæggende byggeklodser i Node-RED at kende: noder, forbindelser og deploy-cyklussen. Du vil også få hands-on erfaring med at importere eksisterende flows og bygge et simpelt dashboard.

---

## � Grundbegreber

### Nodes (Noder)
Noder er de grundlæggende byggesten i Node-RED. Hver node har en specifik funktion:
- **Input-noder**: Startpunkter for flows (f.eks. inject, http in)
- **Processing-noder**: Transformerer data (f.eks. function, change, switch)
- **Output-noder**: Endepunkter for flows (f.eks. debug, http response)

### Wires (Forbindelser)
Forbindelser mellem noder viser dataflowet i dit system. Data bevæger sig fra venstre mod højre gennem forbindelserne.

### Messages (Beskeder)
Data sendes mellem noder som besked-objekter (`msg`). Det vigtigste felt er typisk `msg.payload`, som indeholder hovedindholdet.

### Deploy (Aktivering)
Når du har bygget dit flow, skal du klikke på "Deploy" knappen for at aktivere det i Node-RED runtime.

---

## 🛠️ Øvelse 1: Dit første flow

### Trin 1: Opret et simpelt flow
1. Åbn Node-RED i din browser ved at navigere til http://localhost:1880
2. Find **inject**-noden i paletten til venstre (under "common")
3. Træk den ind på arbejdsfladen
4. Find **debug**-noden i paletten (også under "common")
5. Træk den ind på arbejdsfladen
6. Forbind de to noder ved at trække en linje fra inject-nodens højre udgang til debug-nodens venstre indgang
7. Dobbeltklik på inject-noden for at konfigurere den
   - Indstil payload type til "string"
   - Indtast "Hello, Node-RED!" som payload
   - Klik på "Done"
8. Klik på "Deploy" knappen øverst til højre

### Trin 2: Test dit flow
1. Åbn debug-panelet ved at klikke på bug-ikonet i øverste højre hjørne
2. Klik på knappen på inject-noden (den lille firkant til venstre for noden)
3. Observer output i debug-panelet - du bør se "Hello, Node-RED!"

### Trin 3: Tilføj automatisk udløsning
1. Dobbeltklik på inject-noden igen
2. Aktivér "Repeat" muligheden
3. Vælg "interval" og indstil det til hver 5. sekund
4. Klik på "Done"
5. Klik på "Deploy" igen
6. Observer debug-panelet, hvor du nu bør se beskeder dukke op hvert 5. sekund

---

## 🛠️ Øvelse 2: Importér og udvid et flow

### Trin 1: Importér det forberedte flow
1. Klik på "hamburger-menuen" (≡) i øverste højre hjørne
2. Vælg "Import"
3. Klik på "select a file to import"
4. Vælg filen `first_flow.json` fra denne mappe
5. Klik på "Import"

### Trin 2: Undersøg flowet
1. Du bør nu se et nyt flow med flere noder
2. Klik på "Deploy" for at aktivere det
3. Observer debug-panelet for at se output fra flowet

### Trin 3: Installér Dashboard-noder
1. Klik på "hamburger-menuen" (≡) i øverste højre hjørne
2. Vælg "Manage palette"
3. Gå til fanen "Install"
4. Søg efter "node-red-dashboard"
5. Klik på "Install" ved siden af "node-red-dashboard"
6. Bekræft installationen

### Trin 4: Tilføj en gauge til dashboard
1. Find **ui_gauge**-noden i paletten (under "dashboard")
2. Træk den ind på arbejdsfladen
3. Dobbeltklik på gauge-noden for at konfigurere den:
   - Opret en ny gruppe og fane hvis nødvendigt
   - Sæt enheden til "°C" (grader celsius)
   - Sæt minimum til 0 og maximum til 100
   - Klik på "Done"
4. Forbind den relevante node fra det importerede flow til gauge-noden
5. Klik på "Deploy"
6. Åbn dashboard ved at klikke på dashboard-fanen i sidepanelet og derefter på launch-knappen

---

## 📊 Øvelse 3: Udvid dashboardet

### Trin 1: Tilføj et diagram
1. Find **ui_chart**-noden i paletten (under "dashboard")
2. Træk den ind på arbejdsfladen
3. Dobbeltklik for at konfigurere den:
   - Placér den i samme gruppe som gauge-noden
   - Vælg "Line chart" som type
   - Indstil "X-axis" til "Last 5 minutes"
   - Klik på "Done"
4. Forbind den relevante node til chart-noden
5. Klik på "Deploy"
6. Tjek dashboardet for at se diagram og gauge sammen

### Trin 2: Forbedre flowet
1. Tilføj en **function**-node til flowet
2. Konfigurer den til at tilføje et tidsstempel til beskederne:
   ```javascript
   msg.timestamp = new Date().toLocaleTimeString();
   return msg;
   ```
3. Placér den i flowet før dashboard-noderne
4. Klik på "Deploy"

---

## ✅ Afleveringsopgave

### Del 1: Grundlæggende flow
1. Opret et flow der:
   - Genererer et tilfældigt tal mellem 0-100 hvert 2. sekund
   - Viser tallet i debug-panelet
   - Visualiserer det på dashboard med en gauge
   - Viser en historisk graf over de sidste 20 værdier

### Del 2: Dokumentation
1. Tag et screenshot af dit flow i Node-RED-editoren
2. Tag et screenshot af det kørende dashboard
3. Gem screenshot som `hello_dashboard.png`
4. Commit filen til dit Git-repository

### Vurderingskriterier
- Fungerende inject-node med periodisk generering af data
- Korrekt konfigureret gauge og chart på dashboard
- Velorganiseret layout på både flow og dashboard
- Korrekt indsendt screenshot med commit

---

## 💡 Nyttige tips

- **Brug af debug**: Debug-noden er din bedste ven under udvikling. Brug den ofte for at se hvad der sker.
- **Node-hjælp**: Klik på et nodetype i paletten og derefter på info-fanen i sidepanelet for at læse dokumentation.
- **Navngiv noder**: Giv dine noder beskrivende navne for at gøre flowet mere forståeligt.
- **Organisér flowet**: Brug wirecolors og layout-værktøjer til at gøre flowet mere overskueligt.
- **Gem ofte**: Brug "Export" funktionen i menuen til at tage backups af dine flows.

---

## � Yderligere læsning

- [Node-RED Dokumentation](https://nodered.org/docs/)
- [Node-RED Dashboard Guide](https://flows.nodered.org/node/node-red-dashboard)
- [Getting Started with Node-RED](https://nodered.org/docs/getting-started/)

Når du har fuldført denne øvelse, er du klar til at udforske flere avancerede funktioner i Node-RED, som beskrevet i den næste sektion, `03-begreber/`.
