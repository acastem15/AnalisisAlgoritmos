import sys
import time
from collections import deque, defaultdict

class DirectedWeightedGraph:
    def __init__(self):
        self.grafo = defaultdict(dict)

    def addEdge (self, u, v, capacidad):
        '''Añade el eje de u a v'''
        
        
        if (v in self.grafo and u in self.grafo[v]) or (u in self.grafo and v in self.grafo[u]):
            print ("ERROR: Hay más de un eje entre dos nodos de la red")
            sys.exit(1)
        
        '''
        if v in self.grafo and u in self.grafo[v]: #verifica si existe el eje en sentido contrario y crea nodo auxiliar
            w = cantorPairing(u,v) * -1
            self.grafo[u][w] = {"capacidad": capacidad, "flujo": 0, "original": True}
            self.grafo[w][v] = {"capacidad": capacidad, "flujo": 0, "original": True}
        else: 
            self.grafo[u][v] = {"capacidad": capacidad, "flujo": 0, "original": True}
        '''
        self.grafo[u][v] = {"capacidad": capacidad, "flujo": 0, "original": True}
        
        if v not in self.grafo:
            self.grafo[v] = {}
       
        if u not in self.grafo[v]:
            self.grafo[v][u] = {"capacidad": 0, "flujo": 0, "original": False}
       
            

    def augmentPath(self, fuente, destino, precede):
      
        visitados = set() #crear el set de visitados
        
        cola = deque([fuente])  # meto fuente a la cola; deque significa Double-Ended Queue, no confudir con desencolar
        
        visitados.add(fuente) #marco la fuente como visitado

        while cola:
            u = cola.popleft() #saco el primero de la cola
            for v, datos in self.grafo[u].items():
                if (v not in visitados) and (datos["capacidad"] > 0): #recorro cada adyacente y confirmo si se puede recorrer
                    cola.append(v) #lo agrego a la cola
                    visitados.add(v) #lo marco como visitado
                    precede[v] = u #marco que llegué desde u
                    if v == destino:
                        return True #llegué al destino!
        
        return False #no llegué al destino desde la fuente, ya no hay camino aumentante

    def edmonsKarp (self, fuente, destino):
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

def cantorPairing(u,v):
    return (u+v)*(u+v+1) // 2 + v

def llenarGrafo(entrada):
    '''Llena la matriz de adyacencia a partir del archivo de entrada'''

    with open(entrada) as archivo:
        lineas = archivo.readlines()
    
    destino =  int(lineas[0].strip()) - 1
    fuente = 0
    grafo = DirectedWeightedGraph()

    for linea in lineas[1:]:
        u,v,capacidad = map(int, linea.split())
        grafo.addEdge(u,v,capacidad)

    grafo.edmonsKarp(fuente, destino)

if __name__ == "__main__":
    inicio = time.time()
    if len(sys.argv) != 2:
        print ("Usage: python EdmonsKarp.py <entrada.txt>")
        sys.exit(1)

    entrada = sys.argv[1]
    llenarGrafo(entrada)  
    fin = time.time()

    print(f"\nTiempo de ejecución: {fin - inicio:.6f} segundos")