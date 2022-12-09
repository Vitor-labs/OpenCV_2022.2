import cv2


def rescale_frames(frame, scale_factor=0.5):
    width = int(frame.shape[1] * scale_factor)
    height = int(frame.shape[0] * scale_factor)
    # resize image
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
    # LINEAR | CUBIC for resize to an bigger image

# Face detection, using Haar cascade classifier
filename = "data\images\\roduraigo.jpeg"
img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier('haar_face.xml')
faces_rect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

faces = str(len(faces_rect))

faces_img = img.copy()

for x, y, w, h in faces_rect:
    cv2.rectangle(faces_img, (x,y), (x+w, y+h), (0, 255, 255), thickness=2)

resized = rescale_frames(faces_img, 0.25)

cv2.imshow(f'Detected {faces} faces', resized)
cv2.waitKey(0)