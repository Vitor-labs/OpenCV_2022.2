import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = sys.argv[1]
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#dimensoes
width  = img.shape[1]
height = img.shape[0]

edges = cv2.Canny(gray, 100, 200)

lines = cv2.HoughLines(edges, 1, np.pi/180, 150)


def drawLines(img, rho,theta):

	a = np.cos(theta)
	b = np.sin(theta)

	x0 = rho*a
	y0 = rho*b

	x1 = int(x0 + width*(-b))
	y1 = int(y0 + height*(a))

	x2 = int(x0 - width*(-b))
	y2 = int(y0 - height*(a))

	cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


# Desenha todas as linhas
for r_theta in lines:
	arr = np.array(r_theta[0], dtype=np.float64)
	rho, theta = arr
	drawLines(img, rho,theta)



plt.subplot(311),plt.imshow(gray,cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(312),plt.imshow(edges,cmap = 'gray'),plt.title('Edges')
plt.xticks([]), plt.yticks([])
plt.subplot(313),plt.imshow(img),plt.title('Linhas')
plt.xticks([]), plt.yticks([])

plt.show()
