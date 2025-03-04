

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


    return results
        

def extend_v1(results,sufList,query,index,sign):
    halfNextSuffixText = sufList[index].text
    halfNextSuffixPos = sufList[index].position
    substrSuf = halfNextSuffixText[0:len(query)]

    while query==substrSuf: 
        #print(substrSuf,query,index)
        results.append(f"{halfNextSuffixPos}-{halfNextSuffixPos+len(query)-1}")
        if sign =="left":
            index-=1
        else:
            index+=1
        halfNextSuffixText = sufList[index].text
        halfNextSuffixPos = sufList[index].position
        substrSuf = halfNextSuffixText[0:len(query)]

    return results

def search_v2(text,posList,query,results):

    numSuf = len(posList)
    half = numSuf//2
     # print ("half actual: "+str(half))
    initial_pos, size = list(posList.items())[half]

     # print (posList)
     # print ("error: ", half in posList)
    end_pos = initial_pos + size -1
    halfSuffixText = text[initial_pos:end_pos]
    halfSuffixPos = initial_pos

    subStrSuf = halfSuffixText[0:len(query)]


    #print("check",halfSuffixText,"pos ",halfSuffixPos,subStrSuf,query)
    index = half
  
    if query==subStrSuf: 
            results.append(f"{halfSuffixPos}-{halfSuffixPos+len(query)-1}")
            #Extend right and left
            if index>0: 
                #Extend left
                results = extend_v2(text,results,posList,query,index-1,"left")
            if index<len(posList)-1:
                results = extend_v2(text,results,posList,query,index+1,"right")


    if numSuf>1 and query!=subStrSuf: 
        halfLeft  = {key: posList[key] for key in list(posList.keys())[:half]}
        halfRight = {key: posList[key] for key in list(posList.keys())[half:]}
    
        if query <subStrSuf: 
            search_v2(text,halfLeft,query,results)
        

        elif query>subStrSuf:
            search_v2(text,halfRight,query,results)


    return results
        
def extend_v2(text,results,posList,query,index,sign):
    initial_pos, size = list(posList.items())[index]
    end_pos = initial_pos + size -1
    halfNextSuffixText = text[initial_pos:end_pos]
    halfNextSuffixPos = initial_pos
    substrSuf = halfNextSuffixText[0:len(query)]

    while query==substrSuf: 
        #print(substrSuf,query,index)
        results.append(f"{halfNextSuffixPos}-{halfNextSuffixPos+len(query)-1}")
        if sign =="left":
            index-=1
        else:
            index+=1
        initial_pos, size = list(posList.items())[index]
        end_pos = initial_pos + size -1
        halfNextSuffixText = text[initial_pos:end_pos]
        halfNextSuffixPos = initial_pos
        substrSuf = halfNextSuffixText[0:len(query)]

    return results