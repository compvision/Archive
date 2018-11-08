import cv2
import numpy as np
from Main import Main

img = cv2.imread("2.2.1 Object Detection Lab Image.jpg")
main = Main(img)
print(main.distance(), main.azimuth(), main.altitude())
main.display()
