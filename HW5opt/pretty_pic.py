# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:07:29 2022

@author: Charl
"""
import images

import math

def pretty_pic_maker(sizeX,sizeY):

    
    #change so size can be adjustable
    pic = [[(y,x,sizeX-x) for y in range (sizeY)] for x in range(sizeX)]
    
    
    radius = 45
    centerPicX = sizeX // 2
    centerPicY = sizeY // 2
    centerX = 2 * sizeX // 5
    centerY = sizeY // 2 -15
    radiusSq = radius**2
    tanPoint = centerX - radius//2 - 10
    heartMnR = 255
    heartMxR = 255
    heartMnG = 50
    heartMxG = 150
    heartMnB = 50
    heartMxB = 150
    gFactor = centerX - radius
    
    
    
    for x in range(centerX - radius, sizeX//2 + 1):
        upperY = int(-math.sqrt((radiusSq-(x-centerX)**2)) + centerY)
        lowerY = int(math.sqrt((radiusSq-(x-centerX)**2)) + centerY)
        altX = sizeX - x
        
        for y in range(upperY,lowerY+1):
            pic[y][x] = (x,sizeX-x,y)
            pic[y][altX] = (altX,sizeX-altX,y)
        
        if x == tanPoint:
            tanGrad = -(x-centerX)/(lowerY-centerY)
            tanC = lowerY - tanGrad*x
        
        if x > tanPoint:
            lowerTanY = int(tanGrad*x+tanC)
            for y in range(lowerY,lowerTanY+1):
                r = heartMnR
                
                pic[y][x] = (x,sizeX-x,y)
                pic[y][altX] = (altX,sizeX-altX,y)
        
        #equation for tangent to circle
        #change colour to be pretty
        
        
    
    #print(pic[0][5])
    images.save(pic,"myPic.png")
    
sizeX = 255
sizeY = 255

pretty_pic_maker(sizeX,sizeY)