# Dag 5: ESP32 HTTP Server PUT Request Actuator Data
I denne del af undervisningen vil vi se på, hvordan man kan håndtere PUT requests i en HTTP server på ESP32 for at opdatere data relateret til aktuatorer.
## Læringsmål
Efter denne opgave vil du kunne:
- Sætte en ESP32 op som en HTTP-server.
- Håndtere PUT-forespørgsler og opdatere aktuator data.
- Teste dit endpoint med `curl` eller en webbrowser eller Node-RED.

## Opgavebeskrivelse
Du skal implementere et HTTP PUT-endpoint på din ESP32, som kan modtage data for at opdatere tilstanden af dine aktuatorer. Dataen skal sendes i plain/text format, og du skal kunne teste dit endpoint ved at sende en PUT request fra Node-RED, en webbrowser eller `curl`.

**Hint**: Du har allerede arbejdet med sensorerne i tidligere opgaver se evt. 
- [Fan control](03-esp32-fan-control.md)
- [Window control](05-esp32-window-servo.md)
- [Door control](06-esp32-door-servo.md)
- [LED control](07-esp32-yellow-led.md)
- [RGB LED control](08-esp32-rgb-led.md)
