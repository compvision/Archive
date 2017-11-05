#Written by Steven Chen
#October 20, 2017

import cv2
import numpy as np
import math

fileName = "rectangle-five-feet.jpg"
orig_img = cv2.imread(fileName)
temp_img = cv2.imread(fileName)

cv2.imshow("orig", orig_img)
cv2.waitKey(0)

hsv_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)

THRESHOLD_MIN = np.array([150,240,95], np.uint8)
THRESHOLD_MAX = np.array([250,255,220], np.uint8)

threshed_img = cv2.inRange(orig_img, THRESHOLD_MIN, THRESHOLD_MAX)

cv2.imshow("THRESHED IMAGE", threshed_img)
cv2.waitKey(0)

(_,contours,_) = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#go through all the contours
count = -1
maxX = 0
maxY = 0
minX = 1000000000
minY = 1000000000
focalLength = 480
width = 0.1

for cont in contours:
	count = count +1
	approx = cv2.approxPolyDP(cont, 0.01*cv2.arcLength(cont,True),True)
	area = cv2.contourArea(approx)
	if (len(approx) == 4 and area > 300):
		for i in approx:
			if i[0][0] > maxX:
				maxX = i[0][0]

			if i[0][0] < minX:
				minX = i[0][0]

			if i[0][1] > maxY:
				maxY = i[0][1]

			if i[0][1] < minY:
				minY = i[0][1]

		imageWidth = maxX -  minX
		imageheight = maxY - minY

		distance  = (width/imageWidth)*focalLength
		print ('distance' + str(distance))

		imageCenter = (maxX + minX)/2
		wholeCenter = np.size(orig_img,0)/2

		offset = abs(imageCenter - wholeCenter)
		azimuth = np.arctan(offset/focalLength)*180/math.pi
		print ('azimuth' + str(azimuth))

		cv2.drawContours(orig_img, [cont], 1, (255,255,255), 5)

cv2.imshow("contours",orig_img)
cv2.waitKey(0)

