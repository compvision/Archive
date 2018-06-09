#here is my outside work code.

import numpy as np
import cv2

#to change the Video feed
vid = 1
cap = cv2.VideoCapture(vid)
#to change the screen capture or webcam feed
screenCapOn = 0
count = -1

#save frames globally
frame1 = 0
frame2 = 0

while(1):
    # Take each frame


    if screenCapOn == 0:
        _, frame1 = cap.read()
        _, frame2 = cap.read()

        diff = cv2.absdiff(frame1,frame2)

        edges = cv2.Canny(diff,100,200)

        img = diff
        #img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        THRESHOLD_MIN = np.array([55, 29, 106],np.uint8)
        THRESHOLD_MAX = np.array([95, 255,248],np.uint8)

        #img_threshed  = cv2.inRange(img_hsv, THRESHOLD_MIN,THRESHOLD_MAX)
        #image, contours, count, = cv2.findContours(img_threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        #for cont in contours:
            #count = count +1
            #approx = cv2.approxPolyDp(cont, epsilon, True)

            #if  len(approx) == 4:
                #cv2.drawContours(image, contours, count,(255,255,255), 10)



    cv2.imshow('Difference',diff)
    cv2.imshow('edges', edges)
    #cv2.imshow('approx', approx)
    key = cv2.waitKey(1) & 0xFF

    #wait until the q key is pressed
    if key == ord('q'):
        break
