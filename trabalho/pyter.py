import cv2
import numpy as np
import os
from hand_detector import HandDetector

header_list = []
header_path = "data/headers"
header_files = os.listdir(header_path)

for file in header_files:
    img = cv2.imread(f'{header_path}/{file}')
    header_list.append(img)

# 0 -> Blue
# 1 -> Eraser
# 2 -> Green
# 3 -> No selection
# 4 -> Red

header = header_list[3] 

detector = HandDetector(max_num_hands=1)

cap = cv2.VideoCapture(0)
cap.set(3, 1400)
cap.set(4, 1000)

while True:
    # Seting the Painel
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)

    # Finding Landmarks
    frame = detector. detect_hands(frame)
    landmarks, bbox = detector.find_position(frame, draw_landmark=False)

    if len(landmarks) != 0:
        print(landmarks)
        # Tip of Fingers
        _, x1, y1 = landmarks[8]
        _, x2, y2 = landmarks[12]


    # Setting Header

    frame[0:200, 0:820] = header
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
