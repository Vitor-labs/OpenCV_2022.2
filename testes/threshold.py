import cv2 as cv
import matplotlib.pyplot as plt


filename = 'data\images\\bg.jpg'
img = cv.imread(filename)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# normal threshold
_, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# inverse threshold
_, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# adaptative, find the optimal threshold value.
adaptive = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 7)

plt.subplot(221), plt.imshow(img), plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(thresh, cmap='gray'), plt.title('Binary')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(thresh_inv, cmap='gray'), plt.title('Binary inv')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(adaptive, cmap='gray'), plt.title('Adaptive')
plt.xticks([]), plt.yticks([])

plt.show()
