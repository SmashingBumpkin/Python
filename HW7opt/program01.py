# -*- coding: utf-8 -*-
'''
    We have a sequence of N integers, with N odd.
    We apply the following procedure to the sequence, that could delete some elements from the sequence.
    - While there exists at least 2 equal numbers in the sequence:
        - we delete 2 of these equal numbers and keep the others in the same order.

    Given a n integer sequence as such, we want to find all final sequences obtained by repeatedly applying
    the above procedure until it's no more possible to do it.
    notice that all these sequences contain the same positive number of different integers.

    E.g. consider the three of sequences that we obtain from the sequence 1 2 0 1 0 0 1 
    by applying the procedure. You can see the tree in the file game_tree.pdf 
    The tree leaves are the final sequences.

    This is an example of a game tree implicitly defined by the game rules.
    - the root is the initial sequence
    - the daughter nodes of any node are obtained by deleting one pair of equal values
    - the leaves are the sequences where the procedure cannot be applied further

    You should define the ex1(sequence) recursive function 
    (or using other recursive functions or methods as you see fit) that:
    - receives as argument a string encoding the sequence of N integers with N odd
    (in the string all numbers are separated by a space)
    - returns a set containing the encodings (strings with integers separated by space)
      of all final sequences that it's possible to produce

    E.g. from the sequence '1 2 0 1 0 0 1' ex1 should return the set
      {'2 0 1', '2 1 0', '1 2 0'}

NOTICE: the timeout for this exercise is 1 second for each test
NOTICE: at heast one of the functions/methods used in the solution SHOULD be recursive
NOTICE: the test machinery automatically recognizes recursione ONLY for functions that are
        defined at the external level (no inner functions) or for methods
        DO NOT define the recursive functions inside another function/method
NOTICE: do not import other libraries or open other files

pytest test_01.py -v -rA
'''

# def ex1(s):
#     #Receive string on numbers convert to list sequence
#     seq = [int(x) for x in s.split()]
    
#     #define an empty output set
#     output = set()
#     #loop through index i in list
#     for i in range(len(seq)):
#         #define a temporary output set
#         #each loop apply ex1rec to tempoutput[i:] and shorten list
#         tempSeq = seq[i:]
#         ex1Rec(tempSeq)
#         outTemp = seq[:i]
#         outTemp.extend(tempSeq)
#         ex1Rec(outTemp)
#         strOut = ""
#         for j in range(len(outTemp)):
#             strOut += str(outTemp[j]) + " "
#         strOut = strOut.strip()
        
#         output.add(strOut)
#         #convert output to string and add to output set
#     return(output)

# def ex1Rec(seq):
#     # Iterate over the list and delete any elements that have at least
#     # two occurrences in the list.
#     for i in seq:
#         if seq.count(i) >= 2:
#             seq.remove(i)
#             seq.remove(i)
#             ex1Rec(seq)
#             break
#     return seq

def ex1(s):
    #Receive string on numbers convert to list sequence
    seq = [int(x) for x in s.split()]
    
    
    comprising = set(seq)
    for num in comprising:
        if seq.count(num) % 2 == 0:
            seq = remove_all(seq, num)
            
    comprising = set(seq)
    seq = remove_consecutive_repeats(seq)
    
    #define an empty output set
    output = set()
    
    #numbers in each set
    comprising = set(seq)
    placeholder = max(comprising)+1
    
    
    #variations of the set
    sequences = [seq]
    
    contLoop = True
    #loop through every number in comprising
        #loop through sequences
            #create a list of new list for each sequence combination
        #remove duplicates from modified list
        #replace current comprising with a the modified list
    
    
    for num in comprising:
        reducedSeq = []
        # print(num)
        for sequence in sequences:
            # print(sequence)
            reducedSeq.extend(remove_int_variations2(sequence, num))
        sequences = remove_repeats(reducedSeq)
    
    for sequence in sequences:
        tempOut = ""
        for num in sequence:
            tempOut += str(num) + " "
        tempOut = tempOut[:-1]
        output.add(tempOut)
            

    return(output)


def remove_all(l, num):
    try:
        l.remove(num)
        return remove_all(l,num)
    except:
        return l

def remove_consecutive_repeats(lst):
    # If the list is empty or has only one element, return it
    if len(lst) <= 1:
        return lst
    
    # If the first two elements in the list are the same, call the function recursively on the rest of the list
    if lst[0] == lst[1]:
        return remove_consecutive_repeats(lst[1:])
    
    # If the first two elements in the list are different, return the first element followed by the result of calling the function recursively on the rest of the list
    else:
        return [lst[0]] + remove_consecutive_repeats(lst[1:])
    



def remove_int_variations2(lst, c):
    if lst.count(c) == 1:
        return [lst]
    
    output = []
    
    for i, num in enumerate(lst):
        if num == c:
            lst[i] = 'z'
            newL = remove_all(lst[:i],c)
            newL.append(c)
            newL.extend(remove_all(lst[i+1:],c))
            lst[i] = c
            output.append(newL)
    
    return output
            
        
def remove_int_variations(lst, c):
    # If the list is empty or does not contain the integer c, return an empty list
    if len(lst) == 0 or c not in lst:
        return []
    
    # If the list contains only one occurrence of the integer c, return the list as a single-element list
    elif lst.count(c) == 1:
        return [lst]
    
    # If the list contains more than one occurrence of the integer c, initialize an empty list to store the variations
    else:
        variations = []
        
        # Iterate over the list
        for i in range(len(lst)):
            # If the current element is the integer c, remove it from the list and call the function recursively on the modified list
            if lst[i] == c:
                new_lst = lst[:i] + lst[i+1:]
                variations.extend(remove_int_variations(new_lst, c))
                
        # Return the list of variations
        return variations


def remove_repeats(lst):
    # If the list is empty or has only one element, return it
    if len(lst) <= 1:
        return lst
    
    # If the first element in the list appears later in the list, call the function recursively on the rest of the list
    if lst[0] in lst[1:]:
        return remove_repeats(lst[1:])
    
    # If the first element in the list does not appear later in the list, return the first element followed by the result of calling the function recursively on the rest of the list
    else:
        return [lst[0]] + remove_repeats(lst[1:])

if __name__ == '__main__':
    mystr = '1 2 0 1 0 0 1'



    # Expected output: [1, 2, 3, 4, 5]

    print(ex1(mystr))
    print("\n" + ' '.join(['1']*2)+' 2')
    print(ex1(' '.join(['1']*2)+' 2'))
    pass
    # put here your personal tests

