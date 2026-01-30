# 🛡️ Dag 02 – Subnet, VLAN & Fejlfinding (med fysisk PLC)

Velkommen til anden undervisningsdag i Industrielt Netværk!

> I dag kobler du den virtuelle verden i GNS3 sammen med rigtig PLC-udstyr: Du segmenterer netværk med subnet og VLAN, og fejlfinder kommunikation mellem både virtuelle pc’er og en fysisk PLC.

---

## 🎯 Læringsmål for dagen

- Forstå forskellen på subnet og VLAN – og hvorfor segmentering er vigtigt i industrien
- Kunne konfigurere subnet og VLAN i GNS3 (med VPCS og fysisk PLC)
- Udføre og dokumentere ping-test mellem virtuel PC og fysisk PLC
- Bruge netværksværktøjer (ping, evt. traceroute) til fejlfinding på tværs af fysisk og virtuel netværksudstyr
- Dokumentere netværksopsætning, resultater og fejl

---

## 📚 Dagens indhold

- **Mini-forelæsning:**  
  Subnet, VLAN, gateway, typiske fejl og netværkssikkerhed
- **Opgaver:**
    1. [Segmentér netværket med subnet og VLAN – GNS3 + fysisk PLC](segmenter-med-subnet-og-vlan-plc.md)
    2. [Ping fra virtuel PC til fysisk PLC](ping-virtuel-til-fysisk-plc.md)
    3. [Fejlfinding – hvis ping fejler](fejlfinding-gns3-fysisk-plc.md)
    4. [Refleksion: Hvad lærte du om integration mellem virtuel og fysisk netværk?](reflekter-over-dag02.md)
- **Fælles opsamling:**  
  Hvilke problemer opstod, hvordan blev de løst, og hvorfor er det vigtigt at kunne netværke med både virtuelle og fysiske enheder?

---

## 🛠️ Opgaver

| #   | Titel                                             | Type        | Aflevering          |
|-----|---------------------------------------------------|-------------|---------------------|
| 1   | Segmentér med subnet og VLAN (GNS3 + PLC)         | Individuel/gruppe | `.md` + diagram   |
| 2   | Ping fra virtuel PC til fysisk PLC                | Individuel  | `.md` + screenshot  |
| 3   | Fejlfinding ved netværksfejl (virtuelt/fysisk)    | Individuel  | `.md` + noter       |
| 4   | Refleksion over integration og fejlfinding        | Individuel  | `.md`               |

Læg alle besvarelser i en undermappe med dit navn (eller gruppe) under `dag02-subnet-vlan`.

---

## 💾 Ressourcer

- [YouTube: VLAN og subnet forklaret (DK/ENG)](https://www.youtube.com/watch?v=_IAUOQpnEjw)
- [GNS3 VLAN tutorial](https://gns3.com/tech/vlan-configuration)
- [Subnetting quick guide](https://www.cloudflare.com/learning/network-layer/subnetting/)
- [Ping & Traceroute guide](https://www.cloudflare.com/learning/network-layer/what-is-ping/)

---

## 📝 Afleveringsguide

1. Opret mappe: `dag02-ditnavn` eller `dag02-gruppeX`
2. Svar på opgaverne i de relevante `.md`-filer
3. Indsæt screenshots og diagrammer som  
```

![navn](billede.png)

```
4. Push til GitHub senest før næste undervisningsgang

> Husk: Beskriv altid, hvordan din virtuelle og fysiske opsætning hænger sammen – både hvis det virker og hvis det fejler!

---

## ❓ Ofte stillede spørgsmål

- **Hvordan dokumenterer jeg ping fra GNS3 til PLC?**  
Tag screenshot af både GNS3 og dit ping-resultat.
- **Kan jeg bruge andet end VPCS i GNS3?**  
Ja, men hold det simpelt – fokus er på netværkskommunikation.
- **Hvad hvis PLC ikke svarer på ping?**  
Tjek kabling, IP-konfiguration, VLAN, firewall – og dokumentér din fejlsøgning!

---

God arbejdslyst – og husk: Den største gevinst er at få virtuel og fysisk netværksudstyr til at spille sammen! 🛠️🤖

**Sig til hvis du vil have opgaveskabeloner/cheat sheet til de enkelte punkter, eller et eksempel på hvordan diagrammet kan tegnes!**
