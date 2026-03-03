# coapmini.py — MicroPython mini-CoAP lib (GET + routing + discovery)
# Mål: generisk, undervisningsklar, ingen eksterne deps.
import time, socket, json

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