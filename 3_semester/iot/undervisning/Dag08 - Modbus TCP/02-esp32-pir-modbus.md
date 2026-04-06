# Opgave 2: ESP32 + PIR som Modbus TCP server

Mål: læs bevægelse i Node-RED.

## Adresser

* Holding register `0` = `0` eller `1`

## main.py

```python
from machine import Pin
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

pir = Pin(14, Pin.IN)

mb = ModbusTCP()
mb.bind(local_ip=ip, local_port=502)
mb.setup_registers({
    "HREGS": {
        "PIR": {"register": 0, "len": 1, "val": 0},
    }
})

while True:
    mb.set_hreg(0, pir.value())
    mb.process()
    time.sleep_ms(50)
```

## Test i Node-RED

* `modbus read`
* Function = `Read Holding Registers (FC3)`
* Address = `0`
* Quantity = `1`

`0` betyder ingen bevægelse. `1` betyder bevægelse.