# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:53:03 2022

@author: Charl
"""

from random import randint

def repeated_chars (charList, outFile):
    
    d = {}
    for el in charList:
        d[el] = d.get(el,0) + 1
    
    with open(outFile,'w') as fileRef:
        [print(key, value, sep='\t',file = fileRef) for key, value in d.items()]
            

mylist = ['1','1','1',6,'a',3.4]
repeated_chars(mylist, 'outfile.txt')

mybiglist = [randint(-100,100) for (_) in range(4000)]
repeated_chars(mybiglist,'bigoutty.txt')