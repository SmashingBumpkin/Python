# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:12:59 2022

@author: Charl
"""

###Hanoi towers###
#Move three discs of increasing size to the last pole of the hanoi towers
#larger discs cannot be on smaller discs

#if all discs are on rh pole, return 

start = [[3,2,1],[0,0,0],[0,0,0]]

def move_discs(lst):
    if lst[2] == [3,2,1]:
        return lst
    
    
def suffix(word):
    if len(word) == 1:
        return [word]
    output = [word]
    output.extend(suffix(word[1:]))
    return output

'''
print([hello].extend([ello].extend([llo].extend([lo].extend([o])))))

print(suffix("hello"))
'''
print(suffix("hello"))