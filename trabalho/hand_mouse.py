import cv2
import autopy
import numpy as np
from hand_detector import HandDetector


W_CAM, H_CAM = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, W_CAM)
cap.set(4, H_CAM)

detector = HandDetector(maxHands=1)

while True:
    # Finding the Hand
    ret, frame = cap.read()

    if not ret:
        print('dafuk')
        break

    frame = detector.detect_hands(frame)
    im_list = detector.find_position(frame)

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
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

