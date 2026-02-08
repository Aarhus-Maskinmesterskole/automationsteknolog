# 🖥️ 10 – PyQt GUI: Simpel brugerflade

PyQt gør det muligt at lave grafiske brugerflader (GUI) i Python. Det bruges ofte til at lave simple overvågnings- eller betjeningspaneler til automation, hvor man kan vise målinger, status eller styre udstyr.

---

## 🔧 Indhold

* Hvad er PyQt?
* Simpelt vindue
* Knapper og labels
* Inputfelter
* Eksempel: Vis og opdater sensorværdi

---

## 📘 1. Hvad er PyQt?

PyQt er en samling Python-moduler, der gør det let at lave vinduer, knapper, tekstfelter osv. Det kræver installation af pakken:

```bash
pip install pyqt6
```

---

## 📘 2. Simpelt vindue

```python
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)
vindue = QWidget()
vindue.setWindowTitle('Automation GUI')
label = QLabel('Velkommen til overvågning!', parent=vindue)
vindue.show()
app.exec()
```

---

## 📘 3. Knap og label

```python
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import sys

def start_motor():
    label.setText('Motoren er startet!')
    label.adjustSize()

app = QApplication(sys.argv)
vindue = QWidget()
vindue.setWindowTitle('Motorstyring')
vindue.adjustSize()

label = QLabel('Status: Klar', parent=vindue)
label.move(20, 20)

knap = QPushButton('Start motor', parent=vindue)
knap.adjustSize()
knap.move(20, 60)
knap.clicked.connect(start_motor)

vindue.resize(1000, 600)
vindue.show()
app.exec()
```

---

## 📘 4. Inputfelt og opdatering

```python
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys

def opdater_sensor():
    vaerdi = inputfelt.text()
    label.setText(f'Sensorværdi: {vaerdi}')
    label.adjustSize()  # Juster label-størrelsen efter tekstændring

app = QApplication(sys.argv)
vindue = QWidget()
vindue.setWindowTitle('Sensorvisning')

label = QLabel('Sensorværdi: --', parent=vindue)
label.move(20, 20)

inputfelt = QLineEdit(parent=vindue)
inputfelt.move(20, 60)

knap = QPushButton('Opdater', parent=vindue)
knap.move(20, 100)
knap.clicked.connect(opdater_sensor)

vindue.resize(220, 150)
vindue.show()
app.exec()

```

---

## 🧪 Øvelser

1. Lav et vindue med en label, der viser "Pumpe status: STOP" og en knap, der ændrer teksten til "Pumpe status: KØRER" når den trykkes.
2. Tilføj et inputfelt, hvor brugeren kan indtaste en temperatur, og vis den i en label.
3. Ekstra: Lav to knapper – en til at starte og en til at stoppe en motor, og opdater status i en label.

---

## ✅ Tjekliste

* [ ] Jeg kan oprette et simpelt PyQt-vindue
* [ ] Jeg kan bruge knapper og labels
* [ ] Jeg kan læse og vise input fra brugeren
* [ ] Jeg har lavet en simpel GUI til automation

---
