import time

import paho.mqtt.client as mqtt
import snap7
from snap7.util import get_bool

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "aams/plc_bridge/start_signal"

PLC_IP = "192.168.0.10"
PLC_RACK = 0
PLC_SLOT = 1
PLC_TCP_PORT = 102

DB_NUMBER = 1
BYTE_OFFSET = 0
BIT_OFFSET = 0
POLL_INTERVAL = 0.2


def read_bool_from_plc(plc_client):
    raw_data = plc_client.db_read(DB_NUMBER, BYTE_OFFSET, 1)
    return get_bool(raw_data, 0, BIT_OFFSET)


def main():
    plc_client = snap7.client.Client()
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    plc_client.connect(PLC_IP, PLC_RACK, PLC_SLOT, tcp_port=PLC_TCP_PORT)
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()

    last_value = None

    print("Snap7 MQTT publisher started")
    print(f"Reading PLC at {PLC_IP} DB{DB_NUMBER}.DBX{BYTE_OFFSET}.{BIT_OFFSET}")
    print(f"Publishing to topic '{MQTT_TOPIC}'")

    try:
        while True:
            current_value = read_bool_from_plc(plc_client)

            if current_value != last_value:
                payload = "1" if current_value else "0"
                message_info = mqtt_client.publish(MQTT_TOPIC, payload, qos=1)

                if message_info.rc == mqtt.MQTT_ERR_SUCCESS:
                    message_info.wait_for_publish(timeout=5)
                    print(f"Published {payload} to '{MQTT_TOPIC}'")
                    last_value = current_value
                else:
                    error_message = mqtt.error_string(message_info.rc)
                    print(f"Publish failed: {error_message}")

            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print("Publisher stopped")
    finally:
        mqtt_client.disconnect()
        mqtt_client.loop_stop()
        plc_client.disconnect()
        plc_client.destroy()


if __name__ == "__main__":
    main()