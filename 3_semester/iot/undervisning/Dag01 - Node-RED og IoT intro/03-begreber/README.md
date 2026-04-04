# 📚 Node-RED Grundbegreber

## 🎯 Formål

Dette afsnit introducerer dig til de centrale begreber i Node-RED-miljøet. Du vil få en dybere forståelse af message-objektet, payloads, topics, flows og context-variabler - som udgør rygraden i Node-RED-programmering. Med denne viden vil du være i stand til at designe mere komplekse og effektive flows.

---

## 💬 Message-objektet (`msg`)

I Node-RED overføres data mellem noder via et JavaScript-objekt kaldet `msg`. Dette objekt kan indeholde vilkårlige egenskaber, men nogle få er specielt betydningsfulde.

### 📦 `msg.payload`

**`msg.payload`** er den mest centrale egenskab i message-objektet og indeholder typisk hoveddataene, som noderne behandler. Det er standardværdien de fleste noder læser fra og skriver til.

- Kan være enhver datatype: string, nummer, boolean, objekt, array
- Ændres typisk af processing-noder
- Er standardoutputtet i debug-panel

**Eksempel:**
```javascript
// En inject-node kan sætte en payload:
msg.payload = "Hello World";

// Eller en function-node kan transformere den:
msg.payload = msg.payload.toUpperCase();
```

### 📌 `msg.topic`

**`msg.topic`** bruges til at kategorisere eller identificere beskeder, især i flows, der håndterer multiple datakilder.

- Ofte brugt til routing af beskeder
- Kan sammenlignes med "subject" i en email
- Særligt nyttig i MQTT-integrationer og multi-source flows

**Eksempel:**
```javascript
// Topic kan bruges til at identificere datakilden:
msg.topic = "temperature_sensor_1";
msg.payload = 22.5;

// Eller til at definere en handling:
msg.topic = "set_temperature";
msg.payload = 21;
```

### 🔄 Andre almindelige message-egenskaber

- **`msg._msgid`**: Automatisk genereret unik ID for hver besked
- **`msg.req` / `msg.res`**: HTTP-request og response objekter (i http noder)
- **`msg.filename`**: Brugt med file noder
- **`msg.error`**: Fejlinformation, når noget går galt

---

## 🌐 Context i Node-RED

Context er Node-RED's mekanisme til at gemme data mellem message-behandlinger. Der er tre niveauer af context:

### 🔹 Node context

Gemmer data specifikt for en enkelt node. Kun tilgængeligt inden for den specifikke node.

```javascript
// Gem i node context
var count = context.get('count') || 0;
count += 1;
context.set('count', count);
```

### 🔹 Flow context

Delt mellem alle noder i samme flow (tab). Perfekt til flow-specifik tilstand.

```javascript
// Gem i flow context
var totalValue = flow.get('total') || 0;
totalValue += msg.payload;
flow.set('total', totalValue);
```

### 🔹 Global context

Delt mellem alle flows i hele Node-RED-instansen. Bruges til applikationsbredde data.

```javascript
// Gem i global context
var deviceStatus = global.get('deviceStatus') || {};
deviceStatus[msg.deviceId] = "online";
global.set('deviceStatus', deviceStatus);
```

---

## 📋 Flows og Tabs

- **Tab**: En side i editoren, normalt repræsenterer et logisk adskilt flow eller subsystem
- **Flow**: En samling af sammenkoblede noder der udfører en bestemt funktion
- **Subflow**: Genbrugelige flow der kan bruges som komponenter i andre flows

**Best practices for flow-organisation:**
1. Del flows op i logiske, funktionelle enheder
2. Giv beskrivende navne til flows/tabs
3. Brug kommentar-noder til at dokumentere flow-funktionalitet
4. Overvej at bruge subflows til gentagende mønstre

---

## 🔄 Message-flow og Message-routing

### 🔀 Grundlæggende flow

I et simpelt flow bevæger beskeder sig fra venstre mod højre, med hver node der behandler beskeden og sender den videre.

### 🧩 Routing-mønstre

- **Sequential**: Besked passerer gennem en række af noder (A → B → C)
- **Parallel**: Besked sendes til flere noder samtidig (A → B, A → C)
- **Conditional**: Baseret på data eller regler sendes beskeden ad forskellige veje
- **Join/Split**: Beskeder kan splittes op eller samles undervejs

### 🚦 Switch-node

Switch-noden er central for betinget message-routing baseret på beskedens indhold.

```
if msg.payload > 20:
   → route to output 1
else:
   → route to output 2
```

---

## 🔍 Debugging og Fejlfinding

### 🐞 Debug-noden

Debug-noden er dit vigtigste værktøj til at inspicere beskeder, der flyder gennem dit system.

**Tips til effektiv debugging:**
- Brug flere debug-noder på strategiske punkter
- Aktivér/deaktivér dem efter behov
- Vælg mellem "msg.payload" og "complete msg object"
- Brug debug-sidebar til at filtrere og søge

### 📊 Status-noder

Status-noder tillader dig at vise statusinformation (farvet prik og tekst) på noder.

```javascript
// I en function-node:
node.status({fill:"green", shape:"dot", text:"Success"});
// Eller ved fejl:
node.status({fill:"red", shape:"ring", text:"Failed: " + err.message});
```

---

## 📝 Praktiske Øvelser

### Øvelse 1: Message Manipulation

1. Opret et flow med inject → function → debug
2. I function-noden, eksperimentér med at manipulere forskellige aspekter af message-objektet:

```javascript
// Eksperiment med egenskaber
msg.payload = "Hello";
msg.topic = "greeting";
msg.customValue = 42;
return msg;
```

### Øvelse 2: Context Variables

1. Opret et flow, der tæller, hvor mange gange en inject-node aktiveres
2. Brug node, flow eller global context til at bevare tællerens værdi
3. Vis den aktuelle tællerværdi i en debug-node

### Øvelse 3: Message Routing

1. Opret et flow med én inject-node og to debug-noder
2. Tilføj en switch-node, der router beskeder baseret på deres payload
3. Konfigurer switch-noden til at sende tal < 50 til første output og resten til andet output
4. Test med forskellige inject-payloads

---

## ✅ Afleveringsopgave

**Beskriv med maksimalt 100 ord forskellen mellem `msg.payload` og `msg.topic` og giv et konkret eksempel på, hvordan de samarbejder i et effektivt flow.**

- Gem din beskrivelse direkte i denne README.md-fil
- Commit din ændring til Git

**Vurderingskriterier:**
- Præcis og koncis forklaring
- Korrekt teknisk forståelse af begreberne
- Relevant praktisk eksempel
- Maksimum 100 ord

---

## 📚 Yderligere Ressourcer

- [Node-RED: Working with Messages](https://nodered.org/docs/user-guide/messages)
- [Node-RED: Working with Context](https://nodered.org/docs/user-guide/context)
- [Node-RED: Creating Flows](https://nodered.org/docs/user-guide/flows)

Se også den vedhæftede `cheat_sheet.md` for hurtige referencer til disse begreber.
