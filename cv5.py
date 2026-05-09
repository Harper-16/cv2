#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:47:00 2026

@author: dhruv
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = plt.imread("/home/dhruv/Pictures/SpongeBob.jpg")
plt.imshow(image)
plt.title("IMAGE")
plt.show()


(h,w) = image.shape[:2]
center = (w //2 , h//2)

M = cv2.getRotationMatrix2D(center,45,1.0)

rotated = cv2.warpAffine(image,M,(w,h))

plt.imshow(rotated)
plt.title("IMAGE")
plt.show()


brightness_matrix = np.ones(image.shape,dtype="uint8") * 50
brightener = cv2.add(image,brightness_matrix)

plt.imshow(brightener)
plt.title("IMAGE")
plt.show()