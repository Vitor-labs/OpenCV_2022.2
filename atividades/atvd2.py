import numpy as np
import cv2 as cv

from cv_utils import wait_key


def gamma_correction_lut(img, gamma, c=1.0):
    # cria uma LookUp Table (LUT)
    GAMMA_LUT = np.array([c*((i / 255.0) ** (1.0 / gamma)) * 255
                          for i in np.arange(0, 256)]).astype("uint8")

    # aplica a transformação usando LUT
    return cv.LUT(img, GAMMA_LUT)


def callback_trackbar(x):
    try:
        gamma = cv.getTrackbarPos('gamma', 'image')
        im_gamma = gamma_correction_lut(img, gamma*0.01)
        cv.imshow('image', im_gamma)
    except Exception as e:
        print(str(e))


img = cv.imread('..\lab02\imagens\jato.jpg')

# limnpando o canal azul
img[:, :, 0] = 0


cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.createTrackbar('gamma', 'image', 0, 100, callback_trackbar)
cv.imshow('image', img)
wait_key('image', 27)  # 27 = ESC
