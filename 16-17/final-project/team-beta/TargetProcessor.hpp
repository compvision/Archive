#include <opencv2/opencv.hpp>
#include <iostream>

#include "Target.hpp"

class TargetProcessor
{
  private:
    int centerX;
    int centerY;
    int minX;
    int maxX;
    int minY;
    int maxY;
    int width;
    int height;
    int imageWidth;
  public:
    int findCenterX();
    int findCenterY();
    double calcDistance();
    double calcAzimuthX();
    double calcAzimuthY();
}
