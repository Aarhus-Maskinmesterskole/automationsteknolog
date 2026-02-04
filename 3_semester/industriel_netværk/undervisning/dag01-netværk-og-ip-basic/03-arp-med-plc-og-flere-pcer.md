# 03 - ARP med PLC og flere PC’er – netværksadfærd i praksis

## 📝 Formål

Formålet er at undersøge, hvordan ARP fungerer, når der kommunikeres mellem PC og PLC, og hvordan billedet ændrer sig, når der tilføjes en ekstra PC på netværket.

## 🎯 Kompetencer

* Kan bruge ping og ARP til at teste netværksforbindelse
* Forstår ARP’s rolle i kommunikation mellem PC og PLC
* Kan observere forskelle, når flere enheder er på netværket
* Kan tolke ARP-tabeller og netværksadfærd

---


## Del 1: 1 PC og 1 PLC

### Forudsætninger

* Din PC og en Siemens PLC er forbundet til samme netværk
* **PLC’en skal have en statisk og unik IP-adresse, som ikke bruges af andre enheder på netværket.**
  - Indstil PLC’ens IP-adresse via TIA Portal eller direkte på enheden, så der ikke opstår IP-konflikter.
* Du kender PLC’ens IP-adresse
* Ping mellem PC og PLC virker

---

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

### 2. Ping PLC’en

Ping PLC’ens IP-adresse:

```
ping <PLC_IP>
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

Find PLC’ens IP-adresse i listen.

---

#### Noter (Del 1)

* PLC’ens IP-adresse: `_____________`
* PLC’ens MAC-adresse (fra ARP-tabellen): `_____________`
* Min PC’s IP-adresse: `_____________`
* Er PLC’ens MAC-adresse synlig **før** eller **efter** ping? `_____________`

---

## Del 2: 2 PC’er og 1 PLC

Nu tilføjes en ekstra PC på netværket. Begge PC’er og PLC’en er på samme subnet.

### 1. Ryd ARP-tabellen på begge PC’er

På **begge PC’er**:

**Windows:**
```
arp -d *
```
**Mac/Linux:**
```
sudo arp -d -a
```

---

### 2. Ping PLC’en fra begge PC’er

På **hver PC**:

```
ping <PLC_IP>
```

Vent til du får svar på begge PC’er.

---

### 3. Ping mellem PC’erne

På **hver PC**:

```
ping <ANDEN_PC_IP>
```

---

### 4. Se ARP-tabellen på begge PC’er

På **hver PC**:

**Windows:**
```
arp -a
```
**Mac/Linux:**
```
arp -a
```

Find både PLC’ens og den anden PC’s IP-adresse i listen.

---

#### Noter (Del 2)

* Min PC’s IP-adresse: `_____________`
* Den anden PC’s IP-adresse: `_____________`
* PLC’ens IP-adresse: `_____________`
* MAC-adresser (fra ARP-tabellen):
  * Min PC: `_____________`
  * Den anden PC: `_____________`
  * PLC: `_____________`
* Er MAC-adresserne synlige **før** eller **efter** ping? `_____________`

---

## Observation

Beskriv kort, hvad der sker i netværket i begge dele:

* Hvad udløser, at MAC-adresserne dukker op i ARP-tabellen?
* Hvad ville der ske, hvis en PC ikke kendte MAC-adressen på PLC eller den anden PC?

*(Skriv dine observationer herunder)*

---

## Refleksion

* Hvorfor er ARP nødvendig, selvom vi allerede bruger IP-adresser?
* Hvad sker der, hvis ARP-opslag fejler mellem PC og PLC – eller mellem to PC’er?

*(Skriv dine svar herunder)*

---

**Ekstra:**  
Hvis du ser andre enheder i ARP-tabellen (fx printere, Sonos, smartphones), selvom du ikke har pinget dem, skyldes det, at de aktivt sender discovery-pakker eller gratuitous ARP. PLC’er og almindelige PC’er gør det typisk ikke – de er passive og venter på, at du kontakter dem først.