import cv2

img = cv2.imread("1.jpg")

green = img[:, :, 1].copy()
blue = img[:, :, 0].copy()

img[:, :, 0] = green
img[:, :, 1] = blue

cv2.imshow("color changed:\n", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
