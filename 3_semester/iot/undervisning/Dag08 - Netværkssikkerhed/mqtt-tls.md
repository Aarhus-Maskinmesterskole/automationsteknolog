# A. Forudsætninger

* Docker Desktop installeret (Compose følger med).
* Python 3.10+ og `pip` i PATH.

---

# B. Projektstruktur

Åbn **vs code** og kør:

```bash
# 1) Lav en ren mappe
mkdir -p ~/Documents/mqtt-lab
```
# 2) I vs code add workspace folder: `~/Documents/mqtt-lab`

# 3) Undermapper
```bash
mkdir -p ~/Documents/mqtt-lab/mosquitto/config ~/Documents/mqtt-lab/mosquitto/certs ~/Documents/mqtt-lab/mosquitto/data ~/Documents/mqtt-lab/mosquitto/log ~/Documents/mqtt-lab/python
```

Strukturen bliver:

```
mqtt-lab/
  docker-compose.yml
  mosquitto/
    config/mosquitto.conf
    certs/           (certifikater)
    data/
    log/
  python/
    sub.py
    pub.py
```

---

# C. docker-compose.yml

Opret filen `docker-compose.yml` i mappen `~/Documents/mqtt-lab` med dette indhold:

```yaml
services:
  # Engangs-service til at lave certifikater i ./mosquitto/certs
  certgen:
    image: alpine:3.20
    working_dir: /work
    volumes:
      - ./mosquitto/certs:/work
    entrypoint: |
      sh -lc '
        set -e
        apk add --no-cache openssl
        # CA (beholdes genbrugeligt)
        if [ ! -f ca.crt ]; then
          openssl genrsa -out ca.key 4096
          openssl req -x509 -new -nodes -key ca.key -days 3650 -sha256 -out ca.crt -subj "/CN=Mqtt Lab CA"
        fi
        # Servercert med SAN for både docker-navn og localhost
        if [ ! -f server.crt ]; then
          openssl genrsa -out server.key 2048
          openssl req -new -key server.key -out server.csr -subj "/CN=mosquitto"
          printf "subjectAltName=DNS:mosquitto,DNS:localhost,IP:127.0.0.1\n" > san.cnf
          openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
            -out server.crt -days 825 -sha256 -extfile san.cnf
        fi
        ls -l
      '

  mosquitto:
    image: eclipse-mosquitto:2
    container_name: mosquitto
    restart: unless-stopped
    ports:
      - "8883:8883"                        # MQTT over TLS
      # - "1883:1883"                      # (valgfrit) plain MQTT: kræver listener 1883 i conf
    volumes:
      - ./mosquitto/config:/mosquitto/config
      - ./mosquitto/data:/mosquitto/data
      - ./mosquitto/log:/mosquitto/log
      - ./mosquitto/certs:/mosquitto/certs

  # Praktisk klient-container til hurtige tests
  tester:
    image: eclipse-mosquitto:2
    depends_on: [mosquitto]
    volumes:
      - ./mosquitto/certs:/certs:ro
```

---

# D. Mosquitto-konfiguration (TLS)

Opret `mosquitto\config\mosquitto.conf`:

```conf
# (Valgfrit) Hvis du også vil have 1883 uden TLS, så af-kommentér sektionen nederst og behold per_listener_settings.
per_listener_settings true

# --- TLS (8883) ---
listener 8883
protocol mqtt
cafile  /mosquitto/certs/ca.crt
certfile /mosquitto/certs/server.crt
keyfile  /mosquitto/certs/server.key
tls_version tlsv1.2
allow_anonymous false
password_file /mosquitto/config/passwd

# --- PLAIN (1883) KUN TIL LAB/TEST ---
# listener 1883
# protocol mqtt
# allow_anonymous true
```

---

# E. Lav certifikater + bruger

Kør fra `~/Documents/mqtt-lab`:


