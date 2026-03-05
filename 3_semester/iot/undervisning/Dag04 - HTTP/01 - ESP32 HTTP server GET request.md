# Dag 4: HTTP Server GET Request with ESP32
## Formål
Lær at implementere et simpelt HTTP GET-endpoint på en ESP32, som kan returnere data i JSON-format. Dette er grundlæggende for at kunne integrere IoT-enheder i et RESTful API-økosystem.

## Læringsmål
Efter denne opgave vil du kunne:
- Sætte en ESP32 op som en HTTP-server.
- Håndtere GET-forespørgsler og returnere `text/plain`.
- Teste dit endpoint med `curl` eller en webbrowser.

## Hvad er en HTTP GET request?
En HTTP GET request bruges til at anmode om data fra en server. Når en klient sender en GET request, forventer den at modtage data i form af en response. GET requests er idempotente, hvilket betyder, at de ikke ændrer serverens tilstand. De bruges typisk til at hente information, som kan være i form af tekst, JSON, HTML eller andre formater.

## Opgavebeskrivelse
### Del A: Implementer HTTP GET-endpoint på ESP32
1. **Opsætning**: Sørg for, at din ESP32 er forbundet til dit Wi-Fi-netværk.
2. **HTTP Server**: Brug ESP32's HTTPServer bibliotek til at oprette en HTTP-server.
3. **Endpoint**: Implementer et GET-endpoint, fx `/api/status`, som returnerer en simpel tekstbesked, fx "ESP32 is online!".
4. **Response**: Sørg for, at din server returnerer `Content-Type: text/plain` i headeren.

### Del B: Test dit endpoint
1. **Find IP-adresse**: Find ESP32's IP-adresse på dit netværk (typisk vist i terminalen ved opstart).
2. **Test med webbrowser**: Åbn en webbrowser og indtast ESP32's IP-adresse efterfulgt af endpointet, fx `http://<ESP32_IP_ADDRESS>:80/api/status`.
3. **Test med curl**: Brug `curl` i terminalen for at teste dit endpoint:
   ```bash
   curl http://<ESP32_IP_ADDRESS>:80/api/status
   ```
   Erstat `<ESP32_IP_ADDRESS>` med den faktiske IP-adresse på din ESP32. **OBS! Curl skal være installeret på din maskine, så derfor er det valgfrit.**
4. **Verifikation**: Du bør se den tekstbesked, du har programmeret i dit GET-endpoint, både i browseren og i terminalen.

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
    print('Connected to Wi-Fi:', wlan.ifconfig())

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

    # Simple response for GET /api/status
    if 'GET /api/status' in request:
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nESP32 is online!'
        cl.send(response.encode())
    else:
        response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\nEndpoint not found.'
        cl.send(response.encode())
    
    cl.close()
```
**Bemærk**: Husk at erstatte `your_SSID` og `your_PASSWORD` med dine faktiske Wi-Fi-oplysninger. Koden ovenfor opretter en simpel HTTP-server på ESP32, som håndterer GET-forespørgsler til `/api/status` og returnerer en tekstbesked.

### Forklaring af koden:
- **Wi-Fi Connection**: Funktionen `my_wifi` håndterer forbindelsen til Wi-Fi-netværket.
- `socket.getaddrinfo("0.0.0.0", 80)[0][-1]`: Henter adresseinformation for at binde serveren til alle tilgængelige netværksinterfaces på port 80. `[0][-1]` udtrækker den relevante del af adressen.
- `s = socket.socket()`: Opretter en TCP/IP socket.
- `s.bind(addr)`: Binder socketen til den specificerede adresse og port.
- `s.listen(1)`: Starter lytning efter indkommende forbindelser.
- `cl, _ = s.accept()`: Accepterer en indkommende forbindelse og returnerer en ny socket (`cl`) til kommunikation med klienten. `_` bruges til at ignorere klientens adresse, da den ikke er nødvendig i dette tilfælde.
- `request = cl.recv(1024).decode('utf-8')`: Modtager data fra klienten og dekoder det til en string.
- `response`: Afhængigt af forespørgslen, opbygges en HTTP-respons. Hvis forespørgslen er til `/api/status`, returneres en succesbesked. For andre forespørgsler returneres en 404-fejl. HTTP-responsen inkluderer statuslinjen, headeren for `Content-Type`, og selve beskeden i body'en.
- `cl.send(response.encode())`: Sender den kodede HTTP-respons tilbage til klienten.
- `cl.close()`: Lukker forbindelsen til klienten efter at have sendt svaret.



