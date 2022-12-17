# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:39:21 2022

@author: Charl
"""
import images
import Pixel
        

class Image:
    def __init__(self, height, width, bgcolor,filename = None):
        self.img = [[bgcolor]*width for _ in range(height)]
        self.h = height
        self.w = width
        self.filename = filename
    
    def save(self, filename):
        if filename:
            images.save(self.img, filename)
        elif self.filename:
            images.save(self.img, self.filename)
        else:
            raise Exception('The image requires a filename')
    
    def draw(self, o, colour):
        if isinstance(o,Pixel):
            self.img[o.row][o.col] = colour
            
i = Image(200,200,(0,0,0))