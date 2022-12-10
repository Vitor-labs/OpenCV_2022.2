import cv2


def wait_key(window_name, key):
    while cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) >= 1:
        keycode = cv2.waitKey(1000) & 0xFF
        if (keycode == key):
            cv2.destroyAllWindows()
            break














