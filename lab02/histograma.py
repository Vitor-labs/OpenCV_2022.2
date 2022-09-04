import cv2
from cv2 import Mat
import matplotlib.pyplot as plt


def rescale_frames(frame: Mat, scale_factor):
    width = int(frame.shape[1] * scale_factor)
    height = int(frame.shape[0] * scale_factor)
    dim = (width, height)
    # resize image
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    return resized


filename = 'imagens\jato.jpg'
im = cv2.imread(filename, 0)
resized = rescale_frames(im, 0.5)

# Calcula o histograma
im_hist = cv2.calcHist([resized], [0], None, [256], [0, 256])

# equaliza histograma
im_hist_eq = cv2.equalizeHist(resized)

# equaliza histograma por CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
im_hist_clahe = clahe.apply(resized)

plt.subplot(321).set_ylabel("Original"), plt.imshow(
    im, 'gray')  # imagem original
plt.subplot(322), plt.plot(im_hist)  # histograma

plt.subplot(323).set_ylabel("Equalizado"), plt.imshow(
    im_hist_eq, 'gray')  # imagem com histograna equalizado por CDF
plt.subplot(324).set_title(""), plt.hist(
    im_hist_eq.ravel(), 256, [0, 256])  # histograma

plt.subplot(325).set_ylabel("Eq. Clahe"), plt.imshow(
    im_hist_clahe, 'gray')  # imagem com histograna equalizado por CLAHE
plt.subplot(326).set_title(""), plt.hist(
    im_hist_clahe.ravel(), 256, [0, 256])  # histograma

plt.xlim([0, 256])
plt.show()

cv2.imshow('hist_eq_clahe', im_hist_clahe)
cv2.imshow('hist_eq', im_hist_eq)
cv2.imshow('imagem', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
