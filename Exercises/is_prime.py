# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:30:37 2022

@author: Charl
"""
import math

#get prime numbers
def is_prime(number):
    i=2
    endWhile = 1 + math.floor(number / 2)
    if number == 2:
        return True
    while i <= endWhile:
        if number % i == 0:
            return False
        i+=1
    return True

print(is_prime(77557187))