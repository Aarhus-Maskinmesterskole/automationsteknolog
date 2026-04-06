# Opgave 4: ESP32 + DHT11 som Modbus TCP server

Mål: læs temperatur og fugtighed i Node-RED.

## Adresser

* Holding register `0` = temperatur x 10
* Holding register `1` = fugtighed x 10

## main.py

```python
from machine import Pin
import dht
import network
import time
from umodbus.tcp import ModbusTCP

SSID = "DIT_WIFI_NAVN"
PASS = "DIT_WIFI_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(SSID, PASS)
    while not wlan.isconnected():
        time.sleep_ms(200)

ip = wlan.ifconfig()[0]
print("IP:", ip)

sensor = dht.DHT11(Pin(4))

mb = ModbusTCP()
mb.bind(local_ip=ip, local_port=502)
mb.setup_registers({
    "HREGS": {
        "TEMP": {"register": 0, "len": 1, "val": 0},
        "HUM": {"register": 1, "len": 1, "val": 0},
    }
})

next_read = 0

while True:
    now = time.ticks_ms()

    if time.ticks_diff(now, next_read) >= 0:
        try:
            sensor.measure()
            mb.set_hreg(0, int(sensor.temperature() * 10))
            mb.set_hreg(1, int(sensor.humidity() * 10))
        except OSError:
            pass

        next_read = time.ticks_add(now, 2000)

    mb.process()
    time.sleep_ms(20)
```

## Test i Node-RED

* `modbus read`
* IP = ESP32 IP
* Port = `502`
* Unit ID = `1`
* Function = `Read Holding Registers (FC3)`
* Address = `0`
* Quantity = `2`

Husk at dividere værdierne med `10`.