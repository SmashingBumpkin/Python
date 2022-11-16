# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:32:00 2022

@author: Charl
"""

#dict of words which start with each letter

def word_starter(strIn: str) -> dict:
    newStr = ""    
    strIn = strIn.split(" ")
    bigDic = {}
    for word in strIn:
        letter = word[0].lower()
        
        try:
            bigDic[letter].append(remove_nonalpha(word[1:]))
        except KeyError:
            bigDic[letter] = [remove_nonalpha(word[1:])]
    return bigDic
    
def remove_nonalpha (stringding):
    output = ""
    for char in stringding:
        if char.isalpha():
            output += char
            
    return output

print(word_starter("this is a Whole bunch of words starting with diff letts.."))
