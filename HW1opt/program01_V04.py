# -*- coding: utf-8 -*-

'''
Let int_seq be a string that contains a sequence of non-negative
    integers separated by commas and subtotal a non-negative integer.

Design a function ex1(int_seq, subtotal) that:
    – takes as parameters 
      a string (int_seq) and a positive integer (subtotal >= 0), and 
    – returns the number of substrings of int_seq such that 
      the sum of their values is equal to subtotal.

Hint: you can obtain a substring by picking any consecutive
    elements in the original string.

For example, given int_seq = '3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' and subtotal = 9, 
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

NOTE: it is FORBIDDEN to use/import any libraries

NOTE: Each test must terminate on the VM before the timeout of
    1 second expires.

WARNING: Make sure that the uploaded file is UTF8-encoded
    (to that end, we recommend you edit the file with Spyder)
'''

def ex1(int_seq, subtotal):
    #create an array of 0s which shows you how many consecutive 0s you have. Eg for array
    #0,5,4,3,0,0,0,3,0,0,0,0,0,0,2
    #returns array:
    #1,0,0,0,3,0,3,0,6,0,0,0,0,6,0
    
    #iterate through array.
    #when a zero is found:
        #iterate through the array, counting how many zeroes are consecutive.
        #input the result of that count into the first and last entries of the range
        #skip forward to the first non zero in range
    
    
    intList = int_seq.split(',')
    zeroList = [0] * len(intList)
    i = 0
    #0,5,4,3,0,0,0,3,0,0,0,0,0,0,2
    try:
        while True:
            intList[i] = int(intList[i])
            if intList[i] == 0:
                zeroCount = 1
                for j in intList[i+1:]:
                    intList[i+zeroCount] = int(j)
                    if intList[i+zeroCount] != 0:
                        break
                    zeroCount += 1
                zeroList[i] = zeroCount
                i += zeroCount
                zeroList[i-1] = zeroCount
            i+=1
    except:
        pass
    zeroList.append(0)
    
    #print(zeroList)
    #print(intList)
    
    count = 0
    i = 0 # end of window
    j = 0 # start of window
    
    winSum = intList[0] #sum of elements in window
    #print(len(intList))
    try:
        while 1:
            while winSum < subtotal: #iterates window to the right while the sum is too low
                i += 1
                winSum += intList[i]
                
            if winSum == subtotal:   #counts when window is correct, checks trailing 0s 
                                    #and iterates if possible
                                    #checks leading 0s
                #Leading zeros is given by zeroList[j]
                #checks trailing 0s
                #trailing zeroes is given by zeroList[i+1]
                #uses equation (total solutions = (1+leading 0s)(1+trailing zeros))
                #iterates j and i to end of 0s, removes last value of j
                i += 1
                if zeroList[i] == 0 and zeroList[j] == 0:
                    count += 1
                    while intList[i] == intList[j]:
                        if zeroList[i] != 0:
                            i -= 1
                        count += 1
                        i += 1
                        j += 1
                    else:
                        j += 1
                    winSum = winSum + intList[i] - intList[j-1]
                else:
                    count += (zeroList[i] + 1)*(zeroList[j] + 1)
                    i += zeroList[i] + 1
                    j += zeroList[j] + 1
                    winSum = winSum + intList[i-1] - intList[j-1]
                    
                        
                
                            
            
        
            while winSum > subtotal: #iterates window left when the sum is too high
                winSum -= intList[j]
                j += 1
    except:
            pass
        
    return count
print(ex1("5,5,5,5",5))

#print(ex1("1,2,1,1,1,2,1",3))

print(ex1('3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2',9))
print(ex1('0,0,3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2,0,0,9,9,0',9))
#          0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
#         [1,0,1,0,1,0,0,1,0,1,0,2,2,0,1,0,0,1,0

if __name__ == '__main__':
    # Insert your own tests here
    pass