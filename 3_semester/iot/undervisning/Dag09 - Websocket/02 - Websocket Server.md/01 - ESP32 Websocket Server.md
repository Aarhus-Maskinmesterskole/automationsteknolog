# WebSocket Server på ESP32 med MicroPython

```python
import network
import time
import uasyncio as asyncio
import ujson as json
import random # Bare til at lave fake sensordata
from microdot import Microdot
from microdot_websocket import with_websocket

# --- 1. Sæt dit Wi-Fi op ---
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_KODEORD"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

print("Forbinder til WiFi...")
while not wifi.isconnected():
    time.sleep(1)

ip_adresse = wifi.ifconfig()[0]
print(f"Forbundet! Gå til http://{ip_adresse} i din browser")

app = Microdot()

# En simpel webside til at demonstrere JSON via WebSockets
HTML_SIDE = """<!DOCTYPE html>
<html>
<head><title>JSON WebSocket</title></head>
<body>
    <h1>Sensordata Live Dashboard</h1>
    <button onclick="hentData()">Hent sensordata nu (som JSON)</button>
    <div id="data-visning" style="margin-top: 20px; font-size: 20px;"></div>

    <script>
        var ws = new WebSocket('ws://' + location.host + '/ws');
        
        ws.onopen = function() {
            console.log("Forbundet til ESP!");
        };
        
        ws.onmessage = function(event) {
            // event.data indeholder den rå tekst-streng fra ESP'en.
            // Vi parser den tekst til et rigtigt JavaScript JSON objekt.
            var indgaaendeData = JSON.parse(event.data);
            
            // Nu kan vi trække de enkelte værdier ud
            document.getElementById('data-visning').innerHTML = 
                "Temperatur: " + indgaaendeData.temp + " °C <br>" +
                "Luftfugtighed: " + indgaaendeData.fugt + " % <br>" +
                "Status: " + indgaaendeData.maskinstatus;
        };
        
        function hentData() {
            // Vi formaterer også det vi sender som JSON
            var forespoergsel = { command: "get_status" };
            ws.send(JSON.stringify(forespoergsel));
        }
    </script>
</body>
</html>
"""

@app.route('/')
async def index(request):
    return HTML_SIDE, 200, {'Content-Type': 'text/html'}

@app.route('/ws')
@with_websocket
async def websocket_handler(request, ws):
    print("Klient forbundet!")
    try:
        while True:
            # 1. Modtag rå tekst (JSON-streng) fra browseren
            indgaaende_tekst = await ws.receive()
            
            # 2. Lav (parse) den om til et rigtigt Python dictionary (Dictionary)
            try:
                modtaget_data = json.loads(indgaaende_tekst)
                print("Modtog JSON command:", modtaget_data)
                
                # 3. Hvis klienten beder om status, laver vi vores udgående data-objekt
                if modtaget_data.get("command") == "get_status":
                    
                    svar_data = {
                        "temp": random.randint(20, 25), # Fake sensortemp
                        "fugt": random.randint(40, 60), 
                        "maskinstatus": "RUNNING"
                    }
                    
                    # 4. JSON-koder/pakker vores dictionary tilbage til tekst-streng
                    json_streng = json.dumps(svar_data)
                    
                    # 5. Send det ned via WebSocket (WebSockets sender altid som tekst/bytes)
                    await ws.send(json_streng)
                    
            except ValueError:
                # Hvis klienten sendte noget, der ikke var gyldigt JSON
                print("Fejl: Modtaget data var ikke gyldigt JSON:", indgaaende_tekst)

    except Exception as e:
        print("WebSocket lukket/fejl:", e)

app.run(port=80, debug=True)
```