Esta entrega contiene las soluciones para los puntos 3 y 5 de la Tarea 1 del curso Análisis 
de Algoritmos presentada por Ana Castellanos, Raul de la Rosa y Daniel Mahecha.

===== Punto 3 =====
Para este punto se modeló el problema de la fiesta de Juan como un grafo en el que los nodos son los amigos de Juan y la presencia de un eje indica la existencia de un conflicto entre la pareja respectiva de amigos de Juan. Para determinar si es posible organizar 2 reuniones de manera que en ninguna haya amigos de Juan que se hayan peleado entre ellas, se realizó una implementación modificada del algoritmo BFS para determinar si el grafo es bipartito. Si es bipartito, es posible
separar a los amigos en conflicto en dos reuniones, si no es bipartito, no es posible organizar 2 reuniones cumpliendo la condición.

La ENTRADA esperada para el problema es un archivo de texto plano que en la primera línea especifica el número de amigos de Juan. Y en las líneas subsecuentes contiene las parejas en conflicto donde cada amigo de Juan está representado por un entero único separados por un espacio sencillo. 

La SALIDA es true si Juan puede organizar dos reuniones que cumplan la condición y false si no puede hacerlo.

Modo de uso:

java bipartiteGraph < <archivo.txt>

Ejemplos de uso:

java bipartiteGraph < bipartiteGraph.txt

java bipartiteGraph < bipartiteGraph2.txt

===== Punto 5 =====
Se modela el mapa de la ciudad como un grafo no dirigido en el que cada intersección de la ciudad es un nodo y los ejes representan las calles, con el costo de conversión a doble vía. Se implementó el algoritmo de Prim para encontrar el árbol de mínimo recubrimiento y su costo, el cual corresponde al mínimo costo de conectar la ciudad con dobles vías de manera que todos los puntos estén conectados por un camino de dobles vías.

La ENTRADA debe ser un archivo de texto plano de columnas separadas por comas (CSV) donde la primera y la segunda columna son las intersecciones que limitan la calle y la tercera columna es el costo de conversión a doble vía.

La SALIDA muestra las calles incluidas en el árbol de recubrimiento mínimo y su costo, así como el costo mínimo total de convertir las calles a dobles vías de tal manera que se cumpla la condición.

Modo de uso:

java PrimAlgorithm <archivo.csv>

Ejemplo de uso:

java PrimAlgorithm calles_conexas.csv
