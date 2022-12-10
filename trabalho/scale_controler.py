import cv2
import math
import numpy as np
from hand_detector import HandDetector

w_cam, h_cam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, w_cam)
cap.set(4, h_cam)

detector = HandDetector(max_num_hands=1)

# =========================== PYCAW ===========================
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
#volume.GetVolumeRange()
#volume.SetMasterVolumeLevel(-20.0, None)
# =========================== PYCAW ===========================

volume_range = volume.GetVolumeRange() # volume range goes from -65 to 0
min_volume = volume_range[0]
max_volume = volume_range[1]
vol, volume_bar = 0, 400
vol_percent = volume.GetMasterVolumeLevel()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error on reading")
        break

    frame = detector.detect_hands(frame)
    landmarks = detector.find_position(frame, draw_landmark=False)

    if len(landmarks) != 0:
        x1, y1 = landmarks[4][1], landmarks[4][2]
        x2, y2 = landmarks[8][1], landmarks[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2 # Centroid Location

        cv2.circle(frame, (x1, y1), 20, (0,255,255), cv2.FILLED)
        cv2.circle(frame, (x2, y2), 20, (0,255,255), cv2.FILLED)
        cv2.line(frame, (x1, y1), (x2, y2), (0,255,255), 3)
        cv2.circle(frame, (cx, cy), 20, (0,255,255), cv2.FILLED)
        
        length = math.hypot(x2 - x1, y2 - y1) # min-max between 50 to 250

        if length < 50:
            cv2.circle(frame, (cx, cy), 20, (255,0,255), cv2.FILLED)

        vol = np.interp(length, [50, 250], [min_volume, max_volume])
        volume_bar = np.interp(length, [50, 250], [400, 150])
        vol_percent = int(np.interp(length, [50, 250], [0, 100]))
        volume.SetMasterVolumeLevel(vol, None)

    # Volume bar visualization
    cv2.rectangle(frame, (50,150), (85,400), (0,255,255), 3)
    cv2.rectangle(frame, (50, int(volume_bar)), (85,400), (0,255,255), cv2.FILLED)
    cv2.putText(frame, f'Volume: {vol_percent}%', (30, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 3)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break