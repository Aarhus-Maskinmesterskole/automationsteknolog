# Opgave 7: ESP32 + dør-servo som Modbus TCP server

Mål: åbn og luk servoen fra Node-RED.

## Adresser

* Coil `0` = lukket/åben

## main.py

```python
from machine import Pin, PWM
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

servo = PWM(Pin(13), freq=50)

def set_angle(angle):
    duty = int(26 + (angle / 180) * 102)
    servo.duty(duty)

def coil_set_cb(reg_type, address, val):
    if address == 0:
    state = bool(val[0]) if isinstance(val, list) else bool(val)
    set_angle(90 if state else 0)

set_angle(0)

mb = ModbusTCP()
mb.bind(local_ip=ip, local_port=502)
mb.setup_registers({
    "COILS": {
        "DOOR": {"register": 0, "len": 1, "val": 0, "on_set_cb": coil_set_cb},
    }
})

while True:
    mb.process()
    time.sleep_ms(10)
```

## Test i Node-RED

* `modbus write`
* Function = `Coil (FC5)`
* Address = `0`
* Payload = `true` eller `false`

`true` åbner servoen. `false` lukker den.