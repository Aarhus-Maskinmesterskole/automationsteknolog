# 🌐 06 – Interaktivt dashboard med Streamlit

Streamlit er et moderne Python-værktøj, der gør det nemt at bygge interaktive visualiseringer direkte i browseren – uden behov for HTML, CSS eller JavaScript. Det er særligt velegnet til at præsentere måledata i realtid eller til at give brugeren mulighed for at filtrere og analysere datasæt visuelt. Det bruges ofte i data science, prototyper og undervisningsprojekter, hvor man hurtigt vil formidle indsigt i et datasæt på en letforståelig måde.

I dette modul bygger du et simpelt dashboard, hvor du kan loade en CSV-fil, vælge kolonner, filtrere data og vise grafer – alt sammen via en enkel brugerflade. Det fungerer som en introduktion til frontend-baseret datapræsentation i Python og åbner op for, hvordan du selv kan formidle analyser og sensordata uden at være afhængig af webudvikling.

---

## 🎯 Læringsmål

* Bruge `streamlit` til at oprette et interaktivt brugerinterface i browseren
* Indlæse og filtrere data dynamisk via widgets (f.eks. selectbox, slider, checkbox)
* Vise figurer med Matplotlib, Pandas og Streamlits egne visualiseringsfunktioner
* Forstå, hvordan Python-scriptet kører som en webapplikation
* Klargøre data og grafik til rapport, præsentation eller interaktiv analyse

---

## ⚙️ Installation og opstart

Først skal du sikre dig, at `streamlit` er installeret i dit Python-miljø. Installer med pip:

```bash
pip install streamlit
```

Du starter et dashboard ved at køre scriptet via terminalen:

```bash
streamlit run dashboard.py
```

Det åbner automatisk en browser med dashboardet. Hvis ikke, kan du selv åbne den viste URL i din browser (typisk [http://localhost:8501](http://localhost:8501)).

---

## 💻 Eksempel – dashboard.py

Herunder ses et simpelt eksempel på et dashboard, hvor brugeren kan uploade en CSV-fil (measurements.csv), vælge en kolonne, indstille en grænseværdi og få vist et filtreret plot.
For at køre dette script skal du i terminal gå til .py fil og kopier measurements.csv til denne mappe. Skriv herefter streamlit run .py (det du nu har kaldt denne).

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

st.title("🔎 Live datavisualisering")

# Forsøg at læse filen, eller generer dummy-data
try:
    data = pd.read_csv("measurements.csv")
except FileNotFoundError:
    st.warning("Kunne ikke finde measurements.csv - bruger eksempeldata i stedet")
    # Opret dummy data
    dates = pd.date_range('2025-09-01', periods=100, freq='H')
    data = pd.DataFrame({
        'timestamp': dates,
        'temperature': np.random.normal(22, 3, 100),
        'humidity': np.random.normal(60, 10, 100),
        'pressure': np.random.normal(1013, 5, 100)
    })

# Resten af koden er uændret
st.subheader("📊 Oversigt")
st.write(data.describe())

# Vælg en sensor-kolonne
sensor_valg = st.selectbox("Vælg sensor", data.columns)

# Slider til at vælge grænse
max_val = int(data[sensor_valg].max() * 1.2) if sensor_valg in data else 1000
grænse = st.slider("Maks tilladt værdi", 0, max_val, int(max_val * 0.8))

# Filtrer data
filtreret = data[data[sensor_valg] < grænse]

# Plot de filtrerede data
fig, ax = plt.subplots()
filtreret[sensor_valg].plot(ax=ax)
ax.set_title(f"{sensor_valg} – filtreret visning")
ax.set_ylabel("Værdi")
st.pyplot(fig)
```

<img width="2585" height="1970" alt="image" src="https://github.com/user-attachments/assets/3de4e9e9-5cd1-47b7-86de-dc37b7981663" />


Dette script demonstrerer, hvordan et simpelt Python-program hurtigt kan blive til en dynamisk, brugerstyret datavisualisering.

---

## 🧪 Øvelser

1. Brug `st.line_chart()` eller `st.bar_chart()` som alternativ til Matplotlib-plot
2. Tilføj en `st.checkbox()` der kan vise eller skjule data over grænseværdien
3. Udvid med muligheden for at vælge to sensorkolonner og vise begge grafer samtidig
4. Brug `st.sidebar` til at flytte interaktive elementer ud til venstremenuen
5. Tilføj `st.download_button()` der gør det muligt at eksportere det filtrerede datasæt
6. Vis en tabel med `st.dataframe()` og lad brugeren selv filtrere via interaktive felter
7. Brug `st.markdown()` til at tilføje overskrifter, info og forklarende tekst i dit dashboard

---

## ✅ Tjekliste

* [ ] Jeg har oprettet og kørt et Streamlit-dashboard lokalt
* [ ] Jeg har uploadet et datasæt og filtreret det med widgets
* [ ] Jeg har visualiseret filtreret data via graf eller tabel
* [ ] Jeg har eksporteret eller givet mulighed for download
* [ ] Jeg har evalueret brugeroplevelsen og layoutet
* [ ] Jeg har forstået, hvordan dette kan anvendes i eksamensprojekt eller dokumentation

---

## 🚀 Udvidelse: Simuleret realtid med Streamlit

Du kan også bruge Streamlit til at vise data løbende – næsten som realtidsopdatering – ved at læse fra en log-fil og opdatere grafen gentagne gange.

```python
import streamlit as st
import pandas as pd
import time

st.title("📈 Realtidssimulering")

# Knappen starter loopet
if st.button("Start simulering"):
    placeholder = st.empty()
    for i in range(30):
        data = pd.read_csv("log.csv")
        placeholder.line_chart(data["værdi"])
        time.sleep(1)
```

> Dette kræver, at `log.csv` bliver opdateret løbende af et andet script – fx via ESP32 eller Python-script der logger seriel data.

---

## 📌 Ekstra idéer

* Tilføj et `st.stop()` hvis brugeren vil afbryde loopet
* Vis både nyeste måling og hele målehistorikken
* Kombinér med annotering eller tærskel-alarm

---

> Streamlit gør det muligt at lave simple "soft real-time" dashboards – og er en god vej til at simulere og teste interface før den endelige løsning er klar.
