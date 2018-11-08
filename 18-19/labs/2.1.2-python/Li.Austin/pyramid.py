from sys import argv

def pyramid(height):
	row = 1
	while row <= height:
		for i in range(0, height - row):
			print(" ", end = "")
		for i in range(0, row):
			print("#", end = "")
		print("  ", end = "")
		for i in range(0, row):
			print("#", end = "")
		for i in range(0, height - row):
			print(" ", end = "")
		print()
		row += 1
pyramid(int(argv[1]))
