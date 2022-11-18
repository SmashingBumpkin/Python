# -*- coding: utf-8 -*-
'''
A series of rectangular posters have been posted on a wall. Each
   poster is partially or totally covered by others. We say that the
   perimeter is the length of the boundary of the union of all the
   posters on the wall.  In "posters.png", for example, all
   the posters on the wall are white with blue pixels on the edges and in
   "posters1.png" the perimeter is highlighted with red pixels.

You should design a program that, provided the list of posters,
   calculates the perimeter and produces an image like "posters1.png".

Design a function ex1(textfile, pngfile) that takes as
   parameters:
   - textfile, a string with the pathname of a text file containing
     the information on the location of posters on the wall,

   - pngfile, a string with the name of the image file in PNG format
     to be produced

   and returns the perimeter of the posters as the number of red
   pixels.

The text file has one line per poster. The order of the lines corresponds   
   to the way in which they are hung on the wall. Each poster is
   represented with two pairs of integers, providing the coordinates of
   the lower left and the top right vertices of the poster, respectively.
   The values of these coordinates are given as ordered pairs, with the x
   coordinate followed by the y coordinate. For example, file "rectangles_1.txt"
   contains coordinates of the 7 posters in "posters.png".
   
The image to be saved in pngfile should have a black background,
   height h+10 and width w+10, where

   - h is the maximum x coordinate where there is at least one poster
   and
   - w is the maximum y coordinate where there is at least one poster.

The pixels of the visible edges of the posters are colored in red, if
   they belong to the perimeter. Otherwise, they are colored in green.
   Notice that a pixel is on the perimeter (and therefore in red) if in its
   neighborhood (the 8 pixels around it) there is at least one
   background pixel.

To load and save the PNG files of images you can use the load and
   save functions offered by the "images" module.

For example: ex1('rectangles_1.txt', 'test_1.png') should build a PNG
   file that is identical to "posters1.png" and return the value 1080.
   
NOTE: The timeout for this exercise is 1.5 seconds for each test.

WARNING: when uploading the file make sure it is in UTF8 encoding
   (for example edit it inside Spyder)
pytest test_01.py -v -rA
'''

import images

def ex1(text_file, pngfile):
    
    #load image data in
    rectList = []
    maxH = 0
    maxW = 0
    with open(text_file, 'r', encoding = 'utf8') as fileRef:
        for line in fileRef:
            c1, c2, c3, c4 = line.strip().split() #c1, c2 = lower left x and y,
            #c3,c4 = upper right x and y
            c1, c2, c3, c4 = int(c1), int(c2), int(c3), int(c4)
            maxH = max(maxH, c2, c4)
            maxW = max(maxW, c1, c3)
            rectList.append((c1,c2,c3,c4))
    
    maxH += 10
    maxW += 10
    
    red = (255,0,0)
    grn = (0,255,0)
    blk = (0,0,0)
    wht = (255,255,255)
    
    picArr = [[blk] * maxW for i in range(maxH)]
    grnArr = []


    
    #iterate through each entry in rectList
    #iterate over center of rectangle and write wht to the entire center
    #iterate around edge of rectangle writing grn keeping track of grn pixels
    for rect in rectList:
        edgeRH = rect[2]
        edgeLH = rect[0]
        edgeTp = rect[3]
        edgeBt = rect[1]
        #fill inside with white
        for x in range(edgeLH+1,edgeRH):
            for y in range(edgeTp+1,edgeBt):
                picArr[y][x] = wht
        
        #iterate over top & btm edge
        for posn in range(edgeLH,edgeRH+1):
            picArr[edgeTp][posn], picArr[edgeBt][posn]  = grn, grn
            grnArr.extend([(edgeTp,posn),(edgeBt,posn)])
        
        #iterate over rh and lh edge
        for posn in range(edgeTp+1,edgeBt):
            picArr[posn][edgeRH], picArr[posn][edgeLH] = grn, grn
            grnArr.extend([(posn,edgeRH),(posn,edgeLH)])
        
    
    #iterate through grn pixels and check if any surrounding pixel is blk.
    #if blk, make pixel red and count
    # for x in range(0,maxW-9):
    #     for y in range(0,maxH-9):
    count = 0
    for y,x in grnArr:
        if (picArr[y][x] == grn and
               (picArr[y+1][x+1] == blk or picArr[y-1][x-1]  == blk or 
                picArr[y+1][x-1]  == blk or picArr[y-1][x+1]  == blk or 
                picArr[y+1][x]  == blk or picArr[y-1][x] == blk or
                picArr[y][x+1]  == blk or picArr[y][x-1]  == blk)):
            
            picArr[y][x] = red
            count += 1 
    
    images.save(picArr,pngfile)
    
    return count




if __name__ == '__main__':
    print(ex1('rectangles_smol.txt', 'test_smol.png'))
    print(ex1('rectangles_1.txt', 'test_1.png'))
    pass
    # insert your examples here

