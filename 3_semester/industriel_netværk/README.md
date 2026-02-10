# 🏭 Industrielt Netværk – PLC, Bus & Industriel Integration

*12 × 3 timer • Aarhus Maskinmesterskole • 2025*

> Hands‑on kursus hvor maskinmestre arbejder med industriel netværksopsætning, protokoller, segmentering og fejlfinding – uden at skulle være netværkseksperter fra starten.

---

## 🎯 Læringsmål

Efter forløbet kan du …

1. **Analysere og opbygge industrielle netværk** (topologi, udstyr, VLAN, subnet).
2. **Sætte adresser og fejlfinde på IP‑ og MAC‑niveau** (GNS3/fysisk).
3. **Segmentere og sikre OT‑trafik** vha. VLAN og access control.
4. **Opsætte og forstå centrale OT‑protokoller:**  
   - Profibus, Profinet, IO-Link, EtherNet/IP, Modbus TCP/RTU
5. **Integrere PLC, HMI og robot (UR/AUBO)** via industrielle protokoller.
6. **Fejlfinde på netværk og protokoller** (ping, traceroute, netværksdokumentation).
7. **Dokumentere, visualisere og præsentere netværksopsætning** for andre (diagram, skriftligt, Github).

---

## 📦 Centrale teknologier & værktøjer

| Kategori     | Værktøj / udstyr                        |
| ------------ | --------------------------------------- |
| Netværk      | GNS3, fysisk switch/router, Siemens PLC |
| Simulation   | GNS3, TIA Portal, Node-RED              |
| Industriel HW| Siemens PLC, Rockwell PLC, UR/AUBO      |
| Protokoller  | Profibus, Profinet, IO-Link, Modbus, EtherNet/IP |
| Analyse      | Ping, traceroute, (Wireshark hvis muligt)|
| Visualisering| Node-RED dashboard (kun OT, ikke IoT)   |
| Sikkerhed    | VLAN, Access-lister, Firewall (GNS3)    |
| Versionsstyring | Git / GitHub                          |

---

## 📁 Repo-struktur

```text
industriel_netværk/
├── README.md                         ← Du er her!
│
├── hardware-og-software/
│   ├── github-use/                   → GitHub guides og tutorials
│   ├── GNS3/                         → GNS3 setup og konfiguration
│   └── GNS3-IMAGE/                   → Router/switch images til GNS3
│
└── undervisning/
    ├── README.md                     → Oversigt over alle dage
    ├── dag01-netværk-og-ip-basic/
    ├── dag02-profinet-og-protokoller/
    ├── dag03-profibus-io-link-teori/
    ├── dag04-rotationsøvelse-1-profibus/
    ├── dag05-modbus-tcp-universial-robots/
    ├── dag06-rockwell/
    ├── dag07-kepserverex-(opc-ua-gateway)/
    ├── dag08-gns3-ping-arp-og-traceroute/
    ├── dag09-gns3-subnet-vlan-segmentering/
    ├── dag11-rotationsøvelse-2-gns3-firewall/
    └── dag12-vpn/
````

> **Bemærk:**
> Hver *dag-mappe* indeholder:
> • **README.md** → Dagens læringsmål, indhold og opgaver
> • **Opgavefiler** (.md) med step-by-step guides
> • **Billeder/diagrammer** til visualisering
> • **Ekstra ressourcer** og bonus-opgaver

---

## 🧩 Moduloversigt

| Dag    | Fokus                                    | Centrale teknologier/værktøjer                |
| ------ | ---------------------------------------- | --------------------------------------------- |
| **01** | [Netværk og IP Basic](undervisning/dag01-netværk-og-ip-basic/) | IP/MAC-adresser, ARP, ping, TIA Portal |
| **02** | [Profinet og Protokoller](undervisning/dag02-profinet-og-protokoller/) | S7comm, OUC (TCON/TDISCON), Web Server, WebSocket |
| **03** | [Profibus & IO-Link Teori](undervisning/dag03-profibus-io-link-teori/) | Bus-principper, master/slave, feltbus-topologi |
| **04** | [Rotationsøvelse 1: Profibus](undervisning/dag04-rotationsøvelse-1-profibus/) | Fysisk Profibus opsætning, fejlfinding |
| **05** | [Modbus TCP & Universal Robots](undervisning/dag05-modbus-tcp-universial-robots/) | Modbus TCP/RTU, UR robot integration |
| **06** | [Rockwell](undervisning/dag06-rockwell/) | Allen-Bradley PLC, EtherNet/IP, Studio 5000 |
| **07** | [KEPServerEX (OPC UA Gateway)](undervisning/dag07-kepserverex-(opc-ua-gateway)/) | OPC UA, protocol translation, data gateway |
| **08** | [GNS3: Ping, ARP og Traceroute](undervisning/dag08-gns3-ping-arp-og-traceroute/) | GNS3 simulation, netværksdiagnostik |
| **09** | [GNS3: Subnet, VLAN, Segmentering](undervisning/dag09-gns3-subnet-vlan-segmentering/) | VLAN configuration, subnetting, routing |
| **10** | _(Pause eller projektarbejde)_ | - |
| **11** | [Rotationsøvelse 2: GNS3 Firewall](undervisning/dag11-rotationsøvelse-2-gns3-firewall/) | Firewall rules, ACL, sikkerhed i OT |
| **12** | [VPN](undervisning/dag12-vpn/) | VPN setup, remote access, sikker forbindelse |

> **💡 Tip:** Klik på dagene ovenfor for at gå direkte til undervisningsmaterialet!

---

## ✅ Slutmål

* Du kan bygge, fejlfinde og dokumentere et industrielt netværk med PLC, bus og segmentering.
* Du kan dokumentere og aflevere dine løsninger i GitHub (markdown + billeder).
* Du kan forklare og demonstrere OT-sikkerhed, netværksdesign og protokolvalg for en industriel case.

---

## 🤝 Hjælp & support

Har du brug for hjælp?
👉 Opret et GitHub issue eller spørg underviseren

---

God arbejdslyst – og velkommen til det industrielle netværksunivers! 🏭🦾
