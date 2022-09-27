import cv2 as cv


img = cv.imread('data\images\dog2.jpg')

# averange bluring
blur = cv.blur(img, (7, 7))
cv.imshow('blur', blur)

# more smooth and natural blur
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('gauss', gaussian)

# more efective on reducing noise (not meant for >3 column size)
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# most efective, retaing the edges
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
