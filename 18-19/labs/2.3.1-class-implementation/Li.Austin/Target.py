class Target(object):
    """description of class"""
    def __init__(self, img, contours):
        self.img = img
        self.xmin, self.ymin = img.shape[:2]
        self.xmax, self.ymax = (0, 0)
        for cont in contours:
            for i in range(len(cont)):
                x = cont[i][0][0]
                y = cont[i][0][1]
                if x < self.xmin:
                    self.xmin = x
                if x > self.xmax:
                    self.xmax = x
                if y < self.ymin:
                    self.ymin = y
                if y > self.ymax:
                    self.ymax = y
    def width(self):
        return self.xmax - self.xmin
    def center(self):
        return ((self.xmin + self.xmax)/2, (self.ymin + self.ymax)/2)
    def img_center(self):
        return (self.img.shape[0]/2, self.img.shape[1]/2)