import cv2
import math
import mediapipe as mp


class HandDetector():
    def __init__(self, static_image_mode=True,
                max_num_hands=2):
        
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
                
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            self.static_image_mode,
            self.max_num_hands)
        self.mp_draw = mp.solutions.drawing_utils

        self.tip_idx = [4,8,12,16,20]


    def detect_hands(self, frame, draw_landmarks=True):
        """
        Returns the hand detected frame as cv2.Mat
        """
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if  self.results.multi_hand_landmarks:
            for hand_landmark in  self.results.multi_hand_landmarks:
                if draw_landmarks:
                    self.mp_draw.draw_landmarks(frame, hand_landmark, self.mp_hands.HAND_CONNECTIONS)
        return frame

    def find_position(self, frame, landmark_number=0, draw_landmark=True):
        """
        returns a list with the coordinates of all landmarks in the detected frame
        """
        x_list = []
        y_list = []
        bbox = []
        self.landmarks = []
        if self.results.multi_hand_landmarks:
            choice = self.results.multi_hand_landmarks[landmark_number]
            for idx, landmark in enumerate(choice.landmark):
                h, w, _ = frame.shape
                cx, cy = int(landmark.x*w), int(landmark.y*h)
                x_list.append(cx)
                y_list.append(cy)
                self.landmarks.append([idx, cx, cy])
                if draw_landmark:
                    _, x, y = self.landmarks[landmark_number]
                    cv2.circle(frame, (x, y), 20, (0,255,255), cv2.FILLED)
            
            xmin, xmax = min(x_list), max(x_list)
            ymin, ymax = min(y_list), max(y_list)
            bbox = xmin, xmax, ymin, ymax

            if draw_landmark:
                cv2. rectangle(frame, (xmin - 20, ymin - 20), 
                              (xmax + 20, ymax +20), (0,255,0), 2)

        return self.landmarks, bbox

    def find_distance(self, point1, point2, frame, draw=True, radius=15, tickness=3):
        x1, y1 = self.landmarks[point1][1:]
        x2, y2 = self.landmarks[point2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(frame, (x1, y1), (x2, y2), (0,255,255), tickness)
            cv2.circle(frame, (x1, y1), radius, (0,255,255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), radius, (0,255,255), cv2.FILLED)
            cv2.circle(frame, (cx, cy), radius, (0,255,0), cv2.FILLED)
        
        length = math.hypot(x2 - x1, y2 - y1)

        return length, frame, [x1, y1, x2, y2, cx, cy]

    def fingers_up(self, ):
        fingers = []
        if self.landmarks[self.tip_idx[0]][1] < self.landmarks[self.tip_idx[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for idx in range(1,5):
            if self.landmarks[self.tip_idx[idx]][2] < self.landmarks[self.tip_idx[idx] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        return fingers
                
def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        ret, frame = cap.read()
        if not ret: 
            print("erro on read the file")
            break
        
        frame = detector.detect_hands(frame)
        landmarks = detector.find_position(frame)

        cv2.imshow("frame", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
