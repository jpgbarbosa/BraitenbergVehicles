def main():
    filename = "maze.txt"

    line = 0;
    column = 0;
    
    f = open(filename, "r")

    #Reads the limits of the maze.
    numbers = f.readline()
    lineLimit = int(numbers.split(" ")[0])
    columnLimit = int(numbers.split(" ")[1])
    print lineLimit, columnLimit

    #Reads the maze itself.
    text = f.readlines()

    #Iterates over the lines.
    for i in text:
        for t in i[0:-1]:
            if (t == "*"):
                if (isHorizontal(line, column, lineLimit, columnLimit, i)): 
                    printHorizontal()
                else:
                    printVertical()
            column += 1

        line += 1
        column = 0;

    print text

#Find if this wall is to be drawn as an horizontal or vertical one.
def isHorizontal(line, column, lineLimit, columnLimit, lineRead):
    #We are defining the top walls.
    if (line == 0 or line == lineLimit - 1):
        return True;
    #We are defining the side walls.
    elif (column == 1 or column == columnLimit - 1):
        return False;

    #Now, we have to look at the interior symbols.
    #This wall is side by side with another wall on the horizontal.
    #It means it's horizontal too. 
    if (lineRead[column+1] == "*" or lineRead[column-1] == "*"):
        return True;

    #In all other cases, it's a vertical wall.
    return False;

#Prints an horizontal wall.
def printHorizontal():
    print "Horizontal"

#Prints a vertical wall.
def printVertical():
    print "Vertical"

if __name__ == "__main__":
    main()
