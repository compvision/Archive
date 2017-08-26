#include "Parser.h"
//we dont need to type 'using namespace std;' since that was defined in Parser.h
Parser::Parser() {

}

string Parser::getCommandRef(string cmd){
	/*
		Put Your Command Reference Code Here (ie the if else statements)
	*/
	if (cmd == "cat"){
		return "prints content of file";
	}
	return "reference";
}
//we dont need to redefine the class here since we already did that in