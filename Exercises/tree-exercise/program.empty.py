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

    '''
    output = 0
    if tree.sx != None and tree.dx != None:
        output += 1
        
    if tree.sx != None:
        output += ex48(tree.sx)
        
    if tree.dx != None:
        output += ex48(tree.dx)
    
    return output

L = [7, [1, [4, [5, [9, None, None], None], None], [
         6, [2, None, [8, None, None]], None]], [3, None, None]]

tree1 = tree.BinaryTree.fromList(L)
print(ex48(tree1))

