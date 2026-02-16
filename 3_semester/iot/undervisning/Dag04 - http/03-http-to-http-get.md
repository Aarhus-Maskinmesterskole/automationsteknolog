# Dag 4: REST og HTTP  
## Opgave: GET fra en medstuderendes Node-RED endpoint (uden kode)

### Formål
Design en letvægts peer-to-peer integration på lokalt netværk:
- **Student A (server)** eksponerer et simpelt HTTP GET-endpoint i Node-RED.
- **Student B (klient)** henter data fra A's endpoint i eget Node-RED og visualiserer dem.

Fokus: REST-principper, statuskoder, JSON-kontrakter og netværksadressering (IP:port, path).

### Læringsmål
Efter opgaven kan du:
- Konfigurere et HTTP GET-endpoint med korrekt responsheader og JSON-kontrakt.
- Forbruge et eksternt endpoint med periodisk polling og inputvalidering.
- Teste med `curl` og diagnosticere almindelige fejl (404/503/timeout).
- Beskrive din API-kontrakt så en peer kan integrere uden at se din løsning.

### Rammer
- Alle maskiner er på samme LAN; Node-RED kører typisk på port `1880`.
- Udveksl IP-adresser i gruppen. Eksempel-base-URL: `http://192.168.1.37:1880`.
- **Ingen** Node-RED-kode/flows deles i denne opgave; kun URL + kontrakt.

---

## Opgavebeskrivelse

### Del A (Server, Student A): Udstil GET-endpoint
**Krav til endpoint:**
- Path: `/api/telemetry` (kan tilpasses; dokumentér hvis du ændrer).
- Metode: `GET`.
- Response: `200 OK` med `Content-Type: application/json` og `Cache-Control: no-store`.
- JSON-kontrakt (minimum):
  - `student` (string),
  - `room` (string),
  - `ts` (ISO8601),
  - `temperature` (number),
  - `humidity` (number).

**Levering til B:** Dokumentér kontrakten (felter, typer, eksempelpayload) samt base-URL og path. Del **kun** disse oplysninger med Student B.

### Del B (Klient, Student B): Forbrug A's endpoint
**Krav til klientflow:**
- Poll A's endpoint periodisk (fx hver 10. sekund).
- Parse JSON og vis felterne i dashboard **eller** Debug.
- Inputvalidering: håndtér manglende felter, ikke-JSON og ikke-200 svar.

> Integrér udelukkende på baggrund af den delte kontrakt.

---

## Test og verifikation (CLI)
Brug `curl` til at verificere serveren, før klienten kobles på:

```bash
# Antag server-IP 192.168.1.37 og Node-RED port 1880
curl -i http://192.168.1.37:1880/api/telemetry
