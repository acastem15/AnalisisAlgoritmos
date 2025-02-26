
from utils.DirectedWeightedGraph import DirectedWeightedGraph
from collections import deque
import time



class RelabelToFrontGraph(DirectedWeightedGraph):
    def __init__(self):

        super().__init__()
        self.N = 0  # Número total de nodos

    def relabelToFront_algorithm(self, fuente, destino, imprimir_resultados):
        n = self.N
        height = [0] * n
        excess = [0] * n
        lista = deque()

        # Inicializamos la altura de la fuente
        height[fuente] = n

        # Pre-flujo: saturamos todas las aristas salientes de la fuente
        for v in list(self.grafo[fuente].keys()):
            capacidad = self.grafo[fuente][v]['capacidad']
            flujo = capacidad

            # Actualizamos la arista directa
            self.grafo[fuente][v]['flujo'] = flujo

            # Actualizamos la arista inversa????
            ##self.grafo[v][fuente]['flujo'] -= flujo

            # Actualizamos los excesos
            excess[fuente] -= flujo
            excess[v] += flujo

            # Si el nodo no es fuente ni destino, lo anadimos a la lista
            if v != fuente and v != destino:
                lista.append(v)

        # Función interna para descargar un nodo u
        def descargar(u):
            while excess[u] > 0:
                # Se recorre la lista de vecinos
                for v in list(self.grafo[u].keys()):
                    edge = self.grafo[u][v]
                    residual = edge['capacidad'] - edge['flujo']
                    if residual > 0 and height[u] == height[v] + 1:
                        delta = min(excess[u], residual)
                        # PUSH
                        edge['flujo'] += delta
                        self.grafo[v][u]['flujo'] -= delta
                        excess[u] -= delta
                        excess[v] += delta

                        """
                        # Si se activa un nodo (tiene exceso) y no es fuente ni destino, se agrega a la cola
                        if v != fuente and v != destino and excess[v] == delta:
                            active.append(v)
                        if excess[u] == 0:
                            break
                        """
                # Si aún queda exceso en u, se hace RELABEL
                if excess[u] > 0:
                    min_height = float('inf')
                    for v in self.grafo[u]:
                        if self.grafo[u][v]['capacidad'] - self.grafo[u][v]['flujo'] > 0:
                            min_height = min(min_height, height[v])
                    if min_height < float('inf'):
                        height[u] = min_height + 1

                    else:
                        break
        #Head para saber desde donde voy a la lista
        head = 0 
        current = 0 
        
        # Bucle principal: procesamos todos los nodos activos
        i=0
        while current < len(lista): 
            v = lista[current]
            i+=1
            """
            print(".....")
            print(i, current)
            print(lista, v)
            print(".....")
            """


            oldHeight = height[current]
            descargar(v)

            if height[current]>oldHeight: 
                lista.remove(v)
                lista.appendleft(v)
                head+=1
                current =head+1
            else: 
                current+=1
            #v = lista[current]
                
        max_flow = excess[destino]

        if imprimir_resultados: 
            f = open("relabelToFrontGraph.txt", "w")
            f.write('Relabel to front\n') 
            for u in self.grafo:
                for v, datos in self.grafo[u].items():
                    if datos["original"]:
                        f.write(str(u)+" "+str(v)+" "+str(datos["flujo"])+"\n")

        return max_flow

    def llenar_grafo_relabeltoFront(self, ruta_entrada, imprimir_resultados):
        with open(ruta_entrada) as archivo:
            lineas = archivo.readlines()

        self.N = int(lineas[0].strip())
        destino =  self.N - 1
        fuente = 0

        for linea in lineas[1:]:
            u, v, capacidad = map(int, linea.split())
            self.addEdge(u, v, capacidad)
        inicio_rf = time.time()
        max_flow = self.relabelToFront_algorithm(fuente, destino, imprimir_resultados=imprimir_resultados)
        fin_rf = time.time()
        return max_flow, fin_rf-inicio_rf