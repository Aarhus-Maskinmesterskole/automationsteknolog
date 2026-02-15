# 🛤️ Dag 10 – Statisk Routing & Route Management

Velkommen til dag 10 af Industrielt Netværk!

> I dag går vi i dybden med statisk routing – det fundament som ALLE industrielle netværk bygger på. I lærer at bygge routing-tabeller, prioritere ruter, håndtere redundans og undgå routing loops.

---

## 🎯 Læringsmål for dagen

- Forstå hvorfor industrielle netværk bruger statisk routing i stedet for dynamisk routing
- Kunne læse og forstå routing-tabeller (`ip route show`, `route -n`)
- Konfigurere statiske ruter mellem flere netværkszoner
- Implementere redundante ruter og forstå route metrics/prioritering
- Identificere og løse routing loops
- Dokumentere routing-topologier med klare netværksdiagrammer

---

## 📚 Dagens indhold

- **Mini-forelæsning:**  
  - Hvorfor statisk routing i OT-netværk?
  - Routing-tabeller og route lookup
  - Metrics, prioritering og redundans
  - Routing loops og TTL
  - Best practices for industriel routing
  
- **Hands-on i GNS3:**
    1. [Grundlæggende statisk routing - 3 netværkszoner](01-basic-static-routing/README.md)
    2. [Multi-router topologi - flere hop](02-multi-router/README.md)
    3. [Redundante ruter og failover](03-redundancy/README.md)
    4. [Fejlfinding: Routing loops og fejlkonfiguration](04-troubleshooting/README.md)

---

## 🛠️ Opgaver

| #   | Titel                                    | Type              | Aflevering          |
|-----|------------------------------------------|-------------------|---------------------|
| 1   | 3-zoners routing (OT, DMZ, IT)           | Individuel/gruppe | `.md` + diagram     |
| 2   | Multi-router netværk                     | Individuel/gruppe | `.md` + route tables|
| 3   | Redundans og backup routes               | Individuel        | `.md` + test        |
| 4   | Fejlfinding: routing loops               | Individuel        | `.md` + løsning     |

Læg alle besvarelser i en undermappe med dit navn (eller gruppe) under `dag10-routing`.

---

## 🏭 Hvorfor statisk routing i industrien?

### ✅ Fordele ved statisk routing i OT-netværk:

- **Forudsigelighed:** Traffik følger altid samme vej
- **Sikkerhed:** Ingen routing-protokoller der kan udnyttes
- **Simpelhed:** Nemt at dokumentere og fejlfinde
- **Performance:** Ingen overhead fra routing-protokoller
- **Oppetid:** Ingen afhængighed af routing-daemons
- **Kontrol:** Fuldstændig kontrol over traffik-flow

### ❌ Hvorfor IKKE DHCP eller dynamisk routing?

- PLC'er, HMI'er og drives skal have faste, kendte IP-adresser
- Ingen ukendteenheder må få netværksadgang
- Netværket skal fungere også ved server-fejl
- Dokumentation og compliance kræver faste adresser

---

## 💾 Ressourcer

- [Linux ip route command guide](https://www.cyberciti.biz/faq/howto-linux-configuring-default-route-with-ipcommand/)
- [Understanding routing tables](https://www.networxsecurity.org/members-area/linux/linux-routing-table.html)
- [Industrial network segmentation](https://www.sans.org/reading-room/whitepapers/ICS/industrial-network-segmentation-39590)
- [Purdue Model - Network Zones](https://www.isa.org/standards-and-publications/isa-publications/intech-magazine/2016/november-december/safeguarding-industrial-control-systems)

---

## 📝 Afleveringsguide

1. Opret mappe: `dag10-ditnavn` eller `dag10-gruppeX`
2. For hver opgave:
   - Tegn netværksdiagram (draw.io, Visio, eller håndtegnet + foto)
   - Dokumenter routing-tabeller fra alle routere (`ip route show`)
   - Screenshot af vellykket ping mellem alle zoner
   - Beskriv hvordan pakker routes mellem zonerne
3. Push til GitHub senest før næste undervisningsgang

---

## 🎯 Praktisk eksempel: 3-zoners industri-netværk

```
┌─────────────┐        ┌─────────────┐        ┌─────────────┐
│  IT Network │        │  DMZ/SCADA  │        │ OT Network  │
│   (Office)  │        │   (HMI)     │        │   (PLC'er)  │
│             │        │             │        │             │
│ 192.168.1.0 │◄──────►│ 10.10.0.0   │◄──────►│ 10.20.0.0   │
│    /24      │        │   /16       │        │   /16       │
└─────────────┘        └─────────────┘        └─────────────┘
      │                      │                      │
Static routes          Static routes          Static routes
dokumenteret           dokumenteret           dokumenteret
```

---

## ❓ Ofte stillede spørgsmål

**Q: Hvad er forskellen på en route og en gateway?**  
A: En gateway er en router-interface der forbinder til et andet netværk. En route er en regel i routing-tabellen der siger "for at nå netværk X, send via gateway Y".

**Q: Hvad betyder "default route"?**  
A: En default route (0.0.0.0/0) er en catch-all route. Hvis ingen specifik route matcher, bruges default route.

**Q: Hvorfor bruger man forskellige metrics?**  
A: Metrics/priority bruges til at vælge mellem flere ruter til samme destination. Lavere metric = højere prioritet.

**Q: Kan man have routing loops med statisk routing?**  
A: Ja! Hvis to routere peger på hinanden for samme destination. Derfor er TTL (Time To Live) vigtig - pakken droppes efter X hops.

---

## 🔧 Vigtige kommandoer

```bash
# Vis routing-tabel
ip route show
route -n

# Tilføj statisk route
ip route add 10.20.0.0/16 via 10.10.1.1

# Tilføj route med metric (prioritet)
ip route add 10.20.0.0/16 via 10.10.1.1 metric 100

# Tilføj default route
ip route add default via 192.168.1.1

# Slet route
ip route del 10.20.0.0/16

# Aktivér routing (ip forwarding)
sysctl -w net.ipv4.ip_forward=1

# Trace pakke-vej
traceroute 10.20.1.50
```

---

God arbejdslyst! Husk: Industrielle netværk lever af præcis, veldokumenteret statisk routing! 🛤️🏭
