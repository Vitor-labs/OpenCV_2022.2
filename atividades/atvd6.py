import cv2
import seam_carving


filename = "ibiza.jpg"
x_scale, y_scale = 0.70, 0.50

img = cv2.imread(filename)
img_h, img_w, _ = img.shape

new_size = (img_w*x_scale, img_h*y_scale)

e_mode = 'forward'
# e_mode = 'backward'

carving_order = 'height-first'
#carving_order = 'width-first'

img_seam = seam_carving.resize(
    img, new_size,
    energy_mode=e_mode,   
    order=carving_order)

    
cv2.imshow("Original", img)
cv2.imshow("Seam Carving", img_seam)

cv2.waitKey(0)