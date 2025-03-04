# Suffix Array CLI y Experimentos

Este repositorio implementa un sistema de búsqueda sobre un texto utilizando arreglos de sufijos, así como un módulo para realizar experimentos de rendimiento. Se han implementado dos versiones del algoritmo de búsqueda:

- **v1:** Utiliza un arreglo de sufijos clásico (sin optimización de espacio).
- **v2:** Utiliza una versión optimizada que construye un diccionario ordenado (lista de posiciones) para reducir el consumo de memoria.

## Estructura del Repositorio

```
.
├── data
│   ├── consulta.txt      # Archivo con las consultas (una por línea)
│   └── texto.txt         # Archivo de texto a procesar
├── experiments.py        # Script para ejecutar experimentos de rendimiento
├── main.py               # Script principal con el CLI (subcomandos: search, experiments)
├── README.md             # Este archivo de documentación
├── results
│   ├── error_v1.txt      # Archivo de salida de errores para la versión v1
│   └── error_v2.txt      # Archivo de salida de errores para la versión v2
├── search.py             # Funciones de búsqueda (search_v1, search_v2) y sus auxiliares
├── suffixArray.py        # Funciones para construir el arreglo de sufijos y obtener posiciones
└── suffix.py             # Clase Suffix, que encapsula cada sufijo (texto y posición)
```

## Descripción de la Implementación

- **suffix.py:**  
  Define la clase `Suffix`, que almacena el sufijo extraído del texto y su posición. Se implementa la comparación para permitir ordenar una lista de objetos `Suffix`.

- **suffixArray.py:**  
  Contiene la función `suffixList_v1`, que genera el arreglo de sufijos a partir del texto. Además, se incluye la función `sufPosition` que, a partir de la lista de sufijos, construye un diccionario ordenado que mapea la posición del sufijo a la longitud del mismo (usado en la versión optimizada v2).

- **search.py:**  
  Implementa dos funciones de búsqueda:
  - `search_v1`: Realiza la búsqueda utilizando el arreglo de sufijos tradicional.
  - `search_v2`: Realiza la búsqueda utilizando el diccionario de posiciones generado para la versión optimizada.
  
  Cada función incluye métodos auxiliares para extender la búsqueda hacia la izquierda y la derecha una vez encontrado un primer match.

- **main.py:**  
  Es el punto de entrada del CLI y utiliza subcomandos para ejecutar en modo de búsqueda o experimentos:
  - **Modo `search`:** Permite procesar un archivo de texto, un archivo de consultas y generar un archivo de resultados. Se elige la versión (`v1` o `v2`) mediante el parámetro correspondiente.
  - **Modo `experiments`:** Ejecuta pruebas de rendimiento con textos y consultas sintéticas, midiendo los tiempos de construcción del arreglo de sufijos y la búsqueda de consultas.

- **experiments.py:**  
  Contiene la función `run_experiments` que genera textos y consultas aleatorias para evaluar el rendimiento de las versiones `v1` y `v2`.

## Uso del CLI

El script principal se ejecuta a través de `main.py` y utiliza subcomandos para diferenciar los modos de ejecución.

### Ejecución en modo búsqueda

Utiliza el subcomando `search` para procesar un texto y un archivo de consultas. Por ejemplo:

```bash
python main.py search -f data/texto.txt -v v2 -c data/consulta.txt -r results/resultados.txt
```

**Parámetros:**

- `-f` o `--file`: Ruta del archivo de texto.
- `-v` o `--version`: Versión del algoritmo (`v1` o `v2`).
- `-c` o `--consultas`: Archivo con las consultas (una por línea).
- `-r` o `--result`: Ruta del archivo donde se guardarán los resultados.

### Ejecución en modo experimentos

Utiliza el subcomando `experiments` para ejecutar pruebas de rendimiento. Por ejemplo:

```bash
python main.py experiments -v v1
```

**Parámetros:**

- `-v` o `--version`: Versión del algoritmo a probar (`v1` o `v2`).

## Notas Adicionales

- Los archivos de datos se encuentran en el directorio `data` y los resultados (por ejemplo, errores o salidas) se guardan en el directorio `results`.
- Puedes modificar los tamaños de texto y la cantidad de consultas en `experiments.py` para ajustar la intensidad de las pruebas de rendimiento.
- La estructura del código permite agregar nuevas optimizaciones o modos de búsqueda sin afectar la interfaz de línea de comandos.
