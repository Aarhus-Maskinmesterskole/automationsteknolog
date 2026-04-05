# 🖥️ 11 – Tkinter GUI: Simpel brugerflade

Tkinter er standardbiblioteket til grafiske brugerflader (GUI) i Python. Det bruges ofte til at lave simple overvågnings- eller betjeningspaneler, hvor man kan vise målinger, status eller styre udstyr i automationsprojekter.

---

## 🔧 Indhold

* Hvad er Tkinter?
* Simpelt vindue
* Knapper og labels
* Inputfelter
* Eksempel: Vis og opdater sensorværdi

---

## 📘 1. Hvad er Tkinter?

Tkinter følger med Python og kræver ingen ekstra installation. Det gør det let at lave vinduer, knapper, tekstfelter osv.

---

## 📘 2. Simpelt vindue

```python
import tkinter as tk

root = tk.Tk()
root.title('Automation GUI')
label = tk.Label(root, text='Velkommen til overvågning!')
label.pack()
root.mainloop()
```

---

## 📘 3. Knap og label

```python
import tkinter as tk

def start_motor():
    label.config(text='Motoren er startet!')

root = tk.Tk()
root.title('Motorstyring')

label = tk.Label(root, text='Status: Klar')
label.pack(pady=10)

knap = tk.Button(root, text='Start motor', command=start_motor)
knap.pack(pady=10)

root.mainloop()
```

---

## 📘 4. Inputfelt og opdatering

```python
import tkinter as tk

def opdater_sensor():
    vaerdi = inputfelt.get()
    label.config(text=f'Sensorværdi: {vaerdi}')

root = tk.Tk()
root.title('Sensorvisning')

label = tk.Label(root, text='Sensorværdi: --')
label.pack(pady=10)

inputfelt = tk.Entry(root)
inputfelt.pack(pady=10)

knap = tk.Button(root, text='Opdater', command=opdater_sensor)
knap.pack(pady=10)

root.mainloop()
```

---

## 🧪 Øvelser

1. Lav et vindue med en label, der viser "Pumpe status: STOP" og en knap, der ændrer teksten til "Pumpe status: KØRER" når den trykkes.
2. Tilføj et inputfelt, hvor brugeren kan indtaste en temperatur, og vis den i en label.
3. Ekstra: Lav to knapper – en til at starte og en til at stoppe en motor, og opdater status i en label.

---

### For de øvede

4. Lav et GUI med en liste (Listbox), hvor brugeren kan vælge mellem flere sensorer, og vis den valgte sensors navn i en label.
5. Tilføj en slider (Scale), hvor brugeren kan justere en værdi (fx setpunkt for temperatur), og vis den aktuelle værdi i en label.

---

### For de advanced

6. Lav et GUI med et simpelt logpanel (Text widget), hvor programmet kan tilføje logbeskeder, når brugeren trykker på knapper.
7. Tilføj en timer-funktion, der opdaterer en label med tid eller tæller op hvert sekund (brug `after()`-metoden).

## ✅ Tjekliste

* [ ] Jeg kan oprette et simpelt Tkinter-vindue
* [ ] Jeg kan bruge knapper og labels
* [ ] Jeg kan læse og vise input fra brugeren
* [ ] Jeg har lavet en simpel GUI til automation

---
