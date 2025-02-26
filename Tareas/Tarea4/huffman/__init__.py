import math
import heapq
from utils import compute_stats
    
def huffman_coding(file_content:str)->tuple[str, dict]:
    """Huffman coding algorithm

    Args:
        file_path (str): _description_
        dict (_type_): _description_

    Returns:
        _type_: _description_
    """    
        
    set_of_chars = set(file_content)

    # Calcular la probabilidad de cada símbolo
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
    
    # Algoritmo de codificación Huffman:
    b_h = huffmanAlgorithm(char_prob)

    coded_file = "".join(b_h[symbol] for symbol in file_content)
    
    return coded_file, b_h

def huffmanAlgorithm(char_prob):
    BH={}
    char_tree = {char:{"parent": None, "code":""} for char in char_prob}
    priority_queue = [(char_prob, char) for char, char_prob in char_prob.items()]
    heapq.heapify(priority_queue)

    if len(priority_queue) == 1:
        _, char = priority_queue[0]
        BH[char] = "0"
        return BH

    while len(priority_queue) > 1:
        prob1, char1 = heapq.heappop(priority_queue)
        prob2, char2 = heapq.heappop(priority_queue)

        new_node = char1 + char2
        new_prob = prob1 + prob2

        char_tree[new_node] = {"parent": None, "code":""}

        char_tree[char1]["parent"] = new_node
        char_tree[char1]["code"] = 1

        char_tree[char2]["parent"] = new_node
        char_tree[char2]["code"] = 0

        heapq.heappush(priority_queue, (new_prob, new_node))

    for char in char_prob:
        code = char_tree[char]["code"]
        BH[char] = code

        parent = char_tree[char]["parent"]
        while parent is not None:
            code = char_tree[parent]["code"]
            BH[char] = str(code) + str(BH[char])

            parent = char_tree[parent]["parent"]    
   
    return BH
