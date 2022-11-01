

def es16(s, k):
    '''Design  function es16(s,k) that receives as input
    - a string s of characters 
    - an integer k 

    and returns the list with the different substrings of s made of
    exactly k distinct characters. The list of substrings are ordered
    by decreasing lengths and, for equal lengths, in alphabetical
    order. The list should not contain duplicates.

    Remember that a substring of s is what you can get from s by
    eliminating 0 or more characters from the left end and 0 or more
    characters from the right end.

    For example,
    - if  s='aabbb' and k=1
    - the function returns the list ['bbb', 'aa', 'bb', 'a', 'b']

    - if  s='bcafedg' and k=3
    - the function returns the list ['afe', 'bca', 'caf', 'edg', 'fed']

    - if s='ccaabbdd' and k=3
    - the function returns the list 
      ['aabbdd', 'ccaabb', 'aabbd', 'abbdd', 'caabb', 'ccaab', 'abbd', 'caab']

    '''
    #Start with i = 0 and j = 0, output = [] and current characters to []
    #iterate through string from 0 to length - k
    #from each character, extend window right until there are k different characters
    #
    #add string to list (if it's not already there)
    #keep extending + adding until # of characters is greater than k
    """
    j, output, curChar, curStr = 0, [], [], ""
    for i in range(len(s) - k+1):
        while len(curChar) <= k and i < len(s):
            curStr += s[i]
            if s[i] not in curChar:
                curChar.append(s[i])
            if len(curChar) == k and curStr not in output:
                output.append(curStr)
            i += 1
        curChar, curStr= [], ""
    output.sort()
    output.sort(key=len, reverse = True)
    return output
    """
    
    output, curStr, curChar = [],  "", set()
    
    for i in range(len(s) - k+1):
        while len(curChar) <= k and i < len(s):
            curChar.add(s[i])
            curStr += s[i]
            if len(curChar) == k and curStr not in output:
                output.append(curStr)
            i += 1
        curStr = ""
        curChar.clear()
    output.sort()
    output.sort(key=len, reverse = True)
    return output

s='bcafedg'
k=3
print(es16(s,k))