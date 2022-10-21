import numpy as np
import cv2 as cv
import sys
import matplotlib.pyplot as plt


def matching_orb(im1,im2):
	orb = cv.ORB_create()
	# find the keypoints and descriptors with ORB
	kp1, des1 = orb.detectAndCompute(im1,None)
	kp2, des2 = orb.detectAndCompute(im2,None)
	# create BFMatcher object
	bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

	# Match descriptors.
	matches = bf.match(des1,des2)
	print(len(matches))

	# Sort them in the order of their distance.
	matches = sorted(matches, key = lambda x:x.distance)

	# Draw first 10 matches.
	img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
	plt.imshow(img3),plt.show()


def matching_sift(im1,im2):
	# Initiate SIFT detector
	sift = cv.xfeatures2d.SIFT_create()
	# find the keypoints and descriptors with SIFT
	kp1, des1 = sift.detectAndCompute(im1,None)
	kp2, des2 = sift.detectAndCompute(im2,None)
	# BFMatcher with default params
	bf = cv.BFMatcher()
	matches = bf.knnMatch(des1,des2,k=2)

	# Apply ratio test
	good = []
	for m,n in matches:
		if m.distance < 0.75*n.distance:#
			good.append([m])
	#cv.drawMatchesKnn expects list of lists as matches.
	img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
	plt.imshow(img3),plt.show()




############


img1 = cv.imread( sys.argv[1],0) # queryImage
img2 = cv.imread( sys.argv[2],0) # trainImage


#SIFT
matching_sift(img1,img2)

#ORB
matching_orb(img1,img2)





