# LatArXiv-context
Este repositorio presenta los elementos básicos para reproducir un análisis de contexto de inserción y mercadeo para un servidor PrePrints y de Datos en Latinoamérica y mundo de habla hispana.

## Estructura del repositorio
A continuación se describe la organización del presente repositorio de datos y códigos. Para trabajar con la API de Sherpa seguimos las orientaciones de [Sherpa Services](https://v2.sherpa.ac.uk/api/ "Sherpa Services API") en donde se indica que hay que crear un usuario en el sistema para acceder al API key necesaria para consultar los datos.
Las orientaciones específicas del [Metadata Schema](https://v2.sherpa.ac.uk/api/metadata-schema.html) se encuentran también en la documentación de Sherpa y se específica los diferentes `item-type` y los metadatos disponibles específicamente para `item-type`: `repository`.


### Directorios

`/DataFrame`: Dentro se pueden encontrar los códigos en Python y los export asociados:
- `/DataFrame/import-repositories.py` crea el dataframe completo llamando a la API de Sherpa y filtrando específicamente que sean repositorios: `item-type`: `repository`. Se excluyen los demás `item-type`: 'funder', 'funder_group', 'publisher', 'publisher_policy', 'publication'.
- `/DataFrame/dataframe.csv` es el archivo exportado de `/DataFrame/import-repositories.py`.