# -*- coding: utf-8 -*-
"""
Tests for util.py
Created on Tue Jun 19 15:32:13 2018

@author: vshrima
"""
from util import *

def main():
    YELLOW = (0,255,255)
    
    # Create a blue canvas of size 500X500
    canvas = createBlankCanvas(color = (255,0,0), height=500,width=500)
    
    # Create a line
    image = createLine(lineThickness=10)
    
    # Create a yellow cross
    cross = createSampleCross(crossColor=YELLOW)
    
    cv2.imshow("Canvas",canvas)
    cv2.waitKey(0)
    cv2.imshow("Line", image)
    cv2.waitKey(0)
    cv2.imshow("Cross",cross)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()