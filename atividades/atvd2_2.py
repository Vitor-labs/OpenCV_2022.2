import cv2 as cv
import numpy as np


line = cv.imread('..\lab02\imagens\line.jpg')
circle = cv.imread('..\lab02\imagens\circle.jpg')

# dimensoes 'line'
width = line.shape[1]
height = line.shape[0]

# rotação 90 graus
x_center = width/2
y_center = height/2
M_rotation = cv.getRotationMatrix2D((x_center, y_center), 90, 1)
tronco = cv.warpAffine(line, M_rotation, (width, height))

# rotação 45 graus
x_center = width/2
y_center = height/2
M_rotation = cv.getRotationMatrix2D((x_center, y_center), 45, 1)

# Computa as transformacoes
braco = cv.resize(line, (int(width*0.75), int(height*0.75)),
                  interpolation=cv.INTER_AREA)
braco_e = cv.warpAffine(braco, M_rotation, (width, height))
braco_d = braco_e[::-1, :]
bracos = np.concatenate((braco_e, tronco, braco_d), axis=1)

cv.imshow('rotate', bracos)
cv.waitKey(0)
cv.destroyAllWindows()
