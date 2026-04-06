# Opgave 1: ESP32 + gul LED som Modbus TCP server

## Mål

Lav en Modbus TCP server på ESP32, så en gul LED kan tændes og slukkes fra Node-RED.

## Hardware

* ESP32
* Gul LED med modstand
* GPIO `12`

## Du skal

1. Forbinde ESP32 til WiFi.
2. Oprette en Modbus TCP server på port `502`.
3. Oprette en coil på adresse `0`.
4. Lade coil `0` styre LED'en.

## Modbus-adresse

* Coil `0` = gul LED

## Test i Node-RED

* Brug `modbus write`
* Function = `Coil (FC5)`
* Address = `0`
* Payload = `true` eller `false`

## Godkendt når

* LED'en tænder ved `true`
* LED'en slukker ved `false`