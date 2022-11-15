#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The objective of the homework assignment is to design and implement a function
# that reads some strings contained in a series of files and generates a new
# string from all the strings read.
# The strings to be read are contained in several files, linked together to
# form a closed chain. The first string in each file is the name of another
# file that belongs to the chain: starting from any file and following the
# chain, you always return to the starting file.

# Example: the first line of file "A.txt" is "B.txt," the first line of file
# "B.txt" is "C.txt," and the first line of "C.txt" is "A.txt," forming the 
# chain "A.txt"-"B.txt"-"C.txt".

# In addition to the string with the name of the next file, each file also
# contains other strings separated by spaces, tabs, or carriage return 
# characters. The function must read all the strings in the files in the chain
# and construct the string obtained by concatenating the characters with the
# highest frequency in each position. That is, in the string to be constructed,
# at position p, there will be the character with the highest frequency at 
# position p of each string read from the files. In the case where there are
# multiple characters with the same frequency, consider the alphabetical order.
# The generated string has a length equal to the maximum length of the strings
# read from the files.

# Therefore, you must write a function that takes as input a string "filename"
# representing the name of a file and returns a string.
# The function must construct the string according to the directions outlined
# above and return the constructed string.

# Example: if the contents of the three files A.txt, B.txt, and C.txt in the
# directory test01 are as follows


# test01/A.txt          test01/B.txt         test01/C.txt                                                                 
# -------------------------------------------------------------------------------
# test01/B.txt          test01/C.txt         test01/A.txt
# house                 home                 kite                                                                       
# garden                park                 hello                                                                       
# kitchen               affair               portrait                                                                     
# balloon                                    angel                                                                                                                                               
#                                            surfing                                                               

# the function most_frequent_chars ("test01/A.txt") will return "hareennt".
# pytest test_01.py -v -rA

                                                                                                                                                                                                                                                                                                                                                                                               
def most_frequent_chars(filename: str) -> str:
    currFile, wordList = filename, []
    #Opens each file, then extracts the next file, then builds the wordlist
    #from the data contained within.
    
    while True:
        with open(currFile, 'r', encoding = 'utf8') as fileRef:
            currFile = fileRef.readline().strip()
            
            for lines in fileRef:
                currWord = lines.strip()
                
                if ' ' in currWord or '\t' in currWord:
                    wordList.extend(currWord.replace('\t', ' ').split())
                elif currWord != '':
                    wordList.append(currWord)
                    
        if currFile == filename:
            break
    
    wordList.sort(key = len, reverse = True)
    return wordlist_to_string(wordList)


def wordlist_to_string(wordList):
    #go through words and add them to dic, or add 1 to count in dic
    #get highest counts from dictionary
    #get earliest letter from highest counts
    #append letter to string
    output = ""
    for posn in range(len(wordList[0])):
        wordDic = {}
        
        try:
            for word in wordList:
                letter = word[posn]
                wordDic[letter] = wordDic.get(letter,0) + 1
        except:
            pass
        
        maxCount = max(wordDic.values())
        output += min([key for key, value in wordDic.items() if value == maxCount])
        
    return output


#print(most_frequent_chars('test04/capillarities.txt'))
#print(most_frequent_chars('test01/A.txt'))
