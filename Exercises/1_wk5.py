# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:57:01 2022

@author: Charl
"""

#input n
#calc
#output Nth term of fibo sequence
#
#

def fiboCalc(n):
    if n == 1 or n == 2:
        return 1
    elif n < 1:
        print("twat")
        return
    return fiboCalc(n-1) + fiboCalc(n-2)

num=6 
print("the ", num, "th term of the fibonacci sequence is", fiboCalc(num))

# write a function that takes as input a list L of floats and
# returns the list obtained by summing up the items in L by groups of 3
# hint: use list slicing to obtain the sublists of L containing 3 items

# for example, given L = [1.5, 0, -1.2, 1.0, -2.5, 0.5, 0, 1.1, -1.5]
# the function returns [0.3, -0.2, -2.7, -1, -2, 1.6, -0.4]

# (1.5 + 0 + (-1.2) = 0.3; 0 + (-1.2) + 1 = -0.2; and so on)

def SumBy3(numbers):
  return [sum(numbers[i:i+3]) for i in range(len(numbers))]
  
print(SumBy3([1.5, 0, -1.2, 1.0, -2.5, 0.5, 0, 1.1, -1.5]))

print(["a"] in ["a","b"])