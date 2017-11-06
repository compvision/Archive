import numpy as np
import cv2
import math

Video_capture = cv2.VideoCapture(1)
switch = 0
THRESHOLD_MIN = np.array([53,5,5],np.uint8)
THRESHOLD_MAX = np.array([58,255,255],np.uint8)

#def __init__(self):

while(True):
    cv2.namedWindow('Output', cv2.WINDOW_NORMAL)

    ret,frame = Video_capture.read()

    if(switch == 1 or switch == 2):
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        frame_threshed = cv2.inRange(hsv_img, THRESHOLD_MIN, THRESHOLD_MAX)

        if(switch == 1):
            cv2.imshow('Output', frame_threshed)

        image, contours, hierarchy = cv2.findContours(frame_threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(image, contours, -1, (255,255,255), 1)

        if(switch == 2):
            cv2.imshow('Output', image)
    if(switch == 0):
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
        THRESHOLD_MIN = np.array([0,5,5],np.uint8)
        THRESHOLD_MAX = np.array([10,255,255],np.uint8)
    if key == 103:
        #green
        THRESHOLD_MIN = np.array([120,5,5],np.uint8)
        THRESHOLD_MAX = np.array([130,255,255],np.uint8)
    if key == 119:
        #white
        THRESHOLD_MIN = np.array([53,5,5],np.uint8)
        THRESHOLD_MAX = np.array([58,255,255],np.uint8)
    if key == 121:
        #yellow
        THRESHOLD_MIN = np.array([53,5,5],np.uint8)
        THRESHOLD_MAX = np.array([63,255,255],np.uint8)
    if key == 111:
        #orange
        THRESHOLD_MIN = np.array([34,5,5],np.uint8)
        THRESHOLD_MAX = np.array([44,255,255],np.uint8)
    if key == 98:
        #blue
        THRESHOLD_MIN = np.array([187,5,5],np.uint8)
        THRESHOLD_MAX = np.array([197,255,255],np.uint8)
