# 🛡️ Opgave 5 – Watchdog-funktion og fejltilstand

I denne opgave skal du implementere en simpel softwarebaseret watchdog, der overvåger dine målinger for systematisk fejl. Hvis systemet registrerer mange ugyldige målinger i træk, skal det udløse en alarm eller skifte til fejlstatus. Watchdogs bruges i mange industrielle systemer for at sikre, at dataflow er sundt og pålideligt.

---

## 🎯 Mål for opgaven

- Overvåge gyldigheden af målinger over tid
- Detektere situationer hvor der forekommer for mange fejl i træk
- Implementere et simpelt system der skifter til fejlstatus
- Lære at tælle og registrere fejltilstande i løbende datastrømme

---

## 🛠️ Fejlbetingelse

> Hvis der optræder 5 eller flere ugyldige målinger i træk, skal systemet registrere en **fejltilstand**.

---

## 👨‍💻 Eksempelkode

```python
import pandas as pd

# Indlæs data med sanity og plausibilitet
df = pd.read_csv("dht22_log_plausibel.csv")

# Kombinér valideringsstatus
df["gyldig"] = df["valid"] & df["plausibel"]

# Watchdog-funktion
watchdog_triggered = False
fejltæller = 0
alarm_tidsstempler = []

for i, gyldig in enumerate(df["gyldig"]):
    if not gyldig:
        fejltæller += 1
        if fejltæller >= 5 and not watchdog_triggered:
            print(f"⚠️  Watchdog udløst ved række {i} ({df.loc[i, 'tid']})")
            watchdog_triggered = True
            alarm_tidsstempler.append(df.loc[i, 'tid'])
    else:
        fejltæller = 0

# Gem med status
df["watchdog_alarm"] = df["tid"].isin(alarm_tidsstempler)
df.to_csv("dht22_watchdog.csv", index=False)
```

---

## 🧪 Udvidelser (frivillige)

- Tilføj kolonne med `fejl_i_træk` for hver række
- Log tidspunkt og temperatur ved hver fejlstatus
- Visualisér rækkeforløb og marker hvor watchdog blev udløst
- Brug `Streamlit` til live-monitorering og alarmer

---

## ✅ Tjekliste

- [ ] Jeg har implementeret en tæller for fejl i træk
- [ ] Jeg har udløst fejlstatus når tærsklen nås
- [ ] Jeg har markeret tidspunktet for watchdog-udløsning
- [ ] Jeg har forstået hvordan en watchdog forbedrer robusthed

---

> En god watchdog beskytter ikke bare mod fejl – den forhindrer dem i at blive videreført. Det er sidste linje i dit datasikkerhedssystem.
