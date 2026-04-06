import time

import paho.mqtt.client as mqtt
import snap7
from snap7.util import set_int

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "aams/plc_bridge/setpoint"

PLC_IP = "192.168.0.11"
PLC_RACK = 0
PLC_SLOT = 1
PLC_TCP_PORT = 102

DB_NUMBER = 1
SETPOINT_OFFSET = 2

MQTT_SETPOINT = 0

plc = snap7.client.Client()
plc.connect(PLC_IP, PLC_RACK, PLC_SLOT, tcp_port=PLC_TCP_PORT)

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    global MQTT_SETPOINT
    MQTT_SETPOINT = int(msg.payload.decode().strip())
    print(f"Setpoint from MQTT: {MQTT_SETPOINT}")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

while True:
    # 1. Read input from MQTT
    client.loop(timeout=0.01)

    # 2. Run the program
    setpoint = MQTT_SETPOINT

    # 3. Update output to PLC
    raw_data = bytearray(2)
    set_int(raw_data, 0, setpoint)
    plc.db_write(DB_NUMBER, SETPOINT_OFFSET, raw_data)

    time.sleep(0.1)