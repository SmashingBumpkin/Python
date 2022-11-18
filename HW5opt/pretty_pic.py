# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:07:29 2022

@author: Charl
"""
import images
pic = [[(y,x,255-x) for y in range (255)] for x in range(255*2//2)]


#print(pic[0][5])
images.save(pic,"myPic.png")