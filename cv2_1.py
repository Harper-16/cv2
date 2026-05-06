#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:39:53 2026

@author: dhruv
"""

import cv2

main_image = cv2.imread('path/to/image')

# =============================================================================
# grayscale
# =============================================================================
gray_image = cv2.cvtColor(main_image,cv2.COLOR_BGR2GRAY)

# resizeing it
image = cv2.resize(gray_image,(224,224))

# =============================================================================
# display settings
# =============================================================================
cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image',800,500)


# =============================================================================
# loading img
# =============================================================================
cv2.imshow('Loaded Image',image)

key = cv2.waitKey(0)

cv2.destroyAllWindows()

if key == ord('s'):
    file_name = 'grayscale_resized_img.jpg'
    cv2.imwrite(file_name,image)
    print(f"Image has been saved {file_name}")
else:
    print("Image not saved")

# =============================================================================
# print dimentions
# =============================================================================
print(f'Image Dimentions: {image.shape}')
