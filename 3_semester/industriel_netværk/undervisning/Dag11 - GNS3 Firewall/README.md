# 🛡️ Dag 11 – GNS3 Firewall

Velkommen til dag 11 af Industrielt Netværk!
I dag arbejder vi med firewall-regler og beskyttelse af OT-netværk i GNS3, inkl. nftables, RDP og adgangskontrol.

---

## Placering i forløbet

1. Forrige dag: [Dag10 - GNS3 Routing og ACL/README.md](./../Dag10%20-%20GNS3%20Routing%20og%20ACL/README.md)
2. Denne dag: filtrering og kontrol af trafik oven på routing
3. Næste dag: [Dag12 - GNS3 VPN/README.md](./../Dag12%20-%20GNS3%20VPN/README.md)

---

## Dagens progression

1. Start med Linux-router og grundlæggende trafik mellem netværk
2. Indfør nftables-regler til at tillade og blokere trafik
3. Arbejd med RDP og adgangskontrol i et kontrolleret setup
4. Brug rotationsøvelsen til at samle routing, firewall og dokumentation

---

## 🎯 Læringsmål

- Forstå OT-netværkssikkerhed: firewall, segmentering, ACL
- Udføre fejlfinding: ping, traceroute, fysisk/logisk analyse
- Identificere og løse netværksfejl (IP-konflikt, VLAN, gateway)
- Dokumentere fejl og løsninger systematisk

---

## 📚 Indhold

- **Mini-forelæsning:**  
  - OT vs. IT-sikkerhed, trusler og beskyttelse
  - Firewalls, access control, fysisk adskillelse
  - Fejlfinding: ping, traceroute, netværksdiagrammer
- **Hands-on i GNS3:**  
  - Opret Linux-router med flere netværk
  - Konfigurér firewall med nftables
  - Test og dokumentér fejl (forkert subnet, IP-konflikt, VLAN-fejl)
  - RDP-adgang og sikkerhed (se 03 - RDP.md)
  - Router- og firewall-opgaver (se 01 - Router NFT Opgaver.md)

---

## 🛠️ Opgaver

| #   | Titel                       | Type      |
|-----|-----------------------------|-----------|
| 1   | Fejlfinding i GNS3          | Individuel/gruppe |
| 2   | Firewall & ACL konfiguration| Individuel/gruppe |
| 3   | Dokumentér fejl og løsning  | Individuel |

> Opgavebeskrivelser og eksempler findes i `01 - Router NFT Opgaver.md`.  
> RDP-opsætning og sikkerhed: se `03 - RDP.md`.  
> Firewall-konfiguration: se `02 - NFTables.md`.

---

## Anbefalet gennemførelse

1. Start med [01 - Router NFT Opgaver.md](./01%20-%20Router%20NFT%20Opgaver.md)
2. Brug derefter [02 - NFTables.md](./02%20-%20NFTables.md) som reference og udbygning
3. Tilføj [03 - RDP.md](./03%20-%20RDP.md) når basisfiltrering virker
4. Brug rotationsøvelsen til sidst som opsamling og repetition

---

## 💾 Ressourcer

- [OT-netværkssikkerhed: Intro (pdf, dansk)](https://www.industriensnetvaerk.dk/wp-content/uploads/2021/01/Industrielt-netvaerk-og-sikkerhed.pdf)
- [GNS3: Simulering af firewalls](https://gns3.com/tech/firewall-simulation)
- [Ping & Traceroute – Hurtig guide](https://www.cloudflare.com/learning/network-layer/what-is-ping/)
- Eksempler og guides:  
  - `01 - Router NFT Opgaver.md` – opgaver og konfiguration  
  - `03 - RDP.md` – remote desktop og sikkerhed  
  - `02 - NFTables.md` – avanceret router/firewall

---

## ❓ FAQ

- **Må vi arbejde i grupper?**  
  Ja – men alle skal bidrage til dokumentation.
- **Hvordan viser jeg en firewall-konfiguration?**  
  Brug screenshots fra GNS3, kopier konfigurationskode, eller upload et billede af dit setup.
- **Hvad gør jeg hvis jeg ikke kan finde en fejl?**  
  Beskriv hvordan du ledte, og hvad du forsøgte. Spørg underviser eller gruppen.

---

Held og lykke med fejlfinding og sikkerhed – det er her du lærer at redde produktionen! 🦺🔐
