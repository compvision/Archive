#include<iostream>
#include<opencv2/opencv>

class AppConfig {
private:
    int deviceID;
    int isFile;
    int isDevice;
    int isHeadless;
    int isNetworking;
    int isDebug;
public:
  int checkdeviceID();
  int checkisFile();
  int checkisDevice();
  int checkisHeadless();
  int checkisNetworking();
  int checkisDebug();

}
