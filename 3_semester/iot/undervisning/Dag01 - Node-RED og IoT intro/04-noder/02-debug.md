# 🔍 Debug Node

Debug-noden er din vindue ind i Node-RED flowet. Den gør det muligt at se og inspicere beskeder, der flyder gennem systemet, og er et afgørende værktøj for fejlfinding og flowudvikling.

## 🎯 Formål

I denne guide lærer du om debug-noden og hvordan du kan:
- Overvåge og inspicere beskeder i dit flow
- Tilpasse hvordan data vises i debug-panelet
- Bruge forskellige output-niveauer til organisering
- Filtrere debug-output for bedre overblik

---

## ⚡ Grundfunktionalitet

Debug-noden har én primær funktion: At vise indholdet af en besked i debug-panelet. Den kan konfigureres til at vise:

- **Hele beskedobjektet** (`msg`) - alle egenskaber
- **Kun en specifik egenskab** (typisk `msg.payload`)
- **Beskedstatus** - til et statusfelt i Node-RED-editoren

Output fra debug-noden vises i debug-panelet, som åbnes ved at klikke på bug-ikonet i den højre sidepanel i Node-RED-editoren.

---

## 🛠️ Konfiguration

![Debug Node Configuration](https://nodered.org/docs/user-guide/images/editor-debug-node-properties.png)

### Output-indstillinger

- **msg.payload**: Viser kun beskedens payload
- **complete msg object**: Viser hele beskedobjektet med alle egenskaber
- **selected properties**: Viser kun de specificerede egenskaber
- **to status**: Viser værdien i et statusfelt under noden i editoren

### Visnings-indstillinger

- **Debug panel**: Send output til debug-panelet i editoren
- **Console**: Send output til system-konsollen (hvor Node-RED kører)
- **Sidebar tab**: Specificér en bestemt fane i debug-panelet
- **Debug level**: Vælg mellem debug, trace, log, warn, error niveauer

---

## 💡 Eksempler

### Eksempel 1: Simpel payload-debug

```
[Inject] → [Debug]
```

Konfiguration:
- Output: msg.payload
- Mål: Debug panel

Dette vil vise payload-værdien i debug-panelet, når inject-noden aktiveres.

### Eksempel 2: Vis hele beskedobjektet

```
[Inject] → [Function] → [Debug]
```

Konfiguration:
- Output: complete msg object
- Mål: Debug panel

Function-node:
```javascript
// Tilføj flere egenskaber til beskeden
msg.sensorId = "temp001";
msg.unit = "celsius";
msg.timestamp = new Date().toISOString();
return msg;
```

Dette vil vise alle beskedegenskaber, inklusive de tilføjede.

### Eksempel 3: Status-display

```
[Inject] → [Debug]
```

Konfiguration:
- Output: msg.payload
- Mål: Node status

Dette vil vise payload-værdien direkte i flowet som en status under noden.

---

## 🔎 Debug-panelet

Debug-panelet har flere nyttige funktioner:

### Kontroller

- **Clear** (🧹): Rydder alle meddelelser i panelet
- **Pause/Resume** (⏸/▶️): Midlertidigt stopper/genoptager visning af nye meddelelser
- **Filter** (🔍): Filtrer meddelelser baseret på tekst

### Formateringsmuligheder

- **Expand/Collapse** (▶/▼): Udvid eller sammenfold objekter
- **Format** ({}): Formater JSON-data
- **Raw/Parsed**: Skift mellem rå og fortolket visning
- **Copy Value** (📋): Kopiér værdi til udklipsholder

### Organisation med debug-niveauer

Debug-noder kan opdeles i forskellige output-niveauer:
- **debug**: Standard fejlfindingsinformation
- **trace**: Detaljeret tracing information
- **log**: Generelle loghændelser
- **warning**: Advarsler, men ikke kritiske
- **error**: Fejlhændelser

Dette hjælper med at organisere og filtrere debug-output.

---

## ⚠️ Fejlfindingstips

- **For mange beskeder?** Brug filter-funktionen i debug-panelet
- **Komplekse objekter?** Skift til formateret JSON-visning
- **Langsom editor?** Deaktiver debug-noder du ikke bruger (klik på grøn prik)
- **Mistede en besked?** Brug pauseknappen til at fryse debug-panelet

---

## 🏋️ Øvelser

### Øvelse 1: Multiple Debug Points

1. Opret et flow med en inject-node
2. Tilføj en function-node der ændrer payload
3. Tilføj debug-noder på følgende steder:
   - Efter inject-noden (vis kun payload)
   - Efter function-noden (vis hele beskedobjektet)
4. Deploy og sammenlign output

### Øvelse 2: Debug-niveauer

1. Opret et flow med to inject-noder
2. Tilføj en debug-node efter hver:
   - Første debug: Niveau = debug
   - Anden debug: Niveau = error
3. Deploy og se hvordan de vises forskelligt i debug-panelet
4. Brug filter-dropdown til at vise kun error-meddelelser

### Øvelse 3: Status Debug

1. Opret et flow med en inject-node der sender tilfældige tal
2. Tilføj en function-node der beregner temperaturniveauer:
   ```javascript
   var temp = msg.payload;
   if (temp < 18) {
       msg.level = "cold";
   } else if (temp > 25) {
       msg.level = "hot";
   } else {
       msg.level = "comfortable";
   }
   return msg;
   ```
3. Tilføj to debug-noder:
   - Første: Vis payload i debug-panelet
   - Anden: Vis level som node-status

---

## 🔍 Yderligere ressourcer

- [Node-RED Documentation - Debug Node](https://nodered.org/docs/user-guide/nodes#debug)
- [Working with Debug Panel](https://nodered.org/docs/user-guide/editor/workspace/debug)
- [Debugging Techniques in Node-RED](https://nodered.org/docs/user-guide/runtime/logging)
