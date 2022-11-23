def es10(ftext,k):
    #  Design and implement the function es10(ftext,k) that takes as input
    # a text file path and an integer k, and returns a string with length
    # k.

    # The input text file contains strings of different length (one per
    # line and each line ends with '\n'), as the file f9.txt.

    # The k characters of the string returned by the function are
    # obtained considering all the strings in ftext that are k character
    # long.  The i-th character of the string will be the character that
    # appears most frequently as the i-th character of the strings with
    # length k in ftext. In case of equal occurrences, the first
    # character in alphabetical order among the most frequent characters.
    # An empty string will be returned if the text file does not contain
    # words with length k.

    # As an example, for the text file f9.txt and k=3 the function
    # returns the string 'are' because in the f9.txt file there are the
    # following 4 strings with length 3: tre due amo or
    
    with open(ftext,'r',encoding='utf8') as fileRef:
        listWords = [i.strip().lower() for i in fileRef if len(i.strip()) == k]
    
    output = ""
    for i in range(k):
        letterFreq = {} #dict of letters and their frequencies
        for element in listWords:
            try:
                letterFreq[element[i]] = letterFreq.get(element[i],0) + 1
            except IndexError:
                print("FUCK!")
        currLtr = ''
        currFreq = 0
        for key, value in letterFreq.items():

            if value >= currFreq:
                if value > currFreq:
                    currLtr = key
                    currFreq = value
                elif key < currLtr:
                    currLtr = key
        output += currLtr    
    return output

print(es10('ft9.txt',3))
es10('ft9.txt', 3)
es10('ft9.txt', 6)
print(es10('ft9.txt', 10))