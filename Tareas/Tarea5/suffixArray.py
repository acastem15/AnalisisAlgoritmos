
from suffix import Suffix


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

def sufPosition (sufList): 
    posList =[]
    for suf in sufList:
        posList.append(suf.position)
    return posList

def sufText (sufList): 
    textList =[]
    for suf in sufList:
        textList.append(suf.text)
    return textList

def suffixList_v2(text):

    arrayList = []
    size = len(text)-1

    while size>=0: 
        suf = text[size:]

        suffixObj = SuffixBetter(suf,size)

        arrayList.append(suffixObj)
        size-=1
    arrayList.sort()

    return arrayList

