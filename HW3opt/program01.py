# -*- coding: utf-8 -*-

# A binary sequence S is stored in a text file. We are interested in the frequency
#     of segments in S: we recall that a segment is a sub-sequence made of
#     consecutive elements; its frequency indicates the number of times that
#     segment occurs in S. Take as an example the following text file,
#     named ‘ft1.txt’. The file contains the following sequence:

#     01010010010001000111101100001010011001111000010010011110010000000

# The frequency of segment ‘00’ is 12. The frequency of segment ‘1000’ is 5.
#     Notice that the sequence is split into three consecutive lines.

# Let min_len and max_len two integers such that min_len <= max_len. We aim at
#     extracting the segments of S that are of length between min_len and
#     max_len. Furthermore, we want to list the n highest frequencies and the
#     related segments, where n is a given integer.
#     Should only m < n distinct segments of length between min_len and max_len
#     occur, the output should consist of fewer elements (that is, only m
#     entries).

# Design a function ex1(text_f, min_len, max_len, n) that takes as arguments:
#     - text_f: the path of the text file in which the binary sequence is
#       stored, in one or more consecutive lines;
#     - min_len, max_len: two integers such that min_lem <= max_len, indicating
#       the minimum and maximum length of the segments of which we want to
#       compute the frequency, respectively;
#     - n: an integer indicating the maximum number of highest frequencies we want
#       to report; and returns:
#     - a list of pairs (tuples of arity 2) defined as follows.

# Every pair in the list consists of:
#     1) the frequency, and
#     2) the list of segments that occur with that frequency.
#     We recall that the list should contain at most the highest n frequencies
#     (or fewer, if there are less than n distinct frequencies).
#     The list is sorted lexicographically with respect to the first element of
#     the tuple. The lists in the second element of every pair are sorted
#     lexicographically too.

# For instance, ex1('tf1.txt', 2, 4, 20) returns the following list:
#     [ (1, ["1011", "1101"]),
#       (2, ["0101", "0110", "1010"]), 
#       (3, ["0111", "101", "1110", "1111"])     
#       (4, ['0001', '0011', '1100' ]),
#       (5, ['011', 1000', '110' ]),
#       (6, ['0000', '111']),
#       (7, ['0010','1001' ]),
#       (8, ['0100']),
#       (10,['010']),
#       (11,['000', '001', '11']),
#       (12,['100']),
#       (15,['01','10']),
#       (23,['00'])
#     ]

# NOTE: the timeout for this exercise is of 0.5 seconds for each test.

# WARNING: Make sure that the uploaded file is UTF8-encoded
#     (to that end, we recommend you edit the file with Spyder)

#pytest test_01.py -v -rA

#import time
def ex1(text_file, min_len, max_len, n):
    
    
    #t = time.time()
    #open file and put entire contents into a single string with no \n
    with open(text_file, "r", encoding = "utf8") as fileRef:
        strIn = ""
        for line in fileRef:
            strIn += line.strip()
    
    #if max_len - min_len > n:
    #    max_len = min_len + n
    
    #Outermost loop - width = length of window, from min_len to max_len
    #next loop - loop through the string in window of size width
    #add key to list with val 0 if it's not there already
    #add 1 to val
    #print(time.time() - t)
    #t = time.time()
    strDict = {}
    
    for width in range(min_len, max_len+1):
        for posn in range(len(strIn)-width+1):
            key = strIn[posn:posn+width]
            strDict[key] = strDict.get(key,0) + 1
    # 
    
    
    #search output0 for value
    #if not found append value to output0 and [key] to output1
    #if found append key to correct index of output1
    #zip together output0 and output1
    #print(time.time() - t)
    #t = time.time()
    
    
    # output0 = []
    # output1 = []
    
    # for key in strDict:
    #     value = strDict[key]
    #     try:
    #         output1[output0.index(value)].append(key)
    #     except:
    #         output0.append(value)
    #         output1.append([key])    
    
    
    
    output0 = list(set(strDict.values()))
    output0.sort()
    output0 = output0[-n:]
    limit = output0[0]
    output1 = list([] for _ in range(len(output0)))
    for key, value in strDict.items():
        if value >= limit:
            output1[output0.index(value)].append(key)
            
    for line in output1:
        line.sort()

    return list(zip(output0,output1))    
        
    

if __name__ == '__main__':
    
    #t= time.time()
    output = ex1('ft1.txt', 2, 4, 20)
    #print(ex1('ft1.txt', 2, 4, 20))
    #print(ex1('ft2.txt', 2, 5, 10))
    #print(ex1("ft100.txt", 23, 49, 17))
    #output = ex1('ft9600.txt', 23, 69, 22)
    #output = ex1('ft3600.txt', 5, 39, 35)
    #print("Total:",time.time()-t)
    #for i in output:
    #    print(i)
        #print(i[0], len(i[1]))
        
        #pass
    
    pass
    