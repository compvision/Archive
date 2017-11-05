#Written by Steven Chen
#September 23, 2017

import sys

class Parser:
	def createPyramid(what,input):
		numlayers = (int)(input)

		for x in range(1,numlayers+1):
			string = ""
			for y in range(0,numlayers-x):
				string = string + " "
			for z in range(0,2*x-1):
				if(z%2==0):
					string = string +  "*"
				else:
					string = string + " "
			print(string)

	def input(what,input):
		if input == "help":
			print "List of Commands: nano, ls, cd, -p"
		elif input == "nano":
			print "A terminal text editor (you can't use nano now)"
		elif input == "ls":
			print "lists everything in the current directory"
		elif input == "cd":
			print "change directory"
		elif input == "-p":
			print "Prints a pyramid with the number of layers based on the input"
		else:
			print "Error: argument not documented, use pyramid.py -h for list of documented commands"

parser = Parser()

input = sys.argv
if(len(input)) > 1:
	if input[1] == "-h":
		if len(input) == 2:
			parser.input("help")
		elif len(input) == 3:
			parser.input(input[2])
		else:
			print "ERROR: use pyramid.py -h for help"
	elif input[1] == "-p":
		if len(input) == 3:
			parser.createPyramid(input[2])
		else:
			print "ERROR: use pyramid.py -h for help"
	else:
		print "ERROR: use pyramid.py -h for help"
else:
	print "ERROR: use pyramid.py -h for help"
