# ⚙️ 05 – Udvidelser og fejlhåndtering i visualisering

I takt med at du begynder at arbejde med rigtige målinger fra ESP32, PLC eller andre kilder, vil du uundgåeligt møde målefejl, afvigelser og uregelmæssigheder i datasættet. Det kan være værdier, der ligger langt uden for det forventede område, manglende datapunkter (`NaN`) eller svingende dataserier med mange udsving. Hvis ikke disse behandles korrekt, risikerer du at præsentere grafer og resultater, der er misvisende eller direkte forkerte.

Dette modul handler derfor om at gøre dine visualiseringer robuste og informative – også når data ikke er perfekte. Du lærer at identificere outliers, rense datasæt, udfylde huller og tilpasse grafer, så de tydeligt formidler relevante indsigter. Desuden introduceres avancerede teknikker som betinget farvestyling og brug af subplots, så dine figurer bliver mere fleksible og læsbare.

---

## 🎯 Læringsmål

* At kunne identificere og fjerne outliers (ekstremt høje eller lave måleværdier) fra CSV-data
* At håndtere manglende data (`NaN`) i CSV-filer på en måde der bevarer datakvalitet
* At filtrere målinger fra CSV baseret på betingelser – fx vis kun værdier over en tærskel
* At arbejde med betinget visualisering af CSV-data, hvor farver og form tilpasses måleværdi
* At strukturere visualiseringer med subplots og flere akser baseret på CSV-kolonner

---

## 📊 Arbejde med CSV-data som udgangspunkt

Alle eksempler i dette modul tager udgangspunkt i CSV-filer med sensordata. Her er en typisk struktur:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Indlæs data fra CSV-fil
data = pd.read_csv("measurements.csv")
print(data.head())  # Vis første 5 rækker
print(data.info())  # Vis datatyper og missing values
```

**Eksempel på CSV-struktur:**
```csv
timestamp,temperatur,fugtighed,tryk,co2_niveau
2024-01-01 08:00:00,22.5,45.2,1013.2,420
2024-01-01 08:05:00,22.8,44.9,1013.1,425
2024-01-01 08:10:00,999.9,43.1,1013.0,430
2024-01-01 08:15:00,23.1,,1012.8,435
```

---

## 🧼 Filtrering og fjernelse af outliers fra CSV-data

Outliers i CSV-filer kan fx skyldes sensorfejl, hvor temperatursensoren pludselig aflæser 999.9°C eller -273°C.

```python
# Indlæs CSV-fil
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("measurements.csv")

# Undersøg data før filtrering
print("Data før filtrering:")
print(f"Min temperatur: {data['temperature'].min()}")
print(f"Max temperatur: {data['temperature'].max()}")
print(f"Antal målinger: {len(data)}")

# Fjern outliers - temperaturer uden for realistisk interval
data_filtered = data[(data["temperature"] > 10) & (data["temperature"] < 25)]

# Fjern også outliers i fugtighed (0-100%)
data_filtered = data_filtered[(data_filtered["humidity"] >= 0) & 
                              (data_filtered["humidity"] <= 65)]

print("\nData efter filtrering:")
print(f"Min temperatur: {data_filtered['temperature'].min()}")
print(f"Max temperatur: {data_filtered['temperature'].max()}")
print(f"Antal målinger: {len(data_filtered)}")

# Visualiser før og efter filtrering
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Før filtrering
axs[0].plot(data['temperature'], 'o-', markersize=3)
axs[0].set_title("Før outlier-filtrering")
axs[0].set_ylabel("Temperatur (°C)")

# Efter filtrering
axs[1].plot(data_filtered['temperature'], 'o-', markersize=3)
axs[1].set_title("Efter outlier-filtrering")
axs[1].set_ylabel("Temperatur (°C)")

plt.tight_layout()
plt.show()
```

---

## 🕳️ Håndtering af manglende data i CSV-filer

Manglende værdier i CSV-filer vises som `NaN` når de indlæses med pandas.

```python
import pandas as pd
import matplotlib.pyplot as plt
# Indlæs CSV med manglende værdier
data = pd.read_csv("measurements.csv")

# Check for manglende værdier
print("Manglende værdier pr. kolonne:")
print(data.isnull().sum())

