# 🐍 README – Dag 04: Python + Seriel datamodtagelse

På denne undervisningsdag forbinder du din computer med ESP32 via seriel kommunikation. Du bruger `pyserial` i Python til at læse data, gemme det som **CSV** eller **JSONL** (én måling pr. linje), og du får værktøjer til live-visualisering og simpel realtids-behandling.

---

## 🎯 Læringsmål

* Installere og teste `pyserial`
* Læse og parse serielle målinger fra ESP32
* Logge data til **CSV** (let til Excel/Pandas) og **JSONL** (stream-venligt)
* Visualisere målinger live og lave enkel realtidsbehandling (fx glidende middel, tærskler)

---

## 📚 Modulstruktur og filer

```
dag04-python-serial/
├── 01-installation-pyserial.md                    # Installer og test pyserial, find korrekt seriel port
├── 02-modtag-seriel-data.md                      # Læsning af rå serielle linjer og basis-parsing
├── 03-serial-temperatur-csv.md                   # Log temperatur → CSV med tidsstempel
├── 04-serial-humidity-csv.md                     # Log luftfugtighed → CSV
├── 05-serial-temperature-luftfugtighed-csv.md    # Log både temperatur + luftfugtighed → CSV
├── 06-serial-temperature-jsonl.md                # Log temperatur → JSONL (én JSON pr. linje)
├── 07-serial-humidity-jsonl.md                   # Log luftfugtighed → JSONL
├── 08-serial-temperature-humidity-jsonl.md       # Log både temperatur + luftfugtighed → JSONL
├── 09-live-visualisering.md                      # Real-time visning med matplotlib (valgfri)
├── 10-realtime-processing.md                     # Simpel realtidsbehandling/alarmer (valgfri)
└── README.md
```

---

## 💼 Relevans for praksis

I industrielle og embedded systemer flyder målinger ofte over UART/seriel. Du lærer at:

* Fange og kvalitetssikre data i realtid
* Gemme målinger robust til senere dokumentation og analyse
* Vælge format: **CSV** til tabeller/regneark, **JSONL** til streaming og fleksibel struktur

---

## ✅ Dagens output

* Et Python-script der læser stabilt fra ESP32
* En logfil i **CSV** og/eller **JSONL** med tidsstempel og sensordata
* En enkel live-graf og en skitse til realtidsbehandling

---

## 🧩 Tips & fejlfinding

* Kontroller portnavn/baudrate i både ESP32-koden og Python.
* Sørg for én måling pr. linje i seriel output.
* Hvis grafen hakker: brug en ringbuffer og `plt.pause()` i små trin.

> Nu kobler du ESP32 til Python – og gør dine målinger brugbare til analyse, visualisering og beslutninger.
