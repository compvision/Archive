#include "targetDetector.hpp"

targetDetector::targetDetector(){

}

Target targetDetector::processImage(Mat image){}

  VideoCapture cap(0); // open the default camera
  if(!cap.isOpened())  // check if we succeeded
      return -1;

      Mat edges;
      namedWindow("edges",1);
      for(;;)
      {
    Mat frame;
    cap >> frame;
    if(waitKey(30) >= 0) break;
}
     cvtColor(fame, img_hsv, CV_BGR2HSV);
     std::vector<cv::Mat> channels;
     split(img_hsv, channels);

     Mat hueOrig = channels.at(0).clone();
     Mat threshLower, threshUpper;
     Mat result;

     threshold(hueOrig, threshLower, 60, 255, CV_THRESH_BINARY);
     threshold(hueOrig, threshUpper, 180, 255, CV_THRESH_BINARY_INV);

     result = threshLower & threshUpper;
     //imshow("Flag", result);

     Mat edges;
     std::vector<std::vector<Point> > contours;

     Canny(result, edges, 100, 200, 3, false);

     //imshow("Cannied", edges);

     cv::findContours(edges, contours, CV_RETR_LIST, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));

     std::vector<Point> output;

     approxPolyDP(contours[i], output, cv::arcLength(cv::Mat(contours.at(i)), true) * 0.02
     , bool closed);

     return output;

     waitKey(0);

   }
}