# Strategi 1: Erstat NaN med gennemsnitsværdi
data_mean_filled = data.copy()
for column in ['temperature', 'humidity']:
    if data_mean_filled[column].isnull().sum() > 0:
        mean_val = data_mean_filled[column].mean()
        data_mean_filled[column].fillna(mean_val, inplace=True)
        print(f"Erstattede {data[column].isnull().sum()} NaN værdier i {column} med gennemsnit: {mean_val:.2f}")

# Strategi 2: Interpolér mellem værdier
data_interpolated = data.copy()
for column in ['temperature', 'humidity']:
    data_interpolated[column] = data_interpolated[column].interpolate(method="linear")

# Visualiser de forskellige strategier
fig, axs = plt.subplots(3, 1, figsize=(12, 10))

# Original data med NaN
axs[0].plot(data['temperature'], 'o-', markersize=3, label='Original (med NaN)')
axs[0].set_title("Original CSV-data med manglende værdier")
axs[0].set_ylabel("Temperature (°C)")
axs[0].legend()

# Med gennemsnit
axs[1].plot(data_mean_filled['temperature'], 'o-', markersize=3, label='NaN erstattet med gennemsnit', color='orange')
axs[1].set_title("NaN erstattet med gennemsnitsværdi")
axs[1].set_ylabel("Temperature (°C)")
axs[1].legend()

# Med interpolation
axs[2].plot(data_interpolated['temperature'], 'o-', markersize=3, label='NaN interpoleret', color='green')
axs[2].set_title("NaN erstattet med lineær interpolation")
axs[2].set_ylabel("Temperatur (°C)")
axs[2].set_xlabel("Måling nummer")
axs[2].legend()

plt.tight_layout()
plt.show()
```

---

## 🎨 Farvekodning og betinget styling af CSV-data

Farvekodning er særligt nyttigt når du arbejder med CSV-data fra overvågningssystemer.

```python
import pandas as pd
import matplotlib.pyplot as plt
# Indlæs CSV-data
data = pd.read_csv("measurements.csv")

# Definer alarmniveauer
temp_alarm = 25  # Temperatur alarm ved 25°C
co2_alarm = 1000  # CO2 alarm ved 1000 ppm

# Opret betinget farvekodning baseret på CSV-værdier
def get_temp_color(temp_value):
    if temp_value > temp_alarm:
        return 'red'
    elif temp_value > 20:
        return 'orange' 
    else:
        return 'blue'

# Anvend farvekodning på CSV-data
colors = [get_temp_color(temp) for temp in data['temperature'] if not pd.isna(temp)]
valid_temps = data['temperature'].dropna()
valid_indices = valid_temps.index

