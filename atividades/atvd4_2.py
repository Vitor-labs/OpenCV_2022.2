import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

'''
 Utilizando a transformada de Hough para detecção de linhas, elabore um programa para 
leitura do código de barras presente na imagem “barcode-code-128.png”.
 - O código utiliza o formato CODE-128.
 '''

def detect_lines(img):
    dst = cv.Canny(img, 50, 100, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    lines_p = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if lines_p is not None:
        for i in range(0, len(lines_p)):
            l = lines_p[i][0]
            cv.line(img, (l[0], l[1]), (l[2], l[3]), (255,255,255), 1, cv.LINE_AA)
    
    cv.imshow("Detected Lines", img)

    cv.waitKey(0)

    return img

def detect_code(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert roi into gray
    blur = cv.GaussianBlur(gray,(5,5),1) #apply blur to roi
    canny = cv.Canny(blur,10,50) #apply canny to roi

    #Find my contours
    contours =cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)[0]

    #Loop through my contours to find rectangles and put them in a list, so i can view them individually later.
    cntr = []
    for i in contours:
            epsilon = 0.05*cv.arcLength(i,True)
            approx = cv.approxPolyDP(i,epsilon,True)

            if len(approx) == 4:
                cv.drawContours(img,cntr,-1,(0,255,0),2)
                cv.imshow('Roi Rect ONLY',img)
                cntr.append(approx)

    return img

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

img = cv.imread("barcode-code-128.png")
lines_img = detect_lines(img)
code = detect_code(lines_img)
barcode_reader(code)
