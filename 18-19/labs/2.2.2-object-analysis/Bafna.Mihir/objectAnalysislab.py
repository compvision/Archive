import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

# definitions/instantiations to make code cleaner
img  = cv2.imread("ReflectiveRectangle.JPG")
h,w = img.shape[:2]
imgXcenter = w/2
imgYcenter = h/2
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
minThreshold = np.array([0,0,236],np.uint8)
maxThreshold = np.array([255,100,255],np.uint8)
threshold = cv2.inRange(hsv, minThreshold, maxThreshold)
lightblue = (255, 221, 0)
degrees = u'\N{DEGREE SIGN}'
centimeters = " cm"
focalLength = 700
height = 25
width = 50

def getMinMax():
    Xmax = 0
    Ymax = 0
    Xmin = 1000
    Ymin = 1000
    for corner in approx:
        if(Xmax<corner[0][0]):
            Xmax = corner[0][0]
        if(Xmin>corner[0][0]):
            Xmin = corner[0][0]
        if(Ymax<corner[0][1]):
            Ymax = corner[0][1]
        if(Ymin>corner[0][1]):
            Ymin = corner[0][1]
    return(Xmax,Xmin,Ymax,Ymin,(Xmax-Xmin))

def findDistanceAzimuth(f,w,iw,x,h):
    d = (f*w)/iw
    az = math.atan(x/f)*180/math.pi
    al = math.atan(h/f)*180/math.pi
    return round(d,2),round(az,4),round(al,4)


# main code
HSV,contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    epsilon = 0.1 * cv2.arcLength(contours[c],True)
    approx = cv2.approxPolyDP(contours[c],epsilon, True)
    if(len(approx)==4 and cv2.contourArea(approx)>300):
        cv2.drawContours(img, contours, c, lightblue, 2)
        Xmax,Xmin,Ymax,Ymin,ImageWidth= getMinMax()
        Xcenter = int((Xmax+Xmin)/2)
        Ycenter = int((Ymax+Ymin)/2)
        xfromcenter = imgXcenter-Xcenter
        yfromcenter = imgYcenter-Ycenter

cv2.line(img,(Xcenter,Ycenter),(Xcenter,Ycenter),lightblue,5)  # center point for testing
distance,azimuth,altitude = findDistanceAzimuth(focalLength,width,ImageWidth,xfromcenter,yfromcenter)
cv2.imshow("drawContours", img)

print("\n"+"Distance = " + str(distance)+centimeters)
print("Azimuth = " + str(azimuth)+degrees)
print("Angle of Altitude = "+ str(altitude)+degrees+"\n")


cv2.waitKey(0)
