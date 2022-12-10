import cv2
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
        landmarks = []
        if self.results.multi_hand_landmarks:
            choice = self.results.multi_hand_landmarks[landmark_number]
            for idx, landmark in enumerate(choice.landmark):
                h, w, _ = frame.shape
                cx, cy = int(landmark.x*w), int(landmark.y*h)
                landmarks.append([idx, cx, cy])
                if draw_landmark:
                    _, x, y = landmarks[landmark_number]
                    cv2.circle(frame, (x, y), 20, (0,255,255), cv2.FILLED)
        return landmarks


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
        if len(landmarks) != 0: print("Landmarks:", landmarks[8])

        cv2.imshow("frame", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
