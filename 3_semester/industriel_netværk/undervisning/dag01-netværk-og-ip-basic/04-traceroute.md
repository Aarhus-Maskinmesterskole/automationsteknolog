# 04 - Traceroute – følg pakkens vej gennem netværket

## 📝 Formål

Formålet er at forstå, hvordan datapakker bevæger sig gennem flere netværksenheder (routere) fra din PC til en destination, og hvordan ICMP bruges til at kortlægge ruten.

## 🎯 Kompetencer

* Kan bruge traceroute/tracert til at analysere netværksveje
* Forstår hvordan TTL og ICMP Time Exceeded virker
* Kan tolke output fra traceroute og identificere netværkshop
* Kan observere og forklare netværksadfærd i praksis

---

## Forudsætninger

* Din PC har adgang til internettet eller et netværk med flere routere
* Du kender IP-adressen eller domænenavnet på en destination (fx 8.8.8.8 eller www.google.com)

---

## Sådan gør du

### 1. Kør traceroute/tracert fra din PC

**Windows (Kommandoprompt):**
```
tracert <DESTINATION>
```

**Mac/Linux (Terminal):**
```
traceroute <DESTINATION>
```

Eksempel:
```
tracert 8.8.8.8
```

---

### 2. Analyser output

Se listen over hop (routere) mellem din PC og destinationen. Læg mærke til:
* Hvor mange hop er der?
* Hvilke IP-adresser eller navne har de enkelte hop?
* Er der hop, der ikke svarer (*** eller timeout)?

---

### 3. Gentag med en anden destination

Prøv fx:
```
tracert www.dr.dk
tracert www.google.com
```

Sammenlign ruterne – er de ens eller forskellige?

---

## Noter

Udfyld nedenstående:

* Destination: `_____________`
* Antal hop: `_____________`
* IP-adresser/navne på første og sidste hop: `_____________`
* Er der hop, der ikke svarer? `_____________`

---

## Observation

Beskriv kort, hvad der sker i netværket, når du bruger traceroute:

* Hvordan finder traceroute ud af ruten?
* Hvilken rolle spiller TTL og ICMP Time Exceeded?
* Hvorfor kan nogle hop være skjulte eller ikke svare?

*(Skriv dine observationer herunder)*

---

## Refleksion

* Hvad kan du bruge traceroute til i fejlfinding?
* Hvad kan begrænse eller forvirre resultatet af en traceroute?

*(Skriv dine svar herunder)*