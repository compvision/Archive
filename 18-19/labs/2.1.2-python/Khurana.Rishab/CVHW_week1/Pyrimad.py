class Pyrimad:
	h = int(input("What do you want the height of your pyrimad (integers only and must be from 3 to 100"))
	def printPyramid(height):
		k = 2 * height - 2;
		for i in range(0, height):
			for j in range(0, k):
				print(end=" ")
			k=k-1
			for j in range(0, i+1):
					print("* ", end="")
			print("\r")
	if (h >= 3 and h <= 100):
		printPyramid(h)
	if (h < 3 or h > 100):
		print("Pleases input a number from 3 to 100")