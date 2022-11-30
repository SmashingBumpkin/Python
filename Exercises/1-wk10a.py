#########       BINARY TREES        #########
"""
Binary/n-ary

binary tree has up to 2 children

n-ary has any number of children

Trees are inherently recursive

3 way to print binary tree = 
pre-visit
in-visit
post-visit
"""

class BinaryTree:
    node = None
    left = None
    right = None
    level = 0
    
    def __init__ (self, nodeVal):
        self.node = nodeVal
        self.level = 0
        
    def setRight(self, inRH):
        self.right = inRH
        inRH.level = self.level + 1
    
    def setLeft(self, inLH):
        self.left = inLH
        inLH.level = self.level + 1
    
    def __repr__(self):
        ###     PRE-VISIT     ###
        # res = '\t' * self.level + str(self.node) + '\n'
        
        # if self.left is not None:
        #     res += '\t' * self.level + str(self.left)
        
        # if self.right is not None:
        #     res += '\t'*self.level + str(self.right)
        # return res
        
        # return (str(self.node) +"\n"
        #         +" /      \ \n" +
        #         str(self.left.node) + "\t" + str(self.right.node))
        ###     IN-VISIT     ###
        res = ""
        
    
N0 = BinaryTree("Phil")
N1 = BinaryTree("dirty dez")
N2 = BinaryTree("Polly")
N3 = BinaryTree("Paul")
N4 = BinaryTree("dirty daz")
N5 = BinaryTree("Pol")
N6 = BinaryTree("Philly")
N7 = BinaryTree("dirty bez")
N8 = BinaryTree("Pauly")


N0.setLeft(N1)
N0.setRight(N2)
N1.setLeft(N3)
N1.setRight(N4)
N2.setLeft(N5)
N2.setRight(N6)
N3.setLeft(N7)
N3.setRight(N8)


print(N0)
# print(N1)
# print(N2)
# print(N3)