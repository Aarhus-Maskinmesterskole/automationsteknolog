# 02 – Hvad er Ethernet/IP og pycomm3?

## Hvad er Ethernet/IP?

Ethernet/IP (Ethernet Industrial Protocol) er en åben industri-protokol, der bruges til at kommunikere med PLC'er og andre automationsenheder over Ethernet. Den bygger på standard Ethernet-teknologi og TCP/IP, men tilføjer et lag til industriel dataudveksling.

**Typiske egenskaber:**
- Bruges især til Allen-Bradley/AB (Rockwell) PLC'er (ControlLogix, CompactLogix m.fl.)
- Kommunikation foregår via IP-adresse og port 44818
- Understøtter både cyklisk (I/O) og acyklisk (explicit message) dataudveksling

## Hvad er pycomm3?

`pycomm3` er et Python-bibliotek, der gør det nemt at kommunikere med Allen-Bradley PLC'er via Ethernet/IP. Det håndterer alt det tekniske i protokollen, så du kan læse og skrive tags direkte fra Python.

**Fordele:**
- Simpelt API: Læs og skriv tags med få linjer kode
- Understøtter symbolsk adgang til tags (du bruger tag-navnet, ikke adresse)
- Kan bruges til både læsning, skrivning og overvågning

## Symbolsk adgang til tags

Når du bruger pycomm3, tilgår du PLC'ens tags symbolsk – dvs. du bruger tag-navnet præcis som det står i PLC-programmet (fx `Motor_Status`, `Tank_Level`, `Start_PB`).

**Eksempel:**
- Læsning: `plc.read('Motor_Status')`
- Skrivning: `plc.write(('Start_PB', True))`

Du behøver altså ikke kende den fysiske adresse (som i Modbus eller S7), men kun navnet på tagget. Det gør det nemt og overskueligt, især i større projekter.

## Sammenligning: Symbolsk vs. adressebaseret

- Symbolsk (pycomm3, Allen-Bradley): Brug tag-navn, fx `Motor_Status`
- Adressebaseret (Modbus, Siemens S7): Brug adresse, fx DB1.DBX0.0 eller 40001

**Fordel ved symbolsk:**
- Mindre risiko for fejl
- Kode og PLC-program matcher direkte
- Let at vedligeholde

## Typisk brug

1. Installer pycomm3: `pip install pycomm3`
2. Find PLC'ens IP-adresse
3. Brug tag-navne fra PLC-programmet i din Python-kode

**Bemærk:**
- Du skal have adgang til PLC'ens tag-navne (navngivning i controlleren)
- Nogle tags kan være beskyttede eller kræve særlige rettigheder

---

**Kort opsummering:**
- Ethernet/IP bruges til at kommunikere med Allen-Bradley PLC'er over netværk
- pycomm3 gør det let at læse/skrive tags fra Python – du bruger altid tag-navnet (symbolsk adgang)
