from EdmonsKarp import EdmonsKarpGraph
from PushRelabel import PushRelabelGraph
import sys
import time

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print ("Usage: python main.py <entrada.txt>")
        sys.exit(1)
        
    entrada = sys.argv[1]
    
    inicio_ek = time.time()
    grafo = EdmonsKarpGraph()
    grafo.llenar_grafo_edmonsKarp(ruta_entrada=entrada)  
    fin_ek = time.time()    
    
    inicio_pr = time.time()
    grafo = PushRelabelGraph()
    grafo.llenar_grafo_pushrelabel(ruta_entrada=entrada)
    fin_pr = time.time()
    
    print(f"\nTiempo de ejecución (EdmonsKarp): {fin_ek - inicio_ek:.6f} segundos")
    print(f"\nTiempo de ejecución (PushRelabel): {fin_pr - inicio_pr:.6f} segundos")