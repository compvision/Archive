# Week 3 HW

###The Assignment

- Create a “Parser” Object and a main.cpp file to handle IO
- Must have 2 functions
	- Pyramids
		- Use Pointers! (if you can)
		
		```c++
		#include <iostream>
		using namespace std;
		
		void pyramid(string* loc, int levels) {
			std::string s = *loc;
			s = "*\n**\n***\n****"; //no you can't do this, you gotta do it with for loops
			//put code here (s+= "*") and etc, \n gives you a line break
			*loc = s;
		
		}
		
		int main() {
			string str = "";
			string* strLoc = &str;
			pyramid(strLoc, 3);
			cout << str << endl;
		}
		
					
								
		``` 
	- Reference
		- Must be able to take command line input 
		- Example Usage

		```bash
		./program -h ->returns a list of commands
		./program -h [Command] -> returns description of that command
		./program -h nano -> returns "A terminal text editor (you can't use nano now)
		```
*Pick the three most useful commands (or more) to put into the data base*

[Commands Reference](https://compvision.github.io/commands)


###Turning it in

As usual, fork [this repo](https://github.com/compvision/week3hw), and put your code (call it FirstName_LastName), and submit a pull request
