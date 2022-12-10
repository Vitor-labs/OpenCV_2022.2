import cv2
import seam_carving


def retarget_frames(frame, size, e_mode='forward', carving_order='height-first'):
    return seam_carving.resize(
        frame, size,
        energy_mode=e_mode,   
        order=carving_order)

def show_retarget_video():
    cap = cv2.VideoCapture('v1.avi')

    while True:
        _, frame = cap.read()

        if not _:
            print("error on reading")
            break

        x_scale, y_scale = 0.70, 0.50

        img_h, img_w, _ = frame.shape
        new_size = (img_w*x_scale, img_h*y_scale)

        ret = retarget_frames(frame, new_size)
        cv2.imshow('Retarget video', ret)
        
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_retarget_video()

    