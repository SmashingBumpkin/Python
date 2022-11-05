# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:17:43 2022

@author: Charl
"""

#Write a function that gets a list of ints and returns a new list with only 
#the elements in an even position.

listy = [0,1,2,3,4,5,6,7]

def even_posns(listx):
    return [value for count, value in enumerate(listx) if count % 2 == 0]

print(even_posns(listy))

#Write a function that gets a list with any possible value types and returns 
#a new list with only the integers of the list in input.
listy = [0,1,2,3,4,5,6,7,"a","b"]

def int_only(listx):
    return [value for value in listx if type(value) == int]
print(int_only(listy))

listy = [0,1,2,3,4,5,6,7,"a","b"]

def int_only2(listx):
    [listx.remove(value) for value in listx[:] if type(value) != int]
    pass
print(int_only2(listy))
print(listy)


#Write a function that gets an int n and creates a list with all the integers 
#from 0 to n. Then, starting from 2, it removes from the list all the 
#multiples of the list elements. The function returns the list with the 
#remaining elements.

#Write a function that gets two lists of ints and appends in the first list 
#only the elements of the second list that are not already in the first list.
listyB = [5,6,8,9,110]

def list_merger(listA, listB):
    return [listA.append(value) for value in listB if value not in listA]
print(list_merger(listy, listyB))

print(listy)

#Write a function that gets two lists of integers. It inserts new elements in
#the first list, considering the elements of the second list as positions in 
#the first list and the indexes of the elements as the values to be inserted 
#(i.e., if the second list is [4, 2, 3] it inserts 0 in position 4, 1 in 
#position 2 and 2 in position 3). If a position is outside the first list, the
#value is ignored.


def list_inserter(listA: list, listB: list):
    
    for posn, value in enumerate(listB):
        print(posn, value)
        try:
            listA[value] = posn
        except IndexError:
            pass
        
list_inserter(listy, listyB)

print(listy)













