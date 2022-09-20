import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = sys.argv[1]
img = cv2.imread(filename,0)

#dimensoes
l = img.shape[0]
c = img.shape[1]


#fft usando opencv e shift com numpy
##Com o metodo cv2.dft(...) o resultado e um array com dois canais, 
##sendo um array para o eixo real e outro para o imaginario
##A imagem precisa ser float
img_fft = np.fft.fftshift((cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)))


#mascaras no dominio do espaco (escolher uma)

# media
#mask = np.float32([[1, 1, 1],[1, 1, 1],[1, 1, 1]])*(1/9)

# sobel in x direction
mask = np.float32([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])

# sobel in y direction
#mask= np.float32([[-1,-2,-1],[0, 0, 0],[1, 2, 1]])

# laplacian
#mask=np.float32([[0, 1, 0],[1,-4, 1],[0, 1, 0]])


#mascara redimensionada (valores movidos para o centro)
filter_mask = np.zeros((l,c))
filter_mask[(l//2)-1:int(np.ceil(l/2))+1,(c//2)-1:int(np.ceil(c/2))+1] = mask

#mascara no dominio da frequencia (fft e shift)
fft_mask = np.fft.fftshift(cv2.dft(np.float32(filter_mask),flags = cv2.DFT_COMPLEX_OUTPUT))
mask_abs = cv2.magnitude(fft_mask[:,:,0],fft_mask[:,:,1])

#Normaliza valores para o interalo min-max (opcional)
#min=0.0
#max=1.0
#mask_abs = cv2.normalize(mask_abs,  None, min, max, cv2.NORM_MINMAX)


#replica a magnitude da mascara para os dois canais
fft_mask[:,:,0] = mask_abs
fft_mask[:,:,1] = mask_abs

#filtra no dominio da frequencia
fft_filtered = cv2.multiply(img_fft,fft_mask)

#inverte a FFT
img_back = cv2.idft(np.fft.ifftshift(fft_filtered))
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

#diferenca em relacao a imagem original
#img_dif = cv2.normalize(img_back,  None, 0, 255, cv2.NORM_MINMAX)
#img_dif = cv2.subtract(np.float32(img),img_dif)

#image plot
imagens = [img,
           np.log(cv2.magnitude(img_fft[:,:,0],img_fft[:,:,1])),
           mask_abs,
           img_back]

titles = ['original','fft original','fft mascara','filtrada']
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(imagens[i],cmap = 'gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

plt.show()        


   
