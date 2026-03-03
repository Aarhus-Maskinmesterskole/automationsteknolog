# 🔘 Opgave 04 – Del Knapdata via CoAP

I denne opgave skal du programmere ESP32 til at læse input fra en fysisk knap og gøre tilstanden (og antallet af tryk) tilgængelig via en CoAP server.

![alt text](image-3.png)

## 🎯 Formål

Lær at:
- Læse digital input fra en knap
- Opsætte en tæller der registrerer hvor mange gange der er trykket (debounce)
- Dele den aktuelle tilstand (trykket/sluppet) og tryk-historik (tæller) via CoAP GET anmodninger

---

## 💡 Python-kode

Opret en ny fil i Thonny og skriv følgende:

```python
# ESP32 + Knap CoAP Server
# Returnerer knappens nuværende tilstand samt antal gange trykket

import time
import network
from machine import Pin
from coapmini import CoapServer

# ===== KONFIGURATION =====
WIFI_SSID = "DIT_WIFI_NAVN"
WIFI_PASSWORD = "DIT_WIFI_PASSWORD"
BUTTON_PIN = 16  # GPIO 16
# =========================

# Opsæt knap med pull-up resistor. (0 = trykket ned, 1 = sluppet op)
# Bemærk at knappen forbindes mellem GPIO 16 og GND på ESP32!
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

def wifi_connect(ssid, password):
    print("Forbinder til WiFi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    
    ip = wlan.ifconfig()[0]
    print(f"Forbundet! IP Adresse: {ip}")
    return ip

# Globale variabler til tællerlogik
button_count = 0
last_button_state = 1
last_press_time = 0
DEBOUNCE_TIME = 200  # 200 ms for at afvise falske hardware dobbelttryk

def update_button_state():
    """Tjekker om knappen trykkes og opdaterer tælleren (Køres hurtigt i server loopet)"""
    global button_count, last_button_state, last_press_time
    
    current_button_state = button.value()
    current_time = time.ticks_ms()
    
    # Tjek om knappen er gået fra 1 (sluppet) til 0 (trykket nede)
    if last_button_state == 1 and current_button_state == 0:
        if time.ticks_diff(current_time, last_press_time) > DEBOUNCE_TIME:
            button_count += 1
            print(f"🔘 Knap trykket! (Tæller: {button_count})")
            last_press_time = current_time
            
    last_button_state = current_button_state

def read_button():
    """Opkaldsfunktionen, der returnerer datastrukturen tilbage til CoAP Requestet"""
    global button_count
    state = "trykket" if button.value() == 0 else "sluppet"
    
    # Her returnerer vi både om knappen er nede *LIGE NU*, 
    # samt *HVOR MANGE GANGE* den har været trykket statistisk set.
    return {
        "status": state,
        "tryk_count": button_count
    }

def main():
    # Forbind til WiFi og gem IP
    ip = wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    
    # Start CoAP Server
    srv = CoapServer()
    
    # Kobl en URL (/button) sammen med vores funktion
    srv.add("/button", read_button)
    
    print(f"Klar! Hent knap-status med GET coap://{ip}:5683/button")
    
    # Fordi vi ikke kan sætte serveren til at "serve_forever" her - 
    # idet vi også hele tiden skal holde øje med hvornår knappen trykkes fysisk,
    # laver vi vores ESP32 hoved-loop fuldstændig manuelt.
    while True:
        # 1: Tjek fysisk om knappen trykkes, og opdatér den interne tæller
        update_button_state()
        
        # 2: Lyt meget kort (i fx 100ms) om vi har modtaget CoAP forespørgsler over nettet. (Serve-once)
        srv._sock.settimeout(0.1) 
        srv._serve_once(suppress_errors=True)

if __name__ == '__main__':
    main()
```

### Konfigurér og kør

1. **Rediger følgende i koden:**
   - `WIFI_SSID` → Dit WiFi-navn
   - `WIFI_PASSWORD` → Dit WiFi-password

2. **Husk at justere CoAP Server klassen i biblioteket hvis _serve_once ikke findes:** *(Tilføjelsen er lavet til det nyeste coapmini)*
   Sørg for at du har den nyeste `coapmini.py` version i roden af din ESP32.

3. **Kør programmet:**
   - Gem filen som `main.py`
   - Tryk **F5**
   - Notér den IP-adresse, der udskrives i Shell-vinduet. Tryk på knappen og se Outputtet tælle op.

### Sådan tester du det:
I Node-RED (eller et andet CoAP værktøj):
1. Vælg en **coap request** node.
2. Sæt metoden til `GET`.
3. Sæt URL til `coap://<din-esp32-ip>:5683/button` (Husk IP fra Thonny).
4. Forbind en **inject**-node foran (Sæt den evt. til at spørge ESP32'en hvert 1. sekund).
5. Forbind en **debug**-node bagefter for at se, hvordan ESP'en besvarer med sit tællertal og aktuelle status.

---

## 📝 Forklaring

**Sådan virker koden:**

1. **Pull-up resistor**: 
   - Knappen er forbundet til GND
   - `Pin.PULL_UP` trækker automatisk den digitale pin op til 1 (Høj) når knappen **ikke** er trykket.
   - Pinnen falder til 0 (Lav) når knappen **trykkes** ned og rammer GND.
   - Derfor: `0 = trykket`, `1 = Sluppet`.

2. **Debouncing & Non-blocking loops**:
   - Da vi er en server, skal vi både høre efter netværket (*CoAP anmodninger*) og hele tiden tjekke knappen (*Loop*).
   - Derfor kører vi vores egen `While True:` løkke for enden, fremfor automatikken. 
   - Vi har også programmeret koden til at ignorere mikrobølger i det fysiske stål i knappen (`DEBOUNCE_TIME`), så ét klik ikke med det samme fejllæses som 3 klik.
   - Sparer båndbredde sammenlignet med konstant polling
   - To beskeder sendes: status ("PRESSED") og tæller

**MQTT Payload:**
- Topic `button`: `b"PRESSED"` når knappen trykkes
- Topic `button_count`: Tæller antal tryk (1, 2, 3, ...)

**Hvorfor 10ms polling?**
- Balance mellem responsivitet og CPU-forbrug
- Hurtig nok til at fange menneskelige knaptryk
- Langsom nok til ikke at spilde strøm
