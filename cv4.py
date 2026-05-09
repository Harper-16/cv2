#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:21:08 2026

@author: dhruv
"""

import cv2 
import matplotlib.pyplot as plt

image = plt.imread("/path/to/image")

image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("RGB IMAGE")
plt.show()

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

plt.imshow(gray_image,cmap ="gray")
plt.title("GRAY IMAGE")
plt.show()

cropped_image = image[100:200,300:400]

cropped_rgb = cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)

plt.imshow(cropped_rgb)
plt.title("CROPPED IMAGE")
plt.show()
