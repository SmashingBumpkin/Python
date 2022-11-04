# -*- coding: utf-8 -*-
'''
A binary sequence S is stored in a text file. We are interested in the frequency
    of segments in S: we recall that a segment is a sub-sequence made of
    consecutive elements; its frequency indicates the number of times that
    segment occurs in S. Take as an example the following text file,
    named ‘ft1.txt’. The file contains the following sequence:

    01010010010001000111101100001010011001111000010010011110010000000

The frequency of segment ‘00’ is 12. The frequency of segment ‘1000’ is 5.
    Notice that the sequence is split into three consecutive lines.

Let min_len and max_len two integers such that min_len <= max_len. We aim at
    extracting the segments of S that are of length between min_len and
    max_len. Furthermore, we want to list the n highest frequencies and the
    related segments, where n is a given integer.
    Should only m < n distinct segments of length between min_len and max_len
    occur, the output should consist of fewer elements (that is, only m
    entries).

Design a function ex1(text_f, min_len, max_len, n) that takes as arguments:
    - text_f: the path of the text file in which the binary sequence is
      stored, in one or more consecutive lines;
    - min_len, max_len: two integers such that min_lem <= max_len, indicating
      the minimum and maximum length of the segments of which we want to
      compute the frequency, respectively;
    - n: an integer indicating the maximum number of highest frequencies we want
      to report; and returns:
    - a list of pairs (tuples of arity 2) defined as follows.

Every pair in the list consists of:
    1) the frequency, and
    2) the list of segments that occur with that frequency.
    We recall that the list should contain at most the highest n frequencies
    (or fewer, if there are less than n distinct frequencies).
    The list is sorted lexicographically with respect to the first element of
    the tuple. The lists in the second element of every pair are sorted
    lexicographically too.

For instance, ex1('tf1.txt', 2, 4, 20) returns the following list:
    [ (4, ['0001', '0011', '1100' ]),
      (5, ['011', 1000', '110' ]),
      (6, ['0000', '111']),
      (7, ['0010','1001' ]),
      (8, ['0100']),
      (10,['010']),
      (11,['000', '001', '11']),
      (12,['100']),
      (15,['01','10']),
      (23,['00'])
    ]

NOTE: the timeout for this exercise is of 0.5 seconds for each test.

WARNING: Make sure that the uploaded file is UTF8-encoded
    (to that end, we recommend you edit the file with Spyder)

'''
#import time

def ex1(text_file, min_len, max_len, n):
    #t= time.time()
    
    # Enter your code here
    
    fileRef = open(text_file, "r", encoding = "utf8")
    strIn = ""
    for line in fileRef:
        strIn += line.strip()
    
    #Outermost loop - window = substring length, from min_len to max_len
    #next loop - loop through the string in windows
    #if window is in dict, add 1, else add to dict at = 1
    
    #print(time.time()-t)
    #t= time.time()
    
    strDict = {}
    i=0
    for width in range(min_len, max_len+1):
        for posn in range(len(strIn)-width+1):
            strDict[strIn[posn:posn+width]] = strDict.get(strIn[posn:posn+width],0) + 1
    
    
    #print(time.time()-t)
    #t= time.time()
    
    
    
    #iterate through keys in dict
    #iterate through elements of output
    #if value of key is in output list, add key to output
    #
    #else append a append new tuple to output

    
    output = [(-1,'-1')]
    
    for element in strDict:
        enterIf = True
        for i in range(len(output)):
            if output[i][0] == strDict[element]:
                output[i][1].append(element)
                enterIf = False
                break
        if enterIf:
            output.append((strDict[element],[element]))
    
    #print(time.time()-t)
    #t= time.time()
    
    output.remove((-1,'-1'))  
    
    #sort output
    #count entries until greater than n. Remove all entried after n
    
    output.sort()
    
    for line in output:
        line[1].sort()
        
    output = output[-n:]
    
    #print(time.time()-t)
    #t= time.time()
    
    return output


if __name__ == '__main__':
    
    #t= time.time()
    #output = ex1('ft1.txt', 2, 4, 20)
    #print(ex1('ft1.txt', 2, 4, 20))
    #print(ex1("ft100.txt", 23, 49, 17))
    output = ex1('ft9600.txt', 23, 69, 22)
    for i in output:
        #print(i)
        pass
    #print("Total:",time.time()-t)