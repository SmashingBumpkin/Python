# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:05:51 2022

@author: Charl
"""


#_______________________
#_______RECURSION_______
#_______________________

#Calculate factorial recursively

#x! = x * x-1 * x-2... until 0
#BASE CASE - X = 1 (1!)
import time
def factorialization(myInput: int):
    if myInput == 1:
        return 1
    return myInput * factorialization(myInput -1)

def facto2(myInput: int):
    j=1
    for i in range(myInput-1):
        #print(i)
        j=(i+1)*j
    return j

def count_a(S: str) -> int:
    if "a" not in S:
        return 0
    return 1 + count_a(S[S.index("a")+1:])
    
S = ""
S[0:1] == ""
S[0] == ""

if __name__ == "__main__":
    stringy = "aaajsndfoanfaaa"
    print(count_a("anffnaaa"))
    print(count_a(stringy))
    # t = time.time()
    # print("lol")#factorialization(2000))
    # for i in range(2000):
    #     factorialization(2000)
    # print(time.time()-t)
    # t = time.time()
    # for i in range(2000):
    #     facto2(2000)
    # print("jeeeeez")#facto2(2000))
    # print(time.time()-t)
    
    #print(len(str(facto2(300000))))
    pass