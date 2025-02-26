# README - Programa de Flujo Máximo

## Descripción General
Este programa implementa los algoritmos de Edmonds-Karp y Push-Relabel para calcular el flujo máximo en una red desde un nodo fuente (0) hasta un nodo destino (N-1). El programa recibe un archivo de entrada que describe la red y muestra los resultados de ambos algoritmos, incluyendo el flujo en cada eje, el flujo total y los tiempos de ejecución.

## Requisitos Previos
- **Python 3.8 o superior**: El programa está desarrollado en Python y requiere una instalación funcional de Python 3.
- **Archivo de entrada válido**: Debe seguir el formato especificado en la sección **Formato del Archivo de Entrada**.

## Estructura del Proyecto
```
.
├── EdmonsKarp/            # Implementación del algoritmo Edmonds-Karp
│   └── __init__.py
├── PushRelabel/           # Implementación del algoritmo Push-Relabel
│   └── __init__.py
├── main.py                # Script principal para ejecutar los algoritmos
├── utils/
│   ├── DirectedWeightedGraph.py  # Clase para representar grafos dirigidos
│   ├── random_network_generator.py  # Generador de redes de prueba
│   └── __init__.py
└── test_data/             # Archivos de prueba de ejemplo
    ├── redOK.txt
    ├── redOK_1000.txt
    ├── redOK_10000.txt
    └── redAntiparalelos.txt
```

## Uso del Programa
1. **Ejecución básica**:
   ```bash
   python main.py <ruta_al_archivo_de_entrada>
   ```
   Ejemplo con datos de prueba:
   ```bash
   python main.py test_data/redOK.txt
   ```

2. **Salida**:
   - El programa imprime en la consola:
     - El flujo en cada eje y el flujo máximo para ambos algoritmos.
     - El tiempo de ejecución de cada algoritmo.
     - Tres archivos con los ejes (origen destino flujo), que indica el flujo que se envia por cada eje, para cada algoritmo
   - Para guardar la salida en un archivo (flujo y tiempo máximo de ejecución), redirija la salida estándar:
     ```bash
     python main.py entrada.txt > salida.txt
     ```

## Formato del Archivo de Entrada
- La primera línea contiene la cantidad de nodos `N`.
- Las siguientes líneas tienen tres números por fila: `nodo_origen`, `nodo_destino`, `capacidad`.
- Ejemplo:
  ```
  4
  0 1 10
  1 2 5
  2 3 8
  ```

## Salida del Programa
- Para cada algoritmo:
  - Lista de ejes en formato `u v flujo`, donde `u` es el nodo origen, `v` el destino, y `flujo` el flujo asignado.
  - Línea final con el flujo máximo total.
- Tiempos de ejecución de cada algoritmo en segundos.

## Generación de Redes de Prueba
El script `utils/random_network_generator.py` genera redes aleatorias válidas. Para usarlo:
```bash
python -m utils.random_network_generator
```
- Parámetros ajustables en el código:
  - Número de nodos (`n`).
  - Nombre del archivo de salida (`archivo_salida`).

## Validación de Antiparalelos
El programa verifica que no existan ejes antiparalelos (ejes en ambas direcciones entre dos nodos). Si se detectan, el programa termina con un mensaje de error.

## Notas Adicionales
- **Nodos fuente y destino**: El nodo fuente siempre es `0` y el destino es `N-1`.
- **Eficiencia**: El algoritmo Push-Relabel suele ser más eficiente en grafos densos. Considerando que la complejidad de Edmonds-Karp es O(V·E²) y la de Push-Relabel es O(V²·E), en un grafo denso donde E ≈ V², la complejidad de Edmonds-Karp se aproxima a O(V⁵), siendo mayor que la de Push-Relabel. Por lo tanto, en estos casos, Push-Relabel podría representar una mejor opción computacional.
- **Compatibilidad**: El programa funciona en cualquier sistema operativo con Python 3 instalado.