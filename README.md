# LatArXiv-context
Este repositorio presenta los elementos básicos para reproducir un análisis de contexto de inserción y mercadeo para un servidor PrePrints y de Datos en Latinoamérica y mundo de habla hispana.

## Estructura del repositorio
A continuación se describe la organización del presente repositorio de datos y códigos. Para trabajar con la API de Sherpa seguimos las orientaciones de [Sherpa Services](https://v2.sherpa.ac.uk/api/ "Sherpa Services API") en donde se indica que hay que crear un usuario en el sistema para acceder al API key necesaria para consultar los datos.
Las orientaciones específicas del [Metadata Schema](https://v2.sherpa.ac.uk/api/metadata-schema.html) se encuentran también en la documentación de Sherpa y se específica los diferentes `item-type` y los metadatos disponibles específicamente para `item-type`: `repository`.


### Directorios

`/DataFrame`: Dentro se pueden encontrar los códigos en Python y los export asociados:
- `/DataFrame/import-repositories.py` crea el dataframe completo llamando a la API de Sherpa y filtrando específicamente que sean repositorios: `item-type`: `repository`. Se excluyen los demás `item-type`: `funder`, `funder_group`, `publisher`, `publisher_policy`, `publication`.
- `/DataFrame/dataframe.csv` es el archivo exportado de `/DataFrame/import-repositories.py`.
- `/DataFrame/dataframe-validacion.py` con este archivo se hace una validación del dataframe para corroborar que sea correcto. En este caso se corre un código para filtrar y mostrar todos los repositorios con `organisation_country` identificados con `br`. Arroja el mismo resultado de 173 repositorios que muestran las [estadísticas oficiales de OpenDOAR para Brazil](https://v2.sherpa.ac.uk/view/repository_by_country/Brazil.html) al día de la fecha (26/3/2024).
- `/DataFrame/tabla-lat-esp.py` crea una tabla que filtra `/DataFrame/dataframe.csv` por países de Latinoamérica más España y los ordena acorde a la cantidad de repositorios registrados en Sherpa, de mayor a menor. Adicionalmente, se mapea todos los identificadores de los países para colocar una etiqueta legible a cada una. 
- `/DataFrame/tabla-lat-esp.html` es el archivo exportado de `/DataFrame/tabla-lat-esp.py`.
- `/DataFrame/top_5_lat_esp.py` crea la tabla que filtra países de Latinoamérica más España en `/DataFrame/dataframe.csv` y filtra los 5 repositorios con mayor número de contenido depositado en cada país según el valor en `metadata_record_count`. A su vez, el valor arrojado se ordena de mayor a menor y en orden de países según se muestra en `/DataFrame/tabla-lat-esp.html`.
- `/DataFrame/top_5_lat_esp.html` es la tabla exportada de `/DataFrame/top_5_lat_esp.py`.