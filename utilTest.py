# -*- coding: utf-8 -*-
"""
Tests for util.py
Created on Tue Jun 19 15:32:13 2018

@author: vshrima
"""
from util import *
def main():
    
    # Create a black canvas of 300px*300px size
    img_black_default = createBlankCanvas()
    
    # Create a yellow canvas of 500px*200px size
    img_yellow_500_200 = createBlankCanvas(color=(0,255,255),height=500,width=200)
    
    # Plot a black line on yellow canvas
    img_black_line = createLine(image=img_yellow_500_200,color=(0,0,0))
    # Plot a white line on black canvas
    img_white_line = createLine(image=img_black_default)
    
    # Create a white cross on black canvas
    whiteCross = createSampleCross()
    # Create a blue cross on white canvas
    blueCross = createSampleCross(bgColor=(255,255,255),crossColor=(255,0,0))

    # Create a blue rectangle filled with yellow
    blue_rect_yellow_fill = createRectangle(image=img_black_default,fill=True,fillColor=(0,255,255),lineThickness=3,color=(255,0,0),bottomRightPoint=(100,100),topLeftPoint=(50,50))
    # Create a yellow rectangle filled with blue
    finalImage = createRectangle(image=blue_rect_yellow_fill,topLeftPoint=(100,100),lineThickness=5,color=(0,255,255),fillColor=(255,0,0),fill=True)
    
    # Display results
    cv2.imshow("Blank canvas", img_black_default)
    cv2.waitKey(0)
    cv2.imshow("Yellow canvas", img_yellow_500_200)
    cv2.waitKey(0)
    cv2.imshow("Black canvas with white line", img_white_line)
    cv2.waitKey(0)
    cv2.imshow("Yellow canvas with black line", img_black_line)
    cv2.waitKey(0)
    cv2.imshow("White cross on black canvas", whiteCross)
    cv2.waitKey(0)
    cv2.imshow("Blue cross on white canvas", blueCross)
    cv2.waitKey(0)
    cv2.imshow("Blue rectangle filled with yellow", blue_rect_yellow_fill)
    cv2.waitKey(0)
    cv2.imshow("Final image",finalImage)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()