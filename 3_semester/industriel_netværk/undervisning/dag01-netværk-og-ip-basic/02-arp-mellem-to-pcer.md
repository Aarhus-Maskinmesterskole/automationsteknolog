# 02 - ARP mellem to PC’er – hvad sker der, når to computere kommunikerer?

## 📝 Formål

Formålet er at forstå, hvad der sker i netværket, når to PC’er kommunikerer via IP. Du skal se, hvordan **ARP** bruges til at koble **IP-adresser** sammen med **MAC-adresser**, og hvorfor dette er afgørende i et lokalt netværk.

## 🎯 Kompetencer

* Kan bruge ping og ARP til at teste netværksforbindelse
* Forstår sammenhængen mellem IP-adresser og MAC-adresser
* Kan forklare ARP’s rolle i et lokalt netværk
* Kan observere og tolke netværksadfærd i praksis

---

## Forudsætninger

* Begge PC’er er forbundet til samme netværk
* Du kender IP-adressen på begge PC’er
* Ping mellem PC’erne virker

---

## Sådan gør du

### 1. Ryd ARP-tabellen på din PC

**Windows (Kommandoprompt som administrator):**
```
arp -d *
```

**Mac/Linux (Terminal):**
```
sudo arp -d -a
```

---

### 2. Ping den anden PC

Ping den anden PC’s IP-adresse:

```
ping <ANDEN_PC_IP>
```

Vent til du får svar.

---

### 3. Se ARP-tabellen igen

**Windows:**
```
arp -a
```

**Mac/Linux:**
```
arp -a
```

Find den anden PC’s IP-adresse i listen.

---

## Noter

Udfyld nedenstående:

* Den anden PC’s IP-adresse: `_____________`
* Den anden PC’s MAC-adresse (fra ARP-tabellen): `_____________`
* Min PC’s IP-adresse: `_____________`
* Er den anden PC’s MAC-adresse synlig **før** eller **efter** ping? `_____________`

---

## Observation

Beskriv kort, hvad der sker i netværket:

* Hvad udløser, at den anden PC’s MAC-adresse dukker op i ARP-tabellen?
* Hvad ville der ske, hvis din PC ikke kendte den anden PC’s MAC-adresse?

*(Skriv dine observationer herunder)*

---

## Refleksion

* Hvorfor er ARP nødvendig, selvom vi allerede bruger IP-adresser?
* Hvad sker der, hvis ARP-opslag fejler mellem to PC’er på samme netværk?

*(Skriv dine svar herunder)*

---

**Ekstra:**  
Hvis du ser andre enheder i ARP-tabellen (fx printere, Sonos, smartphones), selvom du ikke har pinget dem, skyldes det, at de aktivt sender discovery-pakker eller gratuitous ARP. Almindelige PC’er gør det typisk ikke – de er passive og venter på, at du kontakter dem først.