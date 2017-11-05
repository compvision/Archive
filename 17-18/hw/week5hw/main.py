#Written by Steven Chen
#October 13, 2017

import cv2
import numpy as np
import math

#read image and convert to hsv
fileLocation = "hwimg.png"
img = cv2.imread(fileLocation)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#threshold the image
THRESHOLD_MIN = np.array([1,0,0], np.uint8)
THRESHOLD_MAX = np.array([50,255,255], np.uint8)
threshed_img = cv2.inRange(hsv_img, THRESHOLD_MIN, THRESHOLD_MAX)

#find Contours
(_, contours, _) = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#set initial contour and area
maxContour = cv2.approxPolyDP(contours[0], 0.01*cv2.arcLength(contours[0],True), True)
maxArea = 0

#go through all contours and check which ones the biggest
for cont in contours:
    temp = cv2.approxPolyDP(cont, 0.1*cv2.arcLength(cont,True), True)
    area = cv2.contourArea(temp)
    if(area > maxArea):
        maxContour = cont
        maxArea = area

print(maxArea)
cv2.drawContours(img, [maxContour], -1, (0,255,255),10)

cv2.imshow("final", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
