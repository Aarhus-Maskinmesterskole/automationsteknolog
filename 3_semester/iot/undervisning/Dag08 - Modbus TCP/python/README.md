# Python-filer til Dag08

Denne mappe er reference til læreren eller til eleverne bagefter.

`.md`-filerne i hovedmappen er selve opgaverne.

`.py`-filerne her er løsningsforslag og testfiler.

## Indhold

* `01` til `09` matcher de enkelte delopgaver
* `umodbus` er MicroPython-biblioteket der skal kopieres til ESP32
* `lcd_api.py` og `i2c_lcd.py` bruges til LCD-opgaven

## Brug af mappen

Tanken er:

* Eleverne læser først opgavebeskrivelsen i `.md`
* De skriver derefter selv løsningen
* De bruger kun `python`-mappen som støtte eller facit bagefter

## Bemærk

MicroPython-imports som `machine`, `network`, `dht` og `neopixel` kan godt blive markeret som fejl i VS Code på pc'en.

Det er normalt. De moduler findes på ESP32 med MicroPython-firmware.