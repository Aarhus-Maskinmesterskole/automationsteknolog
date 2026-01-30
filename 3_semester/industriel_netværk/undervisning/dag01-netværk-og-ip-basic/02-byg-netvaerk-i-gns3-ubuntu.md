# 🛠️ Byg et netværk i GNS3 med Ubuntu-container

## 📝 Formål

Formålet er at lære at opbygge et simpelt netværk i GNS3 med både virtuelle PC’er (VPCS) og en Ubuntu Docker-container, så du er klar til at arbejde med netværk og kommunikation.

## 🎯 Kompetencer

- Kan oprette et projekt i GNS3 og starte GNS3 VM
- Kan indsætte og forbinde VPCS-enheder, switch og Ubuntu Docker-container
- Forstår forskellen på fysiske og virtuelle enheder

---

## Trin-for-trin: Netværksopbygning

### 1. Start GNS3 VM

- Sørg for at “GNS3 VM” kører i VirtualBox eller VMware.
- I GNS3: Gå til **Edit > Preferences > GNS3 VM**
  - Sæt hak ved “Enable the GNS3 VM”
  - Tjek, at den står som “Connected”.

### 2. Opret et nyt projekt

- Klik på **File > New blank project**
- Navngiv projektet fx `UbuntuNetvaerk`

### 3. Indsæt enheder

- Under “Browse all devices”:
  - Træk **2 x VPCS** (“Virtual PC”) ind på arbejdsområdet
  - Træk en **Ethernet Switch** ind
- Under “Docker containers”:
  - Højreklik → **New template**
  - Vælg “Run this Docker image on the GNS3 VM”
  - Søg efter `ubuntu`, klik “Pull”, og følg guiden
  - Træk **Ubuntu**-containeren ind på arbejdsområdet

### 4. Forbind alle enheder

- Brug “Add a link” (lyn-ikon)
- Forbind:
  - VPCS1 → Switch
  - VPCS2 → Switch
  - Ubuntu-container → Switch

### 5. Start alle noder

- Klik på den grønne “Play”-knap for at starte alle enheder

---

## 📷 Dokumentation

- Tag et screenshot af dit netværk i GNS3 (“Network topology”)
- Gem billedet – du skal bruge det i næste opgave

---

Nu er dit netværk bygget, og du er klar til at arbejde videre med IP-adresser og ping i næste fil!
