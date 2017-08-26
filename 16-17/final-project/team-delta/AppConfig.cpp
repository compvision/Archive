#include "AppConfig.hpp"

AppConfig::AppConfig() :
  deviceID(0),
  isFile(0),
  isDevice(0),
  isHeadless(0),
  isNetworking(1),
  isDebug(0)
{
}


std::string AppConfig::getFileName(){ return fileName;}
int AppConfig::getDeviceID(){return deviceID;}
int AppConfig::getIsFile(){return isFile;}
int AppConfig::getIsDevice(){return isDevice;}
int AppConfig::getIsHeadless(){return isHeadless;}
int AppConfig::getIsNetworking(){return isNetworking;}
int AppConfig::getIsDebug(){return isDebug;}
void AppConfig::setFileName(std::string _FileName){fileName = _FileName;}
void AppConfig::setDeviceID(int _DeviceID){deviceID = _DeviceID;}
void AppConfig::setIsFile(int _IsFile){isFile = _IsFile;}
void AppConfig::setIsDevice(int _IsDevice){isDevice = _IsDevice;}
void AppConfig::setIsHeadless(int _IsHeadless){isHeadless = _IsHeadless;}
void AppConfig::setIsNetworking(int _IsNetworking){isNetworking = _IsNetworking;}
void AppConfig::setIsDebug(int _debug){isDebug = _debug;}
