# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:20:34 2022

@author: Charl
"""

# write a function that converts a binary number (passed as a string)
# to the equivalent decimal value (returned as an integer)
# for example, passing "01110100" to the function, you should get
# the integer value 116

# then, write another function that converts a list of binary
# numbers (passed as a parameter) to the list of equivalent
# decimal values (returned as a list of integers)

def Binary2Decimal_Value(bin: str) -> int:
  bitValue = 1
  total = 0
  
  for i in bin[::-1]:
      total += int(i) * (bitValue)
      bitValue = bitValue * 2

  return total
  

def Binary2Decimal(bin_list: list) -> list:
    decList = [0] * len(bin_list)
    posn = 0
    
    for j in bin_list:
        bitValue = 1
        total = 0
        
        for i in j[::-1]:
            total += int(i) * (bitValue)
            bitValue = bitValue * 2
            
        decList[posn] = total
        posn += 1
    
    return decList


# assume you are given a list of single characters (i.e., every list item
# is a 1 character-long string) and an integer value k > 0.
# write a function that countes and returns the number of characters
# in the list that repeat k or more times consecutively.

# for example, if the list is ['a', 'a', 'z', 'b', 'b', 'b', 'a', 'a', 'a', 'z', 'c', 'c']
# for k = 1, the fuction returns 6, as all characters repeat al least one time;
# for k = 2, the function returs 4, as a, b, a and c repeat 2, 3, 3, 2 times, respectively;
# for k = 3, the function returns 2, as b and a repeat 3, 3 times, respectively;
# for k = 4 (or more), the function returns 0.

def RepeatingChars(charList : list, k : int) -> int:
    #loop through each element of charList
    #count +1
    #on next loop, if element = previous element, count +1
    #else append count to list of counts
    #end loop and return # elements in count greater than k
    lastChar = ""
    consecList = []
    count = 0
    for i in charList:
        if i == lastChar:
            count += 1
        else:
            consecList.append(count)
            count = 1
            lastChar = i
    consecList.append(count)
    return len([i for i in consecList if i >= k])
          


if __name__ == "__main__":
  print(Binary2Decimal_Value("01110100")) # 116
  print(Binary2Decimal(["00", "01", "10", "11"])) # [0, 1, 2, 3]
  print(RepeatingChars(['a', 'a', 'z', 'b', 'b', 'b', 'a', 'a', 'a', 'z', 'c', 'c'], 1))
  print(RepeatingChars(['a', 'a', 'z', 'b', 'b', 'b', 'a', 'a', 'a', 'z', 'c', 'c'], 2))
  print(RepeatingChars(['a', 'a', 'z', 'b', 'b', 'b', 'a', 'a', 'a', 'z', 'c', 'c'], 3))
  print(RepeatingChars(['a', 'a', 'z', 'b', 'b', 'b', 'a', 'a', 'a', 'z', 'c', 'c'], 4))
  

# The goal of this assignment is to write a text-based version of the hangman game:

# https://en.wikipedia.org/wiki/Hangman_(game)
# http://www.playhangman.com/PH.asp?g=cats
# https://play.google.com/store/apps/details?id=com.klikapp.hangman2
# https://itunes.apple.com/IE/app/id327449554

# we assume that the program contains a pre-defined list of words among
# which the secret one is chosen from

# the best approach will be to solve simpler problems first and then
# combine their solutions into the a single program, for example
# (the list is only a suggestion, it does not mean that you have to follow it):
#    • problem 1: given a word of any length, generate a string of the same
#      length containing stars only (e.g., given the word "hello",
#      you will generate "*****")
#    • problem 2: given a string, replace the n-th character of
#      the string with a different one
#    • problem 3: given a word and a character, generate a string of
#      the same length containing stars everywhere, except for the
#      positions occupied by the character (e.g., given "hello" and "l",
#      you will generate "**ll*")
#    • problem 4: given a string containing a mix of characters and stars,
#      count the number of stars (e.g., given "**llo", you will get 2)

def HangMan():
    # your code goes here
    word = "shlong"
    censored = ""
    for i in word: censored += "_ " 
    print("Your word is: ", censored)
    guesses = 8
    for i in range(8):
        print("you have ", guesses - i, "guesses left")
        guess = input("Input your guess here: ")
        
        
if __name__ == "__main__":
  HangMan()