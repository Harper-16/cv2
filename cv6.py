#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:21:24 2026

@author: dhruv
"""

import cv2 
import matplotlib.pyplot as plt

image_path = "/path/to/image"

image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

height, width , _=image_rgb.shape

rect1_width ,rect1_height= 150,150

top_left_pos = (20,20)
bottom_right_pos = (top_left_pos[0]+rect1_width,top_left_pos[1]+rect1_height)

cv2.rectangle(image_rgb,top_left_pos,bottom_right_pos,(0,255,255),3)

rect2_width ,rect2_height= 200,150

top_left_pos1 = (width-rect2_width-20,height- rect2_height-20)
bottom_right_pos1 = (top_left_pos1[0]+rect2_width,top_left_pos1[1]+rect2_height)

cv2.rectangle(image_rgb,top_left_pos1,bottom_right_pos1,(255,255,0),3)


center1_x = top_left_pos[0] +rect1_width //2
center1_y = top_left_pos[1]+ rect1_height //2

cv2.circle(image_rgb,(center1_x,center1_y),15,(255,0,255),-1)


center2_x = top_left_pos1[0] +rect2_width //2
center2_y = top_left_pos1[1]+ rect2_height //2

cv2.circle(image_rgb,(center2_x,center2_y),15,(255,0,255),-1)

cv2.line(image_rgb,(center1_x,center1_y),(center2_x,center2_y),(0,255,0),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Region 1', (top_left_pos[0], top_left_pos[1] - 10), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region 2', (top_left_pos1[0], top_left_pos1[1] - 10), font, 0.7, (255, 255, 0), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'CENTER 1', (center1_x - 40, center1_y + 40), font, 0.7, (255, 0, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'CENTER 2', (center2_x - 40, center2_y + 40), font, 0.7, (255, 0, 255), 2, cv2.LINE_AA)



plt.imshow(image_rgb)

plt.axis('off')

plt.show()


