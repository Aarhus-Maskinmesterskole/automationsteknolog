import pandas as pd
data = pd.read_csv('Teknolog/02-semester/teknologi-og-projektudvikling/03-præsentationer/dag02-csv-pandas/01-kort-version/python/sensor.csv', sep=',')
print(data.head(51))
print(data.info())
print(data.describe())
x_val = []
for x in range(0,51):
    x_val.append(x)
data['water_level'] = x_val
print(data)
