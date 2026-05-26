#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:11:03 2026

@author: dhruv
"""

import os
# Suppress Qt/Wayland backend logs and warnings in the terminal
os.environ["OPENCV_LOG_LEVEL"] = "ERROR"

import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """
    Applies color modifications based on the requested filter type.
    OpenCV images use BGR channel layout (0: Blue, 1: Green, 2: Red).
    """
    filtered_image = image.copy()
    
    if filter_type == 'red_tint':
        filtered_image[:, :, 0] = 0  # Zero Blue
        filtered_image[:, :, 1] = 0  # Zero Green
        
    elif filter_type == 'blue_tint':
        filtered_image[:, :, 1] = 0  # Zero Green
        filtered_image[:, :, 2] = 0  # Zero Red
        
    elif filter_type == 'green_tint':
        filtered_image[:, :, 0] = 0  # Zero Blue
        filtered_image[:, :, 2] = 0  # Zero Red
        
    elif filter_type == 'reduced_green':
        filtered_image[:, :, 1] = (filtered_image[:, :, 1] * 0.5).astype(np.uint8)
        
    elif filter_type == 'reduced_blue':
        filtered_image[:, :, 0] = (filtered_image[:, :, 0] * 0.5).astype(np.uint8)
        
    # 'original' skips all blocks and returns the unmodified image copy
    return filtered_image

# Load your image (replace 'your_image.jpg' with your actual file path)
image = cv2.imread('/home/dhruv/Pictures/4.jpg') 

if image is None:
    print("Error: Image is not found!")
else:
    filter_type = "original"
    
    # Display system menu instructions
    print("Press the following keys to see the filter:")
    print("o: original")
    print("r: red_tint")
    print("t: blue_tint")
    print("e: green_tint")
    print("g: reduced_green")
    print("b: reduced_blue")
    print("q: quit program")

    # Interactive window loop
    while True:
        # Generate the selected filter and display the window
        display_img = apply_color_filter(image, filter_type)
        cv2.imshow('Image Viewer', display_img)
        
        # Capture keystrokes with a 10ms refresh delay
        key = cv2.waitKey(10) & 0xFF
        
        # Handle menu navigation triggers
        if key == ord('o'):
            filter_type = "original"
        elif key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('t'):
            filter_type = "blue_tint"
        elif key == ord('e'):
            filter_type = "green_tint"
        elif key == ord('g'):
            filter_type = "reduced_green"
        elif key == ord('b'):
            filter_type = "reduced_blue"
        elif key == ord('q'):
            print("Exiting application...")
            break

    # Clean up resources and close system windows
    cv2.destroyAllWindows()
