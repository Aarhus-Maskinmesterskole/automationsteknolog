# Opgave 2: ESP32 + PIR som Modbus TCP server

## Mål

Læs en PIR-sensor på ESP32 og gør sensorens status tilgængelig via Modbus TCP.

## Hardware

* ESP32
* PIR sensor
* GPIO `14`

## Du skal

1. Forbinde ESP32 til WiFi.
2. Oprette en Modbus TCP server på port `502`.
3. Oprette et holding register på adresse `0`.
4. Skrive sensorens aktuelle værdi til registeret.

## Modbus-adresse

* Holding register `0` = PIR status

## Test i Node-RED

* Brug `modbus read`
* Function = `Read Holding Registers (FC3)`
* Address = `0`
* Quantity = `1`

## Godkendt når

* Du kan læse `0` når der ikke er bevægelse
* Du kan læse `1` når der er bevægelse