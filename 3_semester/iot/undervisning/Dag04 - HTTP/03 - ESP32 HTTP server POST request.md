# Dag 4: HTTP Server POST Request with ESP32
## Formål
Lær at implementere et HTTP POST-endpoint på en ESP32, som kan modtage data i text/plain format. Dette er vigtigt for at kunne sende data fra en klient (fx Node-RED) til en IoT-enhed og integrere i et RESTful API-økosystem.
## Læringsmål
Efter denne opgave vil du kunne:
- Sætte en ESP32 op som en HTTP-server, der kan håndtere POST-forespørgsler.
- Modtage og parse data sendt i text/plain format.
- Teste dit POST-endpoint med `curl` eller Node-RED's HTTP Request node [04 - Node-RED HTTP Client POST request](04%20-%20Node-RED%20HTTP%20Client%20POST%20request.md).

## Hvad er en HTTP POST request?
En HTTP POST request bruges til at sende data til en server for at oprette eller opdatere en ressource. Når en klient sender en POST request, indeholder den data i body'en af forespørgslen, som serveren kan bruge til at udføre en handling, såsom at gemme data eller opdatere eksisterende information. 

## Opgavebeskrivelse
### Del A: Implementer HTTP POST-endpoint på ESP32
1. **Opsætning**: Sørg for, at din ESP32 er forbundet til dit Wi-Fi-netværk.
2. **HTTP Server**: Brug ESP32's HTTPServer bibliotek til at oprette en HTTP-server.
3. **Endpoint**: Implementer et POST-endpoint, fx `/api/data`, som kan modtage data i text/plain format og gemme det i en variabel.
4. **Response**: Sørg for, at din server returnerer `Content-Type: text/plain` i headeren og en bekræftelsesbesked, fx "Data received!".
### Del B: Test dit endpoint
1. **Find IP-adresse**: Find ESP32's IP-adresse på dit netværk (typisk vist i terminalen ved opstart).
2. **Test med curl**: Brug `curl` i terminalen for at teste dit POST-endpoint:
   ```bash
   curl -X POST -d "Hello ESP32!" http://<ESP32_IP_ADDRESS>:80/api/data
   ```
   Erstat `<ESP32_IP_ADDRESS>` med den faktiske IP-adresse på din ESP32. **OBS! Curl skal være installeret på din maskine, så derfor er det valgfrit.**
3. **Verifikation**: Du bør se bekræftelsesbeskeden, du har programmeret i dit POST-endpoint, i terminalen. Du kan også udskrive den modtagne data i ESP32's terminal for at bekræfte, at den er korrekt modtaget.
---
## Eksempel på kode (Micropython)
```python
import network # For Wi-Fi connection
import socket # For creating the HTTP server
# Connect to Wi-Fi
ssid = 'your_SSID'
password = 'your_PASSWORD'
def my_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print('Connected to Wi-Fi:', wlan.ifconfig()[0])
my_wifi(ssid, password)
# Create HTTP server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('Listening on', addr)
while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024).decode('utf-8')
    print('Request:', request)
    # Check if it's a POST request to /api/data
    if 'POST /api/data' in request:
        # Extract the data from the request body
        data = request.split('\r\n\r\n')[1]  # Get the body after the headers
        print('Received data:', data)
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nData received!'
    else:
        response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\nEndpoint not found.'
    cl.send(response.encode('utf-8'))
    cl.close()
```

### Forklaring af koden
- Koden starter med at importere nødvendige biblioteker for Wi-Fi og socket-programmering.
- Funktionen `my_wifi` håndterer forbindelsen til Wi-Fi-netværket.
- HTTP-serveren oprettes ved at binde en socket til port 80 og lytte efter indkommende forbindelser.
- Når en klient forbinder, modtages og dekodes HTTP-forespørgslen.
- Hvis forespørgslen er en POST til `/api/data`, udtrækkes dataen fra body'en, og en bekræftelsesbesked sendes tilbage.
- Hvis endpointet ikke findes, returneres en 404-fejl.
- `data = request.split('\r\n\r\n')[1]` bruges til at adskille HTTP-headeren fra body'en, hvor dataen er placeret.

**Bemærk**: Husk at erstatte `your_SSID` og `your_PASSWORD` med dine faktiske Wi-Fi-oplysninger. Koden ovenfor opretter en simpel HTTP-server på ESP32, som håndterer POST-forespørgsler til `/api/data` og returnerer en bekræftelsesbesked.
