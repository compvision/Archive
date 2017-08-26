#include <iostream>
#include "Parser.h"
using namespace std;

/**
	Example Usage of Pointers. You Must Rewrite this method so that the pyramid is printed as such:
      *
     ***
    *****
   *******
  *********
 ***********
*************

**/
void pyramid(int levels, string* output){
	for (int i = 0; i < levels; i++){
		for (int j = i; j < levels; j++){
			(*output)+="*";
		}
		(*output)+="\n";
	}
}

int main(){
	cout << "Enter in Amount of Levels: \n-->";
	int levels;
	cin >> levels;
	string py = "";
	string* pyLoc = &py;
	pyramid(levels, pyLoc);
	cout << "As Promised:\n\n" << *pyLoc << "\n\n";
	
	cout << "This next part must be done through cmdline args, this is just to prove that the classes i wrote work";
	cout << endl << endl;
	Parser p;
	cout<<"Cat Command: " << p.getCommandRef("cat") << endl;

	return 0;
}