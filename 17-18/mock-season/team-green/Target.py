import cv2
import math

class Target:
    def __init__(self):
        self.ang = math.atan2(0.0508,0.2032)
        
    def createTarget (self, temp):

        self.cont = temp
        
        avgX = 0

        avgY = 0
  
        minX = temp[0][0][0]

        maxX = temp[0][0][0]
   
        minY = temp[0][0][1]

        maxY = temp[0][0][1]
        
        pref = temp[0]
        
        hyp = 0
   
        #sets mins and maxs based on the first points x and y, to be changed later
        #temp is an input from approxpolydp, an array of points, of a single target (one rectangle)
        
        for p in temp: #iterate through each point
            
            if p[0][0] < minX: #if the point's x is less than the lowest x previouly
                minX = p[0][0] #set lowest x to current points x
            
            if p[0][0] > maxX:
                maxX = p[0][0]
			
            if p[0][1] < minY:
                minY = p[0][1]
            
            if p[0][1] > maxY:
                maxY = p[0][1]
            
            hyp1 = math.sqrt((temp[0][0][0]-p[0][0])**2 + (temp[0][0][1] - p[0][1])**2)
                             
            if hyp1 > hyp:
                hyp = hyp1
                
            #minX, maxX, minY, maxY will have their respective values based off all the points in temp

        self.width1 = maxX-minX #width is highest x minus lowest x
        
        self.height1 = maxY-minY#height is highest y minus lowest y
        
        
        
        self.height = hyp*math.sin(self.ang)*0.677
        
        self.width = hyp*math.cos(self.ang)*0.677
        
        avgX = (maxX+minX)/2 
        
        avgY = (maxY+minY)/2
        
        self.centerPoint = [avgX, avgY] #the center is the average x and y in an array
    
   
    def getWidth(self):
        
        return self.width
    
    def getHeight(self):
        
        return self.height
    
    def getCenter(self):
        
        return self.centerPoint
    
    def getType(self):

        if (self.width1 > self.height1):
            if (math.fabs(self.ang - math.atan2(self.height1,self.width1)) > .1):
                return "S"
            else:
                return "H"
        elif (self.height1 > self.width1):
            if (math.fabs(self.ang - math.atan2(self.width1,self.height1)) > .2):
                print (math.fabs(self.ang - math.atan2(self.width1,self.height1)))
                return "S"
            else:
                return "V"
        else:
            return "Error"
        
            
    #returns respective values

        