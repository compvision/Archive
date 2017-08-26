#include<iostream>
#include<opencv2/opencv>

AppConfig::AppConfig() {
    deviceID(0);
    isFile(0);
    isDevice(0);
    isHeadless(0);
    isNetworking(1);
    isDebug(0);
}

int AppConfig::checkdeviceID() {
  return deviceID;
}
int AppConfig::checkisFile() {
  return isFile;
}
int AppConfig::checkisDevice() {
  return isDevice;
}
int AppConfig::checkisHeadless() {
  return isHeadless;
}
int AppConfig::checkisDebug() {
  return isDebug;
}
int AppConfig::checkisNetworking() {
  return isNetworking;
}
