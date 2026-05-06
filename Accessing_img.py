#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:39:53 2026

@author: dhruv
"""

import cv2

image = cv2.imread('path/to/the/image')

cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image',800,500)


cv2.imshow('Loaded Image',image)

cv2.waitKey(0)

cv2.destroyAllWindows()

print(f'Image Dimentions: {image.shape}')
