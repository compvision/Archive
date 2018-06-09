import numpy as np
import math

from Target import Target
class TargetProcessor:
    def __init__(self):
        self.RectHeight = 0.05
        self.RectWidth = 0.20
        self.RectHypotenuse = 0.21
        self.focalLen = 480
        self.horizCent = 240
        self.vertiCent = 320
        #sets non changing values when object instance is created
    def loadTarget(self, target): #inputs a Target object
        self.imgWidth = target.getWidth()
        self.imgHeight = target.getHeight()
        imgCenter = target.getCenter()
        self.hypotenuse = target.getHypotenuse()
        RectcentX = imgCenter[0]
        RectcentY = imgCenter[1]
        self.offsetX = float(RectcentX - self.horizCent)
        self.offsetY = float(-1*(RectcentY - self.vertiCent))
        #uses target methods to find changing values

    def findDistance(self):
        if self.hypotenuse == 0: #makes sure not dividing by 0
            self.hypotenuse = 1
        dist = float(self.RectHypotenuse * self.focalLen) / self.hypotenuse #calculates distance using objects values
        return (dist)

    def findAzimuth(self):
        azimuth = np.arctan(self.offsetX/ self.focalLen)*180/math.pi #calculates azimuth using objects values
        return (azimuth)

    def findAltitude(self):
        altit = np.arctan(self.offsetY/ self.focalLen)*180/math.pi #calculates altitude using objects values
        return (altit)
