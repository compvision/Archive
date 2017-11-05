#Written by Sahith Konakalla
#September 29, 2017

import sys
import cv2
import numpy as np

if (sys.argv[1] == "-i" and len(sys.argv) == 3):
    fileLocation = sys.argv[2]
    img = cv2.imread(fileLocation) 
    
    cv2.imshow("Image", img) 
    cv2.waitkey(0)
    
    cv2.destroyAllWindows()

elif (sys.argv[1] == "-l" and len(sys.argv) == 3):

    cv2.NamedWindow("Camera Feed", cv2.CV_WINDOW_AUTOSIZE)

    port = (int)(sys.argv[2])
    capture = cv2.CaptureFromCAM(port)

    while True:
       frame = cv2.QueryFrame(capture)
       cv2.ShowImage("Camera Feed", frame)

       key = cv2.waitKey(10)
       if key == 27:
           break
    cv2.destroyWindow("Camer Feed")

