import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d





#parametros
width = 100
height = 100
freq_r = 0
freq_c = 0

#matrizes
dft_float = np.zeros((height,width,2),np.float32)

img       = np.zeros((height,width),np.uint8)
espectro  = np.zeros((height,width,1),np.uint8)


#janelas
cv2.namedWindow('dft',cv2.WINDOW_NORMAL)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)


#trackbar
def callback_func(x):
    pass

cv2.createTrackbar('lin','dft',0,height-1,callback_func)
cv2.createTrackbar('col','dft',0,width-1,callback_func)

cv2.imshow('dft',espectro)





while(1):

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
        
    #obtem as frequencias
    freq_r = cv2.getTrackbarPos('lin','dft')
    freq_c = cv2.getTrackbarPos('col','dft')
    
    #desenha linhas
    espectro[:,:] = 0
    cv2.line(espectro,(0,freq_r),(height-1,freq_r),255,1)
    cv2.line(espectro,(freq_c,0),(freq_c,width-1),255,1)
  
    #dft inversa
    dft_float[:,:,1]=0.0
    dft_float[freq_r,freq_c,1]=1.0
    inverse = cv2.idft(dft_float, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
    


    img = cv2.normalize(inverse,  img, 0, 255, cv2.NORM_MINMAX)
    img = np.uint8(img)
    cv2.imshow('dft',espectro)
    cv2.imshow('image',img)


cv2.destroyAllWindows()

#plot 3D image
fig = plt.figure()
ax = plt.axes(projection='3d')


def f(x, y):
    return img[x,y]


# Data for a three-dimensional line
xline = np.arange(height)
yline = np.arange(width)

X, Y = np.meshgrid(xline, yline)


Z = f(X,Y)

ax.contour3D(X, Y, Z, 50, cmap='binary')
plt.show()




