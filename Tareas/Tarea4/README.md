
# README - Tarea 4

## Descripción General
Este programa implementa la codificación de Shannon Fano, Huffman; así como la codificación/decodificación de un texto basado en alguna de estas codificaciones. 

## Requisitos Previos
- **Python 3.10 o superior**: El programa está desarrollado en Python y requiere una instalación funcional de Python 3.

## Estructura del Proyecto
```
.
├── huffman/            #implementación de codificación huffman
│   └── __init.py__/     # Contiene codificación Hufman implementado con un heapq
├── shannon_fano/           # Implementación de random graphs
│   └── __init.py__/    #Contiene codificación shannon Fano
├── utils/           # Herramientas
│   └── __init.py__/    #Contiene funciones para codificar, decodificar y calcular stats
├── results/           # Aqui se guardan los resultados tanto el archivo comprimido como la codificación, sp es espacio y \n se guarda como \\n

```

## Uso del Programa
1. **Ejecución básica - main.py**:
    ```bash
    python main.py numIt numVertex maxEdges step fixedEdges writeGraphs writePr
    ```