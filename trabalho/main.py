import cv2
import numpy as np
import HandTrackingModule as htm


W_CAM, H_CAM = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, W_CAM)
cap.set(4, H_CAM)

detector = htm.HandDetector(maxHands=1)

while True:
    # Finding the Hand
    ret, frame = cap.read()

    if not ret:
        print('dafuk')
        break

    frame = detector.findHands(frame)
    im_list, bbox = detector.findPosition(frame)

    # Geting the tip of the index and middle finger
    # Checking which fingers are up
    # Index Finger -> Moves the mouse
    # Converting coordinates
    # Smoothing Values
    # Moving Mouse
    # Index & Middle Finger -> Click
    # Find distance between two fingers
    # if is short -> click

    cv2.imshow('frame', frame)
    cv2.waitKey(1)

