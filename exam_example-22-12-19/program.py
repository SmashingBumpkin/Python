#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER
 3) Change the directory name examPY in your matriculation number

To pass the exam you have to:
    - solve at least 3 func problems and
    - solve at least 1 rec problem
    - get a score greater or equal tu 18

The final score is the sum of the solved problems.
"""
name       = "NAME"
surname    = "SURNAME"
student_id = "MATRICULATION NUMBER"

#########################################

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################

# %%  ---- FUNC1 ----
''' func1: 2 points

A dictionary D is given as input. D has integer keys and its values are
lists of integers with repetitions.

D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6], 0: [1, 2, 1]}

Write the function func1(D) that builds and returns the
list W that contains the values obtained by taking, for each key in D,
the corresponding item from the list associated to the key.
The returned list must be sorted in reverse order.

The above example should return:

    W = [3, 5, 1]

'''

def func1(string_list: dict):
    return [value[key] for key, value in string_list.items()]


# %%  ---- FUNC2 ----
''' func2: 2 points

Implement the func2(list_all, list_rm) function to destructively delete
from list_all all the integers that are contained in list_rm.

Example: if  list_all = [2, 3, 4, 4, 4, 3, 4, 5, 6]
         and list_rm = [4, 3, 2, 5]
         list_all must be destructively changed to [6],
         as all values except 6 have been deleted.

'''

def func2(list_all, list_rm):
    for item in list_all[:]:
        if item in list_rm:
            list_all.remove(item)


# %%  ---- FUNC3 ----
'''  func3: 2 points

Implement the func3(strList) that:
- takes as input a list of strings
- computes the sum of the ascii codes of the characters of each string,
obtaining an integer value for each string;
- returns the maximum of the integer values.

'''

def func3(strList):
    # YOUR CODE HERE
    integerList = []
    for string in strList:
        string.split()
        stringTotal = 0
        for character in string:
            stringTotal += ord(character)
        integerList.append(stringTotal)
    return max(integerList)


# %%  ---- FUNC4 ----
""" func4: 6 points

    Implement the function  func4(grid, path) that takes as arguments:
    - grid: a 2 dimensional matrix represented as lists of lists
    - path: a string
    The function returns a list.

    The path string represents a series of moves in the grid.
    We start from the 0,0 top/left corner.
    The possible moves are: 'L' (left), 'R' (right), 'U' (up), 'D' (down), 'S' (stay).
    There cannot exist in path any move bringing you out of the grid.
    The function returns the list of values encountered by moving in the grid
    by following the path movements.

    Example:
        Supposing the grid is:
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 0, 1, 2]]
        path = 'RRD' -> [2, 3, 7]
        path = 'RRDDL' -> [2, 3, 7, 1, 0]
        path = 'DDRLRL' -> [5, 9, 0, 9, 0, 9]

"""

def func4(grid, path):
    # WRITE HERE YOUR CODE
    moveDict = {
        "L": (0,-1),
        "R": (0, 1),
        "U":(-1, 0),
        "D": (1, 0),
        "S": (0, 0)}
    output = []
    y, x = 0, 0
    for character in path:
        y += moveDict[character][0]
        x += moveDict[character][1]
        output.append(grid[y][x])
    return output
        
    


# %%  ---- FUNC5 ----
""" func5: 6 points

Write a function func5(points) that takes a list of (x,y) coordinates
of N points in the Cartesian plane and returns a tuple of
two elements ((X, Y), R). Each point is a pair of integers. For each pair of
2 consecutive points we consider the pair's barycenter and radius.
We define:
- "barycenter" of a pair of points as the point (X,Y) obtained by
calculating the average the points' x and y coordinates;
- "radius" R of a pair of points as the distance of the point furthest
farthest from the pair's barycenter.

The function must return the barycenter (X, Y) and the radius R of the pair of
points with the smallest radius, that is, a tuple in which the first element is
(X,Y), the coordinates of the pair barycenter, and the second one is the radius R.
All values should be reported to an accuracy of 3 decimal places.

  - NOTE: It can be assumed that for each test there is a unique pair of
    points that satisfies the requirement
  - NOTE: The distance between 2 points (x1, y1) and (x2, y2)
    is the Euclidean distance: sqrt[(x1-x2)² + (y1-y2)²]

