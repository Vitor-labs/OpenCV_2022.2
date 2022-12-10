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
color = (255,255,255)
brush_tickness = 15
eraser_tickness = 100
frame_canvas = np.zeros((1000,1400,3),np.uint8)

detector = HandDetector(max_num_hands=1)
xp, yp = 0, 0

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
        xp, yp = 0, 0
        # Tip of Fingers
        _, x1, y1 = landmarks[8]
        _, x2, y2 = landmarks[12]

        # checking with fingers are up
        fingers = detector.fingers_up()

        # Selection Mode: 2 fingers
        if fingers[1] and fingers[2]:
            cv2.rectangle(frame, (x1, y1-15), (x2, y2-15), color, cv2.FILLED)
            print("Selection Mode")
            #Check selection or click
            if y1 < 125:
                if 15 < x1 < 200:
                    header = header_list[0] # Blue
                    color = (255,0,0)
                elif 210 < x1 < 400:
                    header = header_list[4] # Red
                    color = (0,0,255)
                elif 405 < x1 < 580:
                    header = header_list[2] # Green
                    color = (0,255,0)
                elif 615 < x1 < 800:
                    header = header_list[1] # Eraser
                    color = (0,0,0)

        if fingers[1] and fingers[2]==False:
            cv2.circle(frame, (x1, y1), 15, color, cv2.FILLED)
            print("Drawing Mode")

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if color == (0,0,0):
                cv2.line(frame, (xp, yp), (x1, y1), color, eraser_tickness)
                cv2.line(frame_canvas, (xp, yp), (x1, y1), color, eraser_tickness)
            else:
                cv2.line(frame, (xp, yp), (x1, y1), color, brush_tickness)
                cv2.line(frame_canvas, (xp, yp), (x1, y1), color, brush_tickness)
            
            xp, yp = x1, y1

    gray = cv2.cvtColor(frame_canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame, img_inv)
    frame = cv2.bitwise_or(frame, img_inv)
    
    # Setting Header
    frame[0:200, 0:820] = header
    #frame = cv2.addWeighted(frame, 0.5, frame_canvas, 0.5, 0)

    cv2.imshow("Frame", frame)
    cv2.imshow("Canvas", frame_canvas)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