# 1) Certifikater (engangs)
docker compose run --rm certgen
* Det skal se nogenlunde sådan ud:
```bash
PS C:\Users\aso\Documents\mqtt-lab> docker compose run --rm certgen
[+] Creating 1/1
 ✔ Network mqtt-lab_default  Created                                      0.0s 
fetch https://dl-cdn.alpinelinux.org/alpine/v3.20/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.20/community/x86_64/APKINDEX.tar.gz
(1/1) Installing openssl (3.3.5-r0)
Executing busybox-1.36.1-r30.trigger
OK: 9 MiB in 15 packages
Certificate request self-signature ok
subject=CN=mosquitto
total 20
-rw-r--r--    1 root     root          1814 Oct 29 20:05 ca.crt
-rw-------    1 root     root          3272 Oct 29 20:05 ca.key
-rw-r--r--    1 root     root            41 Oct 29 20:05 ca.srl
-rw-r--r--    1 root     root            56 Oct 29 20:05 san.cnf
-rw-r--r--    1 root     root          1493 Oct 29 20:05 server.crt
-rw-r--r--    1 root     root           891 Oct 29 20:05 server.csr
-rw-------    1 root     root          1700 Oct 29 20:05 server.key
PS C:\Users\aso\Documents\mqtt-lab>
```

# 2) Opret bruger "test" med kode "hemmeligt"
docker run --rm -u root `
  -v "$PWD\mosquitto\config:/mosquitto/config" `
  eclipse-mosquitto:2 `
  sh -lc "mosquitto_passwd -b -c /mosquitto/config/passwd test 'hemmeligt' && chmod 640 /mosquitto/config/passwd && chown mosquitto:mosquitto /mosquitto/config/passwd"

# 3) Start broker
docker compose up -d mosquitto
docker compose logs -f mosquitto
```

I loggen skal du se noget ala:

```bash
[+] Running 1/1
 ✔ Container mosquitto  Started                                                           0.3s 
mosquitto  | 1761768543: mosquitto version 2.0.22 starting
mosquitto  | 1761768543: Config loaded from /mosquitto/config/mosquitto.conf.
mosquitto  | 1761768543: Opening ipv4 listen socket on port 8883.
mosquitto  | 1761768543: Opening ipv6 listen socket on port 8883.
mosquitto  | 1761768543: mosquitto version 2.0.22 running

```

---

# F. Hurtig CLI-test (fra tester-container)
Opret 2 nye terminal i vs code, og kør (husk at være i `~/Documents/mqtt-lab`):
```powershell
# SUB (i ét vindue)
docker compose run --rm tester `
  mosquitto_sub -h mosquitto -p 8883 -t test/# -u test -P 'hemmeligt' --cafile /certs/ca.crt -V mqttv5 -v

# PUB (nyt vindue)
docker compose run --rm tester `
  mosquitto_pub -h mosquitto -p 8883 -t test/hej -m "hello from docker" -u test -P 'hemmeligt' --cafile /certs/ca.crt -V mqttv5
```

Hvis SUB ser beskeden, er brokeren klar ✅

---

# G. Python-klienter (pub/sub)

## 1) Installer bibliotek

```powershell
py -m pip install paho-mqtt
```

## 2) `python\sub.py`

```python
# sub.py
import argparse, ssl, time
from paho.mqtt import client as mqtt

p = argparse.ArgumentParser()
p.add_argument("--host", default="localhost")
p.add_argument("--port", type=int, default=8883)
p.add_argument("--topic", default="test/#")
p.add_argument("--username", default="test")
p.add_argument("--password", default="hemmeligt")
p.add_argument("--cafile", default=r".\ca.crt")
p.add_argument("--tls-insecure", action="store_true")
a = p.parse_args()

c = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
                protocol=mqtt.MQTTv5)
c.username_pw_set(a.username, a.password)

if a.port == 8883:
    c.tls_set(ca_certs=a.cafile or None,
              cert_reqs=ssl.CERT_REQUIRED,
              tls_version=ssl.PROTOCOL_TLS_CLIENT)
    c.tls_insecure_set(a.tls_insecure)

def on_connect(client, userdata, flags, rc, props=None):
    print(f"[connect] rc={rc}")
    if rc == 0:
        r = client.subscribe(a.topic)
        print(f"[sub sent] mid={r[1]} topic={a.topic}")

def on_subscribe(client, userdata, mid, granted_qos, props=None):
    print(f"[suback] mid={mid} granted={granted_qos}")

def on_message(client, userdata, msg):
    ts = time.strftime("%H:%M:%S")
    try: payload = msg.payload.decode("utf-8")
    except UnicodeDecodeError: payload = repr(msg.payload)
    print(f"[{ts}] {msg.topic} | {payload}")

c.on_connect = on_connect
c.on_subscribe = on_subscribe
c.on_message = on_message

c.connect(a.host, a.port, 60)
try:
    c.loop_forever()
except KeyboardInterrupt:
    c.disconnect()
```

