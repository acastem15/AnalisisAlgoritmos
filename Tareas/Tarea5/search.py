

def search_v1 (text,sufList,query,results): 

    #Stop recursion
    numSuf = len(sufList)
    half =numSuf//2

    halfSuffixText = sufList[half].text
    halfSuffixPos = sufList[half].position

    subStrSuf = halfSuffixText[0:len(query)]


    #print("check",halfSuffixText,"pos ",halfSuffixPos,subStrSuf,query)
    index = half
  
    if query==subStrSuf: 
            results.append(f"{halfSuffixPos}-{halfSuffixPos+len(query)-1}")
            #Extend right and left
            print("VAMO A EXTENDER")
            if index>0: 
                #Extend left
                results = extend_v1(results,sufList,query,index-1,"left")
            if index<len(sufList)-1:
                results = extend_v1(results,sufList,query,index+1,"right")


    if numSuf>1 and query!=subStrSuf: 
        halfLeft = sufList[0:half]
        halfRight = sufList[half:]
    
        if query <subStrSuf: 
            search_v1(text,halfLeft,query,results)
        

        elif query>subStrSuf:
            search_v1(text,halfRight,query,results)
    elif numSuf==1 and query!=subStrSuf:
        print("End recursion")

    return results
        

def extend_v1(results,sufList,query,index,sign):
    halfNextSuffixText = sufList[index].text
    halfNextSuffixPos = sufList[index].position
    substrSuf = halfNextSuffixText[0:len(query)]

    while query==substrSuf: 
        print(substrSuf,query,index)
        results.append(f"{halfNextSuffixPos}-{halfNextSuffixPos+len(query)-1}")
        if sign =="left":
            index-=1
        else:
            index+=1
        print("HEEEEEY INDEX",index)
        halfNextSuffixText = sufList[index].text
        halfNextSuffixPos = sufList[index].position
        substrSuf = halfNextSuffixText[0:len(query)]

     
    print("Ya no es igual")
    return results
         
