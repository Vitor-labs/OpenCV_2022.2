import cv2 as cv
from cv2 import Mat


def rescale_frames(frame: Mat, scale_factor):
    width = int(frame.shape[1] * scale_factor)
    height = int(frame.shape[0] * scale_factor)
    dim = (width, height)
    # resize image
    resized = cv.resize(frame, dim, interpolation=cv.INTER_AREA)
    return resized


def show_rescaled_imgs():
    # read image
    frame = cv.imread('data/images/th1.webp')
    # rescale image
    resized = rescale_frames(frame, 1.5)
    # show image
    cv.imshow('frame', resized)
    # wait for key press
    cv.waitKey(0)
    # release resources
    cv.destroyAllWindows()


def show_rescaled_video():
    # read video
    cap = cv.VideoCapture('data/videos/v2.mp4')
    # rescale video
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        resized = rescale_frames(frame, 0.5)
        cv.imshow('frame', resized)

        if cv.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    #    show_rescaled_imgs()
    show_rescaled_imgs()
