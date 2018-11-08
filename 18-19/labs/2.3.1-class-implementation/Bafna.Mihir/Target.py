class Target:
    corners = []
    Xmax = 0
    Ymax = 0
    Xmin = 1000
    Ymin = 1000
    Xmid = 0
    Ymid = 0

    def __init__(self,array):
        self.corners = array
        self.getMinMax()
        self.Xmid = int((self.Xmax+self.Xmin)/2)
        self.Ymid = int((self.Ymax+self.Ymin)/2)

    def getMinMax(self):
        for corner in self.corners:
            if(self.Xmax<corner[0][0]):
                self.Xmax = corner[0][0]
            if(self.Xmin>corner[0][0]):
                self.Xmin = corner[0][0]
            if(self.Ymax<corner[0][1]):
                self.Ymax = corner[0][1]
            if(self.Ymin>corner[0][1]):
                self.Ymin = corner[0][1]

    def topRight(self):
        return(self.Xmax,self.Ymin)

    def topLeft(self):
        return(self.Xmin,self.Ymin)

    def bottomRight(self):
        return(self.Xmax,self.Ymax)

    def bottomLeft(self):
        return(self.Xmin,self.Ymax)

    def middleLeft(self):
        return(self.Xmin,self.Ymid)

    def middleRight(self):
        return(self.Xmax,self.Ymid)

    def middleTop(self):
        return(self.Xmid,self.Ymin)

    def middleBottom(self):
        return(self.Xmid,self.Ymax)

    def center(self):
        return(self.Xmid,self.Ymid)

    def width(self):
        return(self.Xmax-self.Xmin)

    def height(self):
        return(self.Ymax-self.Ymin)
