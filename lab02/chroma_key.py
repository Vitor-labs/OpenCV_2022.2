import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

from cv_utils import waitKey



#abre imagens
im_foreground = cv2.imread('./imagens/fg.jpg')
im_background = cv2.imread('./imagens/bg.jpg')

#converte cores
im_foreground = cv2.cvtColor(im_foreground, cv2.COLOR_BGR2RGB)
im_background = cv2.cvtColor(im_background, cv2.COLOR_BGR2RGB)

#split
im_r,im_g,im_b = cv2.split(im_foreground)

#dimensoes
width  = im_foreground.shape[1]
height = im_foreground.shape[0]

#redimensiona o background
dim = (width, height)
im_bg = cv2.resize(im_background, dim, interpolation = cv2.INTER_AREA)

#threshold
ret,im_bg_msk = cv2.threshold(im_g,250,255,cv2.THRESH_BINARY)

#replica mascara para todos os canais
im_bg_msk = cv2.cvtColor(im_bg_msk, cv2.COLOR_GRAY2RGB)

im_fg_msk = cv2.bitwise_not(im_bg_msk)

#combina as imagens
im_fg = cv2.bitwise_and(im_foreground, im_fg_msk)
im_bg = cv2.bitwise_and(im_bg, im_bg_msk)
#im_fg= cv2.add(im_bg, im_fg)

#mostra imagens intermediarias com matplotlib
plt.subplot(321), plt.imshow(im_background, cmap='gray')
plt.subplot(322), plt.imshow(im_foreground, cmap='gray')
plt.subplot(323), plt.imshow(im_bg_msk, cmap='gray')
plt.subplot(324), plt.imshow(im_fg_msk, cmap='gray')
plt.subplot(325), plt.imshow(im_bg, cmap='gray')
plt.subplot(326), plt.imshow(im_fg, cmap='gray')
plt.show()

#resultado final
im_result = cv2.add(im_bg, im_fg)
im_result = cv2.cvtColor(im_result, cv2.COLOR_RGB2BGR)
cv2.imshow('resultado', im_result)

waitKey('resultado', 27)









