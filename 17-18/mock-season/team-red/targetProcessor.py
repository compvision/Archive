import numpy as np
import math

from Target import Target

class targetProcessor:
	def __init__(self):
		self.RectHeight = 0.05
		self.RectWidth = 0.20
		self.focalLen = 720
		self.horizCent = 240
		self.vertiCent = 320
	def loadTarget(self, target):
		self.imgWidth = target.width1
		self.imgHeight = target.height1
		self.centerX = target.centerX
		self.offsetX = float(self.centerX -self.horizCent)
	def findAzimuth(self):
		azimuth = np.arctan(self.offsetX/ self.focalLen)*180/math.pi
		return (azimuth)
