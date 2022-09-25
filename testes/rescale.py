import cv2 as cv


def rescale_frames(frame, scale_factor=0.5):
    width = int(frame.shape[1] * scale_factor)
    height = int(frame.shape[0] * scale_factor)
    # resize image
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)


def show_rescaled_imgs():
    # read image
    frame = cv.imread('jato.jpg')
    scale = 2.5
    # rescale image
    resized = rescale_frames(frame, scale)
    # show image
    cv.imshow(f'frame on {scale}x', resized)
    # wait for key press
    cv.waitKey(0)
    # release resources
    cv.destroyAllWindows()


def show_rescaled_video():
    # read video
    cap = cv.VideoCapture('../data/videos/v1.avi')
    # rescale video
    while True:
        ret, frame = cap.read()

        if not ret:
            print('dafuk')
            break

        resized = rescale_frames(frame, 1.75)
        cv.imshow('frame', resized)

        if cv.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    # show_rescaled_imgs()
    show_rescaled_video()
