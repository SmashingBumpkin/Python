import tree

def ex6(stringSet):
    '''Design a function ex6(string_set) such that:
    - it is recursive or uses recursive function(s)/methods(s)
    - it receives a set of strings 'string_set' as argument
    - it exploits the strings in 'string_set' to reconstruct a binary
      tree in which the values of the nodes are single characters
    - it returns the reconstructed binary tree as a tree of nodes of
      type BinaryTree, defined in the attached tree.py library.
    Each string of 'string_set' represents a sequence of the values of
    the nodes traversed following the path from a leaf to the root of a
    binary tree. The tree is such that:
    - the value of each node is one single character
    - each internal node is locally ordered from left to right, namely:
      - each left child has a value smaller than that of the father
      - each right child has a value greater than that of the father
    
    Example: if the tree to reconstruct is
    
                      i     
                      |
              |-----------------|               
              h                 m 
              |                 |   
          |--------|        |------|   
          c        j        k      p
          |        |               |
       |-----|  |-----|         |-----|
       a     f  g     k         m     q    
    
    The set of strings is:
       { 'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi' }
    
    WARNING: it's FORBIDDEN to use any method defined in the class tree.py
    '''
    # insert here your code
    stringList = list(stringSet)
    root = tree.BinaryTree(stringList[0][-1])
    for string in stringList:
        ex6_helper(root, string[:-1])
    return root
    

def ex6_helper(root,string):
    try:
        if string[-1] < root.value: #left side
            if root.left == None:
                root.left = tree.BinaryTree(string[-1])
            ex6_helper(root.left, string[:-1])
        elif string[-1] > root.value: #rhside
            if root.right == None:
                root.right = tree.BinaryTree(string[-1])
            ex6_helper(root.right, string[:-1])
    except: pass
    return root

def stringer(string,letterList):
    try:
        if string[0] in letterList:
            return string[0] + stringer(string[1:],letterList)
        else:
            return stringer(string[1:],letterList)
    except:
        return ""




if __name__ == "__main__":
    ex6({ 'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi' })
    mystring = "yooo whats up guys its vsauce herea"
    mylist = ["a","b","c","d"]

    print(stringer(mystring,mylist))