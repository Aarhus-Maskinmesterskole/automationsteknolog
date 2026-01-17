# 05 – Simpelt PLC-dashboard med matplotlib (FuncAnimation)

I denne opgave skal du lave et Python-program, der løbende læser Tank_Level fra PLC'en og viser det i et simpelt plot med matplotlibs FuncAnimation.

---

## Opgave

- Læs Tank_Level fra PLC'en i et main loop
- Brug try/except til at håndtere fejl
- Plot værdien løbende med matplotlibs FuncAnimation
- Ved Ctrl+C skal kommunikationen lukkes pænt og programmet stoppe

---

## Eksempel på løsning med FuncAnimation

```python
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pycomm3 import LogixDriver

PLC_IP = "192.168.1.209"
times = []
levels = []
t0 = time.time()

fig, ax = plt.subplots()
line, = ax.plot([], [], label="Tank_Level")
ax.set_xlabel("Tid (s)")
ax.set_ylabel("Tank_Level")
ax.legend()

try:
    with LogixDriver(PLC_IP) as plc:
        def update(frame):
            level = plc.read("Tank_Level").value
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
```

---

**Tip:**
- Du kan ændre PLC_IP hvis nødvendigt.
- Stop programmet med Ctrl+C.
