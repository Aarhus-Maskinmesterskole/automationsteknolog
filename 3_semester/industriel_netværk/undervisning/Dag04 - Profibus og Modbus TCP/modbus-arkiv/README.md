# 🏭 AAMS Industrielt Netværk - Modbus TCP Opgaver

**Underviser:** Anders S. Østergaard  
**Dato:** 2. september 2025  
**GitHub:** @sandoe

## 📋 Formål

Disse opgaver er designet til at give praktisk erfaring med **Modbus TCP kommunikation** i industrielle netværk. Du lærer at:

- 🔗 Etablere kommunikation mellem Siemens S7 PLC'er
- 📡 Konfigurere IP netværk til industriel automation
- 🐍 Integrere IT systemer (Python, Node-RED) med OT udstyr
- 🔧 Fejlsøge netværksproblemer i industrielle miljøer
- 📊 Implementere data indsamling og visualisering

## 🎯 Læringsmål

Efter gennemførelse af opgaverne kan du:

✅ **Netværk:** Konfigurere IP adresser og subnets til industrielle enheder  
✅ **Modbus TCP:** Implementere server/client kommunikation mellem PLC'er  
✅ **TIA Portal:** Opsætte Ethernet kommunikation og Modbus instruktioner  
✅ **PLCsim:** Arbejde med virtuelle PLC'er i simulerede miljøer  
✅ **Integration:** Forbinde IT systemer til industrielle netværk  
✅ **Fejlsøgning:** Diagnosticere og løse kommunikationsproblemer

## 📚 Opgave Oversigt

### 🔧 Opgave 1: To PLC'er - Grundlæggende Modbus
**Mål:** Få to fysiske S7-1200 PLC'er til at kommunikere via Modbus TCP

- 🖥️ **Setup:** S7-1200 (Server) ↔ S7-1200 (Client)
- 🌐 **Netværk:** /29 subnet (192.168.1.1-3)
- 📊 **Data:** Simpel INT værdi udveksling
- ⚡ **Fokus:** Grundlæggende Modbus TCP opsætning

---

### 💻 Opgave 2: Fysisk + Virtual - PLCsim Integration  
**Mål:** Kombiner fysisk PLC med PLCsim simulation

- 🖥️ **Setup:** S7-1200 (Fysisk Server) ↔ PLCsim S7-1200 (Virtual Client)
- 🌐 **Netværk:** /24 subnet (192.168.1.10-12)
- 📊 **Data:** Process data (temperatur, tryk, status)
- ⚡ **Fokus:** Virtual/fysisk integration og PLCsim netværk

---

### 🚀 Opgave 3: S7-1200 + S7-1500 - Hybrid Arkitektur
**Mål:** Feltstation kommunikerer med SCADA controller

- 🖥️ **Setup:** S7-1200 (Fysisk) ↔ PLCsim Advanced S7-1500 (Virtual)
- 🌐 **Netværk:** /24 subnet (192.168.1.10-12)
- 📊 **Data:** Simpel INT register læsning
- ⚡ **Fokus:** Realistisk industriel arkitektur

---

### 🌐 Opgave 4: Node-RED Dashboard - Multi-PLC Monitoring
**Mål:** Web-baseret overvågning af multiple PLC'er

- 🖥️ **Setup:** Node-RED Client ↔ S7-1200 + S7-1500 Servers
- 🌐 **Netværk:** /24 subnet (192.168.1.10-12)
- 📊 **Data:** Live dashboard med gauges og trends
- ⚡ **Fokus:** IT/OT integration og data visualisering

---

### 🐍 Opgave 5: Python Client - Programmatisk Data Access
**Mål:** Custom Python applikation til PLC data læsning

- 🖥️ **Setup:** Python Script ↔ S7-1200 (Server)
- 🌐 **Netværk:** /24 subnet (192.168.1.10-11)
- 📊 **Data:** Real-time data logging og alarm håndtering
- ⚡ **Fokus:** Programmatisk Modbus implementation

## 🛠️ Forudsætninger

### Hardware
- 🔧 Siemens S7-1200 PLC(er)
- 🖥️ PC med Windows 10/11
- 🌐 Ethernet switch
- 🔌 Netværkskabler

### Software
- 📊 TIA Portal v17+ (med S7-1200/1500 licens)
- 🔄 PLCsim / PLCsim Advanced
- 🐍 Python 3.7+ (til opgave 5)
- 🌐 Node.js + Node-RED (til opgave 4)

### Netværk Viden
- 🌐 Grundlæggende TCP/IP forståelse
- 📡 Subnet masking (/24, /29, /30)
- 🔍 Ping og telnet kommandoer
- 🛠️ Grundlæggende fejlsøgning
