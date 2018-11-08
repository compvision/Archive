import cv2
import numpy as np
from matplotlib import pyplot as plt

img  = cv2.imread("ReflectiveRectangle.JPG")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("original", img)

minThreshold = np.array([0,0,236],np.uint8)
maxThreshold = np.array([255,100,255],np.uint8)

threshold = cv2.inRange(hsv, minThreshold, maxThreshold)
HSV,contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    epsilon = 0.1 * cv2.arcLength(contours[c],True)
    approx = cv2.approxPolyDP(contours[c],epsilon, True)
    if cv2.contourArea(approx)>300:
        cv2.drawContours(img, contours, c, (255, 221, 0), 2)


cv2.imshow("drawContours", img)


cv2.waitKey(0)
