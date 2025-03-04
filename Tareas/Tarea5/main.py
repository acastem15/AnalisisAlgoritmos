import sys
import argparse
import suffixArray as sa

from search import search_v1
from search import search_v2
from experiments import run_experiments

def main():
    parser = argparse.ArgumentParser(description="Suffix array")
    parser.add_argument('-f', '--file', required=True, help='Ruta del texto')
    parser.add_argument('-v', '--version', required=True, choices=['v1', 'v2'], help='Version del arreglo de sufijos. v1 sin optimización de espacio, v2 con optimización')
    parser.add_argument('-c', '--consultas', required=True,help='Archivo con consultas ( una por linea)')
    parser.add_argument('-r', '--result', required=True, help='Ruta del archivo de salida')
    
    args = parser.parse_args()
    

    file_path = args.file
    consultas = args.consultas
    version = args.version
    r = args.result

    #Leer el texto
    f = open(file_path,"r")
 
    text = ""
    for l in f:
        text +=l.replace('\n',"")
    print(text)
    f.close()

    if version=="v1":

        sufList = sa.suffixList_v1(text)#Lista de objetos del tipo sufijo
        posList = sa.sufPosition(sufList)
        textList = sa.sufText(sufList)
        
    elif version=="v2": 
        sufList = sa.suffixList_v1(text)#Lista de objetos del tipo sufijo
        posList = sa.sufPosition(sufList)
        #textList = sa.sufText(sufList)
        del sufList

    #print(textList)
    #Leer las consultas
    consultas = open(consultas,"r")

    result = open(r, "w")


    
    if version=="v1":
        for c in consultas:
            c = c.strip()
            matches =""
            for match in search_v1(text,sufList,c,[]):
                matches+=match+" "
            matches.strip()
            res = f"{c} {matches}\n"
            print(c,search_v1(text,sufList,c,[]))
            result.write(res)
    elif version=="v2":
        for c in consultas:
            c = c.strip()
            matches =""
            for match in search_v2(text,posList,c,[]):
                matches+=match+" "
            matches.strip()
            res = f"{c} {matches}\n"
            print(c,search_v2(text,posList,c,[]))
            result.write(res)
            
            #search_v2(text,sufList,c,[])
        
    result.close()
    consultas.close() 

    print()
    
    
    run_experiments()
    




if __name__ == "__main__":
    main()
