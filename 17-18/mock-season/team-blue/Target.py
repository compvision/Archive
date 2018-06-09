import cv2

class Target:

    def __init__ (self, temp):

        self.hypotenuse = 0

        avgX = 0

        avgY = 0

        minX = temp[0][0][0]

        maxX = temp[0][0][0]

        minY = temp[0][0][1]

        maxY = temp[0][0][1]
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

            hyp = ((temp[0][0][0]-p[0][0])**2 + (temp[0][0][1]-p[0][1])**2)**(1/2)

            #minX, maxX, minY, maxY will have their respective values based off all the points in temp
            if (hyp > self.hypotenuse):
                self.hypotenuse = hyp

        self.width = maxX-minX #width is highest x minus lowest x

        self.height = maxY-minY#height is highest y minus lowest y

        avgX = (maxX+minX)/2

        avgY = (maxY+minY)/2

        self.centerPoint = [avgX, avgY] #the center is the average x and y in an array

    def getHypotenuse(self):

        return self.hypotenuse

    def getWidth(self):

        return self.width

    def getHeight(self):

        return self.height

    def getCenter(self):

        return self.centerPoint

    def Orientation(self):
        if(self.width < (4*self.height + self.width/2) and (self.width > 4*self.height - self.width/2)):
            return "H"
        elif(self.height < (4*self.width + self.height/2) and (self.height > 4*self.width - self.height/2)):
            return "V"
        else:
            return "S"
    #returns respective orientation
