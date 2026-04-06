# 📘 DAG 6 – Modbus TCP Integration

Modbus TCP bruges bredt i industrien som grænseflade mellem intelligente enheder og overordnede systemer. Mange enheder – fx Danfoss VLT, Schneider PowerTag, Carlo Gavazzi, WAGO mv. – eksponerer data via Modbus TCP. I dette modul lærer du at forstå protokollen, oprette klient/server-forbindelser og integrere data i andre systemer.

---

## 📦 Moduloversigt

| Afsnit | Titel         | Indhold                                                                                                 |
| ------ | ------------- | ------------------------------------------------------------------------------------------------------- |
| 01     | Grundbegreber | Adresseområder, registertyper, funktionskoder, forskellen mellem TCP og RTU (kort introduktion)         |
| 02     | Server/Client | Praktisk kommunikation mellem Modbus TCP-klient og -server. Vi bruger Node-RED, ESP32 og Home Assistant |
| 03     | Gateway       | Forstå og bygge TCP ↔ RTU gateways. Node-RED og ESP32 som bro, brugsscenarier                           |
| 04     | IoT house     | Meget simple ESP32-opgaver som Modbus TCP server: DHT11, PIR, knap, servo, LED, RGB og LCD             |

> 🔧 Bemærk: Python og Node.js anvendes kun i avancerede eksempler og ikke i kerneopgaverne.

---

## 🎯 Læringsmål

* Forstå Modbus TCP som industri-protokol
* Kunne læse og skrive registre fra fx PowerTags eller Danfoss-enheder
* Oprette klient/server kommunikation og forstå adressering
* Få kendskab til forskellen mellem TCP og RTU (uden at arbejde direkte med RTU)
* Integrere Modbus TCP-data i moderne systemer (fx Node-RED, MQTT, Home Assistant)

---

## 🛠 Kompetencer efter dette modul

Efter gennemført modul kan deltageren:

* Forklare forskellen på Modbus TCP og RTU på et grundlæggende niveau
* Analysere registertabeller og identificere relevante adresser og datatyper
* Opsætte og teste kommunikation mellem klient og server i et Modbus TCP-netværk
* Bruge værktøjer som Node-RED, ESP32 eller Home Assistant til at afprøve forbindelser
* Forstå principperne bag gateway-funktionalitet (uden at implementere RTU-kommunikation)
* Fejlsøge almindelige problemer som forkerte adresser, timeout og byte order
* Forstå hvordan Modbus TCP indgår som interface i hybride eller proprietære systemer

---

## Meget simple ESP32-opgaver

Filerne `01` til `09` er en ekstra enkel serie, hvor ESP32 er Modbus TCP server.

Fælles for alle opgaver:

* Kopiér `umodbus` fra `python/micropython-modbus-develop/umodbus` til `/lib` på ESP32
* Ret `SSID` og `PASS` i koden
* Brug `Unit ID = 1`
* Brug `Port = 502`
* Brug `coils` til ON/OFF og `holding registers` til tal for at holde det helt simpelt
* I `python`-mappen ligger matchende `.py`-filer til alle opgaver

---

📌 Opgaverne `01` til `09` er de helt enkle ESP32-eksempler. Brug filerne i `python`-mappen, hvis du vil have samme kode som i `.md`-arkene.
