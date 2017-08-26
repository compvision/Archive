#ifndef AppConfig_hpp
#define AppConfig_hpp
#include <string>

class AppConfig{
    public:
        AppConfig();
        void setDeviceID(int deviceID);
        void setFileName(std::string fileName);
		void setIsDebug(int debug);
		void setIsDevice(int isDevice);
		void setIsFile(int isFile);
        void setIsHeadless(int isHeadless);
        void setIsNetworking(int isNetworking);
        int getDeviceID();
        std::string getFileName();
		int getIsDebug();
		int getIsDevice();
		int getIsFile();
        int getIsHeadless();
        int getIsNetworking();
    private:
        int deviceID;
        std::string fileName;
		int isDebug;
		int isDevice;
		int isFile;
        int isHeadless;
        int isNetworking;
};

#endif
