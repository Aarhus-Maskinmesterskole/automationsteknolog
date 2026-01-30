# Opsætning af Webserver

<a name="subsec:webserver_simulated_physical_plc"></a>

**Mål:** Målet med denne opgave er at opsætte og konfigurere en webserver på en fysisk SIMATIC S7-1200 PLC og en simuleret S7-1500 PLC ved hjælp af Siemens PLCSIM Advanced. Opgaven giver praktisk erfaring med webserverfunktionalitet på en PLC og dens anvendelse til overvågning og kontrol af industrielle processer.

**Opgavebeskrivelse:**

1. **Konfiguration af PLC A (S7-1200 som Webserver):**

   * Opret et nyt projekt i TIA Portal og tilføj en fysisk S7-1200 PLC.
   * Tildel en IP-adresse til PLC'en, fx `192.168.0.1`, og konfigurer de nødvendige netværksparametre.
   * Aktiver webserveren i PLC-indstillingerne under `Properties`.
   * Opret en simpel webside ved hjælp af TIA Portal, der viser vigtige procesdata som sensordata og maskinstatus.

2. **Konfiguration af PLC B (S7-1500 som Simuleret Webserver):**

   * Tilføj en S7-1500 PLC i TIA Portal og opsæt en simulering med PLCSIM Advanced.
   * Tildel en IP-adresse til den simulerede PLC, fx `192.168.0.2`.
   * Aktivér webserveren på S7-1500 under `Properties`, og opret brugerdefinerede websider for at vise og styre procesdata.
   * Start simuleringen og verificer, at webserveren på den simulerede PLC er tilgængelig via en webbrowser ved at bruge IP-adressen.

3. **Test og Verifikation:**

   * Brug en webbrowser til at tilgå PLC'ernes webservere ved hjælp af deres IP-adresser.
   * Test, at procesdata opdateres i realtid, og at kontrolfunktioner på websiden fungerer korrekt.

4. **Dokumentation:**

   * Dokumentér alle konfigurationsindstillinger med skærmbilleder og opsætninger af websiderne.
   * Udarbejd en kort teknisk rapport med skærmbilleder af webserver-konfigurationerne og testresultater.

**Krav:**

* Grundlæggende forståelse af webservere og deres anvendelse i industriel kommunikation.
* Erfaring med TIA Portal og PLCSIM Advanced.
