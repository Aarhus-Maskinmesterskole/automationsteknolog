# 🧾 02 – Seriel output (CSV-format) i MicroPython

Formålet med denne øvelse er at få ESP32 til at sende måledata som **et simpelt, struktureret tekstformat** via USB/seriel, så Python senere nemt kan læse det.

I praksis bruges det samme princip i industrien, når en enhed “streamer” procesdata til en PC/SCADA/gateway.

---

## 🎯 Læringsmål

- Forstå hvad “seriel output” er i Thonny/MicroPython
- Udskrive målinger i et stabilt, maskin-læsbart format
- Udskrive én linje pr. måling (godt til logning)

---

## 🧰 Forberedelse

- ESP32 kører MicroPython (fra modul 01)
- Du kan køre et script i Thonny og se output i konsollen

---

## 1) Først: print én værdi pr. linje

Kør dette script og se at du får et stabilt output:

```python
from time import sleep

counter = 0

while True:
    counter += 1
    print(counter)
    sleep(1)
```

✅ Successkriterie: Du ser tal der tæller op (1, 2, 3, ...) én gang pr. sekund.

---

## 2) CSV-lignende format (2 værdier)

Nu sender vi to værdier pr. linje adskilt af komma, fx:

`23.5,41.2`

```python
from time import sleep

temp_c = 23.5
hum_pct = 41.2

while True:
    print(f"{temp_c},{hum_pct}")
    sleep(1)
```

✅ Successkriterie: Hver linje består af præcis to værdier adskilt af `,`.

---

## 3) Tilføj et “tag” (valgfrit, men robust)

Hvis du vil gøre det mere robust og let at debugge, kan du tilføje et tag i starten:

`SENSOR,23.5,41.2`

```python
from time import sleep

temp_c = 23.5
hum_pct = 41.2

while True:
    print(f"SENSOR,{temp_c},{hum_pct}")
    sleep(1)
```

✅ Successkriterie: Første felt er altid `SENSOR`.

---

## 🔧 Typiske fejl

- Output kommer i klumper: øg `sleep()` (fx 0.5–2 sek)
- Ustabilt format (manglende komma/ekstra tekst): hold output “rent” (én linje pr. sample)

---

## ✅ Tjekliste

- [ ] Jeg kan få stabilt output i Thonny
- [ ] Jeg kan sende data i CSV-format (kommasepareret)
- [ ] Jeg forstår hvorfor formatet er vigtigt for Python/pyserial senere
