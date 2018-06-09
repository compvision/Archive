import cv2
import numpy as np
import math
class TargetDetector:
    def __init__(self): #sets default threshold values
        self.minHue = 50
        self.maxHue = 70
        self.minSat = 0
        self.maxSat = 255
        self.minVal = 230
        self.maxVal = 255
        self.found = False
    def threshInputs(self, th):
        self.minHue = th[0]
        self.maxHue = th[1]
        self.minHue = th[2]
        self.maxHue = th[3]
        self.minVal = th[4]
        self.maxVal = th[5]
        #changes threshold values based on inputs
        
    def targetDetect(self, img):
        def angle(p1, p2, p0):
            dx1 = p1[0][0]-p0[0][0]
            dy1 = p1[0][1]-p0[0][1]
            dx2 = p2[0][0]-p0[0][0]
            dy2 = p2[0][1]-p0[0][1]
            return math.atan(dy1/dx1)-math.atan(dy2/dx2)
            #used by plugging 3 points and outputting the angle it makes

        def right(app, x):
            maxCosine = 0
            for k in range(2, x+1):
                pt1 = app[k%4]
                pt2 = app[k-2]
                pt0 = app[k-1]
                cos = (angle(pt1, pt2, pt0))
                cosine = math.fabs(math.cos(cos))
                maxCosine = max(maxCosine, cosine)
                if(maxCosine<.2):
                    return True
                else:
                    return False
        self.found = False
            #checks for right angles in a target based on how many vertices it should have
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #converts to HSV colorspace

        THRESHOLD_MIN = np.array([self.minHue, self.minSat, self.minVal],np.uint8)
        THRESHOLD_MAX = np.array([self.maxHue, self.maxSat,self.maxVal],np.uint8)
        
        frame = cv2.inRange(img_hsv, THRESHOLD_MIN,THRESHOLD_MAX)
        
        #cv2.imshow('thehe', frame)
        
        count = -1
        
        image, contours, hierarchy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #finds contours in the thresholded image

        for cont in contours: #goes through each contour out of the set, outputted by findContours
            count = count +1
            epsilon = 0.02*cv2.arcLength(cont,True)
            approx = cv2.approxPolyDP(cont, epsilon, True) #approximates a shape out of the contours (orners only)
            if cv2.contourArea(approx) > 1000 and len(approx) == 4: #shape has 4 corners and is not extremely small
            #if right(approx,34):
                approx2 = [approx]
                cv2.drawContours(img, approx2, -1, (255,255,0), 10)
                cv2.drawContours(img, approx, 0, (0,0,255), 10)#draws the contours onto live feed image
                self.found = True
                return approx

                
    def getFound(self):
        return self.found