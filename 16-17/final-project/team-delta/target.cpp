#include "Target.hpp"
#include <opencv2/opencv.hpp>
#include <math.h>
#include <iostream>

Target::Target(std::vector<cv::Point> contour)
{
}

Point getTopPoint(){
  int max = 0;
  int ref = 0;
  for(int i = 0; i <contour.size(); i++){
    if (contour[i].y > max){
      ref = i;
      max = contour[i].y;
    }
  }
  return contour[ref];
}

Point getBottomPoint(){
  int min = 10000;
  int ref = 0;
  for(int i = 0; i <contour.size(); i++){
    if (contour[i].y < min){
      ref = i;
      min = contour[i].y;
    }
  }
  return contour[ref];
}

Point getLeftPoint(){
  int min = 10000;
  int ref = 0;
  for(int i = 0; i <contour.size(); i++){
    if (contour[i].x < min){
      ref = i;
      min = contour[i].x;
    }
  }
  return contour[ref];
}

Point getRightPoint(){
  int max = 0;
  int ref = 0;
  for(int i = 0; i <contour.size(); i++){
    if (contour[i].x > max){
      ref = i;
      max = contour[i].x;
    }
  }
  return contour[ref];
}

double getHeight(){
  return abs(getTopPoint().y - getBottomPoint().y):
}

double getWidth(){
  return abs(getRightPoint().x - getLeftPoint().x):
}

Point getCenter(){

    double totalX=0, totalY=0;

    for(int i = 0; i < edge.size(); i++)
    {
        totalX += edge[i].x;
    }

    return Point(totalX /= i, totalY /= i);

}
