# Opgave 5: ESP32 + knap som Modbus TCP server

## Mål

Læs en knap i Node-RED som coil og gem antal tryk i et holding register.

## Hardware

* ESP32
* Knap
* GPIO `16`

## Du skal

1. Forbinde ESP32 til WiFi.
2. Oprette en Modbus TCP server på port `502`.
3. Oprette coil `0` til knapstatus.
4. Oprette holding register `1` til antal tryk.
5. Lave debounce, så ét fysisk tryk ikke tælles flere gange.

## Modbus-adresser

* Coil `0` = knapstatus
* Holding register `1` = antal tryk

## Test i Node-RED

Til knapstatus:

* Brug `modbus read`
* Function = `Read Coils (FC1)`
* Address = `0`
* Quantity = `1`

Til tælleren:

* Brug `modbus read`
* Function = `Read Holding Registers (FC3)`
* Address = `1`
* Quantity = `1`

## Godkendt når

* Node-RED kan se om knappen er trykket
* Tælleren stiger med `1` for hvert reelt tryk