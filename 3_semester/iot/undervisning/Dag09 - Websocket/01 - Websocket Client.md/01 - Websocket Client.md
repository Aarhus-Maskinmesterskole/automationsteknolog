# WebSocket Client på ESP32 med MicroPython
I denne guide vil vi oprette en simpel WebSocket-klient på en ESP32, der kører MicroPython. Vi vil forbinde til en offentlig WebSocket-server, sende en besked og modtage et svar.

Før du starter, skal du sørge for at hentet følgende biblioteker:
[uwebsockets](https://github.com/danni/uwebsockets)
```python 
import network
import time
import uwebsockets.client

# --- 1. Sæt dit Wi-Fi op ---
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_KODEORD"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

print("Forbinder til WiFi...")
while not wifi.isconnected():
    time.sleep(1)

print("Forbundet til WiFi! IP Adresse:", wifi.ifconfig()[0])

# --- 2. Forbind til WebSocket Server ---
# Vi bruger en offentlig test-server, der "ekkoer" det du sender.
WS_URL = "ws://echo.websocket.events"

try:
    print(f"Forbinder til {WS_URL} ...")
    ws = uwebsockets.client.connect(WS_URL)
    print("WebSocket forbundet!")

    # --- 3. Send og modtag data ---
    besked = "Hej fra ESP32 MicroPython!"
    print(f"Sender: {besked}")
    ws.send(besked)

    # Lyt efter svar (recv blokerer indtil der kommer en besked)
    svar = ws.recv()
    print(f"Modtog: {svar}")

except Exception as e:
    print("Der opstod en fejl:", e)

finally:
    # --- 4. Luk forbindelsen pænt ---
    if 'ws' in locals():
        ws.close()
        print("WebSocket lukket.")
```