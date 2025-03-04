import random
import time
import string
from suffixArray import suffixList_v1, sufPosition
from search import search_v2, search_v1
from traceback import print_exc

def run_experiments(version='v2'):
    """
    Realiza pruebas con textos sintéticos de diferentes tamaños y número de consultas.
    Imprime una tabla con los tiempos de ejecución.
    """
    # Definir tamaños de texto y cantidad de consultas
    text_sizes = [100_000,1_000_000,10_000_000 ]  # Se pueden agregar otros tamaños: 1_000_000, 10_000_000, etc.
    query_counts = [1_000, ]   # Se pueden agregar otros conteos: 10_000, 100_000, 1_000_000, etc.
    
    print("\nEjecutando experimentos de rendimiento:")
    print("=" * 80)
    print(f"{'Tamaño texto':<15} {'Num consultas':<15} {'Tiempo SA (s)':<15} {'Tiempo consultas (s)':<20} {'Tiempo total (s)':<15}")
    print("-" * 80)
    
    for text_size in text_sizes:
        # Generar texto aleatorio (letras minúsculas y espacios)
        print(f"Generando texto aleatorio de {text_size} caracteres...")
        text = ''.join(random.choices(string.ascii_lowercase + ' ', k=text_size))
        
        # Construir el arreglo de sufijos o la lista de posiciones según la versión
        t0 = time.perf_counter()
        base_array = suffixList_v1(text)
        if version == 'v2':
            suffix_array = sufPosition(base_array)
            del base_array
        else:
            suffix_array = base_array
        t1 = time.perf_counter()
        sa_time = t1 - t0
        
        for qc in query_counts:
            # Generar consultas aleatorias (subcadenas del texto)
            print(f"Generando {qc} consultas aleatorias...")
            queries = []
            for _ in range(qc):
                query_len = random.randint(1, 10)
                start_index = random.randint(0, text_size - query_len - 1)
                query = text[start_index:start_index + query_len]
                queries.append(query)
            
            # Medir tiempo de procesamiento de consultas
            t0_query = time.perf_counter()
            c = 0
            for query in queries:
                try:
                    if version == 'v2':
                        _ = search_v2(text, suffix_array, query, [])
                    else:
                        _ = search_v1(text, suffix_array, query, [])
                except:
                    print_exc()
                    with open(f"./results/error_{version}.txt", "w") as f:
                        f.write("text: "+text)
                        f.write("\nquery: "+query)
                        print(f"Error en consulta {c}: {query}")
                    break
                finally:
                    c += 1
            t1_query = time.perf_counter()
            query_time = t1_query - t0_query
            
            total_time = sa_time + query_time
            print(f"{text_size:<15} {qc:<15} {sa_time:<15.3f} {query_time:<20.3f} {total_time:<15.3f}")
    
    print("=" * 80)
