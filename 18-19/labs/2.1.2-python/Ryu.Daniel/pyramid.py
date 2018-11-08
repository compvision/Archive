
def pyramid(height):
	length = height
	space = " "
	row = ""
	star = "*"
	numStars = 1

	for temp in range(height):
		for x in range(length):
			row += space
		length -= 1;
		for s in range(numStars):
			row += star
		row += space
		row += space
		for s in range(numStars):
			row += star
		numStars += 1
		print(row)
		row = ""

pyramid(5)		

    
