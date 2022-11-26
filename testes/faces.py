import cv2

# Face detection, using Haar cascade classifier
filename = "data\images\\copa.png"
img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier('haar_face.xml')
faces_rect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

faces = str(len(faces_rect))

faces_img = img.copy()

for x, y, w, h in faces_rect:
    cv2.rectangle(faces_img, (x,y), (x+w, y+h), (0, 255, 255), thickness=2)

cv2.imshow(f'Detected {faces} faces', faces_img)
cv2.waitKey(0)