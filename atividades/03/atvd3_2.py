import cv2
import numpy as np
"""
2) Escolha uma imagem qualquer colorida e aplique um ou mais filtros convolucionais, de 
forma a resultar em uma imagem em tons de cinza.

Considere a fórmula abaixo, onde Y é o valor do pixel em tons de cinza e R, G e B 
correspondem aos valores dos pixels nos canais Vermelho, Verde e Azul, respectivamente.
                            Y=(0,3×R)+(0,59×G)+(0,11×B
"""
filename = '../data/images/taxis-peru-.jpg'

def convert_to_gray(img):    
    gray = np.array(img, dtype=np.float64) 
    gray = cv2.transform(gray, 
                        np.matrix(
                            [[0.3, 0.6, 0.1]]
                            )
                        )
    img[np.where(gray > 255)] = 255
    return np.array(gray, dtype=np.uint8)

img = cv2.imread(filename)
cv2.imshow("original", img)

gray = convert_to_gray(img)
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)
cv2.imshow("compared", gray2)
cv2.waitKey(0)
