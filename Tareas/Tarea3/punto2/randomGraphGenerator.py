import random
from collections import deque
import numpy as np
import networkx as nx
import sys


def graphGenerator(n, numEdgesMax,fixEdges, archivo_salida,escribir):

    maxEdgesPlanar = numEdgesMax
    #print(maxEdgesPlanar)

    graph = {}
    for v in range(0, n):
        graph[v] = []
    
    realEdges = 0
    if escribir:
        f = open(archivo_salida,"w")
        f.write("source,target\n")
    for v in range(0, n):
        if fixEdges ==False: 
            amountEdges = random.randint(1,maxEdgesPlanar//(n)) 
        else: 
            amountEdges = maxEdgesPlanar//(n)
           
        edgesV = len(graph[v])
        #print(edgesV,amountEdges)
        while edgesV < amountEdges:
            randVertex = random.randint(0,n-1)
            if randVertex != v and (randVertex not in graph[v]) and (v not in graph[randVertex]): 
                graph[v].append(randVertex)
                graph[randVertex].append(v)
                edge = str(v)+","+str(randVertex)+"\n"
                if escribir:
                    f.write(edge)
                realEdges+=1
            edgesV=len(graph[v])

    #print("actual edges",realEdges)

    #Connect disconnected         
    numDisconnected, colors  = findDisconnected(graph)
    #print(colors)
    conectingEdges = connectComponents(numDisconnected,colors)

    
    #print(conectingEdges)

    for e in conectingEdges: 
        v1 = e[0]
        v2 = e[1]
        edge = str(v1)+","+str(v2)+"\n"
        graph[v1].append(v2)
        graph[v2].append(v1)
        if escribir:
            f.write(edge)
        realEdges+=1
    isConnected=True
    if findDisconnected(graph)[0]>1 : isConnected=False    

    if fixEdges==True: 
    
        while realEdges<maxEdgesPlanar: 
            randVertex = random.randint(0,n-1)
            randVertex2 = random.randint(0,n-1)
            if randVertex2 != randVertex and (randVertex not in graph[randVertex2])and (randVertex2 not in graph[randVertex]): 
                    graph[randVertex2].append(randVertex)
                    graph[randVertex].append(randVertex2)
                    edge = str(randVertex)+","+str(randVertex2)+"\n"
                    if escribir:
                        f.write(edge)
                    realEdges+=1
        #print(realEdges)
    #print(realEdges)
    if escribir:
        f.close()
    return graph
    

def findDisconnected(graph):
    visited = deque()
    colors= {}
    actualColor =0; 
    for v in graph.keys(): 
        if v not in visited: #New component
            getIn(visited, colors,actualColor, v, graph)
            actualColor+=1; 
    return actualColor, colors


def getIn(visited, colors,actualColor,  v, graph): 
    visited.append(v)
    colors[v] = actualColor

    for adjVer in graph[v]: 
        if adjVer not in visited: 
            getIn(visited,colors,actualColor,adjVer,graph)

def connectComponents(numDisconnected,colors): 
    #print(colors)
    i = 0
    neededEdges = []
    #print("Num components",numDisconnected)
    if numDisconnected>1:
        while i <numDisconnected-1: 
            colorsi = [k for k, v in colors.items() if v == i+1]#+1 because colors start in 1
            #print(colorsi)
            #Se conecta al primero 
            colorsNext = [k for k, v in colors.items() if v == 0]
       

            #print(colorsNext)
            #print("--------------")
            #Select ranodm from different components
            randomColor1 = colorsi[random.randint(0, len(colorsi)-1)]
            randomColorNext = colorsNext[random.randint(0, len(colorsNext)-1)]
            neededEdges.append((randomColor1,randomColorNext))
            i+=1
        #print(neededEdges,len(neededEdges))
        return neededEdges
    else: 
        return []



def validationPlanar(graph): 
    nxGraph=nx.Graph()
    for n,adj in graph.items(): 

        for adjVertex in adj:
            nxGraph.add_edge(n,adjVertex)

    return nx.is_planar(nxGraph)
    #print(nxGraph.number_of_nodes(), nxGraph.number_of_edges())

    
    
def generateMultipleGraphs_withResultsPlanar(numIt,numVertex,maxEdges,step,archivo,fixedEdges, writeGraphs,writePr):
    if writePr: 
        f = open(archivo,"w")

        header = "numEdges,"

        for i in range(0,numIt): 
        
            header+="it"+str(i)+","
        header+="PrPlanar"+"\n"
        f.write(header)
        
    for numEdges in range (numVertex-1,maxEdges+1,step):
        countTrue = 0 
        lineResults = str(numEdges)+","
        for i in range ( 0,numIt): 

            print("vertex: {0}, edges: {1}, iteration: {2}".format(numVertex,numEdges,i))

        
            archivoSalida = "./results/punto2_grafos/graph_vert"+str(numVertex)+"_edg"+str(numEdges)+"_"+str(i)+".csv"
            graph = graphGenerator(numVertex,numEdges,fixedEdges, archivoSalida,writeGraphs)
            isPlanar = validationPlanar(graph)
            if isPlanar: 
                countTrue+=1
            
            lineResults+=str(isPlanar)+","
            print("..................planar: {0}".format(isPlanar))


        pr = countTrue/numIt
        lineResults+=str(round(pr,3))+"\n"
        if writePr:
            f.write(lineResults)
    if writePr:
        f.close()


archivo = "./results/punto2_grafos/planarityResults_it"+str(sys.argv[1])+".csv"
generateMultipleGraphs_withResultsPlanar(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),archivo,bool(sys.argv[5]),bool(sys.argv[6]), bool(sys.argv[7]))