# 01 – Setup til realtime-plot (Introduktion og opsætning)

Målet: få et Python-miljø op at køre, installere pakkerne **matplotlib** og **pyserial**, teste en basic figur – og finde din serielle port.

## Krav

* Python 3.10+
* VS Code (med Microsoft “Python”-udvidelsen)

## 1) Opret virtuelt miljø og installer pakker

**Windows (PowerShell):**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip matplotlib pyserial
```

**macOS / Linux (bash/zsh):**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip matplotlib pyserial
```

## 2) Test at Matplotlib virker

```python
# fil: test_plot.py
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([0, 1, 2], [0, 1, 0])
ax.set_title("Matplotlib virker")
plt.show()
```

Kør:

```bash
python test_plot.py
```

Du skal se et lille vindue med en trekantet kurve.

## 3) Find din serielle port (ESP32)

Vis alle porte:

```bash
python -m serial.tools.list_ports
```

Typisk navngivning:

* **Windows:** `COM3`, `COM4`, …
* **Linux:** `/dev/ttyUSB0` eller `/dev/ttyACM0`
* **macOS:** `/dev/tty.usbserial-XXXX` eller `/dev/tty.usbmodemXXXX`

> Note: Hvis ingen port vises, så tjek USB-kablet/driveren og at ESP32 er tilsluttet.

Det var det. Næste skridt er at lave et lille script, der **læser en linje fra porten** og senere smider den på en graf.
