## 🐍 Realtime Plotting – Guides og Opgaver – Oversigt
Herunder finder du en anbefalet struktur over guides og opgaver i begynder-realtime plotting. Forløbet dækker live-visualisering af sensordata via seriel USB i Python med fokus på `FuncAnimation`, rullende vindue og enkel robusthed. Hver fil repræsenterer en konkret lektion eller øvelse, der bygger ovenpå den forrige.

📘 Guides (teori og kodeeksempler)
**01-setup-realtime-plot.md** Introduktion og opsætning.

* Python + venv, VS Code, pakker: `matplotlib`, `pyserial`
* test af Matplotlib-plot og figur/akse
* valg af seriel port (Windows/macOS/Linux)

**02-funcanimation-plot-temperature.md**.

* Live plot temperatur fra ESP32 med `FuncAnimation(fig, update, init_func, interval)` på PC

**03-funcanimation-plot-humidity.md**.

* Live plot humidity fra ESP32 med `FuncAnimation(fig, update, init_func, interval)` på PC

**04-funcanimation-plot-ldr.md**.

* Live plot lysfølsom modstand fra ESP32 med `FuncAnimation(fig, update, init_func, interval)` på PC

**05-funcanimation-plot-gas.md**.

* Live plot gas (mq2) fra ESP32 med `FuncAnimation(fig, update, init_func, interval)` på PC

**06-funcanimation-plot-distance.md**.

* Live plot distance (bar plot) fra ESP32 med `FuncAnimation(fig, update, init_func, interval)` på PC

**07-funcanimation-multiple-plots.md**.

* Live plot flere sensorer i et plot og add legend fra ESP32 med `FuncAnimation(fig, update, init_func, interval)` på PC

**08-funcanimation-multiple-plots.md**.

* Live plot flere sensorer i subplot og add legend fra ESP32 med `FuncAnimation(fig, update, init_func, interval)` på PC
