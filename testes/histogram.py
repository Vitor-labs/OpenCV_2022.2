import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('data\images\jato.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title('Histogram')
plt.xlabel('Bins')
plt.ylabel('pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
