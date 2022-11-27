# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 11:48:33 2022

@author: Charl
"""
def max_width_el(M):
    return max(max(len(str(el)) for el in row) for row in M)

def print_matrix(M):
    w = max_width_el(M) + 1
    print(w)
    s = "{:"+str(w)+"}"
    s = s*len(M[0])
    
    for row in M:
        print(s.format(*row))
        
mat = [[1,2,3,4,5],[1,1,34,5,6],[1,5,4,6,6]]
print_matrix(mat)


def paint_bkt(img, y, x, col):
    original = img[y][x]
    #check the 4 points around the yx
    #add any points that are original to the set
    #colour the central point and remove from the set
    
    pointSet = set([(y,x)])
    while len(pointSet) > 0:
        y, x = pointSet.pop()
        img[y][x] = col
        for y,x in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:#
            # print(y,x)
            try:
                if img[y][x] == original:
                    pointSet.add((y,x))
            except: 
                pass
        
paint_bkt(mat, -1, -1, "cheese")
print_matrix(mat)

import images

myImage = images.load("output_end_00.png")
paint_bkt(myImage,1,1,(255,255,0))
images.save(myImage,"myImg.png")
