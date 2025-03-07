from utils.DirectedWeightedGraph import DirectedWeightedGraph
import time

class EdmonsKarpGraph(DirectedWeightedGraph):
    
    def __init__(self):
        DirectedWeightedGraph.__init__(self)
        
    def edmonsKarp_algorithm (self, fuente, destino, imprimir_resultados=True):
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
            
        if imprimir_resultados: 
            f = open("EdmondsKarpGraph.txt", "w")
            f.write('Edmonds-Karp\n')   
            for u in self.grafo:
                for v, datos in self.grafo[u].items():
                    if datos["original"]:
                        f.write(str(u)+" "+str(v)+" "+str(datos["flujo"])+"\n")
            f.close()
            #print("\nFlujo Máximo: "+str(maxFlow))
        
        return maxFlow
        
        
        
    def llenar_grafo_edmonsKarp(self, ruta_entrada, imprimir_resultados=False):
        '''Llena la matriz de adyacencia a partir del archivo de entrada'''

        with open(ruta_entrada) as archivo:
            lineas = archivo.readlines()
        
        destino =  int(lineas[0].strip()) - 1
        fuente = 0
        
        for linea in lineas[1:]:
            u,v,capacidad = map(int, linea.split())
            self.addEdge(u,v,capacidad)

        #print(self.grafo)
        inicio_ek = time.time()
        max_flow = self.edmonsKarp_algorithm(fuente, destino, imprimir_resultados=imprimir_resultados)
        fin_ek = time.time()
        return max_flow,fin_ek - inicio_ek