"""

def func5(points):
    # WRITE HERE YOUR CODE
    barycenters, radii = [], []
    for index in range(len(points)-1):
        pointA = points[index]
        pointB = points[index+1]
        barycenter = ((pointA[0]+pointB[0])/2,(pointA[1]+pointB[1])/2)
        barycenters.append(barycenter)
        radii.append(((barycenter[0]-pointA[0])**2 + (barycenter[1]-pointA[1])**2)**0.5)
    position = radii.index(min(radii))
    return ((round(barycenters[position][0],3),round(barycenters[position][1],3)),
            round(radii[position],3))


# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex1: 6 points
    implement the ex1(root, depth) function, recursive or using recursive functions,
    with arguments:
    - root:  the root of a binary tree
    - depth: an integer
    The tree is made of instances of the BinaryTree class defined in tree.py.
    The function should return the product of the sum of all left child nodes
    times the sum of all right child nodes that are at the given depth in the
    tree (assuming the root is at depth 0).

    Example:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    If the tree is the left one and depth=2, the function returns
    9*(1+3)=36.
    If the tree is the right one and depth=3, the function returns
    (2+8+2)*(-1+1+3+9)=144.
    
"""

from tree import BinaryTree

def ex1(root, depth):
    return(ex1_helper(root, depth-1, 0))
    pass

def ex1_helper(root, targetDepth, currentDepth):
    
    if targetDepth == currentDepth:
        left = root.sx.valore if root.sx != None else 0
        right = root.dx.valore if root.dx != None else 0
        return (left, right)
    else:
        left = 0
        right = 0
        for child in [root.sx, root.dx]:
            (tempL, tempR) = ex1_helper(child, targetDepth, currentDepth+1)
            left += tempL
            right += tempR
        return (left, right)
    

# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex2: 6 points
    Implement the ex2(dirin, dirout, depth) function, recursive or using recursive
    functions or methods, that receive the arguments:
    - dirin:  the path of an input directory
    - dirout: the path of an output directory
    - depth:  an integer
    The function must build inside the dirout directory a file for each text
    file (.txt) found in dirin or in one of its subdirectories at the same depth
    (assuming dirin is at depth 0).
    The directory structure containing the txt files must be replicated
    under dirout.

    Each txt file created under dirout must contain the same content of the
    dirin file.
    The function returns the total number of alphabetical characters
    written in the text files created under dirout.

    NOTICE 1: you could find useful the functions: os.listdir, os.path.join,
    os.path.isfile, os.mkdir, os.path.exists ...
    NOTICE 2: it is forbidden to use the os.walk function
        
"""
import os

def ex2(dirin, dirout, depth):
    os.mkdir(dirout)
    return ex2_helper(dirin, dirout, depth, 0)
    # WRITE HERE YOUR CODE
    pass

def ex2_helper(dirin, dirout, depth, currDepth):
    count = 0
    for element in os.listdir(dirin):
        elementIn = dirin + "/" + element
        elementOut = dirout + "/" + element
        if (currDepth <= depth and
            os.path.isdir(elementIn)):
            os.mkdir(elementOut)
            count += ex2_helper(elementIn, elementOut, depth, currDepth+1)
        elif (os.path.isfile(elementIn) and
              elementIn[-4:] == ".txt"):
            with open(elementIn,'r',encoding='utf8') as fileref:
                filecontents = fileref.readlines()
            with open(elementOut, 'w', encoding = 'utf8') as fileref:
                for line in filecontents:
                    fileref.write(line)
                    for char in line:
                        if char.isalpha():
                            count += 1
    return count
    


###################################################################################
if __name__ == '__main__':
    # Place your tests here
    D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6], 0: [1, 2, 1]}
    print(func1(D))
    list_all = [2, 3, 4, 4, 4, 3, 4, 5, 6]
    list_rm = [4, 3, 2, 5]
    func2(list_all, list_rm)
    print(list_all)
    string1 = "ijsdlkjnbkjdfglodhjfgdhjfgl;dsfol;gjl;djfgl;f"
    string2 = "mfgflgl"
    string3 = "ol;ksgjdfnol;dfgl;kdjfgl;dkjsfg';pjdf.lgkhdol;fgjh;gjf;dpfgj;gdjfolghdosfhglkfgdjhdolfgodsfg"
    print(func3([string1, string2, string3]))
    grid = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 0, 1, 2]]
    path = 'RRD'# -> [2, 3, 7]
    path = 'RRDDL'# -> [2, 3, 7, 1, 0]
    path = 'DDRLRL'# -> [5, 9, 0, 9, 0, 9]
    print(func4(grid,path))
    points = [(3,4),(7,10),(3,2),(5.6,4)]
    print(func5(points))
    lista = [1, [2, None,
                    [5, None, None],
                ],
                [3, [4, None, None],
                    [5, None, None],
                ],
            ]
    albero  = BinaryTree.fromList(lista)
    # print(albero)
    print(ex1(albero,2))
    print(ex2("ex3", "ex3Out", 3))
    