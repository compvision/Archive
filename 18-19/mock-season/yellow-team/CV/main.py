from Target import Target
from TargetDetector import TargetDetector as Detector
from TargetProcessor import TargetProcessor as Processor
from Network import Network
import numpy as np
import cv2

crossActualWidth = 2.54*6.5
rectActualWidth = 2.54*7.5
isRect = False
isCross = False
minThreshold = np.array([0,30,60],np.uint8)
maxThreshold = np.array([255,255,255],np.uint8)
# minThreshold = np.array([30,0,200],np.uint8)
# maxThreshold = np.array([90,255,255],np.uint8)
# minThreshold = np.array([50,0,240],np.uint8)
# maxThreshold = np.array([60,255,255],np.uint8)
lightblue = (255, 221, 0)                                                       # variable for the lightblue color
focalLength = 720                                                               # focal length of camera
degrees = u'\N{DEGREE SIGN}'                                                    # for degree sign usage
centimeters = " cm"

# method that prints out the values in a nice format
def displayValues():
    cv2.putText(contoured,"Distance: "+str(proc.getDistance()/2.54)+centimeters, (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255))
    cv2.putText(contoured,"Azimuth: "+str(proc.getAzimuth()), (0,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255))
    cv2.putText(contoured,"Altitude: "+str(proc.getAltitude()), (0,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255))
    # for printing in terminal
    # print("\n"+"Distance = " + str(proc.getDistance())+centimeters)
    # print("Azimuth = " + str(proc.getAzimuth())+degrees)
    # print("Angle of Altitude = "+ str(proc.getAltitude())+degrees+"\n")

#------------------------------- FOR LIVE VIDEO -------------------------------#
cam = cv2.VideoCapture(0)

network = Network()
network.userServer()

while(True):                                                                    # while loop for continuous analyzation of frames through video capture
    network.waitForPing()

    ret, frame = cam.read()
    h,w = frame.shape[:2]                                                       # gets the height and width of the frame for analyzation purposes
    imgXcenter = w/2
    imgYcenter = h/2
    det = Detector()                                                            # makes a new TargetDetector object
    proc = Processor()                                                          # makes a new TargetProcessor object
    if not ret:                                                                 # checks if boolean value ret is false
        continue

    threshold = det.threshold(minThreshold,maxThreshold,frame)                  # getting thresholded frame
    det.Contours(threshold)                                                     # finding contours based on thresholded frame
    det.filterContours()                                                        # filtering the contours by size and number
    contours,index,corners,isCross,isRect = det.getContours()                                  # getting the contours, specific index, and array of corners


    if (corners is not None):                                                   # checking if the corners array returned is not null
        target = Target(corners)                                                # making a new Target object
        Imagewidth = target.getWidth()
        Xmid,Ymid = target.getCenter()
        cv2.line(frame,(Xmid,Ymid),(Xmid,Ymid),lightblue,5)
        cv2.drawContours(frame, contours, index, lightblue, 8)
        if(isRect):
            proc.calculate(focalLength,rectActualWidth,Imagewidth,Xmid-imgXcenter,imgYcenter-Ymid)
            network.setRectAzi(proc.getAzimuth())
        if(isCross):
            proc.calculate(focalLength,crossActualWidth,Imagewidth,Xmid-imgXcenter,imgYcenter-Ymid)
            network.setCrossAzi(proc.getAzimuth())
    contoured=cv2.resize(frame,None,fx=0.5,fy=0.5)
    threshed=cv2.resize(threshold,None,fx=0.5,fy=0.5)


    displayValues()                                                             # method displays values in terminal
    cv2.imshow("contoured", contoured)
    cv2.imshow("threshed", threshed)
    cv2.moveWindow("contoured", 0,20)
    cv2.moveWindow("threshed", 650,20)
    key = cv2.waitKey(10)

    if key == 27:
        cv2.destroyAllWindows()
        break
    # elif key == 116:
    #     cv2.destroyWindow("contoured")
    #     cv2.imshow("threshed", threshed)
    # elif key == 99:
    #     cv2.destroyWindow("threshed")
    #     cv2.imshow("contoured", countoured)
