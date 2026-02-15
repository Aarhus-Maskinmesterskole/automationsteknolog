# S7-Communication

Før du begynder at løse netværksopgaverne i TIA Portal, er det vigtigt at du har forståelse for de forskellige metoder til dataoverførsel og netværkskommunikation. Følgende afsnit vil give dig indsigt i de vigtigste kommunikationsblokke og deres anvendelsesområder. Dette vil danne grundlaget for de praktiske opgaver, du skal udføre.

## Kommunikationsblokke og deres Anvendelse

**BSEND**

* **Datatyper:**

  * **Store Datasæt:** Egnet til at sende større datasæt som komplette datasæt, konfigurationsfiler eller batchprocesdata.
  * **Komplekse Strukturer:** Kan håndtere komplekse datastrukturer, herunder arrays, records eller multi-dimensionelle data.
  * **Kritisk Kontroldata:** Bruges til at transmittere kritisk kontrolinformation, såsom setpunkter, kontrolparametre eller systemtilstande.
* **Brugstilfælde:**

  * **Batchbehandling:** Overførsel af hele batches af data i fremstillingsprocesser.
  * **Konfigurationsoverførsler:** Initiering eller opdatering af systemkonfigurationer.
  * **Kvalitetskontroldata:** Transmitterer detaljerede kvalitetskontroldata til analyse.
  * **Synkronisering af Tilstand:** Holder systemer synkroniseret ved at sende omfattende tilstandsoplysninger.

**TSEND\_C**

* **Datatyper:**

  * **Almindelige Datasæt:** Brugt til almindelig dataoverførsel såsom statusopdateringer og kontrolsignaler.
  * **Strukturerede Data:** Kan håndtere simple strukturer og mindre datasæt.
* **Brugstilfælde:**

  * **Realtidskommunikation:** Bruges til realtidsdataudveksling mellem PLC og andre systemer, fx HMI'er.
  * **Integrering med IT-systemer:** Muliggør kommunikation med IT-systemer eller andre enheder via standard TCP/IP.

**TSEND**

* **Datatyper:**

  * **Sekventielle Data:** Velegnet til overførsel af data i sekventielle eller kontinuerlige strømme.
  * **Mindre Datasæt:** Ideel til mindre, hyppigt opdaterede datasæt.
* **Brugstilfælde:**

  * **Data Logging:** Sender data kontinuerligt til en datalogger.
  * **Overvågning:** Overfører statusopdateringer til overvågningssystemer.

**PUT**

* **Datatyper:**

  * **Enkelte Variabler:** Overfører specifikke dataelementer, såsom enkelte variabler eller små datasæt.
  * **Kritiske Opdateringer:** Egnet til at sende kritiske opdateringer eller kontrolsignaler.
* **Brugstilfælde:**

  * **Direkte PLC-til-PLC Kommunikation:** Anvendes til simpel og direkte dataoverførsel mellem to PLC'er.
  * **Kontrolkommandoer:** Sender kontrolkommandoer til en anden PLC.

**GET**

* **Datatyper:**

  * **Enkelte Variabler:** Henter specifikke dataelementer fra en anden PLC.
  * **Mindre Datasæt:** Henter små datasæt til brug i kontrolprogrammer.
* **Brugstilfælde:**

  * **Data Retrieval:** Bruges til at hente aktuelle værdier fra en anden PLC til overvågning eller videre behandling.
  * **Tilstandsopdateringer:** Modtager opdateringer om systemtilstand fra andre enheder.

**USEND**

* **Datatyper:**

  * **Pakker:** Sender data i form af individuelle pakker.
  * **Best Effort Data:** Velegnet til data, hvor pålidelighed ikke er kritisk.
* **Brugstilfælde:**

  * **Broadcast Kommunikation:** Sender data til flere modtagere i et netværk.
  * **Ikke-kritiske Opdateringer:** Bruges til opdateringer, hvor tab af data kan tolereres, såsom periodiske statusmeddelelser.

---

## PUT-metode

<a name="subsec:put_method_plc_communication_simplified"></a>

**Mål:** Denne opgave har til formål at guide dig gennem den grundlæggende konfiguration og anvendelse af PUT-metoden til dataoverførsel mellem en fysisk SIMATIC S7-1200 PLC og en simuleret SIMATIC S7-1500 PLC. Fokus er på simpel PLC-til-PLC kommunikation uden at inddrage produktionslinjer eller avancerede scenarier.

