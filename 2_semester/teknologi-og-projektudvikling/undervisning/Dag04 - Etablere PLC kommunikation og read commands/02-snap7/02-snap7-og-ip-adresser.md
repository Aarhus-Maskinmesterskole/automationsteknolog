# 🌐 02 – snap7 og IP-adresser (teori)

Denne side forklarer, hvad en IP-adresse er, og hvad snap7-biblioteket bruges til i forbindelse med PLC-kommunikation.

---


## Hvad er en IP-adresse?

- En IP-adresse er et unikt nummer, der identificerer et netkort (network interface) på et netværk (fx i en PLC, PC eller router).
- Det er altså ikke "computeren" i sig selv, men det enkelte netkort (fx WiFi, Ethernet), der har en IP-adresse.
- Den består af fire tal mellem 0 og 255, adskilt af punktummer, fx: `192.168.0.100`
- Hver enhed/netkort på samme netværk skal have en unik IP-adresse.
- IP-adressen bruges, så din computer (via sit netkort) kan finde og kommunikere med PLC’en over netværket.

**Eksempel:**
- PLC: `192.168.0.100`
- Din PC: `192.168.0.20`
- Begge skal være på samme netværk (fx `192.168.0.xxx`)

---

## Hvad er snap7?

- snap7 er et Python-bibliotek, der gør det muligt at læse og skrive data til Siemens S7-PLC’er via netværk.
- snap7 taler det samme "sprog" (protokol) som PLC’en, så du kan hente målinger, status og sende kommandoer direkte fra Python.
- snap7 bruges til at bygge egne programmer, der kan overvåge, logge eller styre en PLC – uden at bruge Siemens’ egne værktøjer.

**Typiske anvendelser:**
- Læse værdier fra PLC (fx temperatur, tryk, status)
- Skrive værdier til PLC (fx start/stop, setpunkter)
- Logge data til fil eller visualisere i Python

---

## Hvad betyder rack, slot og port?

- **Rack** og **slot** bruges til at fortælle snap7, hvor CPU’en sidder i PLC’en:
  - På de fleste Siemens S7-300/400/1200/1500 er rack næsten altid 0.
  - Slot er typisk 1 (S7-300/400) eller 1/0 (S7-1200/1500, prøv begge hvis du er i tvivl).
- **Port** er som regel 102 for S7-kommunikation (standard, skal sjældent ændres).

Eksempel: `client.connect('192.168.0.100', rack=0, slot=1)`

Hvis du ikke kan forbinde, så tjek at du har valgt korrekt rack og slot i forhold til din PLC-type og hardwareopsætning.

---

## Hvordan hænger det sammen?

1. Din PC og PLC skal være på samme netværk og have hver sin IP-adresse.
2. snap7 bruger PLC’ens IP-adresse til at oprette forbindelse.
3. Når forbindelsen er oprettet, kan du læse/skrive data til PLC’en direkte fra Python.

**Eksempel på kode (kun for forståelse):**
```python
import snap7
client = snap7.client.Client()
client.connect('192.168.0.100', 0, 1)  # PLC’ens IP, rack, slot
# Nu kan du læse/skrive data
```

---

## Husk
- Du skal kende PLC’ens IP-adresse for at kunne forbinde.
- Hvis du ikke kan "pinge" PLC’en fra din PC, kan snap7 heller ikke forbinde.
- snap7 virker kun med Siemens S7-300/400/1200/1500 (og Emulate3D).

---
