
from suffix import Suffix
from collections import OrderedDict


def suffixList_v1(text):
    arrayList = []
    size = len(text)-1

    while size>=0: 
        suf = text[size:]

        suffixObj = Suffix(suf,size)

        arrayList.append(suffixObj)
        size-=1
    arrayList.sort()

    return arrayList

from collections import OrderedDict, defaultdict

from collections import OrderedDict, defaultdict

def suffixList_v2(text):
    alphabet = set()  # Conjunto para caracteres únicos
    arrayDict = defaultdict(list)  # Diccionario de listas

    # Construir lista de sufijos por carácter
    for i, character in enumerate(reversed(text)):  

        if character not in alphabet:  
            alphabet.add(character)  

            char_suf_list = [
                Suffix(text[j:], j) for j in range(len(text)) if text[j] == character
            ]
            char_suf_list.sort()  

            arrayDict[character] = sufPosition(char_suf_list)  

    sorted_arrayList_flat = OrderedDict(
        (pos, length) for _, pos_list in sorted(arrayDict.items()) for pos, length in pos_list.items()
    )

    return sorted_arrayList_flat


def sufPosition (sufList): 
    posList =[]
    #posList = {suf.position: len(suf.text) for suf in sufList}
    posList = OrderedDict((suf.position, len(suf.text)) for suf in sufList)
    return posList
   # print(posList)
  #  return posList

def sufText (sufList): 
    textList =[]
    for suf in sufList:
        textList.append(suf.text)
    return textList


