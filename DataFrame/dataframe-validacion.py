import pandas as pd

# Ajusta la ruta del archivo según donde tengas almacenado tu CSV
ruta_csv = r"C:\Users\Patricio\Documents\GitHub\LatArXiv-context\DataFrame\dataframe.csv"

# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv(ruta_csv)

# Contar cuántas entradas hay de Brasil (suponiendo que el código para Brasil es 'br')
conteo_brasil = df[df['organisation_country'] == 'br'].shape[0]

print(f"Número de entradas de Brasil: {conteo_brasil}")
