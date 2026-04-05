# 🗂️ 03 – Data Types: Liste, Set, Tuple og Dict

Denne guide introducerer de vigtigste sammensatte datatyper i Python, som bruges til at håndtere og strukturere data – ofte i forbindelse med målinger, statusser og konfigurationer i industrielle systemer.

---

## 🔧 Indhold

* Liste (`list`)
* Mængde (`set`)
* Tuple (`tuple`)
* Ordbog (`dict`)

---

## 📘 1. Liste (`list`)

En liste bruges til at gemme flere værdier i én variabel – fx målinger fra flere sensorer eller status på flere motorer.

```python
sensorer = ["temperatur", "tryk", "niveau"]
print(sensorer[0])  # Udskriver 'temperatur'

sensorer.append("flow")  # Tilføjer 'flow' til listen
print(sensorer)
```

Lister kan ændres (mutable) og kan indeholde forskellige datatyper.

---

## 📘 2. Mængde (`set`)

Et set bruges til at gemme unikke værdier – fx hvilke alarmer der er aktive. Et set kan ikke indeholde dubletter og rækkefølgen er ikke garanteret.

```python
alarmer = {"høj temperatur", "lavt tryk", "høj temperatur"}
print(alarmer)  # Udskriver kun unikke værdier

alarmer.add("strømsvigt")
print(alarmer)
```

---

## 📘 3. Tuple (`tuple`)

En tuple ligner en liste, men kan ikke ændres (immutable). Bruges fx til faste konfigurationer eller koordinater.

```python
motor_parametre = (1500, 400)  # (omdrejninger/min, volt)
print("Motor kører med", motor_parametre[0], "omdr./min")
```

---

## 📘 4. Ordbog (`dict`)

En dict bruges til at gemme data som nøgleværdi-par – fx status for forskellige pumper eller sensorer.

```python
pumpe_status = {"Pumpe1": "kører", "Pumpe2": "stop"}
print(pumpe_status["Pumpe1"])  # Udskriver 'kører'

pumpe_status["Pumpe2"] = "kører"  # Opdaterer status
print(pumpe_status)
```

---

## 🧪 Øvelser

1. Lav en liste med navne på 3 sensorer og udskriv dem én ad gangen med en for-løkke.
2. Opret et set med 3 forskellige alarmer, tilføj en alarm og udskriv alle unikke alarmer.
3. Gem konfigurationen (max tryk, max temperatur) for en tank i en tuple og udskriv værdierne.
4. Opret en dict med status for 2 motorer, opdater status for én af dem og udskriv hele ordbogen.

---

## ✅ Tjekliste

* [ ] Jeg kan oprette og bruge lister, sets, tuples og dicts
* [ ] Jeg forstår forskellen på mutable og immutable datatyper
* [ ] Jeg kan vælge den rigtige datatype til forskellige opgaver

---
