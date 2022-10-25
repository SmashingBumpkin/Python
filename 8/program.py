'''Two words can be merged if the first word has a suffix of at least
   two characters that is equal to the prefix of equal length of the
   second word.
   The result of the fusion is the word obtained by concatenating the
   first word with the second thanks to the part in common.
   For example:  
   - the two words 'candela' and 'elastico' can merge thanks to the
     suffix 'ela' of 3 characters, and the result of the fusion is the
     word 'candelastico'.
   - the words 'Angelo' and 'gelo' can merge thanks to the suffix
     'gelo', the word resulting is 'Angelo'.
   - the words 'aaaaa' and 'aaab' can merge in different ways: 
     - thanks to the suffix 'aa' you get the fusion 'aaaaaab'. 
     - thanks to the suffix 'aaa' you get the fusion 'aaaaab'.

    Define function es8(word_set) that, given a set of words, returns
    the list with all the possible words resulting from a fusion of
    two words of word_set. Any duplicate in the list is removed. The
    list is sorted in alphabetical order.
  
    For example:

    - if word_set={'aaaa', 'acde', 'aacd', 'aaaade'}, the function
      returns the list:

     ['aaaaaade', 'aaaaade', 'aaaacd', 'aaaade', 'aacde'] 
     thanks to the following fusions:
     'aaaa'  'aaaade' ---> 'aaaaaade' with suffix 'aa'
     'aaaa'  'aaaade' ---> 'aaaaade'  with suffix 'aaa'
     'aaaa'  'aaaade' ---> 'aaaade'   with suffix 'aaaa'
     'aaaa'  'aacd'   ---> 'aaaacd'   with suffix 'aa'
     'aacd'  'acde'   ---> 'aacde'    with suffix 'acd'

'''
def es8(wordList):
  output = []
  for wordA in wordList:
      for wordB in wordList:
          if wordA == wordB:
              continue
          length= min(len(wordA),len(wordB))
          for i in range(2,length+1):
              if wordA[-i::] == wordB[:i:]:
                  mashup = wordA + wordB[i::]
                  if mashup not in output:
                      output.append(mashup)
  output.sort()
  return output
                  

#for all words to all other words, compare end of word A to start of word B
    #compare 2 letters, then iterate up  until the min of the 2 word lengths
    #if there is a match, and it's not already on the list, add it
listWords = {'aaaa', 'acde', 'aacd', 'aaaade'}
print(es8(listWords))