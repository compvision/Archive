import cv2
import numpy as np
import math
from Target import Target

class TargetProcessor:
	#image
	#hsv_image
	def putThreshed(self, threshed):
		global image
		image = threshed
	def contour(self):
		global image
		global contours
		(_,contours,_) = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		return contours
	def calculateData(self):
		count = -1
		maxX = 0
		maxY = 0
		minX = 100000000
		maxX = 100000000
		focalLength = 480
		width = 0.1
		global target
		target = Target()
		for cont in contours:
			count = count +1
			approx = cv2.approxPolyDP(cont, 0.1*cv2.arcLength(cont,True), True)
			if (abs(cv2.contourArea(approx)) > 0):
				for i in approx:
					if i[0][0] > maxX:
						maxX = i[0][0]
					if i[0][0] < minX:
						minX = i[0][0]
					if i[0][1] > maxY:
						maxY = i[0][1]
					if i[0][1] < minY:
						minY = i[0][1]
				imageWidth = maxX - minX
				imageHeight = maxY - minY
				distance =  (width/imageWidth)*focalLength
				imageCenterX = (maxX+minX)/2
				global image
				wholeCenterX = np.size(image,0)/2
				offsetX = abs(imageCenterX - wholeCenterX)
				azimuth = np.arctan(offsetX/focalLength)*180/math.pi
				imageCenterY = (maxY+minY)/2
				wholeCenterY = np.size(image,1)/2
				offsetY = abs(imageCenterY - wholeCenterY)
				altitude = np.arctan(offsetY/focalLength)*180/math.pi
				target.putDistance(distance)
				target.putAzimuth(azimuth)
				target.putAltitude(altitude)
	def getTarget(self):
		global target
		return target
