import numpy as np
import cv2
class TargetDetector:
    lightblue = (255, 221, 0)

    def __init__(self):
        pass

    def getThreshold(self,min,max,frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv, min, max)
        return thresh

    def getContours(self,threshold,frame):
        HSV,contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for c in range(len(contours)):
            epsilon = 0.1 * cv2.arcLength(contours[c],True)
            approx = cv2.approxPolyDP(contours[c],epsilon, True)
            if(len(approx)==4 and cv2.contourArea(approx)>100):
                cv2.drawContours(frame, contours, c, self.lightblue, 2)
                return approx
