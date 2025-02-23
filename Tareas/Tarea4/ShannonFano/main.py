import math

def shannon_fano(symbols, code=''):
    """
    Función recursiva que implementa el algoritmo Shannon-Fano.
    Recibe una lista de tuplas (símbolo, frecuencia) ordenada de forma descendente.
    """
    # Caso base: si solo hay un símbolo, se asigna el código (si está vacío se asigna "0")
    if len(symbols) == 1:
        symbol, freq = symbols[0]
        return {symbol: code if code != '' else '0'}
    
    # Calcular la suma total de frecuencias
    total = sum(freq for symbol, freq in symbols)
    
    # Buscar el punto de partición: el índice donde la suma acumulada se acerca a la mitad
    accum = 0
    partition = 0
    for i, (symbol, freq) in enumerate(symbols):
        accum += freq
        if accum >= total / 2:
            partition = i + 1  # dividir después de este índice
            break

    # Dividir en dos grupos
    left = symbols[:partition]
    right = symbols[partition:]
    
    # Llamadas recursivas añadiendo '0' al grupo izquierdo y '1' al derecho
    codes = {}
    codes.update(shannon_fano(left, code + '0'))
    codes.update(shannon_fano(right, code + '1'))
    return codes

def compute_statistics(codes, frequencies, total_chars):
    """
    Calcula las estadísticas de la codificación:
      - Número de bits esperado por símbolo (longitud promedio).
      - Entropía del mensaje.
      - Longitud máxima del código (peor caso).
      - Número total de bits para el texto completo.
    """
    # Bits esperados (longitud promedio)
    expected_bits = sum((freq / total_chars) * len(codes[symbol]) for symbol, freq in frequencies.items())
    
    # Entropía: H = -∑ p * log₂(p)
    entropy = -sum((freq / total_chars) * math.log2(freq / total_chars) for symbol, freq in frequencies.items() if freq > 0)
    
    # Peor caso: longitud máxima de código asignado
    worst_case = max(len(code) for code in codes.values())
    
    # Número total de bits necesarios para el texto
    total_bits = sum(freq * len(codes[symbol]) for symbol, freq in frequencies.items())
    
    return expected_bits, entropy, worst_case, total_bits

def compress_text(text, codes):
    """Codifica el texto utilizando el diccionario de códigos."""
    return ''.join(codes[ch] for ch in text)

def decompress_text(encoded, codes):
    """
    Función sencilla para descomprimir el texto.
    Reconstruye el mensaje utilizando el mapeo inverso (nota: al ser un código prefijo, se puede leer de forma secuencial).
    """
    # Generar el mapeo inverso: código -> símbolo
    rev_codes = {code: symbol for symbol, code in codes.items()}
    decoded = ''
    buffer = ''
    for bit in encoded:
        buffer += bit
        if buffer in rev_codes:
            decoded += rev_codes[buffer]
            buffer = ''
    return decoded

def main():
    # Solicitar al usuario el nombre del archivo a comprimir
    filename = input("Ingrese el nombre del archivo a comprimir: ")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # Calcular las frecuencias de cada símbolo
    frequencies = {}
    for ch in text:
        frequencies[ch] = frequencies.get(ch, 0) + 1
    total_chars = len(text)

    # Crear una lista ordenada de símbolos (descendente por frecuencia)
    sorted_symbols = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

    # Generar el diccionario de códigos con Shannon-Fano
    codes = shannon_fano(sorted_symbols)

    # Calcular las estadísticas
    expected_bits, entropy, worst_case, total_bits = compute_statistics(codes, frequencies, total_chars)

    # Mostrar los códigos asignados
    print("Códigos asignados:")
    for symbol, code in codes.items():
        # Para una mejor visualización se transforma el salto de línea o espacio
        if symbol == '\n':
            display_symbol = '\\n'
        elif symbol == ' ':
            display_symbol = "' '"
        else:
            display_symbol = symbol
        print(f"'{display_symbol}': {code}")

    # Mostrar las estadísticas
    print("\nEstadísticas de la compresión:")
    print(" - Número de bits esperado por símbolo: {:.4f}".format(expected_bits))
    print(" - Entropía (bits por símbolo): {:.4f}".format(entropy))
    print(" - Longitud máxima de código (peor caso): {} bits".format(worst_case))
    print(" - Número total de bits para el texto: {}".format(total_bits))

    # Codificar el texto
    encoded_text = compress_text(text, codes)
    print("\nTexto codificado (se muestran los primeros 100 bits):")
    print(encoded_text[:100] + ("..." if len(encoded_text) > 100 else ""))

    # Ejemplo de descompresión para validar el proceso
    decoded_text = decompress_text(encoded_text, codes)
    if decoded_text == text:
        print("\nLa compresión y descompresión se realizaron correctamente.")
    else:
        print("\nError: el texto decodificado no coincide con el original.")

if __name__ == "__main__":
    main()
