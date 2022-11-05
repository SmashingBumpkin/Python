

def es36(dictionariesList):
    '''Implement the function es36(dictionariesList) that takes as an
    input a list of dictionaries and returns a dictionary.

    The input dictionaries in the dictionariesList have character
    strings between 'a' and 'z' as key and lists of integers as
    attributes.

    The keys in the output dictionary are the keys common to all the
    dictionaries in dictionariesList.  Each x key of the output
    dictionary is associated with a list of integers.  An integer is
    present in the list of a key x if and only if it is present in the
    attribute list of key x for all the dictionaries of
    dictionariesList.  The list is also sorted in ascending order.

    For example:
    - if the dictionariesList contains the three dictionaries
    {'a': [1,3,5],'b':[2,3 ],'d':[3]},
    {'a':[5,1,2,3], 'b':[2],'d':[3]},
    {'a':[3,5], 'c':[4,1,2],'d':[4]}
    - the returned dictionary is
    {'a':[3,5],'d':[]}

    '''
    #start a new dictionary = first dictionary in list
    #compare first dictionary to next dictionary, remove anything that's not repeated
    #repeat above step to end of list
    dicOut: dict = dictionariesList[0]
    
    #iterate through dictionaries in list
    for dick in dictionariesList:
        #iterate through key/value pairs in dick. Remove any keys that aren't present
        tempDic = dicOut.copy()
        for key, value in tempDic.items():
            if key not in dick:
                dicOut.pop(key)
            #if keys are present, remove anything that's not in dick values for key
            else:
                for element in dicOut[key]:
                    if element not in dick[key]:
                        dicOut[key].remove(element)
    
    for values in dicOut.values():
        values.sort()
    return dicOut
                    

#dicList = [{'a': [1,3,5],'b':[2,3 ],'d':[3]},
#{'a':[5,1,2,3], 'b':[2],'d':[3]},
#{'a':[3,5], 'c':[4,1,2],'d':[4]}]

#print(dicList, dicList[0])

#print(es36(dicList))