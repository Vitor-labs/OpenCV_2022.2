import numpy as np
import cv2

img = cv2.imread('imagens/halftone.png')

kernel = np.ones((100,80)) * cv2.getGaussianKernel(100,10)
#kernel *= kernel.T
kernel /= np.sum(kernel)

image_blur = cv2.filter2D(img,-1,kernel)

cv2.imshow("Filtro", image_blur)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()