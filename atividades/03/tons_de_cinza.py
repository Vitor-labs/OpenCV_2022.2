import cv2
import numpy as np

img = cv2.imread('imagens/panda.jpg')
original = img.copy()
img = np.array(img, dtype=np.float64) 
img = cv2.transform(img, np.matrix([[0.3, 0.59, 0.11]]))

img[np.where(img > 255)] = 255
img = np.array(img, dtype=np.uint8)
cv2.imshow("original", original)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()