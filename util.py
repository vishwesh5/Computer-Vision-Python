# -*- coding: utf-8 -*-
"""
Utility functions

Created on Tue Jun 19 15:22:41 2018

@author: vshrima
"""

import cv2
import numpy as np

def createBlankCanvas(color=(0,0,0),height=300,width=300):
    """
    Creates a blank canvas
    Arguments:
        Color = (B,G,R): background color of canvas
        Height = intger: height of canvas
        Width = integer: width of canvas
    """
    # Separate colors
    blue,green,red = color
    # Create a temp canvas
    img = np.ones((height,width,3),dtype='uint8')
    # Change colors of canvas
    img[:,:,0] = blue
    img[:,:,1] = green
    img[:,:,2] = red
    return img