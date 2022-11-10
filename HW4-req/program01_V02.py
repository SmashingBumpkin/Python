#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
The objective of the homework assignment is to design and implement a function
that reads some strings contained in a series of files and generates a new
string from all the strings read.
The strings to be read are contained in several files, linked together to
form a closed chain. The first string in each file is the name of another
file that belongs to the chain: starting from any file and following the
chain, you always return to the starting file.

Example: the first line of file "A.txt" is "B.txt," the first line of file
"B.txt" is "C.txt," and the first line of "C.txt" is "A.txt," forming the 
chain "A.txt"-"B.txt"-"C.txt".

In addition to the string with the name of the next file, each file also
contains other strings separated by spaces, tabs, or carriage return 
characters. The function must read all the strings in the files in the chain
and construct the string obtained by concatenating the characters with the
highest frequency in each position. That is, in the string to be constructed,
at position p, there will be the character with the highest frequency at 
position p of each string read from the files. In the case where there are
multiple characters with the same frequency, consider the alphabetical order.
The generated string has a length equal to the maximum length of the strings
read from the files.

Therefore, you must write a function that takes as input a string "filename"
representing the name of a file and returns a string.
The function must construct the string according to the directions outlined
above and return the constructed string.

Example: if the contents of the three files A.txt, B.txt, and C.txt in the
directory test01 are as follows


test01/A.txt          test01/B.txt         test01/C.txt                                                                 
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt         test01/A.txt
house                 home                 kite                                                                       
garden                park                 hello                                                                       
kitchen               affair               portrait                                                                     
balloon                                    angel                                                                                                                                               
                                           surfing                                                               

the function most_frequent_chars ("test01/A.txt") will return "hareennt".
pytest test_01.py -v -rA
'''


###NEW PLAN###
#initialize dictionary of dictionaries for each position in word
#Open file
#take first line
#split into word
#split word into enumerated letters
#add entry to position i in dicdic, and add 1 to count of letter in subdic

def most_frequent_chars(filename: str) -> str:
    contLoop, currFile, posnDic = True, filename, {}
    while contLoop:
        with open(currFile, 'r', encoding = 'utf8') as fileRef:
            currFile = fileRef.readline().strip()
            for lines in fileRef:
                currWord = word_returner(lines)
                for word in currWord:
                    for i, letter in enumerate(word):
                        posnDic[i] = posnDic.get(i,{})
                        posnDic[i][letter] = posnDic[i].get(letter, 0) + 1
        if currFile == filename:
            contLoop = False
    return freq_finder(posnDic)

def freq_finder(posnDic):
    output = ""
    for dics in posnDic.values():
        maxCount = max(dics.values())
        output += min([key for key, value in dics.items() if value == maxCount])
    return output

#takes crappy string and returns list of words
def word_returner(currWord):
    currWord = currWord.strip()
    if ' ' or '\t' in currWord:
        return currWord.replace('\t', ' ').split()
        
    elif currWord != '':
        return currWord
                                                                                                                                                                                                                                                                                                                                                                                                            
# def most_frequent_chars(filename: str) -> str:
#     contLoop, currFile, wordList = True, filename, []
#     while contLoop:
#         with open(currFile, 'r', encoding = 'utf8') as fileRef:
#             currFile = fileRef.readline().strip()
#             for lines in fileRef:
#                 currWord = lines.strip()
#                 if ' ' in currWord or '\t' in currWord:
#                     currWord = currWord.replace('\t', ' ').split()
#                     for word in currWord:
#                         wordList.append(word)
#                 elif currWord != '':
#                     wordList.append(currWord)
#         if currFile == filename:
#             contLoop = False
#     return wordlist_to_string(wordList)


# def wordlist_to_string(wordList):
#     #NEW PLAN
#     #Loop through each word, then through each letter.
#     #add each letter to a list in position of index of letter
#     #count most frequent letters/best letter
#     """
#     lim = len(max(wordList,key = len))
#     output = ""
#     letterList = [""] * lim
#     for word in wordList:
#         for i, letter in enumerate(word):
#             letterList[i] += letter
#     for letters in letterList:
#         maxCount = letters.count(max(letters, key=letters.count))
#         maxChars = [c for c in letters if letters.count(c) == maxCount]
        
#         output += min(maxChars)
    
#     """
#     lim = len(max(wordList,key = len))
#     output = ""
#     for posn in range(lim):
#         #go through words and add them to dic, or add 1 to count in dic
#         newWordList = []
#         wordDic = {}
#         for word in wordList:
#             try:
#                 letter = word[posn]
#             except IndexError:
#                 continue
#             newWordList.append(word)
#             wordDic[letter] = wordDic.get(letter,0) + 1
#         wordList = newWordList
#         #get highest counts from dictionary
#         #get earliest letter from highest counts
#         #append letter to string
#         #print(wordDic)
#         maxCount = max(wordDic.values())
#         output += min([key for key, value in wordDic.items() if value == maxCount])
#     return output


#print(most_frequent_chars('test04/capillarities.txt'))
print(most_frequent_chars('test01/A.txt'))
