# Dag 4: REST og HTTP

## Opgave: POST til en medstuderendes Node-RED endpoint (uden kode)

### Formål

Design en letvægts peer-to-peer integration på lokalt netværk:

* **Student A (server)** eksponerer et simpelt HTTP POST-endpoint i Node-RED.
* **Student B (klient)** sender JSON-data til A's endpoint og validerer svaret.

Fokus: korrekt POST-semantik, `Content-Type`, statuskoder, JSON-kontrakt og basal inputvalidering.

### Læringsmål

Efter opgaven kan du:

* Definere og dokumentere et POST-endpoint med tydelig JSON-kontrakt.
* Sende JSON med korrekt `Content-Type: application/json`.
* Håndtere typiske fejlsvar (400/415/503) og verificere med `curl`.

### Rammer

* Alle maskiner er på samme LAN; Node-RED kører typisk på port `1880`.
* Udveksl IP-adresser i gruppen. Eksempel-base-URL: `http://192.168.1.37:1880`.
* **Ingen** Node-RED-kode/flows deles i denne opgave; kun URL + kontrakt.

---

## Opgavebeskrivelse

### Del A (Server, Student A): Udstil POST-endpoint

**Krav til endpoint:**

* Path: `/api/telemetry` (kan tilpasses; dokumentér hvis du ændrer).
* Metode: `POST`.
* Forventet header: `Content-Type: application/json`.
* Body (minimum-kontrakt): se “Kravspec for JSON-kontrakt”.
* Response ved succes: `201 Created`, `Content-Type: application/json`, `Cache-Control: no-store`. Anbefalet: `Location` med evt. ressource-id.
* Response ved fejl:

  * `400 Bad Request` (manglende/ugyldige felter),
  * `415 Unsupported Media Type` (forkert `Content-Type`),
  * `503 Service Unavailable` (intern fejl).

**Levering til B:** Dokumentér kontrakten (felter, typer, eksempelpayload) samt base-URL og path. Del **kun** disse oplysninger med Student B.

### Del B (Klient, Student B): Send POST til A

**Krav til klient:**

* Send POST med `Content-Type: application/json` til A's `/api/telemetry`.
* Inkluder alle krævede felter i body (se kontrakt).
* Håndter svar: succes (`201`) og fejlkoder (`400`/`415`/`503`) vises tydeligt i UI eller Debug.

> Integrér udelukkende på baggrund af den delte kontrakt.

---

## Kravspec for JSON-kontrakt (minimum)

* `student`: string, fx `"anna"`.
* `room`: string, fx `"lab"`.
* `ts`: ISO8601 timestamp, fx `"2025-09-19T10:15:30Z"`.
* `temperature`: number (grader C), fx `22.8`.
* `humidity`: number (pct), fx `41`.

*Anbefalet:* afrund temperatur til én decimal og humidity til heltal. Maksimal body-størrelse fx 1–2 kB.

---

## Test og verifikation (CLI)

Valider med `curl` (ASCII-venligt eksempel):

```bash
# Antag server-IP 192.168.1.37 og Node-RED port 1880
curl -i -X POST http://192.168.1.37:1880/api/telemetry \
  -H "Content-Type: application/json" \
  -d "{\"student\":\"anna\",\"room\":\"lab\",\"ts\":\"2025-09-19T10:15:30Z\",\"temperature\":22.8,\"humidity\":41}"
```

Forventet:

* `HTTP/1.1 201 Created`
* `Content-Type: application/json`
* `Cache-Control: no-store`
* En kort JSON-kvittering (fx `{"status":"ok"}` og evt. `id`).

---

## Fejlhåndtering

Server kan returnere:

* `400 Bad Request`: manglende felter eller ugyldige typer.
* `415 Unsupported Media Type`: manglende/forkert `Content-Type`.
* `503 Service Unavailable`: midlertidig fejl.

Klient skal vise fejlkoder og beskeder tydeligt og **ikke** crashe flowet.

---

## Sikkerhed og etik

* Eksponér kun ufølsomme testdata.
* Hold det på LAN; ingen port-forwarding mod internet.
* Log kun nødvendige metadata; ingen persondata.

---

## Refleksion (kort)

1. Hvornår ville du bruge `POST` fremfor `PUT` i denne kontekst?
2. Hvilke valideringsregler ville du indføre server-side for at undgå fejl og misbrug?
