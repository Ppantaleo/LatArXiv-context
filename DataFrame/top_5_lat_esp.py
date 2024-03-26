import pandas as pd

# Cargar el DataFrame desde el archivo CSV
archivo_csv = r"C:\Users\Patricio\Documents\GitHub\LatArXiv-context\DataFrame\dataframe.csv"
df = pd.read_csv(archivo_csv)

# Predefinir el orden de los países basado en tu lista
orden_paises = ['pe', 'es', 'br', 'co', 'ar', 'mx', 'ec', 'cl', 'cu', 'cr', 'uy', 'ni', 'sv', 'pa', 've', 'do', 'hn', 'py', 'bo', 'pr', 'gt']

# Filtrar por países de interés
df_filtrado = df[df['organisation_country'].isin(orden_paises)]

# Asegurar que 'metadata_record_count' es numérico
df_filtrado.loc[:, 'metadata_record_count'] = pd.to_numeric(df_filtrado['metadata_record_count'], errors='coerce')

# Ordenar el DataFrame filtrado por país según el orden predefinido y luego por 'metadata_record_count' descendente
df_filtrado['orden_pais'] = pd.Categorical(df_filtrado['organisation_country'], categories=orden_paises, ordered=True)
df_ordenado = df_filtrado.sort_values(by=['orden_pais', 'metadata_record_count'], ascending=[True, False])

# Seleccionar las 5 instituciones con mayor número de 'metadata_record_count' por país
top_5_por_pais = df_ordenado.groupby('organisation_country').head(5)

# Filtrar los países que tienen al menos 5 repositorios
paises_con_5_o_mas = top_5_por_pais['organisation_country'].value_counts()[lambda x: x>=5].index.tolist()
top_5_por_pais_filtrado = top_5_por_pais[top_5_por_pais['organisation_country'].isin(paises_con_5_o_mas)]

# Excluir la columna 'repository_id' y 'orden_pais' de los resultados finales
columnas_a_mostrar = ['organisation_country', 'organisation_name', 'repository_name', 'repository_type', 'repository_url', 'metadata_record_count', 'full_text_record_count']
top_5_por_pais_final = top_5_por_pais_filtrado[columnas_a_mostrar]

# Exportar los resultados a un archivo HTML
ruta_html = r"C:\Users\Patricio\Documents\GitHub\LatArXiv-context\DataFrame\top_5_lat_esp.html"
top_5_por_pais_final.to_html(ruta_html, index=False)

print(f"La tabla ha sido exportada exitosamente a {ruta_html}")
