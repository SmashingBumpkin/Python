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

def RepeatingChars(charList : list, k : int) -> int:
  #your code goes here
  pass


if __name__ == "__main__":
  print(RepeatingChars(['a', 'a', 'z', 'b', 'b', 'b', 'a', 'a', 'a', 'z', 'c', 'c'], 1))
  print(RepeatingChars(['a', 'a', 'z', 'b', 'b', 'b', 'a', 'a', 'a', 'z', 'c', 'c'], 2))
  print(RepeatingChars(['a', 'a', 'z', 'b', 'b', 'b', 'a', 'a', 'a', 'z', 'c', 'c'], 3))
  print(RepeatingChars(['a', 'a', 'z', 'b', 'b', 'b', 'a', 'a', 'a', 'z', 'c', 'c'], 4))


if __name__ == "__main__":
  print(Binary2Decimal_Value("01110100")) # 116
  print(Binary2Decimal(["00", "01", "10", "11"])) # [0, 1, 2, 3]