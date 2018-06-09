from CmdLineInterface import CmdLineInterface
from Target import Target
from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor
from VideoDevice import VideoDevice
from GUIManager import GUIManager
from AppConfig import AppConfig
from network import Network
#imports all classes (from file import class)

import numpy as np
import cv2
import math
from socket import *
import sys
import random
#imports libraries

soc = None
conn = None
connected = False

network1 = None
detector = TargetDetector()
mdetector = TargetDetector()
processor = TargetProcessor()
target = Target()
#mprocessor = TargetProcessor()
camera = VideoDevice()

cmdinp = ["main.py", "-d", "1", "--no-networking", "--isDebug"]
slide = False
interface = CmdLineInterface(cmdinp)

#interface = CmdLineInterface(sys.argv) #cmdline input
config = interface.getConfig() #AppConfig object that contains all values from cmdline inputs
gui = GUIManager()
#creates class instances
def nothing(x):
    pass
    

if(config.getIsNetworking()==1):
    if (config.getIsDebug()):
        print ("Networking On\n")
        
    global network1 
    
    if (config.getIsDebug()):
        print ("Creating Network Object\n")
    
    network1 = Network() #creates networking object
    
    if (config.getIsDebug()):
        print ("Creating Network Server\n")
        
    network1.userServer() #creates server
    
elif(config.getIsNetworking==0):
    if (config.getIsDebug()):
        print ("Networking Off\n")
    
camera.startCapture(config.getDeviceID()) #inputs device id from config


if(config.getIsDebug()):
    print("Camera is ready\n")
    #gui.threshWindow()

loop = 1
image = camera.getImage()

while(cv2.waitKey(30) != 27):
    if ((loop % 3) != 0):
        continue
    
    print ("While Loop " + str(loop) + "  \n")
    
    minHue=50
    maxHue=60
    minSat=0
    maxSat=255
    minVal=240
    maxVal=255
    
    thIn = [minHue, maxHue, minSat, maxSat, minVal, maxVal] #thresholding values subject to change
    detector.threshInputs(thIn)
    image = camera.getImage() #live feed image
		
    if(config.getIsDebug()):
        print("Image Read\n")

    detected = detector.targetDetect(image)
    #image is entered into TargetDetect method, outputs an array of points (corners)
    if(config.getIsDebug()):
        print("Image Processed by Target Detector\n")
        
    
    if (detector.getFound() == True): #if target was found
        
        if(config.getIsDebug()):
            print("Target Found\n")

        target.createTarget(detected)#inputs the array of corners into Target object
        
        print (target.getType())
        
        if(config.getIsDebug()):
            print("Image Analyzed\n")
    
        if(config.getIsDebug()):
            print ("Image Being Processed by Target Processor\n")
    
        processor.loadTarget(target)#enters Target instance into processor object instance
        
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
    
        dis = "distance: %s" % distance
        azi = "azimuth: %s" % azimuth
        alt = "altitude: %s" % altitude
        typ = target.getType()
        if(config.getIsNetworking()):
            network1.setDistance(str(distance))
            network1.setAzimuth(str(azimuth))
            network1.setAltitude(str(altitude))
            network1.setOrientation(str(typ))
            #sends distance, azimuth and altitude values with network object
        #wid = "Image Width: %s" % target.getWidth()
        
    else:
        dis = "Not Found"
        azi = "Not Found"
        alt = "Not Found"
        typ = "None"

    hue = "Hue: %s - %s" % (thIn[0], thIn[1])
    val = "Value: %s - %s" % (thIn[4], thIn[5])
    gui.setImage(image) #places image into GUIManager object instance
    gui.setText(hue, -2)
    gui.setText(val, -1)
    gui.setText(typ, 0)
    gui.setText(dis, 1)
    gui.setText(azi, 2)
    gui.setText(alt, 3)
    #adds various texts to the image in GUIManager object
    cv2.imshow("Targeting", gui.getImage()) #shows image from gui object
    loop += 1

cv2.destroyAllWindows()
