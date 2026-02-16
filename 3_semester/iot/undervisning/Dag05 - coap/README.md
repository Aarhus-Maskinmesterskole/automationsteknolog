# coapmini (MicroPython)

Lightweight CoAP GET-server til ESP32. Minimal overflade, indbygget discovery (`/.well-known/core`), nul eksterne afhængigheder. Designet til hurtig time-to-value i undervisning.

## Installér biblioteket på enheden

1. Kopiér **`coapmini.py`** til roden af ESP32-filsystemet (samme sted som `main.py`).
2. Verificér at filen ligger der (fil-liste skal vise `coapmini.py`).

> Done. Klar til brug i alle nye projekter.

---

## Quickstart (nyt projekt)

Opret **`main.py`**:

```python
# main.py — minimal demo med coapmini
import urandom
from coapmini import wifi_connect, CoapServer, CF_JSON

# 1) Wi-Fi
SSID = "YOUR_SSID"
PSK  = "YOUR_PASSWORD"
wifi_connect(SSID, PSK, verbose=True)

# 2) Demo-model (random walk)
def rnd(): return urandom.getrandbits(16)/65535
temp, hum = 22.5, 45.0
def dht_sim():
    global temp, hum
    temp += (rnd()-0.5)*0.4
    hum  += (rnd()-0.5)*1.2
    temp = min(max(temp,18.0),30.0)
    hum  = min(max(hum,25.0),70.0)
    return {"sensor":"DHT22(sim)","temperature":round(temp,2),"humidity":round(hum,2),"unit":"C/%"}

# 3) CoAP-server + routing
srv = CoapServer(port=5683, verbose=True, send_404=True)
srv.add("/dht", dht_sim, rt="sensor.temperature", iface="sensor", ct=CF_JSON)
srv.serve_forever("READY → GET /.well-known/core eller /dht")
```

**coapmini.py**
- Opret en fil i esp32 og kald den coapmini.py
- kopir indholdet ind i filen
  
