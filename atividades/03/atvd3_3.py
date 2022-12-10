import cv2
import numpy as np
"""
3) Repita a questão anterior, mas dessa vez a imagem resultante deve ter uma coloração 
sépia.						Sépia | HEX: #705714
"""
filename = '../data/images/taxis-peru-.jpg'

def convert_to_sepia(img):
	sepia = np.array(img, dtype=np.float64) 
	sepia = cv2.transform(sepia, 
						  np.matrix(
							[[0.27, 0.53, 0.13],
							[0.34, 0.68, 0.16],
							[0.39, 0.76, 0.18]]
							)
						) 
	sepia[np.where(sepia > 255)] = 255
	return np.array(sepia, dtype=np.uint8)

img = cv2.imread(filename)
cv2.imshow("original", img)

sepia = convert_to_sepia(img)

cv2.imshow("sepia", sepia)
cv2.waitKey(0)
