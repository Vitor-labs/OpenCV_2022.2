import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

#abre imagen
filename = sys.argv[1]
im = cv2.imread(filename)

#converte pra RGB
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

#dimensoes
width = im.shape[1]
height = im.shape[0]

#matrizes de transformacao 

#rotation 45 graus
x_center = width/2
y_center = height/2
M_rotation = cv2.getRotationMatrix2D((x_center,y_center),45,1)
#M_rotation = cv2.getRotationMatrix2D((0,0),30,1)

#print M_rotation

#M_rotation = np.float32([[0.86,0.5,0],[-0.5 ,0.86,0]])

print(M_rotation)

#scaling x 0.7
M_scaling = np.float32([[1,0,0],[0,1,0]])

#translation (180,100)
M_translation = np.float32([[1,0,180],[0,1,100]])

#cisalhamento horizontal e vertical
#TODO

#Computa as transformacoes
im_rotated = cv2.warpAffine(im,M_rotation,(width,height))
im_scaled = cv2.warpAffine(im,M_scaling,(width,height))
im_translated = cv2.warpAffine(im,M_translation,(width,height))

#mostra imagens em janelas separadas
#cv2.imshow('original',im)
#cv2.imshow('Rotate',im_rotated)
#cv2.imshow('Scaling',im_scaled)
#cv2.imshow('Translation',im_translated)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#mostra imagens
plt.subplot(221), plt.imshow(im, cmap='gray')
plt.subplot(222), plt.imshow(im_rotated, cmap='gray')
plt.subplot(223), plt.imshow(im_scaled, cmap='gray')
plt.subplot(224), plt.imshow(im_translated, cmap='gray')
plt.show()











