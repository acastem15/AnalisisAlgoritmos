import random

def graphGenerator(n, archivo_salida):

    maxEdgesPlanar = 3*n-6 
    edges = set()
    existentes = set()  

    graph = {}
    for v in range(0, n):
        graph[v] = []
    
    #2024yr4
    realEdges = 0
    f = open(archivo_salida,"w")
    for v in range(0, n):

        amountEdges = random.randint(1,maxEdgesPlanar//(n)) 
        realEdges+=amountEdges   
        edgesV = len(graph[v])
        #print(edgesV,amountEdges)
        while edgesV < amountEdges:
            randVertex = random.randint(0,n-1)
            if randVertex != v and (randVertex not in graph[v]): 
                graph[v].append(randVertex)
                graph[randVertex].append(v)
                edge = str(v)+","+str(randVertex)+"\n"
                f.write(edge)
            edgesV=len(graph[v])

    #print(realEdges)
    #Code to build graph with exactly 3*V-6
    """
    while realEdges<maxEdgesPlanar: 
        randVertex = random.randint(0,n-1)
        randVertex2 = random.randint(0,n-1)
        if randVertex2 != randVertex and (randVertex not in graph[randVertex2]): 
                graph[randVertex2].append(randVertex)
                graph[randVertex].append(randVertex2)
                edge = str(randVertex)+","+str(randVertex2)+"\n"
                f.write(edge)
                realEdges+=1
    """



    #print(realEdges)
    f.close()
    

numEdges = 20
archivoSalida = "./noComplete/graph_"+str(numEdges)+".csv"
graphGenerator(numEdges, archivoSalida)
