import cv2 as cv
import numpy as np


img = cv.imread('data\images\dog2.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[0]//3, img.shape[1]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)

cv.imshow('masked', masked)

cv.waitKey(0)
