# Opgave 3: ESP32 + blæser som Modbus TCP server

## Mål

Styr en blæser fra Node-RED ved at skrive til en coil.

## Hardware

* ESP32
* Blæser eller motor-driver
* GPIO `18` og `19`

## Du skal

1. Forbinde ESP32 til WiFi.
2. Oprette en Modbus TCP server på port `502`.
3. Oprette en coil på adresse `0`.
4. Bruge coil `0` til at tænde og slukke blæseren.

## Modbus-adresse

* Coil `0` = blæser ON/OFF

## Test i Node-RED

* Brug `modbus write`
* Function = `Coil (FC5)`
* Address = `0`
* Payload = `true` eller `false`

## Godkendt når

* Blæseren starter ved `true`
* Blæseren stopper ved `false`