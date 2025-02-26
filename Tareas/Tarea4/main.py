import sys
import argparse
from shannon_fano import shannon_fano_coding
#TODO: huffman algorithm
from huffman import huffman_coding
from utils import decode_str, write_bits_to_file, get_file_size, read_bits_from_file

def main():
    parser = argparse.ArgumentParser(description="Archivo a comprimir usando Shannon-Fano o Huffman")
    parser.add_argument('-f', '--file', required=True, help='PRuta del archivo a comprimir')
    parser.add_argument('-a', '--algorithm', required=True, choices=['sf', 'hf'], help='Algoritmo de compresión a utilizar: Shannon-Fano (sf) o Huffman (hf)')
    
    args = parser.parse_args()
    
    file_path = args.file
    algorithm = args.algorithm
    
    with open(file_path, 'r') as f:
        file = f.read()
    
    if algorithm == 'sf':
        coded_file, b_sf = shannon_fano_coding(file)
    elif algorithm == 'hf':
        coded_file, b_sf = huffman_coding(file)
        #print("Algoritmo de Huffman aún no implementado.")
       # sys.exit()
    
    decoded_text = decode_str(coded_file, b_sf)
    if decoded_text == file:
        print("\nLa codificación es correcta! Al decodificar el texto se obtiene el contenido original.")
    else:
        print("\nError en la codificación! Al decodificar el texto no se obtiene el contenido original.")
    
    byte_coded_file = f'results/{file_path.split("/")[-1].split(".")[0]}.{algorithm}'
    write_bits_to_file(coded_file, byte_coded_file)
    
    original_size = get_file_size(file_path)
    compressed_size = get_file_size(byte_coded_file)
    print(f"\nTamaño del archivo original: {original_size} bits")
    print(f"Tamaño del archivo comprimido: {compressed_size} bits")
    
    bin_file = read_bits_from_file(byte_coded_file)
    
    if file == decode_str(bin_file, b_sf):
        print("\nLa compresión es correcta! Al leer y decodificar el archivo binario se obtiene el contenido original.")
    else:
        print("\nError en la compresión! Al leer y decodificar el archivo binario no se obtiene el contenido original.")
    

if __name__ == "__main__":
    main()
