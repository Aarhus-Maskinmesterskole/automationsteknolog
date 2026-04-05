# 💻 Opgave 2: Logik, Kodning og Dokumentation

Nu skal vi ned i bunden af V'et. Her skal vi designe den præcise logik og implementere koden. I dag er der særligt fokus på, at koden er læsbar og veldokumenteret.

### 2.1 Flowchart eller State Machine
Før I koder, skal I tegne logikken.
*   Lav et flowchart over jeres Python-hovedloop.
*   Hvordan håndteres logik og fejlhåndtering?

### 2.2 Implementering med god stil
Skriv jeres Python-kode. I skal bruge følgende elementer:
*   **Snap7:** Kommunikation med PLC.
*   **Logging:** Skriv data til en CSV-fil.
*   **Docstrings:** Alle jeres funktioner skal have en beskrivelse i toppen:
    ```python
    def read_plc_data(address):
        """
        Læser data fra PLC'en på den angivne adresse.
        :param address: Int, startadressen i DB1
        :return: Bytearray med rå data
        """
        # Kode her...
    ```

### 2.3 Teknisk Dokumentation (Kommentarer)
Sørg for at jeres kode ikke bare virker, men er let at læse for andre. Brug kommentarer til at forklare *hvorfor* I gør som I gør, ikke bare *hvad* koden gør.

---

### ✅ Output for Opgave 2:
- Et flowchart over programlogikken.
- En funktionel Python-fil med docstrings og logning.
