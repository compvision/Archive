import cv2
import numpy as np
import math
from TargetProcessor import TargetProcessor

class TargetDetector:
	#image
	#hsv_image
	def putImage(self, img):
		global image
		image = img
		global hsv_image
		hsv_image  = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	def threshold(self):
		THRESHOLD_MIN = np.array([20,0,220], np.uint8)
		THRESHOLD_MAX = np.array([30,50,255], np.uint8)
		global hsv_image
		threshed_img = cv2.inRange(hsv_image, THRESHOLD_MIN, THRESHOLD_MAX)
		return threshed_img

cv2.namedWindow("Camera Feed", cv2.WINDOW_AUTOSIZE)
capture = cv2.VideoCapture(0)
while True:
	#get image from camera
	ret, frame = capture.read()
	#initialize targetDetector and targetProcessor
	targetDetector = TargetDetector()
	targetProcessor = TargetProcessor()

	#threshold
	targetDetector.putImage(frame)
	threshed = targetDetector.threshold()

	#contour
	targetProcessor.putThreshed(threshed)
	contour = targetProcessor.contour()

	cv2.drawContours(frame, contour, -1, (10,255,255), 5)
	cv2.imshow("Camera Feed", frame)
	key = cv2.waitKey(10)
	if key == 27:
		cv2.destroyWindow("Camera Feed")
		break
