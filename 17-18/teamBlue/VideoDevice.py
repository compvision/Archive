import cv2
import numpy as np
import math

public class:
	cv2.namedWindow("Live Feed", cv2.WINDOW_AUTOSIZE)
	capture = cv2.VideoCapture(0)
	while True:
		ret, frame = capture.read()
		cv2.imshow("Live Feed", frame)
		key = cv2.waitKey(10)
		if key == 27:
			break
			cv2.destroyWindow("Live Feed")

