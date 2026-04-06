# Python-filer til Dag08

Filerne i denne mappe matcher kodeblokkene i `.md`-opgaverne `01` til `09`.

## Modbus-bibliotek

Brug MicroPython-biblioteket i mappen `micropython-modbus-develop/umodbus`.

Kopiér `umodbus` til ESP32 sådan:

```bash
mpremote u0 mkdir :lib
mpremote u0 cp -r micropython-modbus-develop/umodbus :lib/
```

## LCD-opgaven

Til LCD-opgaven skal du også kopiere disse to filer til ESP32:

```bash
mpremote u0 cp lcd_api.py :lcd_api.py
mpremote u0 cp i2c_lcd.py :i2c_lcd.py
```

## Bemærk

Brug `micropython-modbus-develop`, ikke desktop-biblioteket `uModbus` fra PyPI/GitHub til almindelig Python.