import pandas as pd

# Mapeo de códigos de país a nombres completos
nombres_paises = {
    'ar': 'Argentina', 'bo': 'Bolivia', 'br': 'Brasil', 'cl': 'Chile', 'co': 'Colombia',
    'cr': 'Costa Rica', 'cu': 'Cuba', 'do': 'República Dominicana', 'ec': 'Ecuador',
    'sv': 'El Salvador', 'gt': 'Guatemala', 'hn': 'Honduras', 'mx': 'México',
    'ni': 'Nicaragua', 'pa': 'Panamá', 'py': 'Paraguay', 'pe': 'Perú', 'pr': 'Puerto Rico',
    'uy': 'Uruguay', 've': 'Venezuela', 'es': 'España'
}

# Cargar el DataFrame
df = pd.read_csv(r"C:\Users\Patricio\Documents\GitHub\LatArXiv-context\DataFrame\dataframe.csv")

# Lista de códigos de países de Latinoamérica + España en minúsculas
codigos_paises = list(nombres_paises.keys())

# Filtrar solo los registros de los países de interés
df_filtrado = df[df['organisation_country'].isin(codigos_paises)]

# Crear la tabla dinámica y añadir el nombre completo del país
tabla_lat_esp = df_filtrado.pivot_table(index='organisation_country', values='repository_id', aggfunc='count', fill_value=0)
tabla_lat_esp['country_name'] = tabla_lat_esp.index.map(nombres_paises.get)
tabla_lat_esp = tabla_lat_esp.rename(columns={'repository_id': 'count_repositories'})

# Ordenar los resultados por la cantidad de repositorios, de mayor a menor
tabla_lat_esp_sorted = tabla_lat_esp.sort_values('count_repositories', ascending=False)

# Exportar a HTML
ruta_html = r"C:\Users\Patricio\Documents\GitHub\LatArXiv-context\DataFrame\tabla-lat-esp.html"
tabla_lat_esp_sorted.to_html(ruta_html, columns=['country_name', 'count_repositories'], border=0)

print(f"Tabla de datos exportada exitosamente a {ruta_html}")