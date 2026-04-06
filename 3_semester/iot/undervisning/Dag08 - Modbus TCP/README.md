# 📘 Dag08 – Modbus TCP

Denne mappe er lavet som en enkel øvelsesserie i Modbus TCP med ESP32.

Målet er, at læser opgaven, forstår hvad der skal bygges, og derefter selv skriver og tester løsningen.

## Sådan bruges materialet

Arbejdsgangen er tænkt sådan:

1. Læs `.md`-filen for opgaven.
2. Byg kredsløbet og vælg de rigtige GPIO-pins.
3. Skriv selv koden på ESP32.
4. Test fra Node-RED via Modbus TCP.
5. Sammenlign først bagefter med referencefilerne i `python`-mappen, hvis det er nødvendigt.

## Opgaver i serien

* `01` Gul LED
* `02` PIR sensor
* `03` Blæser
* `04` DHT11
* `05` Knap
* `06` Vindue-servo
* `07` Dør-servo
* `08` RGBW LED
* `09` LCD display
* `10` Afsluttende IoT house-opgave

## Fælles ramme

* ESP32 skal være Modbus TCP server
* Port er `502`
* Brug `coils` til ON/OFF
* Brug `holding registers` til tal
* Test opgaverne fra Node-RED

## Om `python`-mappen

`python`-mappen er reference og facit-støtte.

Den er ikke tænkt som det første som i skal have udleveret.

Der ligger også hjælperfiler til nogle af opgaverne:

* `umodbus`
* `lcd_api.py`
* `i2c_lcd.py`

## Afsluttende mål

Når delopgaverne er gennemført, skal i kunne samle flere sensorer og aktuatorer i ét samlet Modbus TCP "hus".
