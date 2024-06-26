# -*- coding: utf-8 -*-


'''
Let int_seq be a string that contains a sequence of non-negative
    integers separated by commas and subtotal a non-negative integer.

A function ex1(int_seq, subtotal) that:
    – takes as parameters 
      a string (int_seq) and a positive integer (subtotal >= 0), and 
    – returns the number of substrings of int_seq such that 
      the sum of their values is equal to subtotal.

For example, given 

int_seq = '3,0,4,0,3,1,0,1,0,0,5,0,4,2' #

and subtotal = 9, 
    the function should return 7. The following substrings, indeed, consist of
    values whose sum is equal to 9:
    int_seq = '3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
            => _'0,4,0,3,1,0,1,0'_____________
               _'0,4,0,3,1,0,1'_______________
               ___'4,0,3,1,0,1,0'_____________
               ___'4,0,3,1,0,1'_______________
               ___________________'0,0,5,0,4'_
               _____________________'0,5,0,4'_
               _______________________'5,0,4'_

'''


def ex1(int_list, subtotal):
    
    count = 0
    i = 1 # end of window
    j = 0 # start of window
    intList = [int(i) for i in int_list.split(",")]
    winSum = intList[0] #sum of elements in window

    try:
        while 1:
            while winSum < subtotal: #iterates window to the right while the sum is too low
                winSum += intList[i]
                i += 1
            
            while winSum == subtotal: #counts when window is correct, checks trailing 0s and iterates if possible
                tempI = i
                count += 1
                try: 
                    while intList[tempI] == 0: 
                        tempI += 1
                        count += 1  #checks trailing 0s and counts them
                    
                except: 
                    pass
                winSum -= intList[j]                    
                j += 1
            
            while winSum > subtotal: #iterates window left when the sum is too high
                winSum -= intList[j]
                j += 1
    except:
        pass
    return count