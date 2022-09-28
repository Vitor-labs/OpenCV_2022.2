import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def show_gray_histogram():
    img = cv.imread('data\images\dog2.jpg')
    blank = np.zeros(img.shape[:2], dtype='uint8')

    # Grayscale Histogram
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    circle = cv.circle(blank, (img.shape[0]//2, img.shape[1]//2), 100, 255, -1)

    mask = cv.bitwise_and(gray, gray, mask=circle)
    hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

    plt.figure()
    plt.title('Gray Histogram')
    plt.xlabel('Bins')
    plt.ylabel('pixels')
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()


def show_colors_histogram():
    # Colour Histogram
    img = cv.imread('data\images\jato.jpg')
    blank = np.zeros(img.shape[:2], dtype='uint8')
    mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
    masked = cv.bitwise_and(img, img, mask=mask)

    plt.figure()
    plt.title('Colour Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv.calcHist([img], [i], mask, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.show()


show_gray_histogram()
show_colors_histogram()
