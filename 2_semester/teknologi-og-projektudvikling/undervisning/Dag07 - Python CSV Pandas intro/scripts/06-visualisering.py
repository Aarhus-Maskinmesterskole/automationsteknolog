import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator

# Forbedrer plot æstetik
sns.set_style('whitegrid')
plt.rcParams.update({
    'font.size': 12,
    'figure.figsize': (12, 8),
    'font.family': 'sans-serif',
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12
})

# Indlæs datasættet
print("Indlæser sensordatasæt...")
file_path = 'Teknolog/02-semester/teknologi-og-projektudvikling/03-præsentationer/dag02-csv-pandas/01-kort-version/python/sensor.csv'
# Pandas understøtter kun kommentar-karakterer med længde 1
data = pd.read_csv(file_path, comment='#')
# Alternativt, hvis der er problemer med kommentarlinjer, kan vi skippe rækker
# data = pd.read_csv(file_path, skiprows=1)  # Spring første linje over

# Konverter timestamp til datetime format
data['timestamp'] = pd.to_datetime(data['timestamp'])
print(f"Datasæt dækker perioden: {data['timestamp'].min()} til {data['timestamp'].max()}")

# Få et overblik over data
print("\nDatasæt overblik:")
print(f"Antal målinger: {len(data)}")
print(f"Antal sensorer: {data['sensor_id'].nunique()}")
print(f"Kolonner: {', '.join(data.columns)}")
print("\nPrøve på data:")
print(data.head())

# Opret en mappe til at gemme plots
import os
plot_dir = os.path.dirname(file_path)
print(f"\nGemmer plots i: {plot_dir}")

# 1. Lav et linjediagram med temperaturdata over tid
print("\n1. Opretter linjediagram af temperatur over tid...")
plt.figure(figsize=(14, 8))

# Plot hver sensors temperaturdata
for sensor in data['sensor_id'].unique():
    sensor_data = data[data['sensor_id'] == sensor]
    plt.plot(sensor_data['timestamp'], 
             sensor_data['temperature'], 
             linewidth=2, 
             marker='o', 
             markersize=5, 
             label=f"{sensor} - {sensor_data['location'].iloc[0]}")

# Tilføj titler, aksetekster og gitter
plt.title('Temperaturmålinger over tid', fontweight='bold')
plt.xlabel('Tidspunkt')
plt.ylabel('Temperatur (°C)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Sensor', frameon=True, facecolor='white', edgecolor='gray')

# Formater x-aksen pænt
plt.gcf().autofmt_xdate()
plt.tight_layout()

# Gem figuren
plt.savefig(f"{plot_dir}/temperatur_linjediagram.png", dpi=300, bbox_inches='tight')
print(f"Plot gemt som: {plot_dir}/temperatur_linjediagram.png")
plt.close()

# 2. Lav et histogram af temperaturværdier
print("\n2. Opretter histogram af temperaturværdier...")
plt.figure(figsize=(14, 8))

# Lav et histogram for hver sensor med transparens
for sensor in data['sensor_id'].unique():
    sensor_data = data[data['sensor_id'] == sensor]
    sns.histplot(sensor_data['temperature'], 
                 bins=15, 
                 kde=True, 
                 alpha=0.6, 
                 label=f"{sensor} - {sensor_data['location'].iloc[0]}")

# Tilføj titler og aksetekster
plt.title('Fordeling af temperaturmålinger', fontweight='bold')
plt.xlabel('Temperatur (°C)')
plt.ylabel('Antal målinger')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Sensor', frameon=True, facecolor='white', edgecolor='gray')

# Sørg for at x-aksen viser hele tal
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tight_layout()

# Gem figuren
plt.savefig(f"{plot_dir}/temperatur_histogram.png", dpi=300, bbox_inches='tight')
print(f"Plot gemt som: {plot_dir}/temperatur_histogram.png")
plt.close()

# 3. Lav et scatter plot over tid - temperatur vs. luftfugtighed
print("\n3. Opretter scatter plot af temperatur vs. luftfugtighed...")
plt.figure(figsize=(14, 8))

# Opret et scatter plot for hver sensor
for sensor in data['sensor_id'].unique():
    sensor_data = data[data['sensor_id'] == sensor]
    plt.scatter(sensor_data['temperature'], 
                sensor_data['humidity'], 
                s=100, 
                alpha=0.7, 
                label=f"{sensor} - {sensor_data['location'].iloc[0]}")

# Tilføj titler og aksetekster
plt.title('Temperatur vs. Luftfugtighed', fontweight='bold')
plt.xlabel('Temperatur (°C)')
plt.ylabel('Luftfugtighed (%)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Sensor', frameon=True, facecolor='white', edgecolor='gray')

# Tilføj trendlinje for hele datasættet
sns.regplot(x='temperature', y='humidity', data=data, 
            scatter=False, ci=None, line_kws={"color":"red", "alpha":0.7, "lw":2})

plt.tight_layout()

# Gem figuren
plt.savefig(f"{plot_dir}/temp_vs_humidity_scatter.png", dpi=300, bbox_inches='tight')
print(f"Plot gemt som: {plot_dir}/temp_vs_humidity_scatter.png")
plt.close()

# 4. Lav et sammensat plot med temperatur, luftfugtighed og tryk for en enkelt sensor
print("\n4. Opretter sammensat plot med multiple sensormålinger...")
fig, axes = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

# Vælg den første sensor som eksempel
chosen_sensor = data['sensor_id'].unique()[0]
sensor_data = data[data['sensor_id'] == chosen_sensor].sort_values('timestamp')
sensor_location = sensor_data['location'].iloc[0]

# Plot temperatur
axes[0].plot(sensor_data['timestamp'], sensor_data['temperature'], 'r-', linewidth=2)
axes[0].set_title(f'Temperatur - {chosen_sensor} ({sensor_location})')
axes[0].set_ylabel('Temperatur (°C)')
axes[0].grid(True, linestyle='--', alpha=0.7)

# Plot luftfugtighed
axes[1].plot(sensor_data['timestamp'], sensor_data['humidity'], 'g-', linewidth=2)
axes[1].set_title(f'Luftfugtighed - {chosen_sensor} ({sensor_location})')
axes[1].set_ylabel('Luftfugtighed (%)')
axes[1].grid(True, linestyle='--', alpha=0.7)

# Plot lufttryk
axes[2].plot(sensor_data['timestamp'], sensor_data['pressure'], 'b-', linewidth=2)
axes[2].set_title(f'Lufttryk - {chosen_sensor} ({sensor_location})')
axes[2].set_xlabel('Tidspunkt')
axes[2].set_ylabel('Lufttryk (hPa)')
axes[2].grid(True, linestyle='--', alpha=0.7)

# Formatér x-aksen pænt
fig.autofmt_xdate()
plt.tight_layout()

# Gem figuren
plt.savefig(f"{plot_dir}/multisensor_plot.png", dpi=300, bbox_inches='tight')
print(f"Plot gemt som: {plot_dir}/multisensor_plot.png")
plt.close()

print("\nAlle plots er genereret og gemt!")
