# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:09:07 2022

@author: Charl
"""

def perf_squares (n):
    square = 1
    while True:
        squared = square**2
        if squared <= n:
            print(squared)
            last_square = squared
        else:
            break
        square += 1
    return last_square
        
print(perf_squares(65))

def two_powers (n):
    twoPower = 1
    while True:
        powered = 2**twoPower
        if powered <= n:
            print(powered)
            last_square = powered
        else:
            break
        twoPower += 1
    return last_square
        
print(two_powers(129))

def odd_sum(a, b):
    if a % 2 == 0:
        a += 1
    
    if b % 2 == 0:
        b -= 1

    output = 0
    for i in range(a,b+1,2):
        output += i
    return output

print(odd_sum(8,12))

def factor_finder(n):
    i = 2
    count = 0
    
    while i <= int(n/2):
        if n % i == 0:
            print(i)
            count += 1
        i += 1
    return count

print(factor_finder(29))