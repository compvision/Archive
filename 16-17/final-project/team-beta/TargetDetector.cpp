#include "TargetDetector.hpp"
#include <iostream>


processImage(Mat input)
{
  Mat img = input.clone();
}

thresholdImage(Mat input)
{
  Mat img;
  cvtColor(input, img, CV_BGR2HSV);

  std::vector<cv::Mat> channels;
  split(hsv, channels); //splitting the channels

  Mat hueOrig = channels.at(0).clone();
  Mat threshLower, threshUpper;
  Mat result;

  threshold(hueOrig, threshLower, 0, 255, CV_THRESH_BINARY);
  threshold(hueOrig, threshUpper, 50, 255, CV_THRESH_BINARY_INV);

  result = threshLower & threshUpper;

}
