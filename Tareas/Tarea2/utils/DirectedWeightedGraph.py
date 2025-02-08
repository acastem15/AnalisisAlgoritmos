from collections import defaultdict, deque
import sys

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


def cantorPairing(u,v):
    return (u+v)*(u+v+1) // 2 + v