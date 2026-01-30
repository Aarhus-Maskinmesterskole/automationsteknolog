# Open User Communication

## TCON & TDISCON

<a name="subsec:tcon_tdiscon_plc_communication"></a>

**Mål:** Formålet med denne opgave er at konfigurere og teste kommunikationen mellem to SIMATIC S7-1500 PLC'er ved brug af TCON (Transport Control Protocol) og TDISCON over et industrielt Ethernet-netværk. Opgaven fokuserer på at etablere en simpel TCP-forbindelse, sende og modtage data, samt afslutte forbindelsen korrekt.

**Opgave:**

1. **Forberedelse:**

   * Sørg for, at du har to S7-1500 PLC'er (eller simulerede PLC'er) tilgængelige i TIA Portal.
   * Tildel unikke IP-adresser til begge PLC'er (fx 192.168.1.1 for PLC A og 192.168.1.2 for PLC B) og forbind dem via Ethernet.

2. **Opsætning af TCON/TCP-forbindelse i Siemens PLC A:**

   * Åbn TIA Portal og opret et projekt med PLC A.
   * Tilføj en TCON-funktionsblok i OB1 for at etablere en TCP-forbindelse til PLC B.
   * Angiv IP-adressen på PLC B (192.168.1.2) som destination og konfigurer en passende port (fx 2000).
   * Konfigurer en timeout på forbindelsen, fx 10 sekunder.

3. **Opsætning af TDISCON i Siemens PLC A:**

   * Tilføj en TDISCON-funktionsblok i OB1 for at afslutte TCP-forbindelsen, når kommunikationen er fuldført.
   * Sørg for, at TDISCON aktiveres, når dataudvekslingen er færdig, eller ved fejl.

4. **Opsætning af TSEND og TRECV-funktionsblokke i Siemens PLC B:**

   * Opret et projekt med PLC B og tilføj en TRECV-funktionsblok i OB1 for at modtage data fra PLC A.
   * Konfigurer en modtagebuffer og sørg for at overvåge, at data modtages korrekt.
   * Tilføj en TSEND-funktionsblok, der sender en bekræftelsesmeddelelse til PLC A efter modtagelse.

5. **Test af dataudveksling:**

   * Implementer en simpel dataudveksling, hvor PLC A sender en tekststreng eller et heltal til PLC B, og PLC B returnerer en bekræftelse.
   * Overvåg og verificér kommunikationen i TIA Portal ved hjælp af diagnostiske værktøjer.

6. **Fejlhåndtering:**

   * Hvis TCP-forbindelsen fejler, opret et alarm- eller logsystem for at håndtere fejlen.

7. **Dokumentation:**

   * Dokumentér TCP-forbindelsens opsætning med skærmbilleder af TCON, TDISCON, TSEND og TRECV konfigurationer.
   * Udarbejd et netværksdiagram, der viser IP-adresser og forbindelsen mellem PLC A og PLC B.

**Krav:**

* Forståelse af konfiguration og fejlfinding af TCON og TDISCON blokke i TIA Portal.
* Grundlæggende viden om TCP/IP-protokollen og netværkskommunikation i industrielle miljøer.

## TSEND\_C & TRCV\_C (Consistent Data Exchange)

<a name="subsec:tsendc_trcvc_plc_communication"></a>

**Mål:** Formålet med denne øvelse er at oprette konsistent dataudveksling mellem to SIMATIC S7-1500 PLC'er ved brug af de konsistente datakommunikationsblokke TSEND\_C og TRCV\_C. Fokus er på forståelsen af konsistent datatransmission i et industrielt Ethernet-netværk.

**Opgave:**

1. **Forberedelse:**

   * Sørg for at have to SIMATIC S7-1500 PLC'er (eller simulerede PLC'er) til rådighed i TIA Portal.
   * Tildel unikke IP-adresser til begge PLC'er (fx 192.168.1.3 for PLC A og 192.168.1.4 for PLC B).

