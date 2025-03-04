

def search (text,sufList,query,result): 


    #Stop recursion
    numSuf = len(sufList)
    half =numSuf//2

    halfSuffixText = sufList[half].text
    halfSuffixPos = sufList[half].position
    if numSuf>1: 

        halfLeft = sufList[0:half]
        halfRight = sufList[half:]
        i=0
        qInSuffix = halfSuffixText.find(query)
        if qInSuffix: 
            result.append(halfSuffixPos+qInSuffix)
        else 


            if query <halfSuffix:
                search(text,halfLeft,query)
                break
            elif c >halfSuffix[i]: 
                search(text,halfRight,query)
                break
            elif c in halfSuffix:  
    else:
        for c in query: 
            if c <halfSuffix[i]:
                search(text,halfLeft,query)
                break
            elif c >halfSuffix[i]: 
                search(text,halfRight,query)
                break
            elif c==halfSuffix[i]: 
                i+=1  


