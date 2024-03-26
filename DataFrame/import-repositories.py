import requests
import pandas as pd

def obtener_todos_los_datos(api_key, limit=100):
    """
    Esta función obtiene todos los datos de la API, manejando la paginación automáticamente.
    """
    items = []
    offset = 0
    while True:
        base_url = 'https://v2.sherpa.ac.uk/cgi/retrieve'
        params = {
            'item-type': 'repository',
            'api-key': api_key,
            'format': 'Json',
            'limit': limit,
            'offset': offset
        }
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            new_items = response.json().get('items', [])
            if not new_items:
                break  # No más datos para recuperar
            items.extend(new_items)
            offset += limit
        else:
            print(f'Error en la solicitud: {response.status_code}')
            break
    return items

def procesar_datos(items):
    """
    Esta función procesa una lista de ítems de repositorios y devuelve una lista de diccionarios aplanados.
    """
    flattened_data = []
    for item in items:
        flattened_data.append({
            'repository_id': item.get('system_metadata', {}).get('id', 'N/A'),
            'repository_name': item.get('repository_metadata', {}).get('name', [{'name': 'N/A'}])[0].get('name', 'N/A'),
            'repository_type': item.get('repository_metadata', {}).get('type', 'N/A'),
            'repository_url': item.get('repository_metadata', {}).get('url', 'N/A'),
            'organisation_name': item.get('organisation', {}).get('name', [{'name': 'N/A'}])[0].get('name', 'N/A'),
            'organisation_country': item.get('organisation', {}).get('country', 'N/A'),
            'metadata_record_count': item.get('repository_metadata', {}).get('metadata_record_count', 0),
            'full_text_record_count': item.get('repository_metadata', {}).get('full_text_record_count', 0),
        })
    return flattened_data

# Configuración inicial
api_key = 'D34D66BA-EB78-11EE-9884-206A371EB7E0'

# Obtener todos los datos
items = obtener_todos_los_datos(api_key)

if items:
    # Procesar datos
    flattened_data = procesar_datos(items)
    
    # Crear DataFrame
    df = pd.DataFrame(flattened_data)
    
    # Exportar a CSV
    output_path = r'C:\Users\Patricio\Documents\GitHub\LatArXiv-context\DataFrame\dataframe.csv'
    df.to_csv(output_path, index=False)
    
    print(f'DataFrame exportado exitosamente a {output_path}')
else:
    print('No se pudieron obtener los datos.')