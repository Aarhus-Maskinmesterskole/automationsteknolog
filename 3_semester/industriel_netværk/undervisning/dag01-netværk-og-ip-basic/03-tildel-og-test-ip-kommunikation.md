# 🌐 Tildel og test IP-kommunikation i GNS3

## 📝 Formål

Formålet er at lære at finde og ændre IP-adresser, finde MAC-adresser, og teste netværkskommunikation mellem VPCS og Ubuntu-container i GNS3.

## 🎯 Kompetencer

- Kan tildele og ændre IP-adresser (VPCS og Ubuntu)
- Kan finde MAC-adresser i både Linux og VPCS
- Kan bruge ping til at teste kommunikation mellem to eller flere enheder
- Kan forklare, hvad der sker netværksmæssigt

---

## 1. Find og ændr IP-adresse på VPCS

- Dobbeltklik på **VPCS1**:
```

ip 192.168.1.10/24 192.168.1.1

```
- Dobbeltklik på **VPCS2**:
```

ip 192.168.1.20/24 192.168.1.1

```

### Find MAC-adresse (VPCS)
- Skriv:
```

show

```
- Notér MAC-adresse for hver VPCS (fx: `00:50:79:xx:xx:xx`)

---

## 2. Tildel IP-adresse og find MAC på Ubuntu (Docker)

- Dobbeltklik på **Ubuntu-container** (åbner terminal).
- Tildel IP:
```

ip addr add 192.168.1.30/24 dev eth0
ip link set eth0 up

```
- Find MAC-adresse:
```

ip link show eth0

```
(MAC-adressen står efter `link/ether`)

---

## 3. Ping mellem enheder

- På **VPCS1**:
```

ping 192.168.1.20
ping 192.168.1.30

```
- På **VPCS2**:
```

ping 192.168.1.10
ping 192.168.1.30

```
- På **Ubuntu**:
```

ping 192.168.1.10
ping 192.168.1.20

```

---

## 📷 Dokumentation

- Tag screenshots af:
  - Konsoller/terminaler med dine kommandoer og svar
  - Mindst én ping-test med succes
- Indsæt billeder i din `.md`-fil:
```

![Ping-resultat](mit-ping.png)

```

---

## Refleksion

- Hvilken forskel var der på at finde MAC-adresse i VPCS vs. Ubuntu?
- Hvad fortæller ping-resultatet dig om netværket?

---

**Du har nu bevist, at dine virtuelle maskiner kan “snakke” sammen på netværket!**
