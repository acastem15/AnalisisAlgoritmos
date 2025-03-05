import sys
import argparse
import suffixArray as sa
from search import search_v1, search_v2
from experiments import run_experiments

def main():
    parser = argparse.ArgumentParser(description="Suffix array")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Modo de ejecución')

    # Subcomando para búsqueda:
    search_parser = subparsers.add_parser('search', help='Ejecutar búsqueda de consultas en el texto')
    search_parser.add_argument('-f', '--file', required=True, help='Ruta del texto')
    search_parser.add_argument('-v', '--version', required=True, choices=['v1', 'v2'],
                               help='Versión del arreglo de sufijos. v1 sin optimización, v2 con optimización')
    search_parser.add_argument('-c', '--consultas', required=True, help='Archivo con consultas (una por línea)')
    search_parser.add_argument('-r', '--result', required=True, help='Ruta del archivo de salida')

    # Subcomando para experimentos:
    experiments_parser = subparsers.add_parser('experiments', help='Ejecutar experimentos de rendimiento')
    experiments_parser.add_argument('-v', '--version', required=True, choices=['v1', 'v2'],
                                    help='Versión del arreglo de sufijos.')

    args = parser.parse_args()

    if args.command == 'search':
        # Leer el texto
        with open(args.file, "r") as f:
            text = f.read().replace('\n', '')
        print(text)

        # Construir el arreglo de sufijos según la versión elegida
        if args.version == "v1":
            sufList = sa.suffixList_v1(text)
            posList = sa.sufPosition(sufList)
        elif args.version == "v2":
            posList = sa.suffixList_v2(text)
            #posList = sa.sufPosition(sufList)
            #del sufList

        # Leer las consultas
        with open(args.consultas, "r") as f:
            consultas = f.readlines()

        with open(args.result, "w") as result:
            if args.version == "v1":
                for c in consultas:
                    c = c.strip()
                    matches = " ".join(search_v1(text, sufList, c, []))
                    print(c, search_v1(text, sufList, c, []))
                    result.write(f"{c} {matches}\n")
            elif args.version == "v2":
                for c in consultas:
                    c = c.strip()
                    matches = " ".join(search_v2(text, posList, c, []))
                    print(c, search_v2(text, posList, c, []))
                    result.write(f"{c} {matches}\n")

    elif args.command == 'experiments':
        # Ejecutar experimentos solo requiere la versión
        run_experiments(args.version)

if __name__ == '__main__':
    main()
