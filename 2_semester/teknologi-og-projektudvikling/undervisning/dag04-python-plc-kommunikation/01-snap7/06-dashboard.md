# 05 – Simpelt PLC-dashboard med matplotlib (FuncAnimation)

I denne opgave skal du lave et Python-program, der løbende læser Tank_Level (REAL) fra PLC'en og viser det i et simpelt plot med matplotlibs FuncAnimation.

---

## Opgave

- Læs Tank_Level fra PLC'en i et main loop
- Brug try/except til at håndtere fejl
- Plot værdien løbende med matplotlibs FuncAnimation
- Ved Ctrl+C skal kommunikationen lukkes pænt og programmet stoppe

---

## Eksempel på løsning med snap7 og FuncAnimation

```python
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import snap7
from snap7.util import get_real

PLC_IP = "192.168.0.1"
RACK = 0
SLOT = 1
DB = 1

client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

times = []
levels = []
t0 = time.time()

fig, ax = plt.subplots()
line, = ax.plot([], [], label="Tank_Level")
ax.set_xlabel("Tid (s)")
ax.set_ylabel("Tank_Level")
ax.legend()

try:
    def update(frame):
        data = cli.db_read(DB, 4, 4)  # DBD4 (REAL) = Tank_Level
        level = get_real(data, 0)
        now = time.time() - t0
        times.append(now)
        levels.append(level)
        line.set_data(times, levels)
        ax.relim()
        ax.autoscale_view()
        return line,

    ani = FuncAnimation(fig, update, interval=1000)
    plt.show()
except KeyboardInterrupt:
    print("Stopper program og lukker forbindelsen...")
finally:
    client.disconnect()
```

---

## Eksempel på løsning med snap7 og FuncAnimation + csv logging

```python
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import snap7
from snap7.util import get_real
from datetime import datetime

PLC_IP = "192.168.0.1"
RACK = 0
SLOT = 0 # sæt til 0 hvis simulering af s7-1500, sæt til 1 for s7-1200
DB = 1
LOGFILE = "tank_level_log.csv"
client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)
times = []
levels = []
t0 = time.time()
fig, ax = plt.subplots()
line, = ax.plot([], [], label="Tank_Level")
ax.set_xlabel("Tid (s)")
ax.set_ylabel("Tank_Level")
ax.legend()
def update(frame):
    data = client.db_read(DB, 4, 4)  # DBD4 (REAL) = Tank_Level
    level = get_real(data, 0)
    now = time.time() - t0
    times.append(now)
    levels.append(level)
    line.set_data(times, levels)
    ax.relim()
    ax.autoscale_view()
    # Log til CSV
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = pd.DataFrame([[timestamp, level]], columns=["timestamp", "Tank_Level"])
    row.to_csv(LOGFILE, mode='a', header=not pd.io.common.file_exists(LOGFILE), index=False)
    return line, ax,
try:
    ani = FuncAnimation(fig, update, interval=1000)
    plt.show()
except KeyboardInterrupt:
    print("Stopper program og lukker forbindelsen...")
finally:
    client.disconnect()
```

**Tip:**
- Du kan ændre PLC_IP, DB og offset hvis nødvendigt.
- Stop programmet med Ctrl+C.
