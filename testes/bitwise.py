import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rect = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circ = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('rectange', rect)
cv.imshow('circle', circ)

# AND -> return the intersection
and_ = cv.bitwise_and(rect, circ)
cv.imshow('and', and_)

# OR -> return the superimpose
or_ = cv.bitwise_or(rect, circ)
cv.imshow('or', or_)

# XOR -> return the non intersection
xor = cv.bitwise_xor(rect, circ)
cv.imshow('xor', xor)

cv.waitKey(0)
