# Dag 4: ESP32 HTTP server - PUT request
I denne del af undervisningen vil vi se på, hvordan man kan håndtere PUT requests i en HTTP server på ESP32. 

## Formål
Lær at implementere et HTTP PUT-endpoint på en ESP32, som kan modtage data i text/plain format. Dette er vigtigt for at kunne opdatere data på en IoT-enhed og integrere i et RESTful API-økosystem.

## Læringsmål
Efter denne opgave vil du kunne:
- Sætte en ESP32 op som en HTTP-server, der kan håndtere PUT-forespørgsler.
- Modtage og parse data sendt i text/plain format.
- Teste dit PUT-endpoint med `curl` eller Node-RED's HTTP Request node [06 - Node-RED HTTP Client PUT request](06%20-%20Node-RED%20HTTP%20Client%20PUT%20request.md).

## Hvad er en PUT request?
En PUT request bruges til at opdatere en ressource på serveren. Det er en måde at sende data til serveren, som kan bruges til at ændre eksisterende data eller oprette nye data, hvis de ikke allerede findes.

## Opgavebeskrivelse
### Del A: Implementer HTTP PUT-endpoint på ESP32
1. **Opsætning**: Sørg for, at din ESP32 er forbundet til dit Wi-Fi-netværk.
2. **HTTP Server**: Brug ESP32's HTTPServer bibliotek til at oprette en HTTP-server.
3. **Endpoint**: Implementer et PUT-endpoint, fx `/api/update`, som kan modtage data i text/plain format og gemme det i en variabel.
4. **Response**: Sørg for, at din server returnerer `Content-Type: text/plain` i headeren og en bekræftelsesbesked, fx "Data updated!".
### Del B: Test dit endpoint
1. **Find IP-adresse**: Find ESP32's IP-adresse på dit netværk (typisk vist i terminalen ved opstart).
2. **Test med curl**: Brug `curl` i terminalen for at teste dit PUT-endpoint:
   ```bash
   curl -X PUT -d "Updated data for ESP32!" http://<ESP32_IP_ADDRESS>:80/api/update
   ```
   Erstat `<ESP32_IP_ADDRESS>` med den faktiske IP-adresse på din ESP32. **OBS! Curl skal være installeret på din maskine, så derfor er det valgfrit.**
3. **Verifikation**: Du bør se bekræftelsesbeskeden, du har programmeret i dit PUT-endpoint, i terminalen. Du kan også udskrive den modtagne data i ESP32's terminal for at bekræfte, at den er korrekt modtaget.
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
    # Check if it's a PUT request to /api/update
    if 'PUT /api/update' in request:
        # Extract the data from the request body
        data = request.split('\r\n\r\n')[1]  # Get the body after the headers
        print('Received data:', data)
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nData updated!'
    else:
        response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\nEndpoint not found.'
    cl.send(response.encode('utf-8'))
    cl.close()
```
### Forklaring af koden
- Koden starter med at importere nødvendige biblioteker for Wi-Fi og socket-programmering.
- Funktionen `my_wifi` håndterer forbindelsen til Wi-Fi-netværket.
- HTTP-serveren oprettes og lytter på port 80 for indkommende forbindelser.
- Når en klient forbinder, modtages og dekodes HTTP-forespørgslen.
- Hvis forespørgslen er en PUT til `/api/update`, udtrækkes dataen fra body'en, og en bekræftelsesbesked sendes tilbage.
- Hvis endpointet ikke findes, returneres en 404 Not Found besked.

**Bemærk**: Husk at erstatte `your_SSID` og `your_PASSWORD` med dine faktiske Wi-Fi-oplysninger. Koden ovenfor opretter en simpel HTTP-server på ESP32, som håndterer PUT-forespørgsler til `/api/update` og returnerer en tekstbesked.

