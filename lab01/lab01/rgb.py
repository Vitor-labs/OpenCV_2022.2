import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

#abre imagem
filename = sys.argv[1]
im = cv2.imread(filename)

#converte cores
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

#split
#im_r,im_g,im_b = cv2.split(im)
im_r = im[:,:,0]
im_g = im[:,:,1]
im_b = im[:,:,2]



#combina as imagens
im = cv2.merge([im_r,im_g,im_b])

#mostra imagens
imagens = [im_r,im_g,im_b]



x_values = np.arange(256)

plt.subplot(1,3,1),plt.imshow(imagens[0],cmap = 'gray')
plt.subplot(1,3,2),plt.imshow(imagens[1],cmap = 'gray')
plt.subplot(1,3,3),plt.imshow(imagens[2],cmap = 'gray')



plt.show()












