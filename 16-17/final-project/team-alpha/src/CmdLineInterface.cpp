#include "AppConfig.hpp"
#include "CmdLineInterace.hpp"
#include <cstdlib>
#include <unistd.h>
#include <getopt.h>
#include <iostream>
#include <boost/lexical_cast.hpp>

CmdLineInterface::CmdLineInterface(int argc, char *argv[])
{
    int isHeadless = 0;
    int isNetworking = 1;
    int isDebug = 0;

    while (true) {
        static struct option long_options[] = {
            {"headless", no_argument, &isHeadless, 1},
            {"no-networking", no_argument, &isNetworking, 0},
            {"debug", no_argument, &isDebug, 1},
            {"device", required_argument, 0, 'd'},
            {"file", required_argument, 0, 'f'},
            {0, 0, 0, 0}
        };

        int option_index = 0;
        int c = getopt_long(argc, argv, "d:f:", long_options, &option_index);

        if (c == -1)
            break;

        switch (c) {
        	case 0:
            	break;
        	case 'd':
            	if(config.getIsFile()){
                	std::cerr << "Usage: " << argv[0] << " (-d <device_num> | -f <filename>) [--no-networking] [--headless] [--debug]" << std::endl;
					printUsage(argv[0]);
                	exit(1);
            	}
            	config.setDeviceID(boost::lexical_cast<int>(optarg));
            	config.setIsDevice(1);
            	break;
        	case 'f':
            	if(config.getIsDevice()){
                	printUsage(argv[0]);
                	exit(1);
            	}
            	config.setFileName(boost::lexical_cast<std::string>(optarg));
            	config.setIsFile(1);
            	break;
        	case '?':
            	exit(127);
            	break;
        	default:
            	abort();
        }
    }

    if (! config.getIsFile() && ! config.getIsDevice()){
        printUsage(argv[0]);
        exit(1);
    }

    config.setIsHeadless(isHeadless);
    config.setIsDebug(isDebug);
    config.setIsNetworking(isNetworking);

    if(isDebug){
        if(isHeadless)
            std::cout << "Headless mode" << std::endl;

        if(!isNetworking)
            std::cout << "No networking mode" << std::endl;

        if(config.getIsDevice())
            std::cout << "Device mode: using /dev/video" << config.getDeviceID() << std::endl;

        if(config.getIsFile())
            std::cout << "File mode: using " << config.getFileName() << std::endl;
    }
}

AppConfig CmdLineInterface::getConfig(){
    return config;
}
