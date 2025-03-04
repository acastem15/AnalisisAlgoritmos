import sys
import argparse
import suffixArray as sa

def main():
    parser = argparse.ArgumentParser(description="Suffix array")
    parser.add_argument('-f', '--file', required=True, help='Ruta del texto')
    parser.add_argument('-c', '--consultas', required=False,help='Archivo con consultas ( una por linea)')
    
    args = parser.parse_args()
    

    file_path = args.file
    consultas = args.consultas

    #Leer el texto
    f = open(file_path,"r")
 
    text = ""
    for l in f:
        text +=l.replace('\n',"")
    print("JEJEJEJEJ",text)
    f.close()

    sufList = sa.suffixList_v1(text)
    
    posList = sa.sufPosition(sufList)
    textList = sa.sufText(sufList)
    for e in textList:
        print(e)



if __name__ == "__main__":
    main()
