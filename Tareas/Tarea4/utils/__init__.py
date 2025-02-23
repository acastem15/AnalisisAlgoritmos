
import os
import math


def get_file_size(file_path:str)->int:
    """Obtiene el tamaño en bits del archivo en 'file_path'.

    Args:
        file_path (str): _description_

    Returns:
        int: _description_
    """    
    return os.path.getsize(file_path)*8


def decode_str(coded_str:str, b_map:dict)->str:
    """Decodifica la cadena codificada 'coded_str' usando el diccionario de códigos 'b_map'.

    Args:
        coded_str (str): _description_
        b_map (dict): diccionario con mapeo símbolo -> código.

    Returns:
        str: _description_
    """    
    
    # Crear el diccionario inverso: código -> símbolo
    inv_b_sf = {code: symbol for symbol, code in b_map.items()}
    
    decoded = ""
    current_code = ""
    for bit in coded_str:
        current_code += bit
        # Si la secuencia acumulada coincide con un código, se añade el símbolo correspondiente
        if current_code in inv_b_sf:
            decoded += inv_b_sf[current_code]
            current_code = ""
    return decoded
    
    
def write_bits_to_file(bitstring, filename):
    """ Escribe la cadena de bits 'bitstring' en el archivo 'filename' como bytes reales.
    Se agrega padding para completar el último byte y se almacena la cantidad de bits de padding
    en el primer byte del archivo.

    Args:
        bitstring (_type_): _description_
        filename (_type_): _description_
    """    
    # Calcular el padding necesario para que la longitud sea múltiplo de 8
    extra_padding = (8 - len(bitstring) % 8) % 8
    padded_bitstring = bitstring + "0" * extra_padding

    # Almacenar el padding en el primer byte
    output_bytes = bytearray()
    output_bytes.append(extra_padding)

    # Convertir cada grupo de 8 bits en un byte
    for i in range(0, len(padded_bitstring), 8):
        byte = padded_bitstring[i:i+8]
        output_bytes.append(int(byte, 2))
    
    # Escribir en modo binario. El archivo resultante siempre tendrá al menos 1 byte extra 
    # para almacenar el padding.
    with open(filename, 'wb') as f:
        f.write(output_bytes)


def read_bits_from_file(filename):
    """ Lee el archivo binario 'filename' y recupera la cadena de bits original,
    quitando el padding indicado en el primer byte.

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """    
    with open(filename, 'rb') as f:
        data = f.read()
    
    # El primer byte indica la cantidad de bits de padding agregados
    extra_padding = data[0]
    
    # Convertir los bytes restantes en una cadena de bits
    bitstring = ""
    for byte in data[1:]:
        bitstring += format(byte, '08b')
    
    # Quitar el padding del final
    if extra_padding:
        bitstring = bitstring[:-extra_padding]
    
    return bitstring


def compute_stats(char_prob:dict, char_code_length:dict, 
                file_content:str, set_of_chars:set):
    """ Calcula e imprime los siguientes estadísticos:
    - Valor esperado de bits por símbolo, de acuerdo a ∑p(x)l(x)
    - Entropía en el peor caso, de acuerdo a log2(n)
    - Entropía de Shannon, de acuerdo a ∑p(x)log2(p(x))
    - Total de bits necesarios para codificar el archivo
    - Almacenamiento real esperado, considerando el byte para almacenar la cantidad de padding y el padding
    
    Args:
        char_prob (dict): _description_
        char_code_length (dict): _description_
        file_content (str): _description_
        set_of_chars (set): _description_
    """    
    # Valor esperado de bits por símbolo
    average_bits = sum(char_prob[char]*char_code_length[char] for char in set_of_chars)
    print(f"Valor esperado de bits por símbolo: {average_bits}")
    # Entropía en el peor caso
    entropy_worst_case = math.log2(len(set_of_chars))
    print(f"Entropía en el peor caso: {entropy_worst_case}")
    # Entropía de Shannon
    entropy =-sum(char_prob[char]*math.log2(char_prob[char]) for char in set_of_chars)
    print(f"Entropía de Shannon: {entropy}")
    # Total de bits necesarios para codificar el archivo
    total_bits  = sum(char_code_length[char] for char in file_content)
    print(f"Total de bits necesarios: {total_bits}")
    # Almacenamiento real esperado, considerando el byte para almacenar la cantidad de padding y el padding mismo
    expected_storage = total_bits+8+total_bits%8
    print(f"Almacenamiento real esperado en bits: {expected_storage}")
    