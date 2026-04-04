# 🧩 Function Node

Function-noden er en af de mest kraftfulde noder i Node-RED. Den giver dig mulighed for at skrive tilpasset JavaScript-kode til at bearbejde beskeder på næsten enhver måde, du kan forestille dig.

## 🎯 Formål

I denne guide lærer du om function-noden og hvordan du kan:
- Skrive tilpasset JavaScript-kode i Node-RED
- Manipulere message-objekter og deres egenskaber
- Gemme og gendanne data ved hjælp af context
- Returnere multiple beskeder fra en enkelt function-node

---

## ⚡ Grundfunktionalitet

Function-noden indeholder en JavaScript-editor, hvor du kan skrive kode, der udføres, når en besked kommer ind i noden. Din kode har adgang til:

- **msg** - Den indgående besked (ofte med en `.payload` egenskab)
- **context** - Node-specifik hukommelse (data gemmes kun i denne node)
- **flow** - Flow-kontekst (data deles mellem noder i samme flow)
- **global** - Global kontekst (data deles mellem alle flows)
- **node** - Referencer til function-noden selv
- **env** - Adgang til miljøvariabler

---

## 🛠️ Grundlæggende syntaks

Function-noden forventer JavaScript-kode, der manipulerer `msg`-objektet og returnerer det (eller en ny besked) ved funktionens afslutning.

```javascript
// Grundlæggende skabelon
var newValue = msg.payload * 2;  // Manipulerer beskedens indhold
msg.payload = newValue;          // Opdaterer payload med ny værdi
return msg;                      // Returnerer den opdaterede besked
```

## 💡 Almindelige brugsmønstre

### Simpel transformation

```javascript
// Konverterer temperatur fra Celsius til Fahrenheit
msg.payload = (msg.payload * 9/5) + 32;
msg.unit = "Fahrenheit";
return msg;
```

### Betingede handlinger

```javascript
// Udfører forskellige handlinger baseret på beskedens indhold
if (msg.payload > 25) {
    msg.status = "high";
    msg.alert = true;
} else if (msg.payload < 10) {
    msg.status = "low";
    msg.alert = true;
} else {
    msg.status = "normal";
    msg.alert = false;
}
return msg;
```

### Brug af kontekst til at huske data

```javascript
// Bruger node-kontekst til at tælle beskeder
var count = context.get('count') || 0;
count += 1;
context.set('count', count);

msg.payload = count;
msg.original = msg.payload;
return msg;
```

### Returnering af flere beskeder

```javascript
// Sender forskellige beskeder til forskellige output
var msg1 = { payload: msg.payload };
var msg2 = { payload: "Besked modtaget: " + msg.payload };

// Return array med én besked per output
return [msg1, msg2];
```

### Stoppe beskedflow

```javascript
// Stopper flowet hvis værdien er uden for område
if (msg.payload < 0 || msg.payload > 100) {
    node.warn("Ugyldig værdi: " + msg.payload);
    return null;  // Returnerer intet = stopper flowet
}
return msg;
```

---

## 🔄 Context Storage

Context giver mulighed for at gemme data mellem forskellige beskedbehandlinger:

### Node Context

```javascript
// Data kun tilgængelig i denne node
var lastValue = context.get('lastValue') || 0;
var change = msg.payload - lastValue;
context.set('lastValue', msg.payload);
msg.change = change;
return msg;
```

### Flow Context

```javascript
// Data deles mellem alle noder i samme flow (tab)
var total = flow.get('total') || 0;
total += msg.payload;
flow.set('total', total);
msg.total = total;
return msg;
```

### Global Context

```javascript
// Data deles mellem alle flows
var deviceStatus = global.get('deviceStatus') || {};
deviceStatus[msg.deviceId] = msg.payload;
global.set('deviceStatus', deviceStatus);
return msg;
```

---

## ⚠️ Fejlhåndtering

### Try-Catch blokke

