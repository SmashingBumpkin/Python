

def es37(dictionariesList):
    '''Write the function es37(dictionariesList) that takes as an input a
    list of dictionaries and returns a dictionary.

    The input dictionaries in dictionariesList have character strings
    between 'a' and 'z' as keys and lists of integers as attributes.

    The output dictionary has as keys the keys common to at least half
    of the dictionaries of the input list.  Each x key of this output
    dictionary is associated with a set.  An integer is present in the
    set with key x if and only if it is present in the attribute list
    of key x for at least one dictionary in dictionariesList.

    For example:
    - if dictionariesList contains the three dictionaries
    {'a': [1,3,5],'b':[2,3 ],'d':[3]},
    {'a':[5,1,2,3], 'b':[2],'d':[3]},
    {'a':[3,5], 'c':[4,1,2],'d':[4]}
    the returned dictionary will be
    {'a':{1,2,3,5},'b':{2,3},'d':{3,4}}
    

    '''
    dicOut = {}
    for element in dictionariesList:
        for key in element.keys():
            dicOut[key] = dicOut.get(key,0) + 1
    
    minFreq = int((len(dictionariesList)/2)+0.5)
    
    tempDic = dicOut.copy()
    
    for key, value in tempDic.items():
        if value < minFreq:
            dicOut.pop(key)
        else:
            dicOut[key] = set()
    
    #iterate through dictionaries in list
    for dick in dictionariesList:
        for key, value in dick.items():
            try:
                dicOut[key] = dicOut[key].union(set(value)) 
            except KeyError:
                pass
            
    return dicOut


dicList = [{'a': [1,3,5],'b':[2,3 ],'d':[3]},
{'a':[5,1,2,3], 'b':[2],'d':[3]},
{'a':[3,5], 'c':[4,1,2],'d':[4]}]

print(es37(dicList))


