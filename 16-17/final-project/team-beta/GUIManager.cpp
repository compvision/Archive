#include <opencv2/opencv>
#include<iostream>

#include "GUIManager.hpp"
#include "Target.cpp"

GUIManager::GUIManager() {
    matImport = target->getMat();
    distance = target->distance();
    azimuthX = target->AzimuthX();
    azimuthY = target->AzimuthY();
}

void GUIManager::showMat() {
  imshow("d=" + distance + ", ax=" + azimuthX + ", ay=" + "azimuthY", matImport);

  waitKey(0);
}