2. **Opsætning af TSEND\_C-funktionsblok i PLC A:**

   * Opret et projekt for PLC A i TIA Portal og tilføj TSEND\_C-funktionsblokken til OB1.
   * Definer et datasæt (fx en array af heltal) til overførsel fra PLC A til PLC B.
   * Konfigurer en timeout for TSEND\_C-blokken og forbind den til den definerede datablok.

3. **Opsætning af TRCV\_C-funktionsblok i PLC B:**

   * Opret et projekt for PLC B i TIA Portal og tilføj TRCV\_C-funktionsblokken til OB1.
   * Definer en modtagebuffer til de data, der modtages fra PLC A.
   * Konfigurer kvitteringsmekanismer til at bekræfte korrekt modtagelse af data.

4. **Test af dataudveksling:**

   * Send et simpelt datasæt fra PLC A til PLC B og verificer modtagelsen i TRCV\_C-blokken.
   * Test kvitteringsmekanismen for at sikre konsistensen af dataoverførslen.

5. **Fejlhåndtering:**

   * Implementer en fejlhåndteringsrutine, der logger fejl, hvis dataoverførslen fejler.

6. **Dokumentation:**

   * Tag skærmbilleder af opsætningen af TSEND\_C og TRCV\_C blokke, samt den modtagne data i PLC B.
   * Udarbejd et netværksdiagram med IP-adresser og forbindelser mellem de to PLC'er.

**Krav:**

* Forståelse for opsætning af TSEND\_C og TRCV\_C blokke.
* Evne til at fejlsøge og sikre konsistent dataoverførsel mellem to PLC'er.

## TMAIL\_C (E-mail Notification)

<a name="subsec:tmailc_plc_communication"></a>

**Mål:** I denne øvelse skal de studerende konfigurere og anvende TMAIL\_C-funktionsblokken til at sende e-mails fra en SIMATIC S7-1500 PLC. Formålet er at anvende e-mailbeskeder til at kommunikere fejlmeddelelser eller statusopdateringer i et industrielt miljø.

**Opgave:**

1. **Forberedelse:**

   * Sørg for at have en SIMATIC S7-1500 PLC eller en simuleret PLC til rådighed i TIA Portal.
   * Tildel en IP-adresse til PLC'en (fx 192.168.1.5) og sørg for, at den er forbundet til netværket med adgang til en SMTP-server.

2. **Opsætning af TMAIL\_C i TIA Portal:**

   * Tilføj TMAIL\_C-funktionsblokken til OB1 i dit projekt.
   * Indtast SMTP-serverens oplysninger, fx IP-adressen på mailserveren (SMTP), port (25 eller 587), og de nødvendige loginoplysninger til e-mail-kontoen.
   * Definer en e-mailbesked, der skal sendes i tilfælde af en fejl, fx "Fejl i linje 1, status = stop".

3. **Test af e-mailafsendelse:**

   * Konfigurer et simpelt testsystem, hvor en bestemt tilstand (fx en fejl eller alarmer) udløser en e-mailbesked.
   * Verificer, at e-mailen sendes korrekt ved at observere e-mailklientens indbakke.

4. **Fejlhåndtering:**

   * Implementer fejlhåndteringsmekanismer, der logger, hvis e-mailen ikke kunne sendes (fx netværksfejl eller manglende SMTP-forbindelse).

5. **Dokumentation:**

   * Dokumentér konfigurationen af TMAIL\_C med skærmbilleder, der viser SMTP-indstillinger og e-mailoplysninger.
   * Tag skærmbilleder af en succesfuld afsendelse af en test-e-mail.

**Krav:**

* Forståelse af opsætning af e-mailkommunikation ved hjælp af TMAIL\_C-blokken.
* Evne til at fejlsøge og sikre korrekt opsætning af SMTP-server og e-mailafsendelse fra en PLC.
