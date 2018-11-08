def printSpaces(spaces):
    for i in range(spaces):
        print(' ', end='')

def printPoints(points):
    for x in range(points):
        print("#", end="")
    printSpaces(2)
    for x in range(points):
        print('#', end='')

def printPyramid(height):
    rowcounter = 0
    pointnumber = 1
    spaces = height-int(pointnumber/2)
    while rowcounter<height:
        printSpaces(spaces)
        printPoints(pointnumber)
        spaces-=1
        rowcounter+=1
        pointnumber+=1
        print(" ")


printPyramid(int(input("Pyramid Height (integer): ")))
