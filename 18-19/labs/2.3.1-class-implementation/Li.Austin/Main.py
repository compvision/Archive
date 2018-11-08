import cv2
from TargetDetector import TargetDetector
from Target import Target
from TargetProcessor import TargetProcessor

class Main(object):
    """description of class"""
    def __init__(self, img):
        self.img = cv2.resize(img, (0, 0), fx = 0.2, fy = 0.2)
        self.detect = TargetDetector(self.img)
        self.detect.threshold([0, 0, 200], [255, 100, 255])
        self.target = Target(self.img, self.detect.findRect())
        self.processor = TargetProcessor(self.img, self.detect.findRect())
    def display(self):
        cv2.imshow("dd", self.img)
        cv2.waitKey(0)
    def distance(self):
        return self.processor.distance(self.target.xmin, self.target.xmax)
    def azimuth(self):
        return self.processor.azimuth(self.target.center(), self.target.img_center())
    def altitude(self):
        return self.processor.altitude(self.target.center(), self.target.img_center())