# Dag 5: ESP32 HTTP Server GET Request Sensor Data
## Formål
Lær at implementere et HTTP GET-endpoint på en ESP32, som kan returnere sensor data i text/plain format. Dette er vigtigt for at kunne integrere IoT-enheder i et RESTful API-økosystem.
## Læringsmål
Efter denne opgave vil du kunne:
- Sætte en ESP32 op som en HTTP-server.
- Håndtere GET-forespørgsler og returnere sensor data i text/plain format.
- Teste dit endpoint med `curl` eller en webbrowser.

## Opgavebeskrivelse
Du skal implementere et HTTP GET-endpoint på din ESP32, som returnerer data fra alle sensorer, du har tilsluttet din ESP32 keystudio Smart House. Dataen skal returneres i text/plain format, og du skal kunne teste dit endpoint ved at sende en GET request fra Node-RED eller en webbrowser.

**Hint!**: Du har tidligere arbejdet med disse sensorer i tidligere opgaver, så du kan genbruge noget af den kode, du allerede har skrevet for at hente data fra sensorerne. Se evt.

- [Dht sensor](01-esp32-dht11.md)
- [PIR sensor](02-esp32-pir-sensor.md)
- [Button](04-esp32-button.md)