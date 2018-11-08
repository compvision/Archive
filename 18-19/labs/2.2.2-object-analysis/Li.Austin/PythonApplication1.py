import cv2
import numpy as np

print(cv2.__version__)
img = cv2.imread("2.2.1 Object Detection Lab Image.jpg")
img = cv2.resize(img, (0, 0), fx = 0.2, fy = 0.2)
#cv2.imshow("o", img)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV", img_hsv)

THRESHOLD_MIN = np.array([0, 0, 200], np.uint8)
THRESHOLD_MAX = np.array([255, 100, 255], np.uint8)
thresh = cv2.inRange(img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

count = 0
xmin, ymin = img_hsv.shape[:2]
xmax, ymax = (0, 0)
for cont in contours:
    epsilon = 0.01 * cv2.arcLength(cont, True)
    approx = cv2.approxPolyDP(cont, epsilon, True)
    if len(approx) == 4 and cv2.contourArea(approx) > 5:
        print(approx)
        cv2.drawContours(img, contours, count, (255, 0, 0), 4)
        for i in range(len(approx)):
            print(approx)
            x = approx[i][0][0]
            y = approx[i][0][1]
            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            if y > ymax:
                ymax = y
    count += 1
xcenter = (xmin + xmax)/2
ycenter = (ymin + ymax)/2
print(xmin, xmax, ymin, ymax)
distance = (700 * 50)/(xmax - xmin)
azimuth = np.rad2deg(np.arctan2(xcenter - img_hsv.shape[0]/2, 700))
altitude = np.rad2deg(np.arctan2(-(ycenter - img_hsv.shape[1]/2), 700))
print(distance, azimuth, altitude)
cv2.imshow("f", img)
cv2.waitKey(0)