## 3) `python\pub.py`

```python
# pub.py
import argparse, ssl, time, threading
from paho.mqtt import client as mqtt

p = argparse.ArgumentParser()
p.add_argument("--host", default="localhost")
p.add_argument("--port", type=int, default=8883)
p.add_argument("-t","--topic", default="test/hej")
p.add_argument("-m","--message", default="Hej fra Python TLS ✓")
p.add_argument("--username", default="test")
p.add_argument("--password", default="hemmeligt")
p.add_argument("--cafile", default=r".\ca.crt")
p.add_argument("--tls-insecure", action="store_true")
a = p.parse_args()

connected = threading.Event()
rc_holder = {"rc": None}

def on_connect(c,u,f,rc,props=None):
    rc_holder["rc"] = rc
    print(f"[connect] rc={rc}")
    connected.set()

def on_disconnect(c,u,flags,rc,props=None):
    print(f"[disconnect] rc={rc}")

c = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
                protocol=mqtt.MQTTv5)
c.username_pw_set(a.username, a.password)
c.on_connect = on_connect
c.on_disconnect = on_disconnect

if a.port == 8883:
    c.tls_set(ca_certs=a.cafile or None,
              cert_reqs=ssl.CERT_REQUIRED,
              tls_version=ssl.PROTOCOL_TLS_CLIENT)
    c.tls_insecure_set(a.tls_insecure)

c.connect(a.host, a.port, 30)
c.loop_start()

if not connected.wait(5):
    raise RuntimeError("Timeout: ingen CONNACK (tjek host/port/TLS/CA).")
if rc_holder["rc"] != 0:
    raise RuntimeError(f"Broker afviste connect: rc={rc_holder['rc']}")

info = c.publish(a.topic, a.message, qos=0, retain=False)
info.wait_for_publish()
print(f"[published] {a.topic} | {a.message!r}")
c.disconnect()
c.loop_stop()
```

## 4) Kopiér CA til python-mappen (nemme stier)

```powershell
Copy-Item .\mosquitto\certs\ca.crt .\python\ca.crt -Force
```

## 5) Kør

```powershell
cd .\mqtt-lab\python\

# subscriber (TLS)
py sub.py --host localhost --port 8883 --cafile "python\ca.crt" --username test --password hemmeligt

# publisher (nyt vindue)
py pub.py  --host localhost --port 8883 --cafile "python\ca.crt" --username test --password hemmeligt -t test/hej -m "hello from python"
```

(Valgfrit) **Plain 1883**: Af-kommentér 1883-listener i `mosquitto.conf`, `docker compose restart mosquitto`, og kør:

```powershell
py sub.py --host localhost --port 1883 --cafile ""
py pub.py  --host localhost --port 1883 -t test/hej -m "plain virker"
```

## 6) Installer wireshark og se TLS-trafik
1. Start wireshark og vælg loopback-interface (eller `vEthernet (WSL)` hvis i WSL).
2. Filtrer på `mqtt` eller `tcp.port == 8883`.
![alt text](image.png)

---

# H. Lyn-fejlfinding (3 linjer)

* **“host name verification failed”**: cert mangler `DNS:mosquitto` → brug certgen ovenfor eller kør med `--tls-insecure` (kun demo).
* **“Not authorized”**: forkert bruger/kode. Genskab:

  ```powershell
  docker run --rm -u root -v "$PWD\mosquitto\config:/mosquitto/config" eclipse-mosquitto:2 `
    sh -lc "mosquitto_passwd -b /mosquitto/config/passwd test 'hemmeligt'"
  docker compose restart mosquitto
  ```
* **“connecting…”** i en klient: tjek at du forbinder til **rigtig port** (8883 med TLS/CA, 1883 uden TLS), og at Node-RED/Python bruger samme host som cert (localhost) eller at cert har `DNS:mosquitto` når du kører i Docker.
