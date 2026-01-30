# 🌍 Få din PC i GNS3 på internettet

## 📝 Formål

Formålet er at lære, hvordan du får en virtuel PC (VPCS eller Ubuntu/Docker) i GNS3 til at kommunikere med internettet. Du får erfaring med Cloud, gateway og praktisk routing – som bruges i al industriel netværksintegration.

## 🎯 Kompetencer

- Kan forbinde en GNS3-node til internettet via Cloud
- Kan forstå gateway/bro-forbindelse mellem lokalnet og internet
- Kan teste og dokumentere ekstern netværksforbindelse (ping, DNS, web)

---

## 1. Forbind din PC til internettet (med Cloud i GNS3)

### A. Tilføj Cloud-node (nemmeste metode)

1. I GNS3, find **Cloud** under “All devices” (eller “End devices”).
2. Træk en **Cloud-node** ind på arbejdsområdet.
3. Forbind din VPCS eller Ubuntu (eller begge) til Cloud-node med “Add a link”.
4. Tænd alle noder (grøn “Play”-knap).

### B. Tildel IP-adresse og gateway

- Dobbeltklik på **VPCS** og skriv:
```

dhcp

````
(så henter PC’en automatisk IP, gateway og DNS fra Cloud)

- Hvis du bruger **Ubuntu**:
- I terminalen skriv:
  ```
  dhclient eth0
  ```
  *(eller brug DHCP manuelt hvis dhclient ikke findes; Ubuntu Docker kan kræve installation af dhclient: `apt update && apt install dhclient`)*

### C. Tjek din IP

- På VPCS:
````

show

```
- På Ubuntu:
```

ip addr show eth0

```

---

## 2. Test internetadgang

- På VPCS:
```

ping 8.8.8.8
ping google.com

```
- På Ubuntu:
```

ping 8.8.8.8
ping google.com

```
*(Hvis du får svar, har du internetadgang!)*

---

## 3. (Ekstra) Brugning af web

- På Ubuntu (Docker) kan du prøve:
```

apt update

```
*(Dette kræver internetadgang og virker kun, hvis du har en “rigtig” Ubuntu og ikke bare Alpine uden pakker!)*

---

## 📷 Dokumentation

- Screenshot af:
  - Din GNS3-topologi med Cloud-node og PC/Ubuntu forbundet
  - Ping-resultater til 8.8.8.8 og google.com

---

## Refleksion

- Hvad er forskellen på en Cloud-node og en almindelig switch?
- Hvad sker der, hvis du ikke tildeler gateway (eller bruger forkert subnet)?
- Hvordan kan du bruge denne opsætning i industrielt netværk?

---

Nu kan du sende trafik ud på internettet – præcis som i rigtige OT- og IT-netværk! 🌍🖧
