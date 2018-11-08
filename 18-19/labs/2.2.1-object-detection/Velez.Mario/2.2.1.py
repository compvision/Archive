import cv2
import numpy as np
import math

img = cv2.imread("Capture.JPG")
cv2.imshow("image", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV", img_hsv)
#cv2.waitKey(0)

THRESHOLD_MIN = np.array([0, 0, 240], np.uint8)
THRESHOLD_MAX = np.array([255, 255, 255], np.uint8)

frame_threshed = cv2.inRange(img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)

image,contours,hierarchy = cv2.findContours(frame_threshed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (255, 0, 255), 10)

cv2.imshow("contours", img)
cv2.imshow("threshed image", frame_threshed)

