import random
from collections import deque
import numpy as np


def graphGenerator(n, archivo_salida):

    maxEdgesPlanar = 3*n-6 
    edges = set()
    existentes = set()  
    #print(maxEdgesPlanar)

    graph = {}
    for v in range(0, n):
        graph[v] = []
    
    #2024yr4
    realEdges = 0
    f = open(archivo_salida,"w")
    for v in range(0, n):

        amountEdges = random.randint(1,maxEdgesPlanar//(n)) 
           
        edgesV = len(graph[v])
        #print(edgesV,amountEdges)
        while edgesV < amountEdges:
            randVertex = random.randint(0,n-1)
            if randVertex != v and (randVertex not in graph[v]) and (v not in graph[randVertex]): 
                graph[v].append(randVertex)
                graph[randVertex].append(v)
                edge = str(v)+","+str(randVertex)+"\n"
                f.write(edge)
                realEdges+=1
            edgesV=len(graph[v])
    #Connect disconnected         
    numDisconnected, colors  = findDisconnected(graph)
    #print(colors)
    conectingEdges = connectComponents(numDisconnected,colors,graph)
    #print(conectingEdges)

    for e in conectingEdges: 
        v1 = e[0]
        v2 = e[1]
        edge = str(v1)+","+str(v2)+"\n"
        graph[v1].append(v2)
        graph[v2].append(v1)
        f.write(edge)



    #print(realEdges)
    #Code to build graph with exactly 3*V-6
    #print(realEdges)
    """
    while realEdges<maxEdgesPlanar: 
        randVertex = random.randint(0,n-1)
        randVertex2 = random.randint(0,n-1)
        if randVertex2 != randVertex and (randVertex not in graph[randVertex2])and (randVertex2 not in graph[randVertex]): 
                graph[randVertex2].append(randVertex)
                graph[randVertex].append(randVertex2)
                edge = str(randVertex)+","+str(randVertex2)+"\n"
                f.write(edge)
                realEdges+=1
    print(realEdges)
    """



    #print(realEdges)
    f.close()

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

def connectComponents(numDisconnected,colors,graph): 
    i = 0
    neededEdges = []
    #print("Num components",numDisconnected)
    if numDisconnected>1:
        while i <numDisconnected: 
            colorsi = [k for k, v in colors.items() if v == i]#+1 because colors start in 1
            #print(colorsi)

            if i == numDisconnected-1: 
                colorsNext = [k for k, v in colors.items() if v == 0]
            else: 
                colorsNext = [k for k, v in colors.items() if v == i+1]

            #print(colorsNext)
            #print("--------------")
            #Select ranodm from different components
            randomColor1 = colorsi[random.randint(0, len(colorsi)-1)]
            randomColorNext = colorsNext[random.randint(0, len(colorsNext)-1)]
            neededEdges.append((randomColor1,randomColorNext))
            i+=2
        return neededEdges
    else: 
        return []




    
    


numEdges = 20
archivoSalida = "./noComplete/graph_"+str(numEdges)+".csv"
graphGenerator(numEdges, archivoSalida)
