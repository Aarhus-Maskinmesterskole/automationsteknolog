# 📝 Øvelse: Forbind ESP32 og Node-RED via WebSockets

Nu skal vi binde det hele sammen! Du har fået et eksempel på, hvordan en ESP32 kan køre en WebSocket server (`01 - ESP32 Websocket Server.md`), og en basal guide til at modtage data i Node-RED (`02 - Node-red Websocket Client.md`).

Din opgave er at få de to systemer til at "snakke sammen" i praksis.

## 🎯 Mål med opgaven
Når du er færdig med opgaven, skal din Node-RED installation kunne hente og vise live "sensor"-data fra din ESP32, helt uden at ESP32'en kører en regulær webserver for din browser. Al kommunikation skal ske i baggrunden over WebSockets med JSON.

## 🛠️ Trinvise opgaver

### 1. Få WebSocket Serveren op at køre (ESP32)
* Kopier koden fra `01 - ESP32 Websocket Server.md` ind i dit udviklingsmiljø (f.eks. Thonny).
* Ret `WIFI_SSID` og `WIFI_PASSWORD` så de passer til dit netværk.
* Kør koden og notér den IP-adresse, som ESP'en udskriver i konsollen.
* **Test:** Sikr dig at den virker, ved at åbne din browser på den angivne IP-adresse og trykke på knappen for at hente data. Serveren virker, hvis du får temperatur og fugtighed vist på skærmen. 

*(Hvis du ikke kan tilgå den, og I bruger eduroam/enterprise netværk på skolen, skal du evt. bruge din mobil som hotspot)*.

### 2. Opsæt WebSocket Klienten i Node-RED
* Åbn din Node-RED (ofte på `http://localhost:1880`).
* Træk en `websocket in` node og en `debug` node ind i dit flow.
* Forbind dem sammen (`websocket in` -> `debug`).
* Dobbeltklik på din `websocket in` node.
  * Sæt type til **"Connect to"**.
  * Ved siden af feltet "URL", klik på den lille knap med blyanten for at tilføje en ny WebSocket-forbindelse.
  * Indtast URL'en til din ESP32. Den skal se sådan her ud: `ws://<DIN_ESP_IP>/ws` (f.eks. `ws://192.168.1.150/ws`).
  * Gem det hele (Deploy).

### 3. Send styre-kommandoer til ESP'en fra Node-RED
I øjeblikket lytter Node-RED blot, men ESP32-koden vi bruger, sender kun data, når den *bliver bedt om det* via en specifik JSON kommando.

* Træk en `inject` node ind i Node-RED (også kendt som en "timestamp" node, men vi vil bruge den som en fysisk knap).
* Træk en `websocket out` node ind på skærmen. 
* Dobbeltklik på `websocket out` noden, og vælg den samme forbindelse/URL, som du oprettede i trin 2.
* Forbind `inject` noden til `websocket out` noden.
* Dobbeltklik på din `inject` node:
  * Ændr "msg.payload" fra `timestamp` til `JSON`.
  * Skriv følgende i JSON feltet: `{"command": "get_status"}`
  * Gem (Deploy).

### 4. Test det hele!
* Se på Node-RED's debug vindue i højre side.
* Tryk på knappen på din `inject` node.
* Du bør nu se JSON data fra ESP32'en poppe op i Node-RED (f.eks. `{"temp": 23, "fugt": 55, "maskinstatus": "RUNNING"}`).

## 🧠 Udfordring / Ekstra opgave 
Lige nu er Node-RED nødt til at trykke på en knap manuelt hver gang den vil have en opdatering.

1. Kan du få Node-RED til **konstant/automatisk** at bede om en opdatering hvert 5. sekund? (Tip: kig i opsætningen for din `inject` node under "Repeat").
2. Hvordan kan du splitte den rå JSON-besked op i Node-RED, så du sender temperaturen ud i én debug-node, og fugtigheden ud i en anden? (Tip: prøv at bruge en `json` node og derefter en `change` node eller en `function` node i Node-RED).