**Opgave:**

1. **Forberedelse:**

   * Sørg for, at du har både en fysisk S7-1200 PLC og en simuleret S7-1500 PLC tilgængelige i TIA Portal. Alternativt kan to simulerede PLC'er anvendes.
   * Giv hver PLC en unik IP-adresse (fx 192.168.0.1 for S7-1200 og 192.168.0.2 for S7-1500).

2. **Opsætning af PUT-funktionsblok i sender-PLC (S7-1200):**

   * Tilføj en PUT-funktionsblok i S7-1200 PLC'ens OB1-program.
   * Brug følgende parametre:

     * **ID**: 1 (fast værdi).
     * **ADDR**: IP-adressen for modtageren (fx 192.168.0.2 for S7-1500).
     * **SRC**: En variabel, der indeholder de data, du ønsker at sende (fx et heltal).
     * **LEN**: Datalængde (fx 1, hvis du kun sender en enkelt værdi som et heltal).
   * Aktivér PUT-funktionsblokken ved at sætte `REQ` høj, når både `DONE` og `ERROR` er inaktive.

3. **Opsætning af modtagerfunktion i modtager-PLC (S7-1500):**

   * I S7-1500 PLC'en skal du opsætte en modtagerfunktion (fx en variabel eller buffer), der vil gemme de data, der modtages fra sender-PLC'en.
   * Overvåg modtagefunktionen for at sikre, at dataene lagres korrekt.

4. **Test af dataoverførsel:**

   * Test dataoverførslen ved at sende en simpel dataværdi (fx heltallet 10) fra sender-PLC'en (S7-1200) til modtager-PLC'en (S7-1500).
   * Verificér, at modtager-PLC'en modtager og gemmer data korrekt i den angivne modtagerbuffer.

5. **Opsætning af flere modtagere (valgfrit):**

   * Hvis du ønsker flere modtagere, kan du opsætte flere PUT-funktionsblokke i sender-PLC'en og tildele unikke IP-adresser til de modtagende PLC'er.

6. **Dokumentation:**

   * Lav et simpelt netværksdiagram, der viser IP-adresserne for sender- og modtager-PLC'erne.
   * Tag skærmbilleder af opsætningen i TIA Portal for PUT-funktionsblokken og modtagerbufferen.

**Krav:**

* Grundlæggende forståelse for PLC-kommunikation og TIA Portal.
* Evne til at konfigurere PUT-funktionsblokke til dataoverførsel mellem to PLC'er.

**Note:** Dette er en simpel konfigurationsopgave. Når kommunikationen fungerer, kan opgaven udvides til at omfatte flere modtagere eller mere komplekse datastrukturer.

---

## GET-metode

<a name="subsec:get_method_plc_communication_simplified"></a>

**Mål:** Formålet med denne opgave er at konfigurere og anvende GET-metoden til at hente data mellem to SIMATIC S7-1500 PLC'er. Fokus er på at etablere en simpel kommunikation, hvor én PLC fungerer som datakilde, og den anden PLC henter dataene uden at inddrage komplekse scenarier eller simulering af produktionslinjer.

**Opgave:**

1. **Forberedelse:**

   * Sørg for, at du har to PLC'er til rådighed i TIA Portal (det kan være både fysiske eller simulerede PLC'er).
   * Tildel unikke IP-adresser til begge PLC'er, fx 192.168.0.1 for kildens PLC og 192.168.0.2 for den modtagende PLC.

2. **Opsætning af GET-funktionsblok:**

   * I kildens PLC, opret et datalager (fx en global variabel), der indeholder de data, der skal hentes af den modtagende PLC.
   * I den modtagende PLC, opret en GET-funktionsblok i OB1.
   * Brug følgende parametre i GET-funktionsblokken:

     * **ID**: 1
     * **ADDR**: IP-adressen for kildens PLC (fx 192.168.0.1).
     * **DATA**: En modtagebuffer (fx en variabel, hvor de hentede data skal lagres).
   * Aktivér GET-funktionsblokken ved at sætte `REQ` høj, når både `DONE` og `ERROR` er inaktive.

