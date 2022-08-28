import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]

img = cv2.imread(filename)
im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
im_dst = cv2.imread(filename,0)

print(im)
print(im.shape)

width = im.shape[1]
height = im.shape[0]

#ler todos os pixels da imagem
for c in range(0, width-1):
	for l in range(0, height-1):
		px = im.item(l,c)

		#negativo
		im_dst.itemset(l,c,255-px)

#		if px > 100:
#			im.itemset(l,c,255)


#redimensiona a imagem
new_width = int(im.shape[1] * .5)
new_height = int(im.shape[0] * .5)
dim = (new_width, new_height)
im_resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)


#threshold
ret,im_thresh = cv2.threshold(im,127,255,cv2.THRESH_BINARY)

#mostra imagem com opencv
cv2.imshow('threashold',im_thresh)
cv2.imshow('resized',im_resized)
cv2.imshow('imagem',im)
cv2.waitKey(0)
cv2.destroyAllWindows()







