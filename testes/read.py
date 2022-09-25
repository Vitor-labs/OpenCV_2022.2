import cv2 as cv


def show_imgs():
    color_img = cv.imread('data/images/th1.webp')
    gray_img = cv.imread('data/images/th1.webp', cv.IMREAD_GRAYSCALE)

    cv.imshow('color_img', color_img)
    cv.imshow('gray_img', gray_img)

    cv.waitKey(0)


def show_video():
    cap = cv.VideoCapture('data/videos/v1.mp4')
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


def capture_video():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('../data/videos/v1.avi', fourcc, 20, (640, 480))

    # record video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()


def main():
    # show_imgs()
    # show_video()
    capture_video()


if __name__ == '__main__':
    main()
