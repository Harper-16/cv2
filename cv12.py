#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:09:12 2026
@author: dhruv
"""

import cv2
import mediapipe as mp

# Initialize Legacy MediaPipe Solutions Objects
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

print("Hand Tracking Started! Press 'q' to quit.")


# =====================================================================
# GESTURE DETECTION FUNCTION (FROM IMAGES 1 & 2)
# =====================================================================
def detect_gesture(hand_landmarks):
    landmarks = hand_landmarks.landmark
    tip_ids = [4, 8, 12, 16, 20]
    pip_ids = [2, 6, 10, 14, 18]
    extended = 0

    # Thumb detection logic
    if abs(landmarks[tip_ids[0]].x - landmarks[pip_ids[0]].x) > 0.04:
        extended += 1

    # Finger detection loop
    for i in range(1, 5):
        if landmarks[tip_ids[i]].y < landmarks[pip_ids[i]].y:
            extended += 1

    # Gesture state translation logic
    if extended >= 4:
        return "Open"
    elif extended <= 1:
        return "Closed Fist"
    else:
        return "Partial"


# =====================================================================
# MAIN PROCESSING LOOP (FROM IMAGES 3 & 4)
# =====================================================================
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    # Process the frame through MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    gesture = "No hand detected"
    hand_label = ""

    # Updated inner landmark evaluation loop structure from Image 4
    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            
            # Extract Left / Right classification tag label string
            hand_label = results.multi_handedness[idx].classification[0].label
            
            # Call your function to calculate the gesture name
            gesture = detect_gesture(hand_landmarks)
            
            # Draw the standard wireframe lines over the hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Highlight individual fingertips with solid magenta circles
            fingertip_ids = [4, 8, 12, 16, 20]
            for tip_id in fingertip_ids:
                lm = hand_landmarks.landmark[tip_id]
                x, y = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (x, y), 10, (255, 0, 255), cv2.FILLED)

    # Render the classification metadata on the interface screen matrix
    display_text = f"Hand: {hand_label} | Gesture: {gesture}" if hand_label else f"Gesture: {gesture}"
    cv2.putText(
        frame, 
        display_text, 
        (50, 50), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        1, 
        (0, 255, 0), 
        2, 
        cv2.LINE_AA
    )

    # Render frame interface loop display
    cv2.imshow('Hand Tracking & Gesture Detection', frame)
    
    # Break out of execution instantly if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
