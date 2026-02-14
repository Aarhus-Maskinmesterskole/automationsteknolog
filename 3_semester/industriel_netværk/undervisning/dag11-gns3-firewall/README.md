# 🛡️ Dag 08 – Fejlfinding & Netværkssikkerhed

Velkommen til dag 8 af Industrielt Netværk!
I dag arbejder vi med fejlfinding og beskyttelse af OT-netværk i GNS3, inkl. firewall, VLAN, NAT og adgangskontrol.

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
  - RDP-adgang og sikkerhed (se RDP.md)
  - NAT og VLAN-router-on-a-stick (se router-nftv.md)

---

## 🛠️ Opgaver

| #   | Titel                       | Type      |
|-----|-----------------------------|-----------|
| 1   | Fejlfinding i GNS3          | Individuel/gruppe |
| 2   | Firewall & ACL konfiguration| Individuel/gruppe |
| 3   | Dokumentér fejl og løsning  | Individuel |

> Opgavebeskrivelser og eksempler findes i `gns3-opgaver.md`.  
> RDP-opsætning og sikkerhed: se `RDP.md`.  
> Avanceret router/firewall: se `router-nftv.md`.

---

## 💾 Ressourcer

- [OT-netværkssikkerhed: Intro (pdf, dansk)](https://www.industriensnetvaerk.dk/wp-content/uploads/2021/01/Industrielt-netvaerk-og-sikkerhed.pdf)
- [GNS3: Simulering af firewalls](https://gns3.com/tech/firewall-simulation)
- [Ping & Traceroute – Hurtig guide](https://www.cloudflare.com/learning/network-layer/what-is-ping/)
- Eksempler og guides:  
  - `gns3-opgaver.md` – opgaver og konfiguration  
  - `RDP.md` – remote desktop og sikkerhed  
  - `router-nftv.md` – avanceret router/firewall

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
