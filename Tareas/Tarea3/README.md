
# README - Grafos planares

## Descripción General
Este programa implementa dos algoritmos, para el primer punto se realiza un algoritmo que siempre genera grafos planares de conformidad a las reglas explicadas en el pdf adjutno. Para el segundo puntos se crea un programa que genera grafos aleatorios dado un número de ejes, una cantidad de vértices y un número de iteraciones por cada número de ejes, así mismo evalua la planaridad de estos grafos aleatorios haciendo uso de la libreria networkx. 

## Requisitos Previos
- **Python 3.10 o superior**: El programa está desarrollado en Python y requiere una instalación funcional de Python 3.
- **Libreria networkx**: Herramienta utilizada para evaluar la planaridad. Se puede instalar con pip con el siguiente comando: 
```
pip install networkx[default]
```
## Estructura del Proyecto
```
.
├── punto1/            #implementación de planar graphs
│   └── results/     # Resultados a partir del script de python
|   └── planaraGraphGenerator.py # Implementación algoritmo que genera grafos planares
├── punto2/           # Implementación de random graphs
│   └── results/    #Grafos generados con numIt = 5,step = 5 desde 19 a 54 ejes
|   └── randomGraphGenerator.py #Algoritmo de grafos aleatorios ( no necesariamente planares)

```

## Uso del Programa
1. **Ejecución básica - randomGraphGenerator**:
    - numIt (int):Número de grafos que se generar por cada número de eje (cuando fixedEdges es True)
    - numVertex (int):Número de vertices en el grafo (se genera de 0 a numVertex-1)
    - maxEdges (int):Máximo número de ejes permitidos en el grafo
    - step (int): Paso entre número de ejes
    - fixedEdges(bool): Booleano que indica si se desea generar un grafo con número aleatorio de ejes entre 0,maxEdges, o con exactamente maxEdges (True).
    - writeGraphs(bool):Booleano que indica se se desea o no escribir un .csv con los grafos generados
    - writePr (bool): Booleano que indica si se desea o no escribir un .csv con los resultados de planaridad de los grafos generados junto con su probabilidad por eje de ser planar.

   ```bash
   python randomGraphGenerator.py numIt numVertex maxEdges step fixedEdges writeGraphs writePr
   ```
   Ejemplo con datos de prueba:
   ```bash
   python randomGraphGenerator.py 5 20 54 5 True True True
   ```
1. **Ejecución básica - PlanarGraphGenerator**:
    n: Numero de vértices del grafo planar a generar
   ```bash
      python planarGraphGenerator.py n
   ```

2. **Salida**:
   El programa genera archivos .csv con los grafos o con el calculo de las probabilidades según sea el caso. 
     - ```python planarGraphGenerator.py numIt numVertex maxEdges step fixedEdges True writePr``` : Hace todos los archivos .csv de los grafos generados aleatoriamente
     - ```python planarGraphGenerator.py numIt numVertex maxEdges step fixedEdges writeGraphs True```: Hace un archivo.csv con los resultados de is_planar() de la libreria networkx para rodas las iteraciones por número de ejes. 
     - ```python planarGraphGenerator.py n```: Genera archivo .csv con un grafo planar de n vertices. 

## Notas Adicionales
- **Compatibilidad**: El programa funciona en cualquier sistema operativo con Python >=3.10 instalado y networkx. 
