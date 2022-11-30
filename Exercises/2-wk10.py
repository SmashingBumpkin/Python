# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:38:26 2022

@author: Charl

write a fucntion that takes an image as a list of lists as an input and a x y pair
representing a point onto the image, and a color and fills the area between 
the border of a non-black color within the image with the color, -> fill bucket.
"""

def draw_square(img, x, y, side, col, fillCol = None):
    
    #draw horz lines
    x2 = x + side
    y2 = y + side
    width = len(img[0])
    height = len(img)
    if -1 < y < height:
        for posn in range(max(x,0), min(x2+1,width)):
            img[y][posn] = col
    if -1 < y2 < height:
        for posn in range(max(x,0), min(x2+1,width)):
            img[y2][posn] = col
    
    
    #draw vert lines
    if -1 < x < width:
        for posn in range(max(y,0),min(y2+1,height)):
            img[posn][x] = col
    
    if -1 < x2 < width:
        for posn in range(max(y,0),min(y2+1,height)):    
            img[posn][x2] = col
        
    #fill 
    if fillCol:
        for posnY in range(max(y+1,0),min(y2,width)):
            for posnX in range(max(x+1,0),min(x2,width)):
                img[posnY][posnX] = fillCol

RED = (255,0,0)
GRN = (0,255,0)
BLK = (0,0,0)
BLU = (0,0,255)
YEL = (255,255,0)
WHT = (255,255,255)
imag = [[BLU] * 100 for _ in range(66)]

draw_square(imag, 80, -5, 30, WHT, RED)
for line in imag:
    # print(line)
    pass
    
import images

images.save(imag,"squareMkr.png")