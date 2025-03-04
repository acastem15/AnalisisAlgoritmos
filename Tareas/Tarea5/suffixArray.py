
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


