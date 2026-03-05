# Dag 4: Node-RED Firebase RTDB Integration
### Beskrivelse 📝
Formålet med denne opgave er at lære, hvordan man interagerer med en **Google Firebase Realtime Database** direkte fra Node-RED. I stedet for at bruge specifikke Firebase-noder, skal du bruge de grundlæggende `http request`-noder. Dette giver en dybere forståelse for, hvordan Firebase's REST API fungerer.

Du skal bygge et flow, der kan både **skrive (PUT)** og **læse (GET)** data til/fra en selvvalgt sti i din database.

---

**Hint:** Se denne video for at løse opgaven [Firebase](https://www.youtube.com/watch?v=55Z5XNs45Nc)

### Forberedelse: Opsætning af Firebase 🔥

Inden du starter i Node-RED, skal du have din Firebase-database klar.

1.  **Opret et Firebase Projekt:** Gå til [Firebase Console](https://console.firebase.google.com/) og opret et nyt projekt, hvis du ikke allerede har et.

2.  **Opret en Realtime Database:** I dit projekts menu, vælg "Build" -\> "Realtime Database" og klik "Create Database".

3.  **Vælg en placering:** Vælg en serverplacering (f.eks. `europe-west1`).

4.  **Start i testtilstand:** For denne opgave skal du vælge at starte databasen i **testtilstand**. Dette slår midlertidigt sikkerhedsreglerne fra, så alle kan læse og skrive til databasen. **VIGTIGT:** Dette er kun til udvikling og test\!

5.  **Find din Database URL:** Øverst i din Realtime Database-visning finder du URL'en. Den ligner typisk `https://dit-projektnavn-default-rtdb.europe-west1.firebasedatabase.app/`. Kopier denne URL.

---

### Krav: Byg dit Node-RED Flow ⚙️

Opgaven er delt i to: at skrive data og derefter læse dem.

#### Del 1: Skriv data til Firebase (PUT Request)

Du skal lave et flow, der sender et simpelt JSON-objekt til din database.

  * **Noder:** `inject`, `function`, `http request`, `debug`.

<!-- end list -->

1.  **`inject` node:** Konfigurer den til at sende et **JSON-objekt** som `msg.payload`. Eksempel:

    ```json
    {
        "sensor": "DHT22",
        "temperature": 23.4,
        "humidity": 45.8,
        "timestamp": "2025-09-18T22:30:00Z"
    }
    ```

    Sørg for, at den også sender et `msg.topic` med den sti, du vil skrive til, f.eks. `iot/living_room/status`.

2.  **`function` node ("Prepare PUT Request"):** Denne node skal forberede HTTP-requestet.

      * **Kode:**
        ```javascript
        // Erstat med DIN Firebase Database URL
        const FIREBASE_URL = "https://dit-projektnavn-default-rtdb.europe-west1.firebasedatabase.app/";

        // Sæt URL'en for requestet. '.json' er VIGTIGT!
        msg.url = FIREBASE_URL + msg.topic + ".json";

        // Sæt metoden til PUT for at overskrive data på stien
        msg.method = "PUT";

        return msg;
        ```

3.  **`http request` node:** Konfigurer den til at bruge metoden og URL'en fra den indgående besked.

      * **Method:** Vælg `- set by msg.method -`
      * **URL:** Lad feltet være tomt, da det sættes af `msg.url`.

4.  **`debug` node:** Forbind den til outputtet af `http request`-noden for at se resultatet fra Firebase.

<!-- end list -->

  * **Test:** Kør flowet. Gå til din Firebase-konsol og verificer, at dataene er blevet skrevet korrekt under stien `iot/living_room/status`.

#### Del 2: Læs data fra Firebase (GET Request)

Nu skal du lave et flow, der kan hente de data, du lige har skrevet.

  * **Noder:** `inject`, `function`, `http request`, `debug`.

<!-- end list -->

1.  **`inject` node:** Denne skal blot starte flowet. Konfigurer den til at sende det samme `msg.topic` som før (`iot/living_room/status`).

2.  **`function` node ("Prepare GET Request"):**

      * **Kode:**
        ```javascript
        // Erstat med DIN Firebase Database URL
        const FIREBASE_URL = "https://dit-projektnavn-default-rtdb.europe-west1.firebasedatabase.app/";

        // Sæt URL'en for requestet. '.json' er VIGTIGT!
        msg.url = FIREBASE_URL + msg.topic + ".json";

        // Sæt metoden til GET
        msg.method = "GET";

        // Ryd payload, da GET requests ikke har en body
        msg.payload = null;

        return msg;
        ```

3.  **`http request` node:** Konfigurationen er den samme som i Del 1.

      * Sørg for, at den returnerer resultatet som et "parsed JSON object".

4.  **`debug` node:** Forbind til outputtet for at se de data, der hentes fra Firebase.

<!-- end list -->

  * **Test:** Kør flowet. Debug-vinduet skal nu vise det JSON-objekt, du skrev til databasen i Del 1.

-----

### Acceptancekriterier ✅

  - [ ] Du har en fungerende Firebase Realtime Database opsat i testtilstand.
  - [ ] Dit Node-RED flow kan succesfuldt **skrive** et JSON-objekt til en valgfri sti i databasen.
  - [ ] Du kan se de skrevne data i Firebase-konsollen.
  - [ ] Dit Node-RED flow kan succesfuldt **læse** de samme data tilbage fra databasen.
  - [ ] De læste data vises korrekt i debug-panelet i Node-RED.

-----

### Ressourcer og Tips 💡

  * **Firebase REST API Dokumentation:** [Firebase Realtime Database REST API](https://firebase.google.com/docs/database/rest/start)
  * **Tip:** Hvorfor `.json`? Firebase's REST API kræver, at du tilføjer `.json` i slutningen af din URL for at fortælle, at du vil interagere med data i JSON-format. Glemmer du det, får du en fejl.
