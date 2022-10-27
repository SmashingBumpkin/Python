# -*- coding: utf-8 -*-

""""
The standard encoding for Roman numerals follows the rules:
- there is no zero
- only the chars 'IVXLCDM' are used, which correspond to the decimal values
  'I' = 1, 'V' = 5, 'X' = 10, 'L' = 50, 'C' = 100, 'D' = 500, 'M' = 1000
- numbers are written from left to right, starting with higher values letters
  (thousands, hundreds, tens, units)
- the value of a Roman numeral is obtained by adding the values of the characters,
  EXCEPT when a character is followed by a higher-value character;
  in that case, the lower-value char is subtracted from instead of summed to
  the higher-value char
- at most, 3 equal symbols can be used together, only for the 'IXCM' ones
  ('III' = 3, 'XXX' = 30, 'CCC' = 300 , 'MMM' = 3000)
- to represent numbers containing digit 4 and/or 9, we use the subtraction from the
  symbol that follows
  e.g.: 4 = 'IV'   9 = 'IX',    40 = 'XL'    39 = 'IXL'   499 = 'ID'

The XKCD encoding

Let us now consider the Roman numerals encoding suggested by Randall Munroe in his XKCD blog.
He encodes each Roman symbol with the corresponding value and then joins all digits together.
E.g.    397 =>  'CCCXCVII' => 100 100 100 10 100 5 1 1 => '10010010010100511'
Let call this encoding "XKCD format".
To go back to our example, the XKCD sequence '10010010010100511' corresponds to 397.

The goal of this homework is to decode a list of strings representing Roman numerals
in the XKCD format, and return the K maximum corresponding values, in decreasing order.

Design and implement the following functions:

NOTICE: no other libraries are allowed.
"""
def decode_XKCD_tuple(xkcd_values : tuple, k : int) -> list:
    '''
    Receives as arguments a list of strings representing values in the
    XKCD format, and a positive integer k <= len(xkcd_values).
    Decodes all XKCD formatted values and return the k higher values
    sorted in decreasing order.

    Parameters
    xkcd_values : list[str]     list of strings (values) in XKCD format
    k : int                     how many values to return
    Returns
    list[int]                   k maximum values in decreasing order
    '''
    # ADD HERE YOUR CODE
    decValues = []
    for i in xkcd_values:
        decValues.append(decode_value(i))
    decValues.sort(reverse = 1)
        
    return decValues[:k]


def decode_value(xkcd : str ) -> int:
    '''
    Decode a string representing a value in XKCD format
    and returns the corresponding decimal value (integer).

    Parameters
    xkcd : str                  string in XKCD format
    Returns
    int                         the corresponding value
    
    E.g.: '10010010010100511' -> 397
    '''
    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


def xkcd_to_list_of_weights(xkcd : str) -> list:
    '''
    Splits an XKCD formatted string into the corresponding
    list of weights, each corresponding to one of the original roman 
    numeral symbols the encoding is based on.

    Parameters
    xkcd : str              XKCD formatted string
    Returns
    list[int]               list of 'weights' corresponding to roman symbols

    E.g.: '10010010010100511' -> [100, 100, 100, 10, 100, 5, 1, 1,]
    '''
    subStr = ""
    i = 0
    #'I' = 1, 'V' = 5, 'X' = 10, 'L' = 50, 'C' = 100, 'D' = 500, 'M' = 1000
    lenXKCD = len(xkcd)
    listXKCD = []
    while i < lenXKCD:
        if xkcd[i:i+4] == "1000":
            listXKCD.append(1000)
            i += 4
            continue
        elif xkcd[i:i+3] == "500":
            listXKCD.append(500)
            i += 3 
            continue
        elif xkcd[i:i+3] == "100":
            listXKCD.append(100)
            i += 3 
            continue
        elif xkcd[i:i+2] == "50":
            listXKCD.append(50)
            i += 2
            continue
        elif xkcd[i:i+2] == "10":
            listXKCD.append(10)
            i += 2
            continue
        elif xkcd[i] == "5":
            listXKCD.append(5)
            i += 1
            continue
        else:
            listXKCD.append(1)
            i += 1
    return listXKCD


def list_of_weights_to_number(weights : list ) -> int:
    '''
    Transforms a list of weights obtained from the XKCD format
    to the corresponding decimal value, by using the 'sum/subtract' rules.

    Parameters
    weights : list[int]    list of 'weights' of Roman numerals
    Returns
    int                    corresponding integer value
    
    E.g.: [100, 100, 100, 10, 100, 5, 1, 1,] -> 397
    '''
    output = 0
    i = 1
    for element in weights[:-1]:
        if element < weights[i]:
            output -= element
        else:
            output += element
        i += 1
    output += weights[-1]
    return output




###################################################################################

if __name__ == '__main__':
   # add here your personal tests
    #print(decode_XKCD_tuple(['10010010010100511','100010010010100511'],2))
    #print(decode_XKCD_tuple(["1101001000"],1)) #889
    #print(decode_XKCD_tuple(["1000100100010100110"],1)) #1999
    #print(decode_XKCD_tuple([ "1000100100010100110",  "100010001050015" , "50010010050101015"], 2)) #[2494, 1999]
    #print(decode_XKCD_tuple([ "150",  "1050110" , "100100010100110", "11000", "1500", "10050010100110"],6))
    #print(decode_value("50010010050101015")) #
    #print(list_of_weights_to_number([500, 100, 100, 50, 10, 10, 1, 5])) #774
    #- the value of a Roman numeral is obtained by adding the values of the characters,
    #  EXCEPT when a character is followed by a higher-value character;
    #  in that case, the lower-value char is subtracted from instead of summed to
    #  the higher-value char
    pass
