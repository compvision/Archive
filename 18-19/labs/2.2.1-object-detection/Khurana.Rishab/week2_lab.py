import cv2
import numpy as np
class week2_lab:
	img = cv2.imread("rect.jpg")
	#cv2.imshow("Original", img)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	#cv2.imshow("HSV", hsv)
	THRESHOLD_MIN = np.array([0,0,200], np.uint8)
	THRESHOLD_MAX = np.array([255,0,255], np.uint8)
	threshedframe = cv2.inRange(hsv, THRESHOLD_MIN, THRESHOLD_MAX)
	#cv2.imshow("Threshed", threshedframe)
	image, contours, hierarchy = cv2.findContours(threshedframe, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, -1, (255,0,0), 5)
	cv2.imshow("Contours", img)
	cv2.waitKey(0)
	