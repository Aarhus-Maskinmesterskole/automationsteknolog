# 🧱 09 – Klasser og objekter i Python

Denne guide introducerer dig til klasser og objekter – grundlæggende begreber i objektorienteret programmering. Klasser gør det muligt at organisere kode i egne datatyper med tilhørende funktioner.

---

## 🔧 Indhold

* Hvad er en klasse?
* Konstruktoren `__init__`
* Instansvariabler og metoder
* Opret og brug objekter
* Flere objekter i praksis

---

## 📘 1. Hvad er en klasse?

En klasse er en skabelon for objekter. Objekter har data (variabler) og funktioner (metoder), som defineres inde i klassen.

```python
class Motor:
    def sig_hej(self):
        print("Motoren er startet!")

    m = Motor()
    m.start()
```

---

## 📘 2. Brug af `__init__()`

Konstruktøren `__init__()` bruges til at sætte startværdier:

```python
class Sensor:
    def __init__(self, navn):
        self.navn = navn

    def vis_status(self):
        print("Sensor:", self.navn, "er OK")

s1 = Sensor("Temperatur")
s1.vis_status()
```

`self` refererer til det objekt, der kalder metoden.

---

## 📘 3. Flere objekter

Du kan oprette flere objekter fra samme klasse:

```python
sensor1 = Sensor("Tryk")
person2 = Person("Sara")

sensor2 = Sensor("Niveau")

sensor1.vis_status()
sensor2.vis_status()
```

Hver instans har sin egen version af variabler og metoder.

---

## 📘 4. Metoder med beregninger

```python
class Pumpe:
    def __init__(self, radius):
        self.radius = radius

    def __init__(self, effekt):
        self.effekt = effekt  # kW

    def status(self):
        if self.effekt > 5:
            return "Stor pumpe"
        else:
            return "Lille pumpe"

p = Pumpe(7.5)
print("Status:", p.status())
```

---

## 🧪 Øvelser

1. Lav en klasse `Motor` med attributter `navn` og `omdrejninger`, og en metode `beskriv()`
2. Opret to `Motor`-objekter og udskriv deres beskrivelse
3. Lav en klasse `Tank` med metoden `volumen()`
4. Udvid `Sensor`-klassen med en metode `er_aktiv()`
5. Ekstra: Brug en liste til at oprette og vise flere sensorer

---

## ✅ Tjekliste

* [ ] Jeg kan oprette en klasse og kalde dens metoder
* [ ] Jeg forstår `__init__` og `self`
* [ ] Jeg har lavet funktioner inde i en klasse
* [ ] Jeg har brugt flere objekter i samme program

---