```python
# coapmini.py — MicroPython mini-CoAP lib (GET + routing + discovery)
# Mål: generisk, undervisningsklar, ingen eksterne deps.
import time, socket, json

try:
    import network
except:
    network = None  # gør lib'et brugbart også uden Wi-Fi (fx sim/test)

# ── Wi-Fi helper (valgfri) ────────────────────────────────────────────────────
def wifi_connect(ssid, psk, *, retries=10, connect_window_ms=7000, verbose=True):
    """Simple robust Wi-Fi connect. Kan udelades hvis man selv styrer netværk."""
    if network is None:
        raise RuntimeError("network-modul ikke tilgængeligt (ikke MicroPython?).")
    wlan = network.WLAN(network.STA_IF)
    # defensiv radio-reset
    try:
        wlan.active(False); time.sleep(0.2)
    except: pass

    backoff = 0.5
    for attempt in range(retries):
        try:
            wlan.active(True); time.sleep(0.2)
            if not wlan.isconnected():
                if verbose: print("Wi-Fi: forbinder …", end="")
                wlan.connect(ssid, psk)
                t0 = time.ticks_ms(); dots = 0
                while not wlan.isconnected() and time.ticks_diff(time.ticks_ms(), t0) < connect_window_ms:
                    time.sleep(0.3); dots += 1
                    if verbose: print(".", end="")
                    if dots % 40 == 0 and verbose: print("\nWi-Fi: forbinder …", end="")
            if wlan.isconnected():
                if verbose:
                    try:
                        print("\nWi-Fi: forbundet", wlan.ifconfig()[0])
                    except:
                        print("\nWi-Fi: forbundet")
                return wlan
        except OSError as e:
            if verbose: print("\nWi-Fi OSError:", e, "→ retry")

        # backoff + cycle radio
        try: wlan.active(False)
        except: pass
        time.sleep(backoff)
        backoff = min(backoff * 1.6, 3.0)
    raise OSError("Wi-Fi: kunne ikke forbinde.")

# ── CoAP primitives (GET-only) ────────────────────────────────────────────────
TYPE_CON, TYPE_NON, TYPE_ACK = 0, 1, 2
CODE_GET = 1
CODE_205_CONTENT = (2 << 5) | 5     # 2.05
CODE_404_NOT_FOUND = (4 << 5) | 4   # 4.04
CF_LINK = 40                        # application/link-format
CF_JSON = 50                        # application/json
CF_TEXT = 0                         # text/plain
PAYLOAD = 0xFF

def _parse_header(pkt):
    if len(pkt) < 4: return None
    tkl  = pkt[0] & 0x0F
    code = pkt[1]
    mid  = (pkt[2] << 8) | pkt[3]
    tok  = pkt[4:4+tkl] if tkl else b""
    typ  = (pkt[0] >> 4) & 3
    pos  = 4 + tkl
    return typ, code, mid, tok, pos

def _read_extended(nib, pkt, pos):
    # CoAP extended nibble (13/14) → return (value, new_pos); 15 er illegal.
    if nib < 13:
        return nib, pos
    if nib == 13:
        if pos >= len(pkt): return None, pos
        return 13 + pkt[pos], pos + 1
    if nib == 14:
        if pos + 1 >= len(pkt): return None, pos
        return 269 + (pkt[pos] << 8) + pkt[pos+1], pos + 2
    return None, pos  # 15 (reserved) → fejl, vi ignorerer konservativt

def _parse_options_uri_path(pkt, pos):
    # Samler ALLE Uri-Path (opt 11) med korrekt kumulativ delta + extended længder.
    path_segments = []
    optno = 0
    n = len(pkt)
    while pos < n:
        if pkt[pos] == PAYLOAD:
            return "/" + "/".join([s for s in path_segments if s]), pos + 1

        if pos >= n: break
        delta_nib = (pkt[pos] >> 4) & 0x0F
        len_nib   = pkt[pos] & 0x0F
        pos += 1
        if pos > n: break

        delta, pos = _read_extended(delta_nib, pkt, pos)
        length, pos = _read_extended(len_nib, pkt, pos)
        if delta is None or length is None: break

        optno += delta
        val = pkt[pos:pos+length]; pos += length

        if optno == 11:  # Uri-Path
            try:
                path_segments.append(val.decode() if val else "")
            except:
                path_segments.append("")

    return "/" + "/".join([s for s in path_segments if s]), pos

def _resp(mid, token, typ, code, payload, cf):
    hdr = bytearray([(1<<6) | (typ<<4) | (len(token)&0x0F),
                     code, (mid>>8)&0xFF, mid&0xFF])
    hdr += token
    # Content-Format (opt #12); vi bruger 1-byte værdi for enkelhed
    hdr += bytes([0xC1, (cf & 0xFF)])
    if payload:
        hdr.append(PAYLOAD); hdr += payload
    return hdr

# ── CoAP server ───────────────────────────────────────────────────────────────
class CoapServer:
    """
    Minimal GET-server med:
      - path routing: add("/dht", handler, rt=..., iface=..., ct=...)
      - auto discovery: /.well-known/core (CoRE Link Format)
      - simpel 4.04 (kan disabled)
    Handler-API: fn() -> dict | str | bytes | andet (→ JSON).
    """
    def __init__(self, *, port=5683, bind_ip="0.0.0.0", verbose=True, send_404=True):
        self._routes = {}  # path -> meta
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind((bind_ip, port))
        self._sock.settimeout(1.0)
        self._verbose = verbose
        self._send_404 = send_404

    def add(self, path, handler, *, rt=None, iface=None, ct=CF_JSON):
        if not path.startswith("/"): path = "/" + path
        self._routes[path] = {"fn": handler, "rt": rt, "if": iface, "ct": ct}

    def _wkc_payload(self):
        # </path>;rt="...";if="...";ct=50,…
        links = []
        for p, m in self._routes.items():
            segs = [f"<{p}>"]
            if m.get("rt"):  segs.append('rt="%s"' % m["rt"])
            if m.get("if"):  segs.append('if="%s"' % m["if"])
            if m.get("ct"):  segs.append('ct=%d' % int(m["ct"]))
            links.append(";".join(segs))
        return ",".join(links).encode()

    def serve_forever(self, banner=None):
        if self._verbose:
            if banner: print(banner)
            routes_list = ", ".join(self._routes.keys()) or "(ingen routes)"
            print("CoAP: lytter på udp/5683; routes:", routes_list)
            print("CoAP: discovery via GET /.well-known/core")

        while True:
            try:
                pkt, addr = self._sock.recvfrom(1152)
            except OSError:
                continue

            ph = _parse_header(pkt)
            if not ph: 
                continue
            req_typ, code, mid, token, pos = ph
            if code != CODE_GET:
                continue

            path, _ = _parse_options_uri_path(pkt, pos)
            if path in ("//", "/"): path = "/"
            if self._verbose:
                try: print("GET", path, "fra", addr[0])
                except: pass

            # Discovery endpoint
            if path == "/.well-known/core":
                payload = self._wkc_payload()
                resp = _resp(mid, token, TYPE_ACK if req_typ==TYPE_CON else TYPE_NON,
                             CODE_205_CONTENT, payload, CF_LINK)
                try: self._sock.sendto(resp, addr)
                except: pass
                continue

            route = self._routes.get(path)
            if not route:
                if self._send_404:
                    # Minimum 4.04 (text/plain); kan slås fra med send_404=False
                    payload = b"4.04 Not Found"
                    resp = _resp(mid, token, TYPE_ACK if req_typ==TYPE_CON else TYPE_NON,
                                 CODE_404_NOT_FOUND, payload, CF_TEXT)
                    try: self._sock.sendto(resp, addr)
                    except: pass
                continue

            # Kald handler og normalisér output
            ct = route.get("ct", CF_JSON)
            try:
                body = route["fn"]()
                if isinstance(body, dict):
                    payload = json.dumps(body).encode(); ct = CF_JSON
                elif isinstance(body, str):
                    payload = body.encode()
                    if ct == CF_JSON: ct = CF_TEXT
                elif isinstance(body, (bytes, bytearray)):
                    payload = bytes(body)
                else:
                    payload = json.dumps({"value": body}).encode(); ct = CF_JSON
            except Exception as e:
                payload = json.dumps({"error": str(e)}).encode(); ct = CF_JSON

            resp = _resp(mid, token, TYPE_ACK if req_typ==TYPE_CON else TYPE_NON,
                         CODE_205_CONTENT, payload, ct)
            try: self._sock.sendto(resp, addr)
            except: pass

# eksportér content-format IDs
CF_JSON = CF_JSON
CF_TEXT = CF_TEXT
CF_LINK = CF_LINK
```

