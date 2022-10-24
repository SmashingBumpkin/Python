# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:47:15 2022

@author: Charl
"""

#Write a function that gets two lists of integers. It inserts new elements in 
#the first list, considering the elements of the second list as positions in 
#the first list and the indexes of the elements as the values to be inserted 
#(i.e., if the second list is [4, 2, 3] it inserts 0 in position 4, 1 in 
#position 2 and 2 in position 3). If a position is outside the first list, 
#the value is ignored.

list1 = [6,7,8,9,10]
list2 = [1,3,3,8,5]

def listInserter(listA, listB):
    posn = 0
    for i in listB:
        listA.insert(i,posn)
        posn += 1
    
    return listA

#Write a function that gets two lists of ints and appends in the first list 
#only the elements of the second list that are not already in the first list.

def listAppender(listA, listB):
    for i in listB:
        if i not in listA: listA.append(i) 
    return listA



print(listInserter(list1, list2))
print(listAppender(list1, list2)) #why are the lists being modified here?
