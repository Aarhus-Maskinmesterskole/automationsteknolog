# Opgave 4: ESP32 + DHT11 som Modbus TCP server

## Mål

Læs temperatur og fugtighed fra en DHT11 og gør værdierne tilgængelige via Modbus TCP.

## Hardware

* ESP32
* DHT11
* GPIO `4`

## Du skal

1. Forbinde ESP32 til WiFi.
2. Oprette en Modbus TCP server på port `502`.
3. Oprette to holding registers.
4. Skrive temperatur og fugtighed ind i registrene.
5. Opdatere målingen med et passende interval.

## Modbus-adresser

* Holding register `0` = temperatur x `10`
* Holding register `1` = fugtighed x `10`

## Test i Node-RED

* Brug `modbus read`
* Function = `Read Holding Registers (FC3)`
* Address = `0`
* Quantity = `2`

## Godkendt når

* Du kan læse to værdier i Node-RED
* Du kan omregne værdierne korrekt ved at dividere med `10`