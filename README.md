# LatArXiv-context
Este repositorio presenta los elementos básicos para reproducir un análisis de contexto de inserción y mercadeo para un servidor PrePrints y de Datos en Latinoamérica y mundo de habla hispana.

## Estructura del repositorio
A continuación se describe la organización del presente repositorio de datos y códigos. Para trabajar con la API de Sherpa seguimos las orientaciones de [Sherpa Services](https://v2.sherpa.ac.uk/api/ "Sherpa Services API") en donde se indica que hay que crear un usuario en el sistema para acceder al API key necesaria para consultar los datos.
Las orientaciones específicas del [Metadata Schema](https://v2.sherpa.ac.uk/api/metadata-schema.html) se encuentran también en la documentación de Sherpa y se específica los diferentes `item-type` y los metadatos disponibles específicamente para `item-type`: `repository`.


### Directorios

#### /DataFrame

El material que aquí se encuentra muestra una primera aproximación generalista a los datos que Sherpa muestra específicamente para `item-type`: `repository`, es decir filtrado para repositorios. Dentro de éste se pueden encontrar distintos `content_types` con los siguientes valores: `journal_articles`, `bibliographic_references`, `conference_and_workshop_papers`, `theses_and_dissertations`, `unpub_reports_and_working_papers`, `books_chapters_and_sections`, `datasets`, `learning_objects`, `software`, `patents`, `other_special_item_types`. Aquí se muestran todos los `content_types` para `item-type`: `repository`.

- `/DataFrame/import-repositories.py` crea el dataframe completo llamando a la API de Sherpa y filtrando específicamente que sean repositorios: `item-type`: `repository`. Se excluyen los demás `item-type`: `funder`, `funder_group`, `publisher`, `publisher_policy`, `publication`. Adicionalmente, dentro de  `item-type`: `repository` solo se consultan y exportan los siguientes campos: `repository_id` `repository_name` `repository_type` `repository_url` `organisation_name` `organisation_country` `metadata_record_count` `full_text_record_count`.
- `/DataFrame/dataframe.csv` es el archivo exportado de `/DataFrame/import-repositories.py`.
- `/DataFrame/dataframe-validacion.py` con este archivo se hace una validación del dataframe para corroborar que sea correcto. En este caso se corre un código para filtrar y mostrar todos los repositorios con `organisation_country` identificados con `br`. Arroja el mismo resultado de 173 repositorios que muestran las [estadísticas oficiales de OpenDOAR para Brazil](https://v2.sherpa.ac.uk/view/repository_by_country/Brazil.html) al día de la fecha (26/3/2024).
- `/DataFrame/tabla-lat-esp.py` crea una tabla que filtra `/DataFrame/dataframe.csv` por países de Latinoamérica más España y los ordena acorde a la cantidad de repositorios registrados en Sherpa, de mayor a menor. Adicionalmente, se mapea todos los identificadores de los países para colocar una etiqueta legible a cada una. 
- `/DataFrame/tabla-lat-esp.html` es el archivo exportado de `/DataFrame/tabla-lat-esp.py`.
- `/DataFrame/top_5_lat_esp.py` crea la tabla que filtra países de Latinoamérica más España en `/DataFrame/dataframe.csv` y filtra los 5 repositorios con mayor número de contenido depositado en cada país según el valor en `metadata_record_count`. A su vez, el valor arrojado se ordena de mayor a menor y en orden de países según se muestra en `/DataFrame/tabla-lat-esp.html`.
- `/DataFrame/top_5_lat_esp.html` es la tabla exportada de `/DataFrame/top_5_lat_esp.py`.
- `/DataFrame/import-dataframe-enriquecido.py` código que agrega a `/DataFrame/import-repositories.py` los campos `oai_url` `software` `content_types` `content_subjects`. Arroja 1 resultado más que `/DataFrame/import-repositories.py` debido a la fecha de consulta. Esta consulta se realizó el día 28/3/2024.
- `/DataFrame/dataframe-enriquecido.csv` es el archivo exportado de `/DataFrame/import-dataframe-enriquecido.py`. Es el archivo esencial sobre el que se trabajará en los directorios que siguen.

##### /DataFrame/PrePrints

Se incluyen los `content_types`: `journal_articles`, `bibliographic_references`, `conference_and_workshop_papers` y `unpub_reports_and_working_papers`. No se identifican facilmente los servidores PrePrints en OpenDOAR. Se tomo el criterio de búsqueda por la palabra "preprint" en el búscador web y se indentificaron los repositorios existentes con ese criterio. Se puede [reproducir la segmentación aquí](https://v2.sherpa.ac.uk/cgi/search/repository/advanced?screen=Search&repository_name_merge=ALL&repository_name=preprint&repository_org_name_merge=ALL&repository_org_name=&content_types_merge=ANY&content_subjects_merge=ANY&org_country_browse_merge=ALL&org_country_browse=&satisfyall=ALL&order=preferred_name&_action_search=Search). En base a esto, los 7 resultados de la búsqueda por nombre tienen como `content_types` los seleccionados aquí. 

- `/DataFrame/PrePrints/tabla-lat-esp-preprints.py` crea una tabla que filtra `/DataFrame/dataframe-enriquecido.csv` por países de Latinoamérica más España y los ordena acorde a la cantidad de repositorios registrados en Sherpa, de mayor a menor. Adicionalmente, se mapea todos los identificadores de los países para colocar una etiqueta legible a cada una. Se incluyen solo los que tengan al menos una coinicidencia con `content_types`: `journal_articles`, `bibliographic_references`, `conference_and_workshop_papers` o `unpub_reports_and_working_papers`.
- `/DataFrame/PrePrints/tabla-lat-esp-preprints.html` es el archivo exportado de `/DataFrame/PrePrints/tabla-lat-esp-preprints.py`.
- `/DataFrame/PrePrints/top5-lat-esp-preprints.py` crea la tabla que filtra países de Latinoamérica más España en `/DataFrame/dataframe-enriquecido.csv` y filtra los 5 repositorios con mayor número de contenido depositado en cada país según el valor en `metadata_record_count`. A su vez, el valor arrojado se ordena de mayor a menor y en orden de países según se muestra en `/DataFrame/PrePrints/tabla-lat-esp-preprints.html` y se mantiene el filtro de `content_types` específico para PrePrints.
- `/DataFrame/PrePrints/top5-lat-esp-preprints.html` es el archivo exportado de `/DataFrame/PrePrints/top5-lat-esp-preprints.py`.


##### /DataFrame/DataSets

Se incluyen los `content_types`: `datasets` y `theses_and_dissertations`. La identificación de esta tipología es más clara en OpenDOAR que para PrePrints.

- `/DataFrame/DataSets/tabla-lat-esp-datasets.py` crea una tabla que filtra `/DataFrame/dataframe-enriquecido.csv` por países de Latinoamérica más España y los ordena acorde a la cantidad de repositorios registrados en Sherpa, de mayor a menor. Adicionalmente, se mapea todos los identificadores de los países para colocar una etiqueta legible a cada una. Se incluyen solo los que tengan al menos una coinicidencia con `content_types`: `datasets` o `theses_and_dissertations`.
- `/DataFrame/DataSets/tabla-lat-esp-datasets.html` es el archivo exportado de `/DataFrame/DataSets/tabla-lat-esp-datasets.py`.
- `/DataFrame/DataSets/top5-lat-esp-datasets.py` crea la tabla que filtra países de Latinoamérica más España en `/DataFrame/dataframe-enriquecido.csv` y filtra los 5 repositorios con mayor número de contenido depositado en cada país según el valor en `metadata_record_count`. A su vez, el valor arrojado se ordena de mayor a menor y en orden de países según se muestra en `/DataFrame/DataSets/tabla-lat-esp-datasets.html` y se mantiene el filtro de `content_types` específico para DataSets.
- `/DataFrame/DataSets/top5-lat-esp-datasets.html` es el archivo exportado de `/DataFrame/DataSets/top5-lat-esp-datasets.py`.



