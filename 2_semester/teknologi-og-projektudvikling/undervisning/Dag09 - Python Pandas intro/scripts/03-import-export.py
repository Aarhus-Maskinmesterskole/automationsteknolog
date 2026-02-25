import pandas as pd
data = pd.read_csv('Teknolog/02-semester/teknologi-og-projektudvikling/03-præsentationer/dag02-csv-pandas/01-kort-version/python/sensor.csv')
print(data.head(5))
data = data[data['temperature']>24]
print(data['temperature'])

pd.DataFrame(data['temperature']).to_csv('Teknolog/02-semester/teknologi-og-projektudvikling/03-præsentationer/dag02-csv-pandas/01-kort-version/python/filtered_temperature.csv', index=False)

