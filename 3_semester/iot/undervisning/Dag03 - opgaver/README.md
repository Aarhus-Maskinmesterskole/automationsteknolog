# Python scripts for Keystudio ESP32 IoT smart house project.

## Publish data from ESP32 to MQTT Broker
```python
# main.py — ESP32 + DHT11 → MQTT (simpel Wi-Fi)
import time, network
from machine import Pin, unique_id
import dht
from umqtt.simple import MQTTClient

# ==== KONFIG ====
WIFI_SSID = "your_wifi_ssid"
WIFI_PASSWORD = "your_wifi_password"

# ==== MQTT KONFIG ====
MQTT_BROKER = "test.mosquitto.org"
TOPIC = b"esp32/temperature"
PUBLISH_INTERVAL = 10  # sekunder

#==== DHT11 KONFIG ====
DHT_PIN = 4
sensor = dht.DHT11(Pin(DHT_PIN))


# ==== SUPER SIMPEL WIFI ====
def wifi_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        # Vent til vi har IP — helt simpelt, ingen timeouts
        while not wlan.isconnected():
            time.sleep(0.3)
    print("Wi-Fi:", wlan.ifconfig())
    time.sleep(5)
    return wlan

def mqtt_client():
    cid = b"esp32-" + ubinascii.hexlify(unique_id())
    return MQTTClient(cid, MQTT_BROKER)

def publish_dht(client, sensor):
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    payload = ('{"temperature": %d, "humidity": %d}' % (t, h)).encode()
    client.publish(TOPIC, payload)
    print("PUB", TOPIC, payload)

def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    data = {
        "temperature": sensor.temperature(),
        "humidity": sensor.humidity()
    }
    client = mqtt_client()
    client.connect()
    print("MQTT: connected")

    while True:
        publish_dht(client, sensor)
        time.sleep(PUBLISH_INTERVAL)

if __name__ == "__main__":
    main()
```

```python
# motion_sensor.py — ESP32 + PIR bevægelsessensor → MQTT
import time, network
from machine import Pin, unique_id
import ubinascii
from umqtt.simple import MQTTClient

# ==== KONFIG ====
WIFI_SSID = "your_wifi_ssid"
WIFI_PASSWORD = "your_wifi_password"

# ==== MQTT KONFIG ====
MQTT_BROKER = "test.mosquitto.org"
TOPIC = b"esp32/motion"
PIR_PIN = 14  # GPIO14 til PIR sensor (HC-SR501 o.l.)

# ==== WIFI ====
def wifi_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(0.3)
    print("Wi-Fi:", wlan.ifconfig())
    return wlan

# ==== MQTT CLIENT ====
def mqtt_client():
    cid = b"esp32-motion-" + ubinascii.hexlify(unique_id())
    return MQTTClient(cid, MQTT_BROKER)

def publish_motion(client, state):
    payload = b"1" if state else b"0"
    client.publish(TOPIC, payload, retain=True)  # retain så seneste tilstand er tilgængelig
    print("PUB", TOPIC, payload)

def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    pir = Pin(PIR_PIN, Pin.IN)  # hvis din PIR kræver pull-down: Pin.IN, Pin.PULL_DOWN
    client = mqtt_client()
    client.connect()
    print("MQTT: connected")

    last_state = pir.value()
    publish_motion(client, last_state)

    while True:
        current_state = pir.value()
        if current_state != last_state:
            publish_motion(client, current_state)
            last_state = current_state
        time.sleep(0.2)

if __name__ == "__main__":
    main()
```

## Subscribe to MQTT topics and control Fan
```python
# digital fan pin 18 and 19
# esp32_fan_control.py — enkel MQTT-styring af blæser med to pins (IN1/IN2)
import network, time
from machine import Pin
from umqtt.simple import MQTTClient

# ==== KONFIG ====
WIFI_SSID = "your_wifi_ssid"
WIFI_PASSWORD = "your_wifi_password"

MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC_FAN = b"esp32/fan_control"   # bytes!
CLIENT_ID = b"esp32_fan_controller"     # bytes!

# ==== BLÆSER-PINS (H-bro eller driver med IN1/IN2) ====
fan_pin1 = Pin(18, Pin.OUT, value=0)  # IN1
fan_pin2 = Pin(19, Pin.OUT, value=0)  # IN2

def fan_off():
    fan_pin1.value(0)
    fan_pin2.value(0)

def fan_on_forward():
    # typisk ON: IN1=1, IN2=0 (tilpas til din driver)
    fan_pin1.value(1)
    fan_pin2.value(0)

# ==== Wi-Fi ====
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        print("Connecting to WiFi...", end="")
        while not wlan.isconnected():
            print(".", end="")
            time.sleep(0.5)
        print()
    print("Connected. IP:", wlan.ifconfig()[0])

# ==== MQTT ====
_last_cmd = None  # deles mellem callback og main-loop

def mqtt_callback(topic, msg):
    # topic og msg er bytes
    global _last_cmd
    try:
        cmd = msg.decode().strip().upper()
    except:
        cmd = ""
    print("MQTT:", topic, msg)
    _last_cmd = cmd  # gem kommando til main-loop

def main():
    connect_to_wifi()

    client = MQTTClient(CLIENT_ID, MQTT_BROKER)
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(MQTT_TOPIC_FAN)
    print("MQTT subscribed to", MQTT_TOPIC_FAN)

    fan_off()
    print("Fan OFF (initial)")

    # Event-loop: hent beskeder og udfør sidste kommando
    last_applied = None
    while True:
        # check_msg() returnerer straks; callback kører ved ny besked
        try:
            client.check_msg()
        except Exception as e:
            print("MQTT error:", e)
            # ultra-simpel genforbindelse
            try:
                client.disconnect()
            except:
                pass
            time.sleep(2)
            client.connect()
            client.subscribe(MQTT_TOPIC_FAN)

        # udfør ny kommando hvis den har ændret sig
        if _last_cmd != last_applied:
            if _last_cmd == "ON":
                fan_on_forward()
                print("Fan ON")
                last_applied = _last_cmd
            elif _last_cmd == "OFF":
                fan_off()
                print("Fan OFF")
                last_applied = _last_cmd

        time.sleep(0.1)

if __name__ == "__main__":
    main()
```