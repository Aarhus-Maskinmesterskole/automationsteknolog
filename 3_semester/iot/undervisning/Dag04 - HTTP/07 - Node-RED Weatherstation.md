# Dag 4: Node-RED Weatherstation
## Beskrivelse 📝
Formålet med denne opgave er at bygge et simpelt, men funktionelt, vejr-dashboard i Node-RED. Flowet skal hente aktuelle vejrdata fra **Weatherstack API** for en selvvalgt by og visualisere dem ved hjælp af `node-red-dashboard`.

Dette projekt giver praktisk erfaring med at kalde eksterne REST API'er, behandle JSON-data og skabe en simpel brugergrænseflade.

---

**Hint:** Se denne video for at løse opgaven [youtube](https://www.youtube.com/watch?v=HUtxwjhkCe4)

## Krav 📋

1.  **Opsætning af Weatherstack**
    * Opret en gratis konto på [weatherstack.com](https://weatherstack.com/).
    * Find din personlige **API Access Key**. Denne skal bruges i dit Node-RED flow.

2.  **Node-RED Flow**
    * **Datahentning:** Opret et flow, der periodisk (f.eks. hvert 15. minut) kalder Weatherstack API'et for en by efter eget valg (f.eks. Aarhus).
        * Brug en `inject`-node til at starte flowet.
        * Brug en `http request`-node til at kalde API'et. URL'en vil se cirka sådan her ud: `http://api.weatherstack.com/current?access_key=DIN_API_NØGLE&query=Aarhus`
    * **Databehandling:** API'et returnerer en del data i JSON-format.
        * Sørg for, at output fra `http request`-noden er parset som et "JSON object".
        * Brug `change`- eller `function`-noder til at udtrække de relevante værdier fra `msg.payload`. Du skal som minimum have fat i:
            * Temperatur (`temperature`)
            * Luftfugtighed (`humidity`)
            * Vindhastighed (`wind_speed`)
            * Vejrbeskrivelse (`weather_descriptions`)

3.  **Visualisering på Dashboard**
    * Installer `node-red-dashboard`, hvis du ikke allerede har den.
    * Opret en ny fane (tab) i dashboardet kaldet "Vejrstation".
    * Visualiser de udtrukne data ved hjælp af passende dashboard-noder:
        * **Gauge:** Vis **temperatur** og **luftfugtighed**.
        * **Text:** Vis **vejrbeskrivelsen** (f.eks. "Sunny") og **vindhastighed**.
        * **(Valgfrit) Chart:** Gem temperaturværdierne over tid og vis dem på en graf.

---

## Acceptancekriterier ✅

- [ ] Flowet kan succesfuldt hente vejrdata fra Weatherstack API'et uden fejl.
- [ ] Data for temperatur, luftfugtighed og vindhastighed bliver korrekt udtrukket fra JSON-svaret.
- [ ] Node-RED Dashboard viser de aktuelle vejrdata i realtid (eller med den indstillede forsinkelse).
- [ ] Dashboardet er overskueligt og let at aflæse.
- [ ] API-nøglen er ikke hårdkodet på en måde, så den er synlig i eksporteret kode (brug f.eks. credentials eller en flow-variabel).

---

## Ressourcer 📚

* **Weatherstack API Dokumentation:** [https://weatherstack.com/documentation](https://weatherstack.com/documentation)
* **Node-RED Dashboard (GitHub):** [https://github.com/node-red/node-red-dashboard](https://github.com/node-red/node-red-dashboard)
* **Node-RED Guide til HTTP Requests:** [https://cookbook.nodered.org/http/simple-get-request](https://cookbook.nodered.org/http/simple-get-request)