```javascript
// Fanger og håndterer fejl
try {
    msg.payload = JSON.parse(msg.payload);
    return msg;
} catch(e) {
    // Rapporterer fejlen i Node-RED og stopper beskedens flow
    node.error("Kunne ikke parse JSON: " + e.message, msg);
    return null;
}
```

### Status visualisering

```javascript
// Viser node status i editoren
try {
    // Dit kode her
    node.status({fill:"green", shape:"dot", text:"Success"});
    return msg;
} catch(e) {
    node.status({fill:"red", shape:"ring", text:"Fejl: " + e.message});
    return null;
}
```

---

## 🛠️ Avanceret funktionalitet

### Multiple Outputs

Du kan konfigurere function-noden til at have flere outputs:

1. Indstil "Outputs" i node-konfigurationen til det ønskede antal (fx 3)
2. Returnér et array med en besked (eller null) for hvert output:

```javascript
// For en node med 3 outputs
var msg1 = { payload: "Output 1" };
var msg2 = null; // Intet sendes fra output 2
var msg3 = { payload: "Output 3" };
return [msg1, msg2, msg3];
```

### Asynkron kode

Fra Node-RED 1.0+ kan du bruge asynkrone funktioner med Promises:

```javascript
// Simulerer en asynkron operation
return new Promise(function(resolve, reject) {
    setTimeout(function() {
        msg.payload = "Forsinket resultat";
        resolve(msg);
    }, 1000);
});
```

### Eksterne biblioteker

Du kan inkludere eksterne npm-moduler ved at installere dem i din Node-RED-installation og bruge `require`:

```javascript
// Eksempel på brug af momentjs, hvis det er installeret
var moment = global.get('moment') || require('moment');
msg.payload = moment().format('YYYY-MM-DD HH:mm:ss');
return msg;
```

---

## 🏋️ Øvelser

### Øvelse 1: Data Transformation

1. Opret et flow med inject → function → debug
2. Konfigurer inject til at sende et JSON-objekt: `{"temp": 22, "unit": "C"}`
3. Skriv en function der konverterer temperaturen til Fahrenheit:
   ```javascript
   if (msg.payload.unit === "C") {
       var celsius = msg.payload.temp;
       msg.payload.temp = (celsius * 9/5) + 32;
       msg.payload.unit = "F";
   }
   return msg;
   ```

### Øvelse 2: Beregn gennemsnit med context

1. Opret et flow med inject (tilfældigt tal) → function → debug
2. I function-noden, beregn rullende gennemsnit:
   ```javascript
   var values = context.get('values') || [];
   values.push(msg.payload);
   
   // Behold kun de seneste 10 værdier
   if (values.length > 10) {
       values.shift();  // Fjern ældste værdi
   }
   
   // Beregn gennemsnit
   var sum = 0;
   for (var i=0; i<values.length; i++) {
       sum += values[i];
   }
   var avg = sum / values.length;
   
   // Gem værdier til næste gang
   context.set('values', values);
   
   // Send gennemsnit videre
   msg.payload = avg;
   msg.count = values.length;
   return msg;
   ```

### Øvelse 3: Multiple outputs

1. Opret en function-node med 3 outputs
2. Forbind de tre outputs til separate debug-noder
3. Skriv kode der sender forskellige data til hvert output:
   ```javascript
   var value = msg.payload;
   
   // Skab tre forskellige beskeder
   var low = { payload: value * 0.9, range: "low" };
   var mid = { payload: value, range: "normal" };
   var high = { payload: value * 1.1, range: "high" };
   
   // Send til alle tre outputs
   return [low, mid, high];
   ```

---

## 🔍 Yderligere ressourcer

- [Node-RED Documentation - Function Node](https://nodered.org/docs/user-guide/writing-functions)
- [JavaScript Basics Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [Working with Context in Node-RED](https://nodered.org/docs/user-guide/context)
