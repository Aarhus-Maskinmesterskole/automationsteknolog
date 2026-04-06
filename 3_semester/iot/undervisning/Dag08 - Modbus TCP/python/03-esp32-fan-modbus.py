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

fan_a = Pin(18, Pin.OUT, value=0)
fan_b = Pin(19, Pin.OUT, value=0)

def coil_set_cb(reg_type, address, val):
    if address == 0:
        state = bool(val[0]) if isinstance(val, list) else bool(val)
        if state:
            fan_a.value(1)
            fan_b.value(0)
        else:
            fan_a.value(0)
            fan_b.value(0)

mb = ModbusTCP()
mb.bind(local_ip=ip, local_port=502)
mb.setup_registers({
    "COILS": {
        "FAN": {"register": 0, "len": 1, "val": 0, "on_set_cb": coil_set_cb},
    }
})

while True:
    mb.process()
    time.sleep_ms(10)