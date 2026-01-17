import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Gør plots pænere
sns.set_style('whitegrid')
plt.rcParams.update({'font.size': 12})

# 1. Indlæs data og konvertér kolonnen 'timestamp' til datetime
print("Indlæser datasæt...")
data = pd.read_csv('Teknolog/02-semester/teknologi-og-projektudvikling/03-præsentationer/dag02-csv-pandas/01-kort-version/python/sensor.csv')

# Konvertér timestamp-kolonnen til datetime
data['timestamp'] = pd.to_datetime(data['timestamp'])
print(f"Tidsserie går fra {data['timestamp'].min()} til {data['timestamp'].max()}")

# 2. Brug set_index() til at sætte timestamp som index
data = data.set_index('timestamp')

# VIGTIG ÆNDRING: Sørg for at indekset er sorteret
data = data.sort_index()

print("\nData med timestamp som index:")
print(data.head())

# 3. Filtrér data til en bestemt dag (1. september 2023)
print("\nFiltrerer data til 1. september 2023...")
single_day = data.loc['2023-09-01']
print(f"Filtreret datasæt indeholder {len(single_day)} målinger")

# Nu kan du filtrere til en bestemt time
single_hour = data.loc['2023-09-01 08:00:00':'2023-09-01 08:59:59']
print(f"Filtreret datasæt for timen 8-9 indeholder {len(single_hour)} målinger")

# 4. Lav en ny DataFrame med gennemsnit hver 10. minut
print("\nLaver 10-minutters gennemsnit...")

# Opretter en liste til at gemme resample-resultater for hver sensor
resampled_dfs = []

# For hver unik sensor, lav en resampling
for sensor_id in data['sensor_id'].unique():
    # Filtrer data for denne sensor
    sensor_data = data[data['sensor_id'] == sensor_id].copy()
    
    # Gem sensor_id og location før resampling
    sensor_location = sensor_data['location'].iloc[0]
    
    # Fjern ikke-numeriske kolonner før resampling
    numeric_data = sensor_data.select_dtypes(include=['number'])
    
    # Resample kun de numeriske kolonner - brug 'min' i stedet for 'T'
    resampled = numeric_data.resample('10min').mean()
    
    # Tilføj sensor_id og location tilbage som kolonner
    resampled['sensor_id'] = sensor_id
    resampled['location'] = sensor_location
    
    # Gem resultatet
    resampled_dfs.append(resampled)

# Kombiner alle resamplede dataframes
resampled_data = pd.concat(resampled_dfs)
print(resampled_data.head())
