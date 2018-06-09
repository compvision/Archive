import cv2
import math

class Target:

	def firstImage(self, approx):
		maxX = approx[0][0][0] 
		minX = 200000.0
		maxY = 0.0
		minY = 200000.0

		for i in approx:
			if (i[0][0] > maxX):
				#global maxX
				maxX = i[0][0]
			elif i[0][0]<minX:
				#global minX
				minX = i[0][0]
			if i[0][1]>maxY:
				#global maxY
				maxY = i[0][1]
			elif i[0][1]<minY:
				#global minY
				minY = i[0][1]
		self.width1 = maxX - minX
		self.height1 = maxY - minY
		self.centerX = (maxX+minX)/2
	def secondImage(self, approx):
		maxX = approx[0][0][0]
		minX = 200000.0
		maxY = 0.0
		minY = 200000.0

		for i in approx:
			if (i[0][0] > maxX):
				maxX = i[0][0]
			elif i[0][0]<minX:
				minX = i[0][0]
			if i[0][1]>maxY:
				maxY = i[0][1]
			elif i[0][1]<minY:
				minY = i[0][1]
		self.width2 = maxX - minX
		self.height2 = maxY - minY
	def getOrientation1(self):
		self.orientation1 = "NONE"
		if (1.0*self.height1)/(1.0*self.width1) < 0.33: #0.5*self.height is the threshold for error
			self.orientation1 = "HORIZONTAL"
		elif (1.0*self.height1)/(1.0* self.width1) > 3.0:
			self.orientation1 = "VERTICAL"
		else:
			self.orientation1 = "SPINNING"
		#self.orientation1 = orientation1
		return self.orientation1
	def getOrientation2(self):
		self.orientation2 = "NONE"
		if (1.0*self.height2)/(1.0*self.width2) < 0.33:
			self.orientation2 = "HORIZONTAL"
		elif (1.0*self.height2)/(1.0*self.width2) > 3.0:
			self.orientation2 = "VERTICAL"
		else:
			self.orientation2 = "SPINNING"
		#self.orientation2 = orientation2
		return self.orientation2
	def finalOrientation(self):
		if self.orientation1 == self.orientation2:
			self.finOrientation = self.orientation1
			return self.orientation1
		else:
			self.finOrientation = "SPINNING"
			return "SPINNING"
