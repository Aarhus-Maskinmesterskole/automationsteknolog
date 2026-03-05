# Dag 4: Node-RED HTTP GET Endpoint
## Formål
Lær at oprette et HTTP GET-endpoint i Node-RED, som kan modtage forespørgsler og returnere data i text/plain format. Dette er vigtigt for at kunne integrere Node-RED med IoT-enheder og RESTful API'er.

## Læringsmål
Efter denne opgave vil du kunne:
- Oprette et HTTP GET-endpoint i Node-RED.
- Returnere data i text/plain format som svar på GET-forespørgsler.
- Teste dit GET-endpoint ved at sende forespørgsler fra en webbrowser, `curl` eller en anden Node-RED HTTP request node.

## Opgavebeskrivelse
### Del A: Opret HTTP GET-endpoint i Node-RED
1. **HTTP In Node**: Træk en `http in` node ind i dit flow.
    1. Dobbeltklik på noden for at konfigurere den.
    2. Indstil metoden til `GET`.
    3. Indtast URL'en for dit endpoint, fx `/api/status`.
2. **Function Node**: Træk en `function` node ind og forbind den til `http in` noden. Dobbeltklik på `function` noden og indtast følgende kode for at returnere en tekstbesked:
    ```javascript
    msg.payload = "Node-RED GET endpoint is working!";
    msg.headers = { "Content-Type": "text/plain" };
    return msg;
    ```
3. **HTTP Response Node**: Træk en `http response` node ind og forbind den til `function` noden.
4. **Deploy**: Klik på "Deploy" for at gemme og køre dit flow.

### Del B: Test dit GET-endpoint
1. **Test med webbrowser**: Åbn en webbrowser og indtast URL'en til dit endpoint, fx `http://<NODE_RED_IP_ADDRESS>:1880/api/status`. Erstat `<NODE_RED_IP_ADDRESS>` med den faktiske IP-adresse på din Node-RED server. Du bør se den tekstbesked, du har programmeret i `function` noden.
2. **Test med curl**: Brug `curl` i terminalen for at teste dit GET-endpoint:
   ```bash
   curl http://<NODE_RED_IP_ADDRESS>:1880/api/status
   ```
   Erstat `<NODE_RED_IP_ADDRESS>` med den faktiske IP-adresse på din Node-RED server. Du bør se den tekstbesked, du har programmeret i `function` noden i terminalen. **OBS! Curl er valgfrit fordi det skal være installeret på din maskine.**
3. **Test med Node-RED HTTP Request Node**: Træk en `http request` node ind i dit flow og konfigurer den til at sende en GET request til dit endpoint, fx `http://<NODE_RED_IP_ADDRESS>:1880/api/status`. Forbind `http request` noden til en `debug` node for at se responsen i debug panelet. Klik på "Deploy" og trig derefter `http request` noden for at se resultatet.
---
