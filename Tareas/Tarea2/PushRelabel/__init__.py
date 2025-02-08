from utils.DirectedWeightedGraph import DirectedWeightedGraph


def push_relabel(graph, source, sink):
    n = len(graph)
    height = [0] * n       # Altura (etiqueta) de cada nodo
    excess = [0] * n       # Exceso de flujo en cada nodo

    height[source] = n
    # Inicialización del preflujo: se empuja todo lo posible desde la fuente.
    for edge in graph[source]:
        edge.flow = edge.capacity
        graph[edge.v][edge.rev].flow = -edge.flow
        excess[edge.v] += edge.flow
        excess[source] -= edge.flow

    # Cola de nodos activos (con exceso > 0, excepto fuente y sumidero)
    active = deque([i for i in range(n) if i != source and i != sink and excess[i] > 0])

    def push(u, edge):
        v = edge.v
        # Cantidad que se puede empujar
        send = min(excess[u], edge.capacity - edge.flow)
        if height[u] > height[v] and send > 0:
            edge.flow += send
            graph[v][edge.rev].flow -= send
            excess[u] -= send
            excess[v] += send
            # Si el nodo v se vuelve activo y no es fuente ni sumidero, se añade a la cola.
            if v != source and v != sink and excess[v] == send:
                active.append(v)
            return True
        return False

    def relabel(u):
        # Se busca la mínima altura de los vecinos con capacidad residual positiva.
        min_height = float('inf')
        for edge in graph[u]:
            if edge.capacity - edge.flow > 0:
                min_height = min(min_height, height[edge.v])
        if min_height < float('inf'):
            height[u] = min_height + 1

    while active:
        u = active.popleft()
        pushed = False
        # Se intenta empujar flujo a través de todas las aristas salientes de u.
        for edge in graph[u]:
            if push(u, edge):
                pushed = True
                if excess[u] == 0:
                    break
        # Si u sigue con exceso, se realiza un "relabel" y se vuelve a poner en la cola.
        if excess[u] > 0:
            relabel(u)
            active.append(u)
    # El flujo máximo es el exceso acumulado en el sumidero.
    return excess[sink]


class PushRelabelGraph(DirectedWeightedGraph):
    
    def __init__(self):
        DirectedWeightedGraph.__init__(self)
        
    def pushrelabel_algorithm (self, fuente, destino):
        maxFlow = 0 # inicializo flujo máximo en 0
        precede = {} # guarda camino en 0

        while self.augmentPath(fuente, destino, precede):
            flujoCamino = float('Inf') #inicio flujo del camino encontrado por el BFS en infinito
        
            v = destino #empiezo desde el destino
            while v != fuente: #si aún no estoy en la fuente, miro cuánto es el flujo mínimo por el camino
                u = precede[v]
                flujoDisponible = self.grafo[u][v]["capacidad"] 
                flujoCamino = min(flujoCamino, flujoDisponible)
                v = u 

            v = destino           
            while v != fuente: #ahora recorro otra vez el camino hacia atrás actualizando las capacidades de cada eje y el flujo del eje para adelante
                u = precede[v]

                self.grafo[u][v]["flujo"] += flujoCamino
                self.grafo[u][v]["capacidad"] -= flujoCamino

                self.grafo[v][u]["capacidad"] += flujoCamino
                v = u

            maxFlow  += flujoCamino #sumo el flujo del camino aumentante al máximo

        for u in self.grafo:
            for v, datos in self.grafo[u].items():
                if "original" in datos and datos["original"]:
                    print(str(u)+" "+str(v)+" "+str(datos["flujo"]))
        print("\nFlujo Máximo: "+str(maxFlow))
        
        
        
    def llenar_grafo_pushrelabel(self, ruta_entrada):
        '''Llena la matriz de adyacencia a partir del archivo de entrada'''

        with open(ruta_entrada) as archivo:
            lineas = archivo.readlines()
        
        destino =  int(lineas[0].strip()) - 1
        fuente = 0

        for linea in lineas[1:]:
            u,v,capacidad = map(int, linea.split())
            self.addEdge(u,v,capacidad)

        self.pushrelabel_algorithm(fuente, destino)