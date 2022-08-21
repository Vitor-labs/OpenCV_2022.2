import cv2 as cv

# resizing an image using cv.resize()


def rescale_imgs(frame, scale_factor):
    width = int(frame.shape[1] * scale_factor)
    height = int(frame.shape[0] * scale_factor)
    dim = (width, height)
    # resize image
    resized = cv.resize(frame, dim, interpolation=cv.INTER_AREA)
    return resized


def rescale_video(video_path, scale_factor):
    # read video
    cap = cv.VideoCapture(video_path)
    # get video properties
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    # get video fps
    fps = cap.get(cv.CAP_PROP_FPS)
    # get video length
    length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    # get video codec
    codec = cap.get(cv.CAP_PROP_FOURCC)
    # create video writer
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('data/videos/v2.mp4', fourcc, fps, (width, height))
    # rescale video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        resized = rescale_imgs(frame, scale_factor)
        out.write(resized)
        cv.imshow('frame', resized)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()


def main():
    # read image
    frame = cv.imread('data/images/th1.webp')
    # rescale image
    resized = rescale_imgs(frame, 2.5)
    # show image
    cv.imshow('frame', resized)
    # wait for key press
    cv.waitKey(0)
    # release resources
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
