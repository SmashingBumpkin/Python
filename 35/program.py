 
import os


def es35(dir1, words):
    """Design the function  es35(dir1, word_set), that takes as inputs:
        dir1:   the path of a directory
        word_set:  a set of words (character strings between 'a' and 'z')
    and does the following:

    it searches in dir1 for files with extension .txt that contain any
    string present in word_set and returns a dictionary of the found
    words. The function does not considers dir1 subdirectories.  The
    returned dictionary only contains the words actually found within
    the .txt files in dir1 and the attribute of each key is a tuple of
    two integers. The first element of the tuple is the total number
    of times the word can be found in dir1 .txt files. The second
    element of the tuple is the number of different dir1 .txt files in
    which the word can be found.

    A word is a sequence made of characters between 'a' and 'z'.  All
    dir1 .txt files contain only words separated by spaces, tabs or
    new line characters, namely, there are no capital letters or punctuation
    marks.

    """
    #find files in folder
    #iterate through each file
    #if txt, search file for words
    #if find word, add word to a list as a tuple of (word, file)
    files = os.listdir(dir1)
    print(files)
    myList = []
    
    for file in files:
        if file[-4:] == ".txt":
            with open(dir1 + "/" + file, 'r', encoding = "utf8") as fileref:
                fullText = "".join(fileref.readlines())
                myList.append(helper(fullText, words))
                
    masterDict = dict()
    for key in myList[0].keys():
        occurences = 0
        files = 0
        for subDict in myList:
            occurences += subDict[key]
            if subDict[key] != 0:
                files += 1 
        if occurences != 0:
            masterDict[key] = (occurences, files)
    
    return masterDict
            
    
def helper(text, words):
    text = text.split()
    fileDict = dict()
    for word in words:
        fileDict[word] = text.count(word)
    print(fileDict)
    return fileDict
    
    

    

if __name__ == "__main__":
    print(es35('A', {'a', 'b', 'c', 'd'}))