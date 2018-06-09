from CmdLineInterface import CmdLineInterface
from Target import Target
from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor
from VideoDevice import VideoDevice
from GUIManager import GUIManager
from AppConfig import AppConfig
#imports all classes

import numpy as np
import cv2
import math
from socket import *
import sys
import network
import random

lastTarget = []
soc = None
conn = None
connected = False

network1 = None

detector = TargetDetector()
processor = TargetProcessor()
camera = VideoDevice()
iterator = 0

#cmdinp = ["main.py", "-d", "0", "--no-networking", "--isDebug"]
#interface = CmdLineInterface(cmdinp)

interface = CmdLineInterface(sys.argv) #cmdline input
config = interface.getConfig() #AppConfig object that contains all values from cmdline inputs
if(config.getIsHeadless() == 0):
    gui = GUIManager()
networking = config.getIsNetworking()
if(networking):
    global network1
    network1 = network.Network()
    network1.userServer()

#creates class instances
camera.startCapture(config.getDeviceID()) #inputs device id from config

if(config.getIsDebug()):
    print("Camera is ready\n")
    #gui.threshWindow()

loop = 1

while(cv2.waitKey(30) != 27):
    loop += 1
    iterator = iterator + 1
    print ("While Loop " + str(loop) + "  \n")
    thIn = [50, 60, 5, 255, 235, 255] #thresholding values subject to change
    detector.threshInputs(thIn)

    image = camera.getImage() #live feed image
    if((iterator%3) != 0):
        continue

    if(config.getIsDebug()):
        print("Image Read\n")

    detected = detector.TargetDetect(image)
    #image is entered into TargetDetect method, outputs an array of points (corners)
    if(config.getIsDebug()):
            print("Image Processed by Target Detector\n")



    if (detector.getFound() == True): #if target was found

        if(config.getIsDebug()):
            print("Target Found\n")


        target = Target(detected)
        orient = target.Orientation()


        if(config.getIsDebug()):
            print("Image Analyzed\n")

        if(config.getIsDebug()):
            print ("Image Being Processed by Target Processor\n")

        processor.loadTarget(target) #enters Target instance into processor object instance

        if(config.getIsDebug()):
            print("Target Loaded\n")

        distance = processor.findDistance() #outputs distance found through TargetProcessor

        if(config.getIsDebug()):
            print("Distance Calculated\n")

        azimuth = processor.findAzimuth() #outputs azimuth found through TargetProcessor

        if(config.getIsDebug()):
            print("Azimuth Calculated\n")

        altitude = processor.findAltitude() #outputs altitude found through TargetProcessor

        if(config.getIsDebug()):
            print("Altitude Calculated\n")

        if(config.getIsDebug()):
            print("Image Processed by TargetProcessor\n")

        dis = "distance: %s" % (distance/0.6)
        azi = "azimuth: %s" % azimuth
        alt = "altitude: %s" % altitude
        ori = "orientation: %s" % orient

        print(dis)
        print(azi)
        print(alt)
        print(ori)

        if(networking):
            network1.setDistance(str(distance))
            network1.setAzimuth(str(azimuth))
            network1.setAltitude(str(altitude))
            network1.setOrientation(str(orient))
        #wid = "Image Width: %s" % target.getWidth()

    else:
        dis = "Not Found"
        azi = "Not Found"
        alt = "Not Found"
    hue = "Hue: %s - %s" % (thIn[0], thIn[1])
    val = "Value: %s - %s" % (thIn[4], thIn[5])
    if(config.getIsHeadless() == 0):
        gui.setImage(image) #places image into GUIManager object instance
        gui.setText(hue, -2)
        gui.setText(val, -1)
        #gui.setText(wid, 0)
        gui.setText(dis, 1)
        gui.setText(azi, 2)
        gui.setText(alt, 3)
        #adds various texts to the image in GUIManager object
        cv2.imshow("Targeting", gui.getImage()) #shows image from gui object


cv2.destroyAllWindows()
