import tree


def ex48(tree):
    '''Design a function ex48(tree) such that:
    - it is recursive or uses recursive functions(s)/method(s),
    - it receives as arguments a tree that consist of nodes of type
      BinaryTree, defined in the attached tree.py library
    - it returns the number of nodes of the tree having EXACTLY two
      children
    Example: if the tree is

             7
            /\
           1  3
          / \
        4    6
       /    /
      5    2
     /     \
    9       8

    the function will return the value 2, since there are only two
    nodes with exactly two children, namely the nodes with value 7 and
    1.
    
    self.valore = V
    self.sx = sx
    self.dx = dx
    '''
    # insert here your code
    # If node has 2 children return 1 + number of 2 children of the nodes down the left path
    # + the number of 2 children of the nodes down the right 
    if tree == None:
        return 0
    
    output = 0 if tree.sx == None or tree.dx == None else 1
    
    return output + ex48(tree.sx) + ex48(tree.dx)

#trediz = [7, [1, [4, [5, [9, None, None], None], None], [
#         6, [2, None, [8, None, None]], None]], [3, None, None]]


#print(ex48(trediz))
#trediz = [9, [2, [6, [5, None, None], [5, None, None]], [6, [5, None, None], [5, None, None]]],
#  [4, [6, [5, None, None], [5, None, None]], [6, [5, None, None], [5, None, None]]]]



#print(ex48(trediz))
