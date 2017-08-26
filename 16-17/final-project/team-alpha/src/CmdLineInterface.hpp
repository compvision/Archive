#ifndef CmdLineInterface_hpp
#define CmdLineInterface_hpp
#include "AppConfig.hpp"

class CmdLineInterface{
	Public:
		CmdLineInterface();
		AppConfig getConfig();
	Private:
		AppConfig config;
};

#endif
