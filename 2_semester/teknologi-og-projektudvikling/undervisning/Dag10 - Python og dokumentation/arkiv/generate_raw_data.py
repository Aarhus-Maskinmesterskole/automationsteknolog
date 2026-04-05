# generer en raw_data.csv fil med 1000 rækker med tilfældige data 
# inkl. nogle NaN-værdier og enkelte fulde NaN-rækker

import pandas as pd
import numpy as np

# --- Grunddata ---
num_rows = 1000
np.random.seed(42)  # for reproducerbare resultater

data = {
    "timestamp": pd.date_range(start="2023-01-01", periods=num_rows, freq="H"),
    "temperature": np.random.uniform(low=-20, high=40, size=num_rows),
    "humidity": np.random.uniform(low=0, high=100, size=num_rows),
    "gas": np.random.uniform(low=0, high=1000, size=num_rows),
    "lux": np.random.uniform(low=0, high=10000, size=num_rows),
    "distance": np.random.uniform(low=0, high=100, size=num_rows)
}

df = pd.DataFrame(data)

# --- Tilføj enkelte NaN-værdier (ca. 2-3% af cellerne) ---
for col in ["temperature", "humidity", "gas", "lux", "distance"]:
    # vælg tilfældige indekser
    n_missing = int(num_rows * 0.02)
    missing_idx = np.random.choice(df.index, n_missing, replace=False)
    df.loc[missing_idx, col] = np.nan

# --- Tilføj hele NaN-rækker (fx 5 tilfældige rækker) ---
full_nan_rows = np.random.choice(df.index, 5, replace=False)
df.loc[full_nan_rows, ["temperature", "humidity", "gas", "lux", "distance"]] = np.nan

# --- (Valgfrit) Udskriv hvor mange NaN vi har lavet ---
print("Antal NaN pr. kolonne:")
print(df.isna().sum())
print("\nIndekser for hele NaN-rækker:", full_nan_rows)

# --- Gem CSV ---
output_path = "raw_data.csv"
df.to_csv(output_path, index=False)

print(f"raw_data.csv fil genereret med {num_rows} rækker, inkl. enkelte NaN og hele tomme rækker.")
print(f"Filen er gemt her: {output_path}")
