import cv2
import numpy as np

src = cv2.imread("rect2.jpg")

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

lower = np.array([0, 0, 200])
upper = np.array([255, 40, 255])
mask = cv2.inRange(hsv, lower, upper)

_, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, 
cv2.CHAIN_APPROX_SIMPLE)
#epsilon = 0.1 * cv2.arcLength(contours, True)
#approx = cv2.approxPolyDP(contours, epsdeilon, True)

for x in range (len(contours)):
    if cv2.contourArea(contours[x]) > 300:
        cv2.drawContours(src, contours, x, (0, 255, 0), 3)


cv2.namedWindow("Frame")
cv2.namedWindow("Mask")

cv2.imshow("Frame", src)
cv2.imshow("Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

