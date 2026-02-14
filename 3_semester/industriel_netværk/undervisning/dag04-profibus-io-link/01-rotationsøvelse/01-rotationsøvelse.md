# 🔄 Rotationsøvelse 1: Modbus TCP, IO-Link og Profibus

> **Formål:** I denne rotationsøvelse arbejder I praktisk med tre vigtige industrielle kommunikationsprotokoller.

---

## 📡 Del A: Modbus TCP - Siemens S7-1200/S7-1500 Server og Client

### Øvelsesbeskrivelse
I denne øvelse skal du opsætte en Modbus TCP server på en Siemens S7-1200 eller S7-1500 PLC. Brug Emulate3D som Modbus TCP client for at læse data fra PLC'en. 

### Opgave
1. Følg videoen for at lære om konfigurationen
2. Lav et transportbånd med start/stop-knapper som styrer transportbåndet i Emulate3D
3. Når en kasse når enden af transportbåndet, skal den tælle op i PLC'en ved at skrive til et holding register

### 🎥 Video
[Modbus TCP med Emulate3D](https://www.youtube.com/watch?v=WTjcJUzEBSk)

---

## 🔌 Del B: IO-Link - Siemens S7-1200 og IO-Link Master

### Øvelsesbeskrivelse
I denne øvelse skal du opsætte en IO-Link Master fra IFM med forskellige sensorer og forbinde det til en Siemens S7-1200 PLC.

### 🎥 Video
[IO-Link Master konfiguration](https://www.youtube.com/watch?v=6METqn73cJA)

---

## 🌐 Del C: Profibus DP - Siemens S7-1200 og ET 200SP

### Øvelsesbeskrivelse
I denne øvelse skal du opsætte en Profibus DP forbindelse mellem en Siemens S7-1200 PLC og en ET 200SP station. Du skal konfigurere kommunikationen og læse/skrive data til de digitale moduler i den decentrale I/O station. 

### Opgave
Dokumentér hvordan man konfigurerer en Profibus DP forbindelse i TIA Portal - tilsvarende opgaven i [dag03-profibus-modbus-tcp/02-profibus-decentral-io.md](../dag03-profibus-modbus-tcp/02-profibus-decentral-io.md)

### 📝 Fokuspunkter
- Master/slave konfiguration
- Digital I/O moduler
- Adressering af decentral I/O
- Test af kommunikation

OBS! Rapporten skal dokumenteres med god forklaring og billeder (husk figur tekst) af konfigurationen for netværket.