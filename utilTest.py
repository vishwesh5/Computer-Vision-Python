# -*- coding: utf-8 -*-
"""
Tests for util.py
Created on Tue Jun 19 15:32:13 2018

@author: vshrima
"""
from util import *

def main():
    img = createBlankCanvas(color = (255,0,0), height=500,width=300)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()