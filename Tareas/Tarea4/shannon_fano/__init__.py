import math
from utils import compute_stats
    
def shannon_fano_coding(file_content:str)->tuple[str, dict]:
    """Shannon-Fano coding algorithm

    Args:
        file_path (str): _description_
        dict (_type_): _description_

    Returns:
        _type_: _description_
    """    
        
    set_of_chars = set(file_content)

    # Calcular la probabilidad de cada símbolo y la longitud de su código
    # según el techo de -log2(p)
    char_prob = {}
    char_code_length = {}
    for char in set_of_chars:
        char_prob[char] = file_content.count(char)/len(file_content) # probabilidad
        char_code_length[char] = math.ceil(-math.log2(char_prob[char])) # longitud
        
    compute_stats(
        char_prob=char_prob, 
        char_code_length=char_code_length, 
        file_content=file_content, 
        set_of_chars=set_of_chars
    )
    
    # Algoritmo de codificación Shannon-Fano:
    l_sf = sorted(char_code_length.items(), key=lambda x: x[1])
    b_sf = {l_sf[0][0]: bin(0)[2:].zfill(l_sf[0][1])}

    # BSF[i]=(BSF[i-1]+1)*2d[i] where d[i] = LSF[i]-LSF[i-1]
    for i in range(1, len(l_sf)):
        d_i = l_sf[i][1]-l_sf[i-1][1]
        b_sf[l_sf[i][0]] = bin((int(b_sf[l_sf[i-1][0]], 2)+1)*2**(d_i))[2:].zfill(l_sf[i][1])
        
        
    coded_file = "".join(b_sf[symbol] for symbol in file_content)
    
    return coded_file, b_sf