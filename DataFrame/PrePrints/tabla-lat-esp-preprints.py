import pandas as pd

# Mapeo de códigos de país a nombres completos
nombres_paises = {
    'ar': 'Argentina', 'bo': 'Bolivia', 'br': 'Brasil', 'cl': 'Chile', 'co': 'Colombia',
    'cr': 'Costa Rica', 'cu': 'Cuba', 'do': 'República Dominicana', 'ec': 'Ecuador',
    'sv': 'El Salvador', 'gt': 'Guatemala', 'hn': 'Honduras', 'mx': 'México',
    'ni': 'Nicaragua', 'pa': 'Panamá', 'py': 'Paraguay', 'pe': 'Perú', 'pr': 'Puerto Rico',
    'uy': 'Uruguay', 've': 'Venezuela', 'es': 'España'
}

# Cargar el DataFrame enriquecido
df = pd.read_csv(r"C:\Users\Patricio\Documents\GitHub\LatArXiv-context\DataFrame\dataframe-enriquecido.csv")

# Filtrar por países de interés
codigos_paises = list(nombres_paises.keys())
df_filtrado = df[df['organisation_country'].isin(codigos_paises)]

# Filtrar por los content_types específicos
content_types_interes = [
    'journal_articles', 'bibliographic_references',
    'conference_and_workshop_papers', 'unpub_reports_and_working_papers'
]

# Asegurarse de que 'content_types' es una cadena antes de intentar iterar sobre ella
df_filtrado = df_filtrado[df_filtrado['content_types'].apply(lambda x: any(ct in str(x) for ct in content_types_interes))]

# Crear una columna con el nombre completo del país utilizando el mapeo
df_filtrado['country_name'] = df_filtrado['organisation_country'].map(nombres_paises)

# Crear la tabla dinámica
tabla_lat_esp = df_filtrado.pivot_table(index='country_name', values='repository_id', aggfunc='count', fill_value=0)
tabla_lat_esp = tabla_lat_esp.rename(columns={'repository_id': 'count_repositories'})

# Ordenar los resultados por la cantidad de repositorios, de mayor a menor
tabla_lat_esp_sorted = tabla_lat_esp.sort_values('count_repositories', ascending=False)

# Exportar a HTML
ruta_html = r"C:\Users\Patricio\Documents\GitHub\LatArXiv-context\DataFrame\PrePrints\tabla-lat-esp-preprints.html"
tabla_lat_esp_sorted.to_html(ruta_html, border=0)

print(f"Tabla de datos exportada exitosamente a {ruta_html}")