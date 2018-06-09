import cv2
import numpy as np
import math
import network
from Target import Target
from time import sleep
from targetProcessor import targetProcessor

global camera
camera = cv2.VideoCapture(1)
global targetFound
targetFound = False
target = Target()
global network1
network1 = network.Network()
network1.userServer()
#outputs livefeed image


def getImage():
	global camera
	ret, image = camera.read()
	return image

#outputs angle of three points
def getContour(image):
	img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	#thresholding

	THRESHOLD_MIN = np.array([100,51,175],np.uint8)
	THRESHOLD_MAX = np.array([150,207,255],np.uint8)

	threshed_img = cv2.inRange(img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)

	cv2.imshow("threshed", threshed_img)


	#contours
	_, contours, _ = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for cont in contours: #for each contour
		epsilon = 0.02*cv2.arcLength(cont,True)
		approx = cv2.approxPolyDP(cont, epsilon, True)
		if (cv2.contourArea(approx) > 500  and len(approx) == 4): #the contour should be reasonably large and have 4 corners
			global targetFound
			targetFound = True
			cv2.drawContours(image,[approx],-1, (255,255,255), 10)
			return approx
found = 0
image = getImage()
targetProcessor = targetProcessor()
count = 0
while found < 2:
	count = count+1
	print(count)
	image = getImage() #get image from live feed
	global targetFound
	targetFound = False
	contours = getContour(image)
	print(count)
	cv2.imshow("hi",image)
	if targetFound:
		found+=1
		if found == 1:
			target.firstImage(contours)
			print("first")
			print(target.getOrientation1())
		elif found  > 1:
			target.secondImage(contours)
			print("second")
			print(target.getOrientation2())
	sleep(1)
	key = cv2.waitKey(10)
	if key == 27:
		cv2.destroyAllWindows()
		break

finalOrient= target.finalOrientation()
print(finalOrient)
targetProcessor.loadTarget(target)
azimuth = targetProcessor.findAzimuth()
print(azimuth)
network1.setAzimuth(azimuth)
network1.setOrientation(finalOrient)
cv2.destroyAllWindows()
