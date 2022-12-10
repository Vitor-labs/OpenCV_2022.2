import numpy as np
import cv2 as cv
import sys

'''
Considere a imagem “placas-transito.jpg” aplique a transformada de Hough para linhas e 
círculos (verifique a documentação do OpenCV) de modo as placas presentes nas imagens. 
Produza uma imagem diferente para cada um dos três modelos de placa
'''
def detect_circles(img):
    copy = img.copy()
    gray = cv.cvtColor(copy, cv.COLOR_BGR2GRAY)
    # Apply a Median blur to reduce noise and avoid false circle detection:
    # Reduce the noise to avoid false circle detection
    gray = cv.medianBlur(gray, 7)
        
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 
                              rows / 4, param1=120, param2=40, 
                              minRadius=50, maxRadius=73)
    
    # Draw the detected circles:
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(copy, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(copy, center, radius, (178, 0, 178), 3)
    
    
    cv.imshow("detected circles", copy)
    cv.waitKey(0)
    
def detect_lines(img):
    dst = cv.Canny(img, 50, 200, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    cdst_p = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)

    lines_p = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if lines_p is not None:
        for i in range(0, len(lines_p)):
            l = lines_p[i][0]
            cv.line(cdst_p, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    
    cv.imshow("Detected Lines", cdst_p)

    cv.waitKey(0)

def main(argv):
    
    default_file = 'placas-transito.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    detect_circles(src)
    detect_lines(src)
    
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])