from Target import Target
from TargetDetector import TargetDetector as Detector
from TargetProcessor import TargetProcessor as Processor
import numpy as np
import cv2

lightblue = (255, 221, 0)
# distance = 2.54*18
# actualWidth = 20.3
focalLength = 700
# actualHeight = 25
actualWidth = 50
minThreshold = np.array([0,0,236],np.uint8)
maxThreshold = np.array([255,100,255],np.uint8)

#----------------------------- FOR STILL FRAMES -------------------------------#
frame  = cv2.imread("ReflectiveRectangle.JPG")
h,w = frame.shape[:2]
imgXcenter = w/2
imgYcenter = h/2

det = Detector()
threshold = det.getThreshold(minThreshold,maxThreshold,frame)
corners = det.getContours(threshold,frame)

target = Target(corners)
Xmid,Ymid = target.center()

processor = Processor()
d,az,al = processor.findDistanceAzimuth(focalLength,actualWidth,target.width(),Xmid-imgXcenter,imgYcenter-Ymid)
processor.displayValues(d,az,al)

cv2.imshow("drawContours", frame)

cv2.waitKey(0)

#-------------------- FOR LIVE VIDEO (comment above code) ---------------------#
# cam = cv2.VideoCapture(0)
#
# while(True):
#     ret, frame = cam.read()
#     h,w = frame.shape[:2]
#     imgXcenter = w/2
#     imgYcenter = h/2
#     if not ret:
#         continue
#
#     threshold = Detector.getThreshold(minThreshold,maxThreshold,frame)
#     corners = Detector.getContours(threshold,frame)
#
#
#     target = Target(corners)
#     Xmid,Ymid = target.Center()
#     d,az,al = Processor.findDistanceAzimuth(focalLength,actualWidth,target.width(),Xmid-imgXcenter,imgYcenter-Ymid)
#     Processor.displayValues(d,az,al)
#
#     cv2.imshow("drawContours", frame)
#
#     if cv2.waitKey(10) == 27:
#         cv2.destroyAllWindows()
#         break
