import cv2 as cv
import numpy as np


img = cv.imread('dog2.jpg')
cv.imshow('DOGO', img)
'''
Rules for tranformations
    -x -> Left
    -y -> Up
     x -> Right
     y -> Down
'''


def translation(img, x, y):
    matrix = np.float32([[1, 0, x], [0, 1, y]])

    return cv.warpAffine(img, matrix, (img.shape[0], img.shape[1]))


def rotation(img, angle, point=None):
    (height, width) = img.shape[:2]

    if point is None:
        point = (height//2, width//2)

    matrix = cv.getRotationMatrix2D(point, angle, 1.0)

    return cv.warpAffine(img, matrix, (width, height))

# ===============================================================


translated_img = translation(img, -100, 200)
cv.imshow('Translated', translated_img)

rotated = rotation(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotation(rotated, -90)
cv.imshow('Rotated 2x', rotated_rotated)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

cv.waitKey(0)
