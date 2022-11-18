# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:32:00 2022

@author: Charl
"""

#To order a list of integers so that the odd numbers appear before the even numbers and the odd numbers are in increasing order, while the even numbers are in decreasing order.

def num_ord(randNums: list) -> list:
    #oddList = list(map(key = lambda: ))
    oddList = sorted([el for el in randNums if el % 2 == 1])
    evenList = sorted([el for el in randNums if el % 2 == 0], reverse = True)
    oddList.extend(evenList)
    return oddList
    
print(num_ord([0,5,3,3,4,2,56,6,7,3,3,5,7,7,2,5,7,8,90,7,4]))

def num_or_k(num):
    return -(num % 2), -num if num % 2 == 0 else num
nums = [0,5,3,3,4,2,56,6,7,3,3,5,7,7,2,5,7,8,90,7,4]

nums.sort(key = num_or_k)
print(nums)

nums = [0,5,3,3,4,2,56,6,7,3,3,5,7,7,2,5,7,8,90,7,4]

print(list(filter(lambda x: x%2, nums)))

nums.sort(key = lambda number: (-(number % 2), -number if number % 2 == 0 else number))
print(nums)

#To order a list of strings considering the number of vowels in increasing order, then the whole length in increasing order, then the reverse alphabetical order.

def word_ord(randWord: list) -> list:
    return sum(1 for el in randWord if el in "aeiou"), -len(randWord), randWord

words = ["pear","sdg","jpth","sdfb","cbn","ngref"]
words.sort(key = word_ord, reverse = True)
print(words)


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
