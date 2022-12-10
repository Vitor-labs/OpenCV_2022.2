import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

'''
 Utilizando a transformada de Hough para detecção de linhas, elabore um programa para 
leitura do código de barras presente na imagem “barcode-code-128.png”.
 - O código utiliza o formato CODE-128.
 '''

def detect_lines(img):
    dst = cv.Canny(img, 50, 200, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    cdst_p = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    lines_p = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 5)
    
    if lines_p is not None:
        for i in range(0, len(lines_p)):
            l = lines_p[i][0]
            cv.line(cdst_p, (l[0], l[1]), (l[2], l[3]), (255,255,255), 1, cv.LINE_AA)

    cv.imshow("Detected Lines", cdst_p)
    cv.waitKey(0)

    return cv.threshold(cdst_p, 100, 255, cv.THRESH_BINARY_INV)[1]

def barcode_reader(img):
    detected = decode(img)

    if not detected:
        print("Barcode Not Detected or your barcode is blank/corrupted!")

    for barcode in detected: 
        # Locate the barcode position in image
        (x, y, w, h) = barcode.rect
            
        # Put the rectangle in image using
        # cv2 to heighlight the barcode
        cv.rectangle(img, (x-10, y-10),
                        (x + w+10, y + h+10),
                        (255, 0, 0), 2)
            
        if barcode.data != "":
            
        # Print the barcode data
            print(barcode.data)
            print(barcode.type)
                 
    #Display the image
    cv.imshow("Image", img)
    cv.waitKey(0)

def rescale_frames(frame, scale_factor=1.5):
    width = int(frame.shape[1] * scale_factor)
    height = int(frame.shape[0] * scale_factor)
    # resize image
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

img = cv.imread("barcode-code-128.png")
img = rescale_frames(img, scale_factor=2)
lines_img = detect_lines(img)
barcode_reader(lines_img)
