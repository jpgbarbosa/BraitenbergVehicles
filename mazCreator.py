objectType = "BraitenbergSound";

def main():
    filename = "maze.txt"

    line = 0;
    column = 0;
    
    f = open(filename, "r")

    #Reads the limits of the maze.
    numbers = f.readline()
    columnLimit = int(numbers.split(" ")[1])
    lineLimit = int(numbers.split(" ")[0])
    print lineLimit, columnLimit

    #Reads the maze itself.
    text = f.readlines()

    #Iterates over the lines.
    for i in xrange(len(text)):
        for t in xrange(len(text[i])):
            if (text[i][j] == "*"):
                self.obj = breve.createInstances ( breve.BraitenbergSound, 1)
                self.obj = breve.createInstances( breveBraitenbergSound, 1)
                self.obj.move( breve.vector(i*10, 2, j*10))
                s.move(breve.vector(i*10, 2, j*10))    
  #              if (isHorizontal(line, column, lineLimit, columnLimit, i)): 
  #                  printHorizontal(line, column)
   #             else:
    #                printVertical(line, column)
    #        column += 1

      #  line += 1
       # column = 0;

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
def printHorizontal(line, column):
    i = 0

    text = "for i in range(1,4):\n\tself.obj = breve.createInstances ( breve." + objectType + ", 1)\n\tself.obj.move( breve.vector(i*"+ "4,0," + str(line) + "))"
    print text

#Prints a vertical wall.
def printVertical(line, column):
    '''
    for i in range(10,14):	
	self.block = breve.createInstances( breve.BraitenbergSound,1)
	self.block.move( breve.vector(i*4,0,5))'''

if __name__ == "__main__":
    main()