**Forventet konsol-output**

```
Wi-Fi: forbundet <ESP-IP>
CoAP: lytter på udp/5683; routes: /dht
CoAP: discovery via GET /.well-known/core
```

---

## Test fra din computer (samme net)

```bash
# Discovery (CoRE Link Format)
coap-client -m get coap://<ESP-IP>:5683/.well-known/core -A application/link-format

# Data (JSON)
coap-client -m get coap://<ESP-IP>:5683/dht -A application/json
```

Eksempel-output:

```
</dht>;rt="sensor.temperature";if="sensor";ct=50
{"sensor":"DHT22(sim)","temperature":22.1,"humidity":44.8,"unit":"C/%"}
```

Node-RED quick client: `coap request` (GET) → `coap://<ESP-IP>:5683/dht`, og sæt `Accept=application/json`.

---

## API—det du skal bruge, og kun det

```python
from coapmini import wifi_connect, CoapServer, CF_JSON, CF_TEXT, CF_LINK
```

### `wifi_connect(ssid, psk, retries=10, connect_window_ms=7000, verbose=True)`

* Robust STA-connect (radio-reset, backoff, statusprint).
* Returnerer `WLAN` ved success.
* Valgfri – håndtér selv Wi-Fi hvis ønsket.

### `CoapServer(port=5683, bind_ip="0.0.0.0", verbose=True, send_404=True)`

* Starter en UDP/5683 CoAP-server.
* `verbose=True`: logger requests og banner.
* `send_404=True`: ukendte paths svarer 4.04 (ellers stilhed).

