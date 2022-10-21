import cv2
import numpy as np
import sys
from cv_utils import waitKey


img = cv2.imread(sys.argv[1],0)


sift = cv2.xfeatures2d.SIFT_create(nfeatures=10)
orb = cv2.ORB_create(nfeatures=1000)

keypoints_sift, descriptors_sift = sift.detectAndCompute(img, None)
keypoints_orb, descriptors_orb = orb.detectAndCompute(img, None)

print("{} pontos detectados com SIFT".format(len(keypoints_sift)))
print("{} pontos detectados com ORB".format(len(keypoints_orb)))

img_sift = cv2.drawKeypoints(img, keypoints_sift, None)
img_orb = cv2.drawKeypoints(img, keypoints_orb, None)

cv2.imshow("SIFT Keypoints", img_sift)
cv2.imshow("ORB Keypoints", img_orb)

waitKey("SIFT Keypoints",27)
waitKey("ORB Keypoints",27)
cv2.destroyAllWindows()
