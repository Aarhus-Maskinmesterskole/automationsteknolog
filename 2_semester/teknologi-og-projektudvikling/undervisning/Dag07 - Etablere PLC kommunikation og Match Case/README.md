# 📘 README – Dag 09: Sanity Checks, Tidsstempling og Plausibilitetstests

Velkommen til dag 09 i forløbet. I dag arbejder vi med kvalitetssikring af vores måledata. Det handler ikke kun om at registrere værdier, men om at vurdere, om de er plausible, rettidige og brugbare. Fokus er på sanity checks, tidsstempling, plausibilitetstests og overvågning af datakvalitet via softwarebaserede watchdog-mekanismer.

---

## 🧭 Formål med dagen

* Forstå hvad sanity checks og plausibilitetstests er – og hvordan de adskiller sig
* Implementere tidsstempling af målinger og vurdere samplingfrekvens
* Identificere fejl, dubletter og outliers i data
* Simulere en softwarebaseret watchdog og rapportere fejltilstande
* Udvikle datavalideringspipeline fra sensor → sanity check → visning/log

---

## 📚 Dagens guider og eksempler

Navigér til mappen:

```
undervisning/dag06_sanitychecks-timestamp/
```

Her finder du:

| Filnavn                           | Indhold                                  |
| --------------------------------- | ---------------------------------------- |
| `06-sanitychecks-timestamp.md`    | Guide til sanity checks og tidsstempling |
| `sanitycheck.py`                  | Python-skabelon til datavalidering       |
| `watchdog.py`                     | Eksempel på overvågning af datastrømme   |
| `simulerede-data.csv` *(valgfri)* | Eksempeldata til test og udvikling       |

---

## 📖 Teori: Sanity checks, Tidsstempling og Plausibilitetstests

### 🔍 Sanity Checks

Sanity checks er hurtige og enkle valideringer af en måling. De bruges til at sikre, at data overholder grundlæggende regler – fx at værdier ligger inden for et bestemt interval, har den korrekte datatype og ikke er tomme eller åbenlyst forkerte. Et sanity check kan fx være:

* Er værdien mellem 0 og 1023?
* Er datatypen et tal og ikke tekst?
* Har værdien ændret sig meget pludseligt?

Sanity checks anvendes ofte lige efter data modtages og før den gemmes eller sendes videre i systemet.

### ⏱️ Tidsstempling

Tidsstempling betyder at tilknytte hver måling et tidspunkt for hvornår den er registreret. I Python gøres dette typisk med `pd.Timestamp.now()`. Et timestamp er vigtigt for:

* at forstå udviklingen over tid
* at opdage uregelmæssigheder i sampling
* at kunne synkronisere data med andre kilder

Tidsstempling er særlig vigtig i systemer, hvor målinger ankommer asynkront eller fra flere enheder.

### ⚙️ Plausibilitetstest

Plausibilitetstest går et skridt videre end sanity checks og tager højde for domænespecifik viden. Her vurderer man, om målingen giver mening ud fra den fysiske kontekst og tidligere værdier. Det kan fx være:

* Målingen ændrer sig ikke mere end x % per sekund
* Værdier må ikke svinge mere end ±50 fra sidste måling
* Sensor A bør altid måle højere end Sensor B

Plausibilitet handler ikke kun om værdien i sig selv – men om sammenhæng og realisme.

### 🛡️ Watchdog-princip

En softwarebaseret watchdog overvåger datakvalitet over tid. Hvis et system registrerer for mange ugyldige eller mistænkelige målinger i træk, kan det udløse en alarm, stoppe logging eller skifte til failsafe-mode. En simpel implementering holder øje med hvor mange `False`-checks der er i træk – fx 5 mislykkede = trigger fejl.

Watchdogs er afgørende i automatiserede systemer, hvor manuel overvågning ikke er mulig.

---

## 💼 Relevans

I praksis er datavalidering afgørende i projekter med IIoT, SCADA og sensorintegration. Dårlige målinger kan føre til fejlbeslutninger og fejlanalyse. Ved at tjekke dine data og tidsstemple korrekt skaber du robusthed – og kvalitet i det videre projekt.

> Sanity checks er den tekniske samvittighed i ethvert dataprojekt. Plausibilitetstests og watchdogs skaber tryghed i datadrevne beslutninger.
