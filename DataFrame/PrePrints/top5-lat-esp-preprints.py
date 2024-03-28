import pandas as pd

# Mapeo de códigos de país a nombres completos
nombres_paises = {
    'es': 'España', 'br': 'Brasil', 'pe': 'Perú', 'co': 'Colombia',
    'ar': 'Argentina', 'mx': 'México', 'cl': 'Chile', 'ec': 'Ecuador',
    'cu': 'Cuba', 'cr': 'Costa Rica', 'uy': 'Uruguay', 'pa': 'Panamá',
    've': 'Venezuela', 'sv': 'El Salvador', 'ni': 'Nicaragua',
    'do': 'República Dominicana', 'hn': 'Honduras', 'py': 'Paraguay',
    'bo': 'Bolivia', 'pr': 'Puerto Rico', 'gt': 'Guatemala'
}

archivo_csv_enriquecido = r"C:\Users\Patricio\Documents\GitHub\LatArXiv-context\DataFrame\dataframe-enriquecido.csv"
df = pd.read_csv(archivo_csv_enriquecido)

# Orden predefinido de los países basado en tu lista
orden_paises = ['es', 'br', 'pe', 'co', 'ar', 'mx', 'cl', 'ec', 'cu', 'cr', 'uy', 'pa', 've', 'sv', 'ni', 'do', 'hn', 'py', 'bo', 'pr', 'gt']

# Filtrar por países de interés
df_filtrado = df[df['organisation_country'].isin(orden_paises)].copy()

# Convertir 'content_types' a cadena y filtrar por los content_types de interés
content_types_interes = ['journal_articles', 'bibliographic_references', 'conference_and_workshop_papers', 'unpub_reports_and_working_papers']
df_filtrado['content_types'] = df_filtrado['content_types'].astype(str)
df_filtrado = df_filtrado[df_filtrado['content_types'].apply(lambda x: any(ct in x.split(', ') for ct in content_types_interes))]

# Convertir 'metadata_record_count' a numérico para ordenamiento
df_filtrado['metadata_record_count'] = pd.to_numeric(df_filtrado['metadata_record_count'], errors='coerce')

# Ordenar por país y por 'metadata_record_count' descendente
df_filtrado['orden_pais'] = pd.Categorical(df_filtrado['organisation_country'], categories=orden_paises, ordered=True)
df_ordenado = df_filtrado.sort_values(by=['orden_pais', 'metadata_record_count'], ascending=[True, False])

# Seleccionar las top 5 instituciones por país
top_5_por_pais = df_ordenado.groupby('orden_pais', observed=True).head(5)

# Añadir nombres de países
top_5_por_pais['country_name'] = top_5_por_pais['organisation_country'].map(nombres_paises)

# Columnas a mostrar en la tabla final
columnas_a_mostrar = ['country_name', 'organisation_name', 'repository_name', 'repository_type', 
                      'repository_url', 'oai_url', 'software', 'content_types', 
                      'metadata_record_count', 'full_text_record_count']

# Exportar a HTML
ruta_html = r"C:\Users\Patricio\Documents\GitHub\LatArXiv-context\DataFrame\PrePrints\top_5_lat_esp_preprints.html"
top_5_por_pais[columnas_a_mostrar].to_html(ruta_html, index=False, border=0)

print(f"La tabla ha sido exportada exitosamente a {ruta_html}")