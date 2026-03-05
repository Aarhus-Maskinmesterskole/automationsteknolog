# Dag 4: Node-RED HTTP Client POST Request
## Formål
Lær at sende data fra Node-RED til en HTTP-server ved hjælp af en POST request. Dette er vigtigt for at kunne integrere Node-RED med IoT-enheder og RESTful API'er.
## Læringsmål
Efter denne opgave vil du kunne:
- Konfigurere en HTTP Request node i Node-RED til at sende POST requests.
- Formatere data korrekt i text/plain format for at sende til en HTTP-server.
- Teste dit POST-endpoint ved at sende data fra Node-RED til en HTTP-server, fx en ESP32.

## Opgavebeskrivelse
### Del A: Konfigurer HTTP POST request i Node-RED
1. **HTTP Request Node**: Træk en `http request` node ind i dit flow.
    1. Dobbeltklik på noden for at konfigurere den.
    2. Indstil metoden til `POST`.
    3. Indtast URL'en til det endpoint, du vil sende data til, fx `http://<ESP32_IP_ADDRESS>:80/api/data`.
2. **Payload**: For at sende data i text/plain format, skal du sørge for, at payloaden er en simpel tekststreng. Du kan bruge en `inject` node til at sende en tekststreng som payload, fx "Hello ESP32!".
3. **Output**: Forbind `http request` noden til en `debug` node for at se responsen i debug panelet.
4. **Inject Node**: Tilføj en `inject` node for at trigge POST requestet manuelt. Forbind den til `http request` noden.
5. **Deploy**: Klik på "Deploy" for at gemme og køre dit flow.

