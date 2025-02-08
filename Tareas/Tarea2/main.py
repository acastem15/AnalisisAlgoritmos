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
    max_flow_ek = grafo.llenar_grafo_edmonsKarp(ruta_entrada=entrada, imprimir_resultados=False)  
    fin_ek = time.time()    
    
    inicio_pr = time.time()
    grafo = PushRelabelGraph()
    max_flow_pr = grafo.llenar_grafo_pushrelabel(ruta_entrada=entrada, imprimir_resultados=False)
    fin_pr = time.time()
    
    print("\n----------- Edmons-Karp -----------")
    print(f"Flujo máximo: {max_flow_ek}")
    print(f"Tiempo de ejecución: {fin_ek - inicio_ek:.6f} segundos")
    
    print("\n----------- Push-Relabel -----------")
    print(f"Flujo máximo: {max_flow_pr}")
    print(f"Tiempo de ejecución: {fin_pr - inicio_pr:.6f} segundos")