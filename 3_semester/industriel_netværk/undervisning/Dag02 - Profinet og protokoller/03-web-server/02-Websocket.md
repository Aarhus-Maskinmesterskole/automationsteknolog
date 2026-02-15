# PLC 1 ↔ Python WebSocket – trin‑for‑trin guide

> **Scope:** Dette er en meget enkel opsætning, hvor **PLC 1** hoster en HTML‑klient i PLC’ens webserver (browser‑UI), og **Python‑serveren** modtager alt via WebSocket.

---

## Arkitektur (kort)

* **PLC 1**: Kører en statisk HTML‑side med JavaScript, der opretter WebSocket‑forbindelse.
* **Python‑server**: Lytter på `ws://<server-ip>:8080/` og logger alle modtagne beskeder (valgfri echo).

Brug egen IP adresse på jeres pc.

```
[PLC 1 HTML-klient]  --ws-->  [Python WS-server]
```

---

## Forudsætninger

* Netværk: PLC 1 og Python‑server er på samme net (eller der er routing/NAT imellem).
* Windows/macOS/Linux til Python‑serveren.
* **Python 3.10+** og pip.

---

## Repo‑struktur (foreslået)

```
.
├─ client/
│  └─ index.html # dette er, hvor PLC'en henter sin statiske website
├─ server/
│  └─ plc2_ws_server.py
└─ README.md   ← denne fil
```

---

## Trin 1 — PLC 1: HTML‑klient

Tænk ikke så meget over html fordi i er ikke website developer!

1. Opret mappen `client/` og læg nedenstående fil som `index.html`.
2. Læg filen på PLC 1’s webserver (hvordan afhænger af PLC‑model). Alternativt kan du teste lokalt ved at åbne filen i en browser.

> **Bemærk:** Denne klient er identisk i ånd med det, du allerede har – felter for `Protocol`, `Host`, `Port`, `Path` samt `Connect/Send`.

```html
<!doctype html>
<html lang="da">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>PLC WebSocket Client</title>
  <style>
    body{font-family:system-ui,Arial,sans-serif;max-width:900px;margin:24px auto;padding:0 12px}
    fieldset{margin:12px 0;padding:12px;border:1px solid #ddd;border-radius:8px}
    label{display:block;margin:6px 0 2px}
    input,select,button,textarea{padding:8px;font-size:14px}
    .row{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
    #log{height:240px;overflow:auto;background:#111;color:#0f0;padding:12px;border-radius:8px}
  </style>
</head>
<body>
  <h1>WebSocket testklient</h1>

  <fieldset>
    <legend>Forbindelse</legend>
    <div class="row">
      <div>
        <label for="proto">Protocol</label>
        <select id="proto"><option>ws</option><option>wss</option></select>
      </div>
      <div>
        <label for="host">Host/IP</label>
        <input id="host" value="127.0.0.1" />
      </div>
      <div>
        <label for="port">Port</label>
        <input id="port" value="8080" />
      </div>
      <div>
        <label for="path">Path</label>
        <input id="path" value="/" />
      </div>
    </div>
    <div style="margin-top:8px">
      <button id="connect">Connect</button>
      <button id="disconnect" disabled>Disconnect</button>
    </div>
  </fieldset>

  <fieldset>
    <legend>Besked</legend>
    <label for="message">Payload</label>
    <input id="message" value="Hello from PLC client" style="width:100%" />
    <div style="margin-top:8px">
      <button id="send" disabled>Send</button>
    </div>
  </fieldset>

  <fieldset>
    <legend>Log</legend>
    <pre id="log"></pre>
  </fieldset>

  <script>
    let ws;
    const $ = (id)=>document.getElementById(id);
    const log = (m)=>{ const el=$('log'); el.textContent += m + "\n"; el.scrollTop = el.scrollHeight; };

    $('connect').addEventListener('click', (e)=>{
      e.preventDefault();
      const url = `${$('proto').value}://${$('host').value}:${$('port').value}${$('path').value}`;
      log('CONNECT ' + url);
      ws = new WebSocket(url);
      ws.onopen = ()=>{ log('OPEN'); $('send').disabled=false; $('disconnect').disabled=false; };
      ws.onmessage = (evt)=> log('RX: ' + evt.data);
      ws.onerror = (err)=> log('ERR: ' + (err?.message || 'unknown'));
      ws.onclose = ()=>{ log('CLOSED'); $('send').disabled=true; $('disconnect').disabled=true; };
    });

    $('disconnect').addEventListener('click', (e)=>{ e.preventDefault(); if(ws){ ws.close(); } });
    $('send').addEventListener('click', (e)=>{
      e.preventDefault();
      const msg = $('message').value;
      if(ws && ws.readyState === WebSocket.OPEN){ ws.send(msg); log('TX: ' + msg); }
      else { log('Not connected'); }
    });
  </script>
</body>
</html>
```

---

## Trin 2 — Python: minimal WebSocket‑server

1. Opret mappen `server/` og gem nedenstående som `plc2_ws_server.py`.
2. Installer dependency:

   * **Windows (PowerShell):**

     ```powershell
     python -m pip install websockets
     ```
   * **Linux/macOS:**

     ```bash
     pip install websockets
     ```
3. Start serveren:

   ```bash
   python server/plc2_ws_server.py --host 0.0.0.0 --port 8080 --path /
   ```

> **Tip:** Til echo‑test: `python server/plc2_ws_server.py --echo`

**`server/plc2_ws_server.py`:**

```python
#!/usr/bin/env python3
# Minimal WS-server (websockets ≥ 12)
# Modtager tekst/binary og logger. Valgfri echo: --echo eller ECHO=1

import os
import argparse
import asyncio
import logging
import websockets

def parse_args():
    p = argparse.ArgumentParser(description="Minimal WS server for PLC2")
    p.add_argument("--host", default="0.0.0.0")
    p.add_argument("--port", type=int, default=8080)
    p.add_argument("--path", default="/")
    p.add_argument("--echo", action="store_true", help="Echo received data back to client")
    p.add_argument("--ping", type=float, default=15.0, help="Ping interval seconds (0=off)")
    return p.parse_args()

async def handler(ws):  # websockets ≥12: kun ét argument
    peer = ws.remote_address
    path = getattr(ws, "path", "/") or "/"
    logging.info(f"[CONNECT] {peer} path={path}")

    if path != EXPECTED_PATH:
        logging.warning(f"[DENY] {peer} wrong path={path} (expected {EXPECTED_PATH})")
        await ws.close(code=1008, reason="Invalid path")
        return

    try:
        async for msg in ws:
            if isinstance(msg, bytes):
                logging.info(f"[RX] {peer} <{len(msg)} bytes binary>")
                if ECHO:
                    await ws.send(msg)
                    logging.info(f"[TX/ECHO] -> {peer} <{len(msg)} bytes>")
            else:
                logging.info(f"[RX] {peer} {msg}")
                if ECHO:
                    await ws.send(msg)
                    logging.info(f"[TX/ECHO] -> {peer} {msg}")
    except websockets.ConnectionClosed as e:
        logging.info(f"[CLOSE] {peer} code={e.code} reason={e.reason}")
    except Exception as e:
        logging.exception(f"[ERROR] {peer}: {e}")
    finally:
        logging.info(f"[DISCONNECT] {peer}")

async def main():
    global EXPECTED_PATH, ECHO
    args = parse_args()
    EXPECTED_PATH = args.path if args.path.startswith("/") else f"/{args.path}"
    ECHO = args.echo or (os.getenv("ECHO") == "1")

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    ping_interval = None if args.ping <= 0 else args.ping

    async with websockets.serve(
        handler,
        args.host,
        args.port,
        ping_interval=ping_interval,
        ping_timeout=(None if ping_interval is None else ping_interval * 2),
        max_size=None,
        max_queue=32,
    ):
        logging.info(f"WS server online: ws://{args.host}:{args.port}{EXPECTED_PATH}  echo={ECHO}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Trin 3 - PLC 1: Enable webserver
1. Lav et projekt
2. Indsæt en PLC S7-1500
3. Gå ind i egenskaber på PLC'en
4. Find menuen 'Web Server' -> 'General' -> kun flueben i 'Activate web server on this module'. Fjern flueben fra 'Permit access only with HTTPS.
5. Find menuen 'User-defined pages. Vælge under HTML directory den mappe hvor du vil placer din html fil. Laves i næste trin!
6. Tryk 'Generate blocks'
7. Find menuen 'User management' under 'Web server' og lav en admin user som har adgang til alt. Lav en super let kode som 'SuperSecret123'
8. Gå til main og indsæt instruktionen '??' og skriv 'www'
9. I venstre side "CTRL_DB" indsæt tallet 333 (findes under web server menuen).
10. Lav en DB. Lav en variabel 'return_val' med data typen 'word' og indsæt den på 'RET_VAL'. Det er en form for status bit.
11. Download som 'Hardware og software (only changes)' og tilgå browser på http://<PLC-IP>

## Trin 4 — Forbind PLC 1 til Python‑serveren

1. Åbn `Find menuen User-defined pages` i PLC 1’s browser.
2. Udfyld felterne:

   * **Protocol:** `ws`
   * **Host/IP:** IP‑adressen på maskinen, der kører Python‑serveren
   * **Port:** `8080`
   * **Path:** `/`
3. Klik **Connect** og derefter **Send**.

**Forventet resultat:**

* Klienten viser `OPEN` og `TX: <din tekst>`.
* Python‑serverens terminal viser linjer som `\[RX] ('192.168.x.y', <port>) Hello from PLC client`.

---

## Trin 4 — Verificér dataflow (acceptkriterier)

* Klienten kan forbinde uden fejl (status `OPEN`).
* Når der sendes en besked, logges den på serveren.
* (Valgfrit) Med `--echo` svarer serveren tilbage, og klientens log viser `RX: ...`.

---

## Fejlfinding (quick wins)

* **Kan ikke forbinde:**

  * Firewall på serveren: Tillad indgående på port 8080.
  * IP/port/path forkert: Tjek at serveren kører og lytter på `ws://<ip>:8080/`.
* **TypeError: handler() missing 'path':**

  * Brug koden i denne README (kompatibel med websockets ≥12), eller pin `websockets<12` hvis du bruger gammel handler‑signatur.
* **Mixed content (HTTPS → WS):**

  * Hvis klient‑HTML’en servés over **HTTPS**, skal du bruge `wss://` (TLS). Ellers blokkerer browseren.
* **Port i brug:**

  * Skift port, fx `--port 9001` på serveren og tilsvarende i klienten.

---

## Videre (valgfrit, når basis fungerer)

* **Service:** Kør Python‑serveren som systemservice (systemd/Task Scheduler).
* **Sikkerhed:** Terminer TLS foran serveren (nginx/Traefik) og skift til `wss://`.
* **Protokol:** Skift fra rå tekst til JSON‑kontrakt `{id, from, to, ts, type, data}` for robusthed.

---