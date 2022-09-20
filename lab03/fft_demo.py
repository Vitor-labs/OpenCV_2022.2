import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d


filename = sys.argv[1]
img = cv2.imread(filename,0)

img_fft = np.fft.fft2(img)
img_fft_shift = np.fft.fftshift(img_fft)

img_fft = np.log(np.abs(img_fft))
img_fft_shift = np.log(np.abs(img_fft_shift))


#image plot
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_fft, cmap = 'gray')
plt.title('fft'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(img_fft_shift, cmap = 'gray')
plt.title('fft shifted'), plt.xticks([]), plt.yticks([])

plt.show()        


   
