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
        color = (B,G,R): background color of canvas
        height = intger: height of canvas
        width = integer: width of canvas
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

def createLine(image=None,firstPoint=None,secondPoint=None,color=(255,255,255),lineThickness=3):
    """
    Creates a lines on an image
    Arguments:
        image = 3D Numpy array; image on which line has to be created
        firstPoint = (x,y); starting point of line
        secondPoint = (x,y); ending point of line
        color = (B,G,R); color of line
        lineThickness = integer; thickness of line in pixels
    """
    # If image argument is not a numpy.ndarray
    if type(image) != type(np.ones((5,5,3))):
        # Create a black 300x300 px image
        image = createBlankCanvas()
    else:
        image = image.copy()
    # If starting point not provided
    if firstPoint == None:
        # Starting point = (0,0)
        firstPoint = (0,0)
    # If ending point not provided
    if secondPoint == None:
        # Ending point = (width,height)
        secondPoint = (image.shape[1],image.shape[0])
    # Create line
    cv2.line(image,firstPoint,secondPoint,color,lineThickness)
    # Return image
    return image

def createRectangle(image=None,topLeftPoint=None,bottomRightPoint=None,color=(255,255,255),lineThickness=3,fill=False,fillColor=None):
    """
    Creates a rectangle on an image
    Arguments:
        image = 3D Numpy array; image on which the rectangle has to be created
        topLeftPoint = (x,y); top left point of the rectangle
        bottomRightPoint = (x,y); bottom right point of the rectangle
        color = (B,G,R); color of the rectangle
        lineThickness = integer; thickness of the line in pixels
        fill = boolean; True if the rectangle is filled
        fillColor = (B,G,R); color to be filled in the rectangle
    """
    # If image argument is not a numpy.ndarray
    if type(image) != type(np.ones((5,5,3))):
        # Create a black 300x300 px image
        image = createBlankCanvas()
    else:
        image = image.copy()
    # If top left corner not provided
    if topLeftPoint == None:
        topLeftPoint = (0,0)
    # If bottom right corner not provided
    if bottomRightPoint == None:
        # bottom right point = (width,height)
        bottomRightPoint = (image.shape[1],image.shape[0])
    # If rectangle has to be filled
    if fill:
        # If fill color has not been provideed
        if fillColor == None:
            # Fill the rectangle with boundary color
            fillColor = color
        # Draw the filled rectangle
        cv2.rectangle(image,topLeftPoint,bottomRightPoint,fillColor,-1)
    # Draw the rectangle
    cv2.rectangle(image,topLeftPoint,bottomRightPoint,color,lineThickness)
    return image
    

def createSampleCross(bgColor=(0,0,0),crossColor=(255,255,255),height=300,width=300):
    """
    Creates a sample cross
    Arguments:
        bgColor = (B,G,R); background color of canvas
        crossColor = (B,G,R); color of the cross
        height = integer; height of the canvas
        width = integer; width of the canvas
    """
    # Create the canvas
    canvas = createBlankCanvas(color=bgColor,height=height,width=width)
    # Create cross on the canvas
    cross = createLine(image=canvas,
                       color=crossColor)
    cross = createLine(image=cross,
                       firstPoint=(0,cross.shape[0]),
                       secondPoint=(cross.shape[1],0),
                       color=crossColor)
    return cross