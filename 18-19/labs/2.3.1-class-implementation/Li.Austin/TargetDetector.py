import cv2
import numpy as np

class TargetDetector(object):
    """description of class"""
    def __init__(self, img):
        self.img = img
        self.img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
    def threshold(self, min, max):
       THRESHOLD_MIN = np.array(min, np.uint8)
       THRESHOLD_MAX = np.array(max, np.uint8)
       self.thresh = cv2.inRange(self.img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)
    def findRect(self):
        result = []
        img_thresh, contours, hierarchy = cv2.findContours(self.thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        count = 0
        for cont in contours:
            epsilon = 0.01 * cv2.arcLength(cont, True)
            approx = cv2.approxPolyDP(cont, epsilon, True)
            if len(approx) == 4 and cv2.contourArea(approx) > 5:
                cv2.drawContours(self.img, contours, count, (255, 0, 0), 4)
                result.append(approx)
            count += 1
        #cv2.imshow(":f", self.img)
        #cv2.waitKey(0)
        return result