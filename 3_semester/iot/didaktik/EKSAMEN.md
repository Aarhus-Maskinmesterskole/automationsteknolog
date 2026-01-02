# IoT Eksamen: Krav og Opgavebeskrivelse

**Aarhus Maskinmesterskole**  
*16. november 2024*

---

## Forudsætninger for at kunne gå til eksamen

For at kunne deltage i IoT-eksamenen skal følgende være opfyldt:

- **Deltagelse i undervisningen:** Aktiv deltagelse i undervisningen og gennemførelse af øvelser og opgaver er påkrævet.
- **Aflevering af projekt:** Det færdige IoT-projekt skal afleveres inden eksamensdagen. Projektet består af en fungerende IoT-løsning samt en 5-minutters videopræsentation, som beskriver og demonstrerer projektets funktioner.
- **Teknisk præsentation:** Du skal kunne præsentere din teknologikæde, dvs. hvordan data strømmer fra sensorer, gennem ESP32, til Node-RED, eller hvordan data fra en ekstern API enten kan påvirke en aktuator gennem Node-RED eller præsenteres i Node-RED.
- **Projektgodkendelse:** Projektet i hele sit omfang skal godkendes af underviser inden igangsættelse og aflevering.

---

## Selvvalgt projekt – Brug af IoT house er valgfrit

Du vælger frit projektets indhold, hardware og use case. Brug af IoT house er valgfrit, og du kan frit vælge egne sensorer, aktuatorer og integrationer, så længe projektet opfylder kravene og godkendes af underviser.

---

## Eksempel på IoT-projekt og videostruktur

Alt efterfølgende er kun et eksempel på, hvordan et IoT-projekt og videopræsentationen kan struktureres. Du har frihed til at vælge dit eget fokus og funktionalitet, men eksemplet her kan bruges som inspiration.

### Eksempel på IoT-projekt: *Smart Indeklimaovervågning*

#### Projektbeskrivelse

I dette eksempelprojekt vil vi overvåge indeklimaet i IoT-huset og automatisk justere temperaturen baseret på både indendørs målinger og udendørs vejrdata. Projektet bruger en temperatur- og fugtighedssensor til at måle indeklimaet samt henter vejrdata fra Weatherstack API.

#### Systemarkitektur

- **Sensorer:** Temperatur- og fugtighedssensor sender data til ESP32.
- **ESP32:** Modtager sensordata og sender dem videre til Node-RED via MQTT-protokollen.
- **Node-RED:** Modtager sensordata og visualiserer dem i et dashboard. Henter aktuelle vejrdata fra Weatherstack API og præsenterer data for brugeren.
- **Ekstern API:** Weatherstack API leverer udendørstemperaturen.
- **Aktuatorer:** Ventilatoren justeres automatisk baseret på sensordata sendt til Node-RED og data fra Weatherstack API.

---

## Eksamensbeskrivelse

### Funktionalitet

- Hvis indendørstemperaturen overstiger 25°C og udendørstemperaturen er lavere, aktiveres ventilatoren automatisk.
- Node-RED-dashboardet viser realtidsmålinger af temperatur, fugtighed og udendørstemperatur.
- Brugeren kan manuelt tænde eller slukke ventilatoren via kontrolpanelet i Node-RED-dashboardet.

> **OBS!** Bemærk, at API’er som Weatherstack ofte har en begrænsning på antallet af forespørgsler per dag. Planlæg din udvikling og testning, så du undgår at løbe tør for forespørgsler.

---

## Eksempel på struktur for videopræsentationen

Videoen kan struktureres som følger:

1. **Introduktion (1 minut):**  
   Præsenter projektets formål samt de valgte komponenter og teknologier. Forklar teknologikæden: Sensorer → ESP32 → Node-RED → API-integration → Aktuatorer (anvend gerne illustrationer og diagrammer).
2. **Demonstration af funktionalitet (2-3 minutter):**  
   Vis dataflowet fra sensorerne til ESP32 og videre til Node-RED. Forklar integrationen med Weatherstack API og demonstrer, hvordan data bruges i Node-RED. Præsenter Node-RED-dashboardet og vis, hvordan dataene præsenteres visuelt (f.eks. grafer og gauges). Forklar protokoller. Demonstrer styring af ventilatoren, både automatisk og manuelt via dashboardet.
3. **Afrunding og refleksion (1 minut):**  
   Opsummer de vigtigste funktioner i projektet. Diskuter eventuelle udfordringer og løsninger. Forklar, hvad du ville forbedre, hvis du havde mere tid.

---

## Tips til et vellykket projekt

- Planlæg API-forespørgslerne grundigt for at undgå begrænsninger.
- Design et overskueligt og brugervenligt dashboard i Node-RED.
- Test alle dele af dit system, herunder sensorer, API-integration og aktuatorkontrol.
- Øv din præsentation, så du kan dække alle punkter klart og tydeligt inden for de 5 minutter.

---

**Vigtigt:** Husk, at dette blot er et eksempel på, hvordan projektet kan udføres. Du har frihed til at vælge dine egne komponenter, funktioner og teknologi, så længe du kan demonstrere en fungerende IoT-løsning, forklare teknologikæden i din præsentation, og projektet er godkendt af underviser.