# Visualiser med betinget farve
plt.figure(figsize=(12, 6))
plt.scatter(valid_indices, valid_temps, c=colors, s=30, alpha=0.7)
plt.axhline(y=temp_alarm, color='red', linestyle='--', label=f'Alarm niveau ({temp_alarm}°C)')
plt.title("Temperatur fra CSV med alarm-farvekodning")
plt.xlabel("Måling nummer (fra CSV)")
plt.ylabel("Temperatur (°C)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Statistik over alarmer
alarm_count = sum(1 for temp in data['temperature'] if temp > temp_alarm)
print(f"Antal temperature-alarmer i CSV-data: {alarm_count}")
```

---

## 🧩 Flere plots af CSV-kolonner (subplots)

Når din CSV-fil indeholder flere sensormålinger, kan subplots give et godt overblik.

```python
import pandas as pd
import matplotlib.pyplot as plt
# Indlæs CSV med flere sensortyper
data = pd.read_csv("measurements.csv")

# Konverter timestamp hvis nødvendigt
if 'timestamp' in data.columns:
    data['timestamp'] = pd.to_datetime(data['timestamp'])

# Opret subplot-figur baseret på CSV-kolonner
fig, axs = plt.subplots(1, 2, figsize=(15, 10))
fig.suptitle('Sensor-data fra CSV-fil', fontsize=16)

# Temperatur (øverst venstre)
if 'temperature' in data.columns:
    axs[0].plot(data['temperature'], color='red', linewidth=2)
    axs[0].set_title('Temperature')
    axs[0].set_ylabel('°C')
    axs[0].grid(True, alpha=0.3)

# Fugtighed (øverst højre)  
if 'humidity' in data.columns:
    axs[1].plot(data['humidity'], color='blue', linewidth=2)
    axs[1].set_title('Relative Humidity')
    axs[1].set_ylabel('%')
    axs[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print statistikker fra CSV-data
print("\n=== Statistikker fra CSV-fil ===")
for column in ['temperature', 'humidity']:
    if column in data.columns:
        print(f"{column.capitalize()}:")
        print(f"  Gennemsnit: {data[column].mean():.2f}")
        print(f"  Min: {data[column].min():.2f}")
        print(f"  Max: {data[column].max():.2f}")
        print(f"  Manglende værdier: {data[column].isnull().sum()}")
```

---

## 🔍 Avanceret CSV-analyse og filtrering

```python
import pandas as pd
import matplotlib.pyplot as plt
# Indlæs CSV og lav avancerede filtreringer
data = pd.read_csv("measurements.csv")

# Filtrér data baseret på flere betingelser fra CSV
# Eksempel: Find målinger hvor temperatur > 23°C OG fugtighed < 50%
filtered_conditions = data[(data['temperature'] > 23) & (data['humidity'] < 50)]

print(f"Antal målinger der opfylder begge betingelser: {len(filtered_conditions)}")

# Vis tidsperioder med høj temperatur og lav fugtighed
if len(filtered_conditions) > 0:
    plt.figure(figsize=(14, 8))
    
    # Plot alle datapunkter
    plt.subplot(2, 1, 1)
    plt.plot(data['temperature'], alpha=0.6, label='Alle temperatur målinger')
    plt.plot(filtered_conditions.index, filtered_conditions['temperature'], 
             'ro', markersize=6, label='Høj temp + lav fugt')
    plt.ylabel('Temperatur (°C)')
    plt.title('Temperatur fra CSV - fremhævede betingelser')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 1, 2)
    plt.plot(data['humidity'], alpha=0.6, label='Alle fugtigheds målinger')
    plt.plot(filtered_conditions.index, filtered_conditions['humidity'], 
             'ro', markersize=6, label='Høj temp + lav fugt')
    plt.ylabel('Fugtighed (%)')
    plt.xlabel('Måling nummer fra CSV')
    plt.title('Fugtighed fra CSV - fremhævede betingelser')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
```

---

## 🧪 Øvelser med CSV-data

1. **Outlier-analyse**: Indlæs en CSV-fil og identificer outliers i forskellige kolonner. Lav plots før og efter filtrering.

2. **Missing data**: Opret en CSV-fil med nogle manglende værdier og test forskellige strategier (gennemsnit, interpolation, fjernelse).

3. **Alarm-visualisering**: Definer alarmniveauer for dine CSV-data og lav en scatter-plot med farvekodning baseret på alarmstatus.

4. **Multi-sensor dashboard**: Brug subplots til at vise alle sensortyper fra din CSV-fil i ét overbliksbillede.

5. **Betinget filtrering**: Find specifikke kombinationer af værdier i din CSV (fx høj temperatur OG lav fugtighed) og visualiser dem.

6. **Tidsbaseret analyse**: Hvis din CSV har timestamps, lav plots der viser udvikling over tid med highlights af kritiske perioder.

---

## ✅ Tjekliste

* [ ] Jeg kan indlæse og analysere CSV-filer med pandas
* [ ] Jeg har filtreret CSV-datasæt for outliers og dokumenteret grænserne  
* [ ] Jeg har behandlet `NaN`-værdier i CSV med enten gennemsnit eller interpolation
* [ ] Jeg har brugt farvekodning til at fremhæve vigtige datapunkter fra CSV
* [ ] Jeg har delt CSV-visualiseringer op i subplots med akseetiketter
* [ ] Jeg kan kombinere flere betingelser til at filtrere CSV-data
* [ ] Jeg har reflekteret over, hvordan datakvalitet i CSV-filer påvirker mine plots

---

> Gode grafer starter med rene CSV-data – men de bedste grafer formidler også usikkerhed og dokumenterer hvad der er fjernet, renset og fremhævet fra de originale CSV-filer.