### `srv.add(path, handler, rt=None, iface=None, ct=CF_JSON)`

Registrér en ressource (endpoint):

* **path**: URI, fx `"/dht"` ( `"dht"` normaliseres også til `"/dht"` ).
* **handler()**: din **funktions-callback uden argumenter**. Køres på hver GET.

  * Returnér:

    * `dict` → sendes som **JSON** (Content-Format=50)
    * `str` → sendes som **text/plain** (CF=0)
    * `bytes|bytearray` → sendes råt (brug `ct` hvis ikke standard)
    * andre typer → pakkes som `{"value": …}` (JSON)
* **rt**: *resource type* til discovery (fx `"sensor.temperature"`).
* **iface**: *interface description* til discovery (fx `"sensor"`).
* **ct**: *content-format ID* (50=JSON, 0=tekst, 40=link-format). Kan som regel udelades ved `dict`.

**Effekt i discovery** (`/.well-known/core`):

```
</dht>;rt="sensor.temperature";if="sensor";ct=50
```

### `srv.serve_forever(banner=None)`

* Kører den blokkerende serverloop. Understøtter:

  * `GET /.well-known/core` → CoRE Link Format (ID 40)
  * `GET /<path>` → 2.05 Content med din payload

---

## Mønstre der skalerer (copy-paste klar)

### Flere endpoints

```python
srv.add("/temp", lambda: {"temperature": 23.1, "unit":"°C"},
        rt="sensor.temperature", iface="sensor")
srv.add("/hum",  lambda: {"humidity": 46.2, "unit":"%"},
        rt="sensor.humidity",    iface="sensor")
```

### Tekst- og bytes-svar

```python
srv.add("/hello", lambda: "hej verden")              # str → text/plain (ct=0)
srv.add("/raw",   lambda: b"\x01\x02\x03", ct=42)    # bytes → custom CF=42
```

### Minimal (uden metadata og ct)

```python
def ping(): return {"status": "ok"}
srv.add("/ping", ping)   # dict → JSON (ct=50) automatisk
```

---

## Troubleshooting (to-the-point)

* **4.04 Not Found** → Path mismatch. Tjek banneret: `routes: /dht, /temp, …` og brug præcis samme URI.
* **Discovery viser ikke dit endpoint** → Sørg for at `srv.add(...)` kaldes **før** `serve_forever()`.
* **Hotspots** blokerer ofte multicast. Unicast discovery (direkte IP) virker fint.
* **Vil du se runtime-paths** → kør med `verbose=True` (standard), så logger serveren `GET /path fra <ip>`.

---

## One-pager demo (klar til undervisning)

```python
import urandom
from coapmini import wifi_connect, CoapServer, CF_JSON

wifi_connect("YOUR_SSID", "YOUR_PASSWORD")

def rnd(): return urandom.getrandbits(16)/65535
temp, hum = 22.5, 45.0
def dht_sim():
    global temp, hum
    temp += (rnd()-0.5)*0.4
    hum  += (rnd()-0.5)*1.2
    temp = min(max(temp,18.0),30.0)
    hum  = min(max(hum,25.0),70.0)
    return {"sensor":"DHT22(sim)","temperature":round(temp,2),"humidity":round(hum,2),"unit":"C/%"}

srv = CoapServer(port=5683, verbose=True, send_404=True)
srv.add("/dht", dht_sim, rt="sensor.temperature", iface="sensor", ct=CF_JSON)
srv.add("/hello", lambda: "hej verden")
srv.serve_forever("READY → GET /.well-known/core, /dht, /hello")
```

**Test**

```bash
coap-client -m get coap://<ESP-IP>:5683/.well-known/core -A application/link-format
coap-client -m get coap://<ESP-IP>:5683/dht   -A application/json
coap-client -m get coap://<ESP-IP>:5683/hello -A text/plain
```

---

Det her er “low-friction onboarding”: én fil at lægge på enheden, én linje per ressource, og discovery “just works”. Når I er klar til næste sprint, kan vi udvide libbet med **Observe** og **POST/PUT** uden at bryde API’et.
