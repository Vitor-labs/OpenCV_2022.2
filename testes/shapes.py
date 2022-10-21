import cv2
'''
Shape detection by contour approximation. Here we assumption that the objects are simple 
shapes, here's an approach using thresholding + contour approximation. Contour 
approximation is based on the assumption that a curve can be approximated by a series of 
short line segments which can be used to determine the shape of a contour. 
'''
def detect_shape(c):
    # Compute perimeter of contour and perform contour approximation
    shape = ""
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)

    # Triangle
    if len(approx) == 3:
        shape = "triangle"

    # Square or rectangle
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)

        # A square will have an aspect ratio that is approximately
        # equal to one, otherwise, the shape is a rectangle
        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

    # Pentagon
    elif len(approx) == 5:
        shape = "pentagon"

    # Hexagon
    elif len(approx) == 6:
        shape = "hexagon"

    # Octagon 
    elif len(approx) == 8:
        shape = "octagon"

    # Star
    elif len(approx) == 10:
        shape = "star"

    # Otherwise assume as circle or oval
    else:
        shape = "circle"

    return shape

# Load image, grayscale, Otsu's threshold
image = cv2.imread('data\images\\barcode-code-128.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find contours and detect shape
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cv2.drawContours(image, cnts, -1, (0,255,0), 1)
for c in cnts:
    # Identify shape
    shape = detect_shape(c)

    # Find centroid and label shape name
    # M = cv2.moments(c)
    # cX = int(M["m10"] / M["m00"])
    # cY = int(M["m01"] / M["m00"])
    # cv2.putText(image, shape, (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2)

cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.waitKey()
