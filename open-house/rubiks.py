import numpy as np
import cv2
import math

Video_capture = cv2.VideoCapture(1)
switch = 0
THRESHOLD_MIN = np.array([53,5,5],np.uint8)
THRESHOLD_MAX = np.array([58,255,255],np.uint8)

#def __init__(self):

num = 0
total = 0

while(True):
    cv2.namedWindow('Output',cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Output', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    ret,frame = Video_capture.read()

    if(switch == 1 or switch == 2):
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        frame_threshed = cv2.inRange(hsv_img, THRESHOLD_MIN, THRESHOLD_MAX)

        if(switch == 1):
            cv2.imshow('Output', frame_threshed)

        image, contours, hierarchy = cv2.findContours(frame_threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #cv2.drawContours(image, contours, -1, (255,255,255), 1)

        if(switch == 2):
            #cv2.imshow('Output', image)
            for count, cont in enumerate(contours):
                epsilon = 0.1*cv2.arcLength(cont, True)
                approx = cv2.approxPolyDP(cont, epsilon, True)
                
                if cv2.contourArea(approx) > 500 and len(approx) == 4:
                    cv2.drawContours(image, contours, count, (255,255,255), 2)
            
            cv2.imshow('Output', image)
            
    elif(switch == 0):
        cv2.imshow('Output', frame)

    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow('Output')
        break
    if key == 32:
        if(switch == 2):
            switch = -1
        switch = switch + 1
    if key == 114:
        #red
        #THRESHOLD_MIN = np.array([0,5,5],np.uint8)
        #THRESHOLD_MAX = np.array([10,255,255],np.uint8)
        THRESHOLD_MIN = np.array([160,5,5],np.uint8)
        THRESHOLD_MAX = np.array([180,255,255],np.uint8)
    if key == 103:
        #green
        #THRESHOLD_MIN = np.array([120,5,5],np.uint8)
        #THRESHOLD_MAX = np.array([130,255,255],np.uint8)
        THRESHOLD_MIN = np.array([60,5,5],np.uint8)
        THRESHOLD_MAX = np.array([82,255,255],np.uint8)
    if key == 119:
        #white
        #THRESHOLD_MIN = np.array([53,5,5],np.uint8)
        #THRESHOLD_MAX = np.array([58,255,255],np.uint8)
        THRESHOLD_MIN = np.array([10,5,5],np.uint8)
        THRESHOLD_MAX = np.array([26,255,255],np.uint8)
    if key == 121:
        #yellow
        #THRESHOLD_MIN = np.array([5,53,5],np.uint8)
        #THRESHOLD_MAX = np.array([63,255,255],np.uint8)
        THRESHOLD_MIN = np.array([18,5,5],np.uint8)
        THRESHOLD_MAX = np.array([28,255,255],np.uint8)
    if key == 111:
        #orange
        #THRESHOLD_MIN = np.array([34,5,5],np.uint8)
        #THRESHOLD_MAX = np.array([44,255,255],np.uint8)
        THRESHOLD_MIN = np.array([0,5,5],np.uint8)
        THRESHOLD_MAX = np.array([10,255,255],np.uint8)
    if key == 98:
        #blue
        #THRESHOLD_MIN = np.array([187,5,5],np.uint8)
        #THRESHOLD_MAX = np.array([197,255,255],np.uint8)
        THRESHOLD_MIN = np.array([95,5,5],np.uint8)
        THRESHOLD_MAX = np.array([110,255,255],np.uint8)
