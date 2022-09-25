import cv2 as cv
import numpy as np


def hello():
    img = np.zeros((600, 400, 3),  # width, heigt and chanels
                   dtype='uint8')
    cv.putText(img, 'Hello, my name is vitor', (10, 200),
               cv.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 255), 1)
    cv.imshow('blank', img)

    cv.waitKey(0)


def bluring(url: str):
    img = cv.imread(url)
    blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
    cv.imshow('Blured Image', blur)
    cv.waitKey(0)


def convert_colors(url: str):
    img = cv.imread(url)
    gray = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow('HSV Image', gray)
    cv.waitKey(0)


def edges(url: str):
    img = cv.imread(url)
    canny = cv.Canny(img, 100, 150)
    cv.imshow('edges', canny)

    dilated = cv.dilate(canny, (9, 9), iterations=1)  # highlights edges
    cv.imshow('dilated', dilated)
    '''
    Eroding method to edges
    
    eroded = cv.erode(dilated, (7,7), iterations=3)

    turn the edges to the original
    '''
    cv.waitKey(0)


def crop(url: str):
    img = cv.imread(url)
    # Cropping
    cropped = img[50:200, 200:400]
    cv.imshow('Cropped', cropped)
    cv.waitKey(0)


crop('jato.jpg')
