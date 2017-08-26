#include "Target.hpp"
#include <opencv2/opencv.hpp>
#include <math.h>
#include <iostream>

Target::Target(std::vector<cv::Point> contour)
{
    edge = contour;

    std::cout << "EDGE" << edge.size();
}
CannyImage(Mat image)
{
  Mat result = image;
  Mat edges;
  std::vector<std::vector<Point> > contours;
  //thresholding...
  Canny(result, edges, 0, 25, 3, false);
  //imshow("Cannied", edges);
  bool done = true;
  bool Find = false;
  cv::findContours(edges, contours, CV_RETR_LIST, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));
  int scaling = 5;
  std::vector<Point> approxContour;

  for(int i = 0; i < contours.size(); i++) //contours.size()??
  {10

    approxPolyDP(contours[i], approxContour, cv::arcLength(cv::Mat(contours.at(i)), done), done);
    //from the powerpoint

    if (approxContour.size() == 10) //not sure what this size is
    {

     cv::drawContours(img, contours, i , Scalar(255,0,0), scaling);

     std::cout << cv::contourArea(approxContour, Find); //

     imshow("This is the image", img);
    }
}
double getMaxY()
{
  cv::Point max(0,0);
  for(unsigned int i = 0; i < edge.size(); i++)
  {
      if(edge[i] > max)
      {
          max = edge[i];
      }
  }
  return max
}

double getMinY()
{
  cv::Point min(10000,10000);
  for(unsigned int i = 0; i < edge.size(); i++)
  {
      if(edge[i] < min)
      {
          min = edge[i];
      }
  }
  return min;
}

double Target::getHeight()
{

    double max = getMaxY();
    double min = getMinY();
    return max - min;
}


double getMaxX()
{
   cv::Point max(10000,10000);
   for(unsigned int i = 0; i < edge.size(); i++)
   {
       if(edge[i].x < max.x)
       {
           max = edge[i];
       }
   }
   return max;
}

double getMinX()
{
  cv::Point min(0,0);
    for(unsigned int i = 0; i < edge.size(); i++)
    {
        if(edge[i].x > min.x)
        {
            min = edge[i];
        }
    }
return min;
}
double Target::getWidth()
{
      double max = getMaxX();
      double min = getMaxY();

      return max - min;
}
