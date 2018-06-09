import numpy as np
import cv2
import math
from Target import Target
from time import sleep

def getContour(image):
	img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	#thresholding
	THRESHOLD_MIN = np.array([50,0,200],np.uint8)
	THRESHOLD_MAX = np.array([90,255,255],np.uint8)

	threshed_img = cv2.inRange(img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)

	cv2.imshow("threshed", threshed_img)
	#cv2.waitKey(0)

	#contours
	_, contours, _ = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for cont in contours: #for each contour
		epsilon = 0.02*cv2.arcLength(cont,True)
		approx = cv2.approxPolyDP(cont, epsilon, True)
		if (cv2.contourArea(approx) > 500  and len(approx) == 4): #the contour should be reasonably large and have 4 corners
			cv2.drawContours(image,[approx],-1, (255,255,255), 10)
			return approx


def classifyOrientation(FileLocation1, FileLocation2,target):
	image1 = cv2.imread(FileLocation1)
	image2 = cv2.imread(FileLocation2)


	contours1 = getContour(image1)
	contours2 = getContour(image2)

	target.firstImage(contours1)
	print("first")
	print(target.getOrientation1())

	target.secondImage(contours2)
	print("second")
	print(target.getOrientation2())

	print(target.finalOrientation())
	return target.finalOrientation()

OrientationsML = open("OrientationsML","a")
FileLocation1 = ""
FileLocation2 = ""
target = Target()
finalOrientation = classifyOrientation(FileLocation1, FileLocation2, target)
result = FileLocation1 + ", " + FileLocation2 + ", " + finalOrientation
OrientationsML.write(result)
OrientationsML.close
