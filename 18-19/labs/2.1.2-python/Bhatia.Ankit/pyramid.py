def printPyramid(num):

    string = ""
    num += 1

    for i in range(num):
        for x in range(num - i):
            string += " "
        for x in range(i):
            string += "#"
        string += "  "
        for x in range(i):
            string += "#"
        print(string)
        string = ""

printPyramid(7)