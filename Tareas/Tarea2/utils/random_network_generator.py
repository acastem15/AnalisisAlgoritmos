import random

def generar_red_flujo(n, archivo_salida="redOK_10000.txt"):
    aristas = set()
    existentes = set()  
    
    # Nodo 0 solo puede enviar flujo
    for v in range(1, min(n, 101)):
        capacidad = random.randint(900, 1000)
        aristas.add((0, v, capacidad))
        existentes.add((0, v))
    
    # Nodo n-1 solo puede recibir flujo
    for u in range(max(0, n-101), n-1):
        capacidad = random.randint(900, 1000)
        aristas.add((u, n-1, capacidad))
        existentes.add((u, n-1))

    
    while len(aristas) < 30000:
        u, v = random.sample(range(1, n-1), 2)  # Evitar nodo 0 y n-1
        if (u, v) not in existentes and (v, u) not in existentes:  # Evitar antiparalelos
            capacidad = random.randint(1, 1000)
            aristas.add((u, v, capacidad))
            existentes.add((u, v))
    
    '''
    while len(aristas) < n + 300:
        u, v = random.sample(range(1, n-1), 2)  # Evitar nodo 0 y n-1
        capacidad = random.randint(1, 1000)
        aristas.add((u, v, capacidad))
        existentes.add((u, v))
    '''
    aristas_ordenadas = sorted(aristas, key=lambda x: x[0])

    with open(archivo_salida, "w") as f:
        f.write(f"{n}\n")  
        for u, v, capacidad in aristas_ordenadas:
            f.write(f"{u} {v} {capacidad}\n")
    

    print(f"Red de flujo generada en {archivo_salida}")

generar_red_flujo(10000)
