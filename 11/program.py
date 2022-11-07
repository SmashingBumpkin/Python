
def ex11(textfile):
  # Design a function ex11(textfile) such that:
  # - it receives as argument the path of a text file that contains
  #   in each line a distinct string of characters
  # - it returns a dictionary having strings as keys and string lists as
  #   values.
  # The dictionary keys are the strings contained in the 'textfile',
  # without any vowel and with the remaining characters sorted in
  # alphabetical order (for example, the string 'angel' generates the
  # key 'ngl').
  # The corresponding value of a key is the list of strings of
  # 'textfile' that generated that key (note that different strings can
  # generate the same key as for 'car', 'core' and 'cure').  The strings
  # in the list are sorted by decreasing length and, with equal lengths,
  # in alphabetical order.

  # Example: for the text file f10.txt, the function returns the
  # dictionary:
  #    {'prt': ['parto', 'porta'], 
  #    'r': ['era', 'ora'], 
  #    'pr': ['arpia', 'arpa'], 
  #    'cs': ['casa', 'cosa'], 
  #    'fll': ['follia', 'fallo', 'folla'], 
  #    'rt': ['otre', 'tre'], 
  #    'lp': ['piolo', 'polo']
  #    }
  
    with open(textfile, 'r', encoding='utf8') as fileRef:
        wordList = [i.strip().lower() for i in fileRef if i.strip() != '']
    #print(wordList)
    
    vowels = "aeiou"
    #iterate through words
    #iterate through letters in words
    newWords = []
    output = {}
    for word in wordList:
        newWord = ""
        for i in word:
            if i not in vowels:
                newWord += i
    
        try:
            output[newWord].append(word)
        except KeyError:
            output.update({newWord:[word]})
    
    return output
    

print(ex11('ft10a.txt'))
print("")
print(ex11('ft10b.txt'))
print("")
print(ex11('ft10c.txt'))