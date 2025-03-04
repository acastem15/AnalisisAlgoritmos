

def search (text,sufList,query,results): 

    #Stop recursion
    numSuf = len(sufList)
    half =numSuf//2

    halfSuffixText = sufList[half].text
    halfSuffixPos = sufList[half].position

    subStrSuf = halfSuffixText[0:len(query)]

    print(0,half,numSuf)

    print("check",halfSuffixText,"pos ",halfSuffixPos,subStrSuf,query)
    if query==subStrSuf: 
            results.append(f"{halfSuffixPos}-{halfSuffixPos+len(query)-1}")

    if numSuf>1 and query!=subStrSuf: 
        halfLeft = sufList[0:half]
        halfRight = sufList[half:]
    
        if query <subStrSuf: 
            search(text,halfLeft,query,results)
        

        elif query>subStrSuf:
            search(text,halfRight,query,results)
    elif numSuf==1 and query!=subStrSuf:
        print("End recursion")

    return results
        