3. **Test af datahentning:**

   * Test datahentningen ved at konfigurere GET-funktionsblokken til at hente simple data, fx en integer-værdi (fx 10) fra kildens PLC og gemme den i modtagerens buffer.
   * Verificér, at GET-funktionsblokken modtager og lagrer data korrekt ved at overvåge `DONE`-variablen og kontrollere modtagebufferen.

4. **Opsætning af flere modtagere (valgfrit):**

   * Hvis du ønsker flere modtagere, kan du opsætte flere GET-funktionsblokke på forskellige PLC'er, der alle henter data fra den samme kilde.
   * Sørg for, at hver modtager har en korrekt konfigureret GET-funktionsblok og unikke IP-adresser.

5. **Dokumentation:**

   * Udarbejd et simpelt netværksdiagram, der viser IP-adresserne for kildens PLC og de modtagende PLC'er.
   * Tag skærmbilleder af opsætningen i TIA Portal, herunder GET-funktionsblokkene og de data, der hentes.

**Krav:**

* Grundlæggende forståelse for PLC-kommunikation og TIA Portal.
* Evne til at konfigurere GET-funktionsblokke til datahentning mellem to PLC'er.

**Note:** Dette er en simpel konfigurationsopgave. Når kommunikationen fungerer, kan opgaven udvides til at omfatte flere modtagere eller mere avanceret dataoverførsel.

---

# S7-Communication Others

## USEND & URCV

<a name="subsec:usend_urcv_plc_communication"></a>

**Mål:** Denne opgave har til formål at guide dig gennem den grundlæggende konfiguration af USEND- og URCV-funktionsblokke mellem to PLC'er, hvor den ene fungerer som sender og den anden som modtager. Opgaven fokuserer på opsætning af simpel kommunikation uden scenarier eller komplekse datastrukturer.

**Opgave:**

1. **Forberedelse:**

   * Sørg for, at du har to PLC'er (eller en fysisk PLC og en simuleret PLC) tilgængelige i TIA Portal.
   * Giv hver PLC en unik IP-adresse (fx 192.168.0.1 for senderen og 192.168.0.2 for modtageren).

2. **Opsætning af USEND i sender-PLC (S7-1200):**

   * Tilføj en USEND-funktionsblok i sender-PLC'ens OB1-program.
   * Brug følgende enkle parametre:

     * **ID**: 1
     * **LEN**: 1 (enkel datalængde, fx en integer).
     * **DEST**: 192.168.0.2 (IP-adressen på modtageren).
     * **SRC**: En variabel (fx et heltal) du ønsker at sende.
   * Aktivér USEND-funktionsblokken ved at sætte `REQ` høj, når både `DONE` og `ERROR` er inaktive.

3. **Opsætning af URCV i modtager-PLC (S7-1500):**

   * I modtager-PLC'ens OB1-program, tilføj en URCV-funktionsblok.
   * Konfigurer følgende parametre:

     * **ID**: 1 (svarende til sender-PLC'en).
     * **ADDR**: En modtagerbuffer (fx en integer-variabel) til at gemme de modtagne data.
     * **NDR**: Denne variabel bliver høj, når data er modtaget korrekt.

4. **Opsætning af flere modtagere (valgfrit):**

   * Hvis du ønsker at tilføje flere modtagere, skal du gentage opsætningen af URCV-funktionsblokken på hver modtager-PLC og tildele dem en unik IP-adresse (fx 192.168.0.3 for en tredje PLC).
   * Sørg for, at USEND-blokken i sender-PLC'en konfigureres med de relevante IP-adresser for hver modtager.

5. **Test af kommunikation:**

   * Test dataoverførslen ved at sende et simpelt heltal (fx værdien 10) fra sender-PLC'en og verificér, at modtager-PLC'en korrekt modtager og lagrer værdien i den opsatte buffer.
   * Overvåg `NDR`-variablen i URCV-blokken for at sikre, at data modtages korrekt.

6. **Dokumentation:**

   * Lav et simpelt netværksdiagram, der viser IP-adresserne på sender og modtagere.
   * Tag skærmbilleder af din opsætning i TIA Portal for både USEND og URCV.

**Krav:**

* Grundlæggende forståelse af PLC-kommunikation og netværksopsætning i TIA Portal.
* Evne til at konfigurere og teste USEND- og URCV-funktionsblokke.

**Note:** Dette er en simpel konfigurationsopgave. Når kommunikationen fungerer, kan opgaven udvides til at omfatte flere modtagere eller mere avanceret dataoverførsel.
