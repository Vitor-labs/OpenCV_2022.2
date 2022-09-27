from matplotlib import pyplot as plt
import cv2 as cv


img = cv.imread('data\images\jato.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)

b, g, r = cv.split(img)

plt.subplot(221), plt.imshow(gray, cmap='gray'), plt.title('gray')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(hsv, cmap='gray'), plt.title('hsv')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(lab), plt.title('lab')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(lab_bgr), plt.title('lab_bgr')
plt.xticks([]), plt.yticks([])

plt.show()

cv.waitKey(0)
