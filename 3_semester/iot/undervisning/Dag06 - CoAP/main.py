# main.py — minimal demo med coapmini
import urandom
import network
import time
from coapmini import CoapServer, CF_JSON

# 1) Wi-Fi Connection
SSID = "YOUR_SSID"
PASSWORD  = "YOUR_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
print("Forbinder til WiFi...")
while not wlan.isconnected():
    time.sleep(0.5)
ip = wlan.ifconfig()[0]
print(f"WiFi forbundet: {ip}")

# 2) Demo-model (random walk)
def rnd(): 
    return urandom.getrandbits(16)/65535

temp, hum = 22.5, 45.0

def dht_sim():
    global temp, hum
    temp += (rnd()-0.5)*0.4
    hum  += (rnd()-0.5)*1.2
    temp = min(max(temp,18.0),30.0)
    hum  = min(max(hum,25.0),70.0)
    return {"sensor":"DHT22(sim)",
            "temperature":round(temp,2),
            "humidity":round(hum,2),
            "unit":"C/%"}

# 3) CoAP-server + routing
srv = CoapServer(port=5683, verbose=True, send_404=True)
srv.add("/dht", dht_sim, rt="sensor.temperature", iface="sensor", ct=CF_JSON)
srv.serve_forever(f"READY → GET coap://{ip}:5683/dht (eller /.well-known/core)")
