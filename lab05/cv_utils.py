import cv2


def waitKey(window_name, key):
    while cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(1000) & 0xFF
        if (keyCode == key):
            cv2.destroyAllWindows()
            break














