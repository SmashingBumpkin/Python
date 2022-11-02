# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:06:23 2022

@author: Charl
"""

# write a function that, given a text file name as parameter,
# counts and returns the number of characters and lines
# in the file

# newline characters should not be counted

def NumCharsAndLinesInFile(textFile : str) -> (int, int):
  # your code goes here
  fileRef, nC, nL = open(textFile, "r", encoding = "utf8"), 0, 0
  for line in fileRef:
      nL += 1
      nC += len(line)
  fileRef.close()
  return nC, nL

"""
if __name__ == "__main__":
  nC, nL = NumCharsAndLinesInFile("textfile.txt")
  print("the file contains %i characters and %i lines" % (nC, nL))
"""


# write a function that counts and returns the number of
# odd and even numbers in a given text file

# the text file name is provided as a parameter to the function

# the file contains some integer numbers separated by
# any number of spaces and on different lines
# (lines can also be empty, or contain spaces only)

# for example, CountOddEvenInFile("numbers.txt") has to
# return (5, 7)

def CountOddEvenInFile(fileName: str) -> (int, int):
  fileRef, odd, even = open(fileName, "r", encoding = "utf8"), 0, 0
  
  for line in fileRef:
      listt = line.strip().split(" ")
      try:
          for _ in range(len(listt)):
              listt.remove("")
      except:
          pass
      for element in listt:
          if int(element) % 2 == 0:
              even += 1
          else:
              odd += 1
              
  fileRef.close()
  return odd, even

"""
if __name__ == "__main__":
  odd, even = CountOddEvenInFile("numbers.txt")
  print("odd:", odd, "even:", even)
"""

# write a function that reads the content of a text file,
# counts the occurrences of each word in the file,
# and saves them in an output text file

# the function takes the 2 file names as input and
# returns the total number of distinct words found
# in the input file

# the output file will contain, on each line, a word
# followed by its occurrences, separated by a space

# a word is any sequence of n > 0 letters

# the input file can contain punctuation (. , ; : ? !) but no numbers

# case is not considered, so "Home" is the same as "home"

# YOU CANNOT USE DICTIONARIES - YOU CAN USE LISTS ONLY

# for example, give the file "lorem-ipsum.txt" as input,
# the function will return 2620 and the first lines of the
# the output file will be:
# lorem 15
# ipsum 16
# dolor 13
# sit 61
# amet 62

def CountWordsInFile(inFile : str, outFile : str) -> int:
    # your code goes here
    fileRef, wordDic = open(inFile, "r", encoding = "utf8"), []
    char_to_replace = {'.': '',
                       ',': '',
                       ';': '',
                       ':': '',
                       '?': '',
                       '!': ''}
    
    
    for line in fileRef:
        listt = str.lower(line.translate(str.maketrans(char_to_replace))).split(" ")
        for element in listt:
            if element in wordDic:
                pass
            
            
    
    fileRef.close()
    return 5

if __name__ == "__main__":
  M = CountWordsInFile("lorem-ipsum.txt", "result.txt")
  print("the file contains %i words" % M)
