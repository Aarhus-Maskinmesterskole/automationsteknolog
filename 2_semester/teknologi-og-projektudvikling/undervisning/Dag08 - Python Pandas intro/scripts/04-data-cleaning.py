import pandas as pd

# Indlæs datasæt med read_csv()
data = pd.read_csv('Teknolog/02-semester/teknologi-og-projektudvikling/03-præsentationer/dag02-csv-pandas/01-kort-version/python/sensor.csv')
print(f"Original størrelse: {len(data)} rækker")

# Undersøg null-værdier
print("\nUndersøger null-værdier...")
null_count = data.isnull().sum()
print(f"Antal null-værdier per kolonne:\n{null_count}")

# Håndter null-værdier - enten dropna() eller fillna()
print("\nHåndterer null-værdier...")
data_cleaned = data.copy()

# Metode 1: Fjern rækker med manglende værdier
rows_before = len(data_cleaned)
data_cleaned = data_cleaned.dropna()
rows_after = len(data_cleaned)
print(f"Fjernede {rows_before - rows_after} rækker med manglende værdier")

# Fjern dubletter og tæl forskellen
print("\nFjerner dubletter...")
rows_before = len(data_cleaned)
data_cleaned = data_cleaned.drop_duplicates()
rows_after = len(data_cleaned)
print(f"Fjernede {rows_before - rows_after} dubletter")

# Fjern værdier uden for et fornuftigt interval
print("\nFjerner værdier uden for fornuftige intervaller...")
rows_before = len(data_cleaned)

# Sæt fornuftige intervaller for hver kolonne (baseret på domæneviden)
# Temperatur: f.eks. mellem -10 og 50 grader Celsius
data_cleaned = data_cleaned[(data_cleaned['temperature'] >= -10) & (data_cleaned['temperature'] <= 50)]

# Luftfugtighed: mellem 0 og 100%
data_cleaned = data_cleaned[(data_cleaned['humidity'] >= 0) & (data_cleaned['humidity'] <= 100)]

# Lufttryk: f.eks. mellem 900 og 1100 hPa
data_cleaned = data_cleaned[(data_cleaned['pressure'] >= 900) & (data_cleaned['pressure'] <= 1100)]

# Batteri: mellem 0 og 100%
data_cleaned = data_cleaned[(data_cleaned['battery_level'] >= 0) & (data_cleaned['battery_level'] <= 100)]

rows_after = len(data_cleaned)
print(f"Fjernede {rows_before - rows_after} rækker med værdier uden for intervaller")

# Gem det rensede datasæt
print("\nGemmer renset datasæt...")
data_cleaned.to_csv('renset.csv', index=False)

print(f"\nFærdig! Det rensede datasæt indeholder {len(data_cleaned)} rækker.")
print(f"Reduktion: {len(data) - len(data_cleaned)} rækker ({((len(data) - len(data_cleaned)) / len(data) * 100):.2f}%)")

