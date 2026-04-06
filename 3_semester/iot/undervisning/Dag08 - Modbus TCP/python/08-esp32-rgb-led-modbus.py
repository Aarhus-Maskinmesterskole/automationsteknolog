from machine import Pin
import neopixel
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

rgb = neopixel.NeoPixel(Pin(26), 4)
state = [0, 0, 0, 0]

def show_color():
    rgb[0] = (255, 0, 0) if state[0] else (0, 0, 0)
    rgb[1] = (0, 255, 0) if state[1] else (0, 0, 0)
    rgb[2] = (0, 0, 255) if state[2] else (0, 0, 0)
    rgb[3] = (255, 255, 255) if state[3] else (0, 0, 0)
    rgb.write()

def coil_set_cb(reg_type, address, val):
    if 0 <= address <= 3:
        state[address] = 1 if (bool(val[0]) if isinstance(val, list) else bool(val)) else 0
        show_color()

show_color()

mb = ModbusTCP()
mb.bind(local_ip=ip, local_port=502)
mb.setup_registers({
    "COILS": {
        "RED": {"register": 0, "len": 1, "val": 0, "on_set_cb": coil_set_cb},
        "GREEN": {"register": 1, "len": 1, "val": 0, "on_set_cb": coil_set_cb},
        "BLUE": {"register": 2, "len": 1, "val": 0, "on_set_cb": coil_set_cb},
        "WHITE": {"register": 3, "len": 1, "val": 0, "on_set_cb": coil_set_cb},
    }
})

while True:
    mb.process()
    time.sleep_ms(10)