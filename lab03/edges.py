import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = sys.argv[1]
img = cv2.imread(filename,0)


#Sobel
img_sobel = cv2.Sobel(img, cv2.CV_8U, dx=1, dy=1)


# DoG
low_sigma = cv2.GaussianBlur(img,(3,3),0)
high_sigma = cv2.GaussianBlur(img,(5,5),0)
img_dog = low_sigma - high_sigma


#Canny
img_canny = cv2.Canny(img,100,200)


plt.subplot(221),plt.imshow(img,cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img_dog,cmap = 'gray'),plt.title('Dog')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_sobel,cmap = 'gray'),plt.title('Sobel')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(img_canny,cmap = 'gray'),plt.title('Canny')
plt.xticks([]), plt.yticks([])


plt.show()
