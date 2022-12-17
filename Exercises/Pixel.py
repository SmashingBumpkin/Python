# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:39:21 2022

@author: Charl
"""
class Pixel:
    '''
    A class to handle pixels made of two integers
    '''
    
    def __init__(self, row, col):
        '''
        A constructor requesting two ints
        '''
        #a method is defined in a class
        #a method always has the keyword "self"
        #if type(row) == int and type(col) == int:
        if isinstance(row, int) and isinstance(row,int):
            self.row = row
            self.col = col
        else:
            raise TypeError("A pixel position is made of 2 integers")
    def get_neighbors(self):
        s = {Pixel(self.row + y, self.col + x) for x in range(-1,2) for y in range(-1,2)
             if (y,x) != (0,0)}
        return s.difference({(self)})
    
    def __str__(self):
        return f"Pixel({self.row},{self.col})"
    
    def __repr__(self):
        return self.__str__()
    
    def distance(self, pixl):
        distX = abs(self.col - pixl.col)
        distY = abs(self.col - pixl.col)
        return int((distX**2+distY**2)**0.5)         