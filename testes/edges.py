import numpy as np
import cv2 as cv
img = cv.imread('data\images\dog2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 125, 175)  # find edges
ret, threshold = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

'''
RETR_TREE -> all hierarchical contours
RETR_EXTERNAL -> all external contours
RETR_LIST -> all contours on image
'''
contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
'''
CHAIN_APPROX_NONE -> does nothing, just return all contours 
CHAIN_APPROX_SIMPLE -> compresses all contours in one that make more sense
'''


blank = np.zeros(img.shape, dtype='uint8')

cv.drawContours(blank, contours, -1, (0, 255, 255))

cv.imshow('contours', blank)
cv.imshow('edges', threshold)
cv.imshow('canny', canny)
print(f'finded {len(contours)} contours')

cv.waitKey(0)
