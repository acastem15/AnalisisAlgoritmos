import math
import sys
def generate_planar_graph(n):
    """
    Genera un grafo planar con n vértices mediante una generación modular de subciclos conectados.

    La construcción se realiza en tres pasos:

    1. Cálculo de x y del remanente:
       Se determina el mayor entero x que satisface:
           x*(x+1)/2 <= n
       utilizando la fórmula analítica:
           x = floor((sqrt(1+8*n) - 1)/2)
       Además se calcula el remanente:
           rem = n - x*(x+1)//2

    2. Definición de subgrafos (subciclos):
       - Si rem > 0 se generan (x+1) subgrafos; de lo contrario, se generan x subgrafos.
       - Los tamaños de los subgrafos se establecen como:
             [x, x-1, x-2, ..., 1] y se incluye rem (si rem > 0)
       - Se ordenan en forma descendente para que el subgrafo de mayor tamaño (el ciclo principal)
         sea el primero.

    3. Conexión de subgrafos:
       Cada subgrafo se une como "apéndice" al inmediato mayor, según las siguientes reglas:
         - Si el subgrafo (apéndice) tiene más de 2 vértices, se forma un ciclo cerrado y se
           conecta a través de dos pares de vértices.
         - Si tiene 2 o menos vértices, se conecta mediante un único eje.
       
    La función devuelve una lista de ejes, donde cada eje es una lista [u, v].
    """
    
    # --- Paso 1: Cálculo de x y del remanente ---
    # Se calcula el valor máximo de x que cumple x*(x+1)/2 <= n utilizando la fórmula analítica.
    x = int(math.floor((math.sqrt(1 + 8*n) - 1) / 2))
    # st es la suma de los primeros x enteros.
    st = x * (x + 1) // 2
    # rem es el remanente de vértices que no se usan en la suma.
    rem = n - st
    
    # --- Paso 2: Definición de subgrafos (subciclos) ---
    # Genera la lista de tamaños para los apéndices: de 1 a x-1.
    appendixes_size = list(range(1, x))
    
    # Si existe remanente (rem > 0), se incluye junto con x; si no, se toma solo x.
    base_sizes = [x, rem] if rem > 0 else [x]
    
    # Se combinan los tamaños base y los de los apéndices, y se ordenan de mayor a menor.
    graph_config = sorted(base_sizes + appendixes_size, reverse=True)

    # Inicializa una lista para almacenar los subciclos (cada uno representado por sus ejes).
    sub_graphs_cycles = [0] * len(graph_config)

    # 'c' es un contador del vértice actual para asignar índices de forma consecutiva.
    c = 1
    # Para cada subgrafo, se generan sus ejes.
    for i, size in enumerate(graph_config):
        sub_graphs_cycles[i] = (
            [[c + j, c + j + 1] for j in range(size - 1)] + [[c + size - 1, c]]
            if size > 2
            else [[c, c + size - 1]]
        )
        # Actualiza el contador de vértices para el siguiente subgrafo.
        c += size
      
    # --- Paso 3: Conexión de subgrafos ---
    # Se conectan los subgrafos consecutivos para formar el grafo planar.
    connections = []
    # Itera sobre cada par consecutivo de subgrafos.
    for i in range(len(sub_graphs_cycles) - 1):
        cycle = sub_graphs_cycles[i]         # Subgrafo actual
        next_cycle = sub_graphs_cycles[i + 1]  # Siguiente subgrafo
        # Se conecta con el siguiente grafo según la regla establecida
        if len(next_cycle) > 2:
            connections.append([cycle[-1][0], next_cycle[-1][0]])
            connections.append([cycle[-1][1], next_cycle[-1][1]])
        else:
            connections.append([cycle[-1][0], next_cycle[0][0]])
        
    # Combina los ejes en una sola lista.
    final_graph = []
    for cycle in sub_graphs_cycles:
        final_graph += cycle
    final_graph += connections

    # Elimina ejes que sean auto-conexiones.
    final_graph = [edge for edge in final_graph if edge[0] != edge[1]]
    
    return final_graph

# Generar grafos planares
if __name__ == '__main__':
    n = int(sys.argv[1])
    graph = generate_planar_graph(n)
   
    
    with open('./results/graph'+str(n)+'.csv', 'w') as f:
        for edge in graph:
            f.write(f'{edge[0]},{edge[1]}\n')
   