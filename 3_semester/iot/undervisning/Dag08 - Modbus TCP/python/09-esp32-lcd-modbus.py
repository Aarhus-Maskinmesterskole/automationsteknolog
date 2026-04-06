from machine import Pin, I2C
from i2c_lcd import I2cLcd
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

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.clear()
lcd.putstr("Venter")

def coil_set_cb(reg_type, address, val):
    if address == 0:
        lcd.clear()
        state = bool(val[0]) if isinstance(val, list) else bool(val)
        if state:
            lcd.putstr("HELLO")
            lcd.move_to(0, 1)
            lcd.putstr("Modbus")
        else:
            lcd.putstr("STOP")
            lcd.move_to(0, 1)
            lcd.putstr("Modbus")

mb = ModbusTCP()
mb.bind(local_ip=ip, local_port=502)
mb.setup_registers({
    "COILS": {
        "LCD_MSG": {"register": 0, "len": 1, "val": 0, "on_set_cb": coil_set_cb},
    }
})

while True:
    mb.process()
    time.sleep_ms(10)