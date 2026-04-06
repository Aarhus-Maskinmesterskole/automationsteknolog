# Opgave 5: ESP32 + knap som Modbus TCP server

Mål: læs knapstatus og antal tryk i Node-RED.

## Adresser

* Coil `0` = knapstatus (`false` eller `true`)
* Holding register `1` = antal tryk

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

button = Pin(16, Pin.IN, Pin.PULL_UP)

mb = ModbusTCP()
mb.bind(local_ip=ip, local_port=502)
mb.setup_registers({
    "COILS": {
        "BUTTON": {"register": 0, "len": 1, "val": False},
    },
    "HREGS": {
        "COUNT": {"register": 1, "len": 1, "val": 0},
    }
})

count = 0
last_raw = button.value()
last_press = 0

while True:
    raw = button.value()
    pressed = (raw == 0)
    now = time.ticks_ms()

    mb.set_coil(0, pressed)

    if last_raw == 1 and raw == 0 and time.ticks_diff(now, last_press) > 200:
        count += 1
        mb.set_hreg(1, count)
        last_press = now

    last_raw = raw
    mb.process()
    time.sleep_ms(20)
```

## Test i Node-RED

* `modbus read`
* Function = `Read Coils (FC1)`
* Address = `0`
* Quantity = `1`

Til tælleren:

* `modbus read`
* Function = `Read Holding Registers (FC3)`
* Address = `1`
* Quantity = `1`

Coil `0` viser om knappen er trykket. Holding register `1` tæller tryk.