#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A real estate owner in California, Lida,  inherits a piece of land. The
land is modeled as a rectangular patch of variable size. The patch of
land is represented with an image (list of lists).

To make some money out of it, she can decide to lease the land to
other people. To do that, she may decide to divide the land into four
other patches. In case she decides to not lease the land, no further
sub-patches are created. On the contrary, in case the land is divided
into four sub-patches, some colored marks (straight lines) on the land
are drawn with a thickness of one pixel to mark the private properties
that are created. There is no prior knowledge of how and where the
lines will be drawn, nor which colors will be used (there is no
regular pattern).  The only knowledge is that the lines are
axis-aligned.

The four leassees that receive the sub-patches of land may take the
same decision that Lida took before them. They may decide to sublease
once again their small patch to others or, else, to keep the land all
for themselves. The decision for each lessee is independent of each
other. For example, lessee #1 may decide to sublease again, while
lessee #2 may keep the land for himself, etc, whereas lessee #3 and #4
may subdivide. If they sublease and divide, they follow the same
policy of dividing in four parts and setting their boundaries with
line drawing but obviously with a different splitting position of
their land. For sure, they will be using a color that is different
from the colors used by Lida yet they will be using the same color
among them, at the same level of splitting.

NOTE: An important note is that the color of the background (bg) of
the land is not given (i.e. we do not know if the bg is black, or
white or blue etc) but we do know that the background land color is
NOT used by any of the lessees ever to mark their boundaries.

The subdivision process could continue until when all the lessees in
all patches stop subdividing their land. This process described here
leads us to the image that is taken as input to a program.

NOTE: You can assume that the smallest possible rectangular patch has
the shortest side of two pixels in length.

Think well about the problem and once you are sure of a solution,
design on the paper (this "design" needs be then described into the
pseudo code part) and then implement a program ex1(input_file,
output_file) which:
  - reads the file indicated by the parameter 'input_file'
    using the 'images' library 
  - preprocesses the image--if needed--and implements a
    *recursive* function to solve the requirements below.
  - counts all the patches of lands that are in the image and returns
    the number of patches. It should return the number of rectangles
    with the color of the background that is present in the
    image. Regarding the simplified case below:

        # +++++++++++++++++++
        # +-1-|-2-|---------+
        # ++++a+++|----5----+
        # +-3-|-4-|---------+
        # ++++++++b++++++++++
        # +-------|--7-|-8--+
        # +---6---|++++c+++++
        # +-------|-10-|-9--+
        # +++++++++++++++++++
  
    the approach should return 10 as the total number of patches. (The
    numbers in the simplified case above are just added for the sake
    of clarity. The image data does not contain those numbers,
    obviously).
  - finally, given that the real estate registry needs to book-keep
    all the boundaries created, the program shall build an output
    image of the size of 1x(N+1). The image encodes as the first pixel
    the color of the background. Then it should encode "the color
    hierarchy" of all the N colors used to subdivide the patches of
    land. The hierarchy is defined by "visiting" first in depth the
    upper left patch, then upper right patch, then lower left, and
    lower right. The colors should be stored in reverse order with
    respect to the "visit" made. With reference to the previous
    semplified case, assuming a boundary color is described with a
    letter, the output image should contain:
             out_colors = bg b c a


    Another case a bit more complex:

         +++++++++++++++++++++++++++++++++++++
         +-1-|-2-|---------|--------|--------+
         ++++a+++|----5----|---6----|----7---+
         +-3-|-4-|---------|--------|--------+
         ++++++++b+++++++++|++++++++c+++++++++
         +-------|--9-|-10-|--------|--------+
         +--8----|++++d++++|---13---|---14---+
         +-------|-11-|-12-|--------|--------+
         ++++++++++++++++++e++++++++++++++++++
         +-15|-16|---------|--------|-21|-22-+
         ++++f+++|---19----|---20---|+++g+++++
         +-17|-18|---------|--------|-23|--24+
         ++++++++h+++++++++|++++++++l+++++++++
         +-------|-26-|-27-|--------|-31-|-32+
         +--25---|++++m++++|---30---|+++n+++++
         +-------|-29-|-28-|--------|-33-|-34+
         +++++++++++++++++++++++++++++++++++++

         n_rect is: 34
         the color hierarchy is:
         bg e l n g h m f c b d a
         
         
         +++++++++++++++++++++++++++++++++++++
         +-1-|-2-|---------|--------|--------+
         ++++c+++|----5----|---6----|----7---+
         +-3-|-4-|---------|--------|--------+
         ++++++++b+++++++++|++++++++b+++++++++
         +-------|--9-|-10-|--------|--------+
         +--8----|++++c++++|---13---|---14---+
         +-------|-11-|-12-|--------|--------+
         ++++++++++++++++++a++++++++++++++++++
         +-15|-16|---------|--------|-21|-22-+
         ++++c+++|---19----|---20---|+++c+++++
         +-17|-18|---------|--------|-23|--24+
         ++++++++b+++++++++|++++++++b+++++++++
         +-------|-26-|-27-|--------|-31-|-32+
         +--25---|++++c++++|---30---|+++c+++++
         +-------|-29-|-28-|--------|-33-|-34+
         +++++++++++++++++++++++++++++++++++++

         n_rect is: 34
         the color hierarchy is:
         bg a b c c b c c b b c c
         NOTE: it is forbidden to import/use other libraries or open files
      except the one indicated

NOTE: The test system recognizes recursion ONLY if the recursive
      function/method is defined in the outermost level.  DO NOT
      define the recursive function within another function/method
      otherwise, you will fail all the tests.
      
      pytest test_01.py -v -rA
"""

import images


def ex1(input_file, output_file):
    # write your code here
    inputImage = images.load(input_file)
    background = inputImage[0][0]
    colours = [background]
    colours.extend(dividing_colour_returner(inputImage, background))
    images.save([colours], output_file)
    squares = (len(colours) - 1)*3 + 1
    # return squares
    return 1

def dividing_colour_returner(inputImage, background):
    height = len(inputImage)-1
    width = len(inputImage[0])-1
    landSplit = False
    output = []
    
    for y in range(height, 0, -1): # Iterate across image
        pixelColour = inputImage[y][width]
        if pixelColour != background and len(set(inputImage[y])) == 1:
            splitColour = inputImage[y][width]
            landSplit = True
            ySplit = y
            break
    
    if landSplit:
        xSplit = inputImage[0].index(splitColour)
        output.append(splitColour)
        subimageNW = [line[0:xSplit] for line in inputImage[0:ySplit]]
        subimageNE = [line[xSplit+1:] for line in inputImage[0:ySplit]]
        subimageSW = [line[0:xSplit] for line in inputImage[ySplit+1:]]
        subimageSE = [line[xSplit+1:] for line in inputImage[ySplit+1:]]
        subimages = [subimageSE, subimageSW, subimageNE, subimageNW]
        for subimage in subimages:
            output.extend(dividing_colour_returner(subimage, background))
    return output

if __name__ == '__main__':
    # write your tests here
    #ex1('puzzles\empty02.in.png','outlol.png')
    # out = ex1('puzzles\small01.in.png','outlol.png')
    # print(out)
    pass
