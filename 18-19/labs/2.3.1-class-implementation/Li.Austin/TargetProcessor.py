import numpy as np

class TargetProcessor(object):
    """description of class"""
    def __init__(self, img, contours):
        self.focal = 700
        self.width, self.height = (50, 25)
    def distance(self, xmin, xmax):
        return (self.focal * self.width)/(xmax - xmin)
    def azimuth(self, center, img_center):
        return np.rad2deg(np.arctan2(center[0] - img_center[0], self.focal))
    def altitude(self, center, img_center):
        return np.rad2deg(np.arctan2(-(center[1] - img_center[1]), self.focal))