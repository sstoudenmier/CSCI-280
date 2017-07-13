'''
Seth Stoudenmier
-----------------------------------
Statement of Authenticity: This work was done solely by myself.
-----------------------------------
Class representing a maze, which consists of a series of PathNodes arranged in a
rectangluar formation.
'''

from PathNode import PathNode

class Maze:

    def __init__(self, mazeTextFileName):

        self.mazeRows = []

        infile = open(mazeTextFileName, 'r')

        for line in infile:
            self.mazeRows.append(line.split())

        self.numRows = len(self.mazeRows)
        self.numCols = len(self.mazeRows[0])

        self.passableTile = '.'

    '''
    Checks to see if the row, col pair is a valid placement.
    @param: row - a row in the maze
            col - a column in the maze
    @return: true if the row, col pair is a valid placement; false otherwise
    '''
    def isValidRowCol(self, row, col):

        if 0 <= row < self.numRows and 0<= col < self.numCols:
            return True
        return False

    '''
    Looks at the PathNodes surrounding a certain PathNode. If they are passable terain then they are returned in a list.
    @param: currNode - a PathNode object representing the current location
    @return: a list of PathNode objects representing the possible locations you can travel from the currNode
    '''
    def getSuccessors(self, currNode):

        successors = []

        currRow = currNode.getRow()
        currCol = currNode.getCol()

        # checking to the North
        if self.isValidRowCol(currRow-1, currCol):
            if self.mazeRows[currRow-1][currCol] == self.passableTile:
                successors.append(PathNode(currRow-1, currCol, currNode))
        # checking to the East
        if self.isValidRowCol(currRow, currCol+1):
            if self.mazeRows[currRow][currCol+1] == self.passableTile:
                successors.append(PathNode(currRow, currCol+1, currNode))
        # checking to the South
        if self.isValidRowCol(currRow+1, currCol):
            if self.mazeRows[currRow+1][currCol] == self.passableTile:
                successors.append(PathNode(currRow+1, currCol, currNode))
        # checking to the West
        if self.isValidRowCol(currRow, currCol-1):
            if self.mazeRows[currRow][currCol-1] == self.passableTile:
                successors.append(PathNode(currRow, currCol-1, currNode))

        return successors

    '''
    Builds a path of PathNodes that has already been found.
    @param: currNode - the goal location found by the pathfinder
    @return: list of PathNodes in order from start to goal
    '''
    def buildPath(self, currNode):

        path = []
        done = False

        while not done:
            path.insert(0, currNode)
            if currNode.getPrevious() is None:
                done = True
            else:
                currNode = currNode.getPrevious()

        return path

    '''
    Find a path of PathNodes from a start and goal PathNode that are provided.
    (Utilizes the BFS.)
    @param: start - a PathNode marking where you start
            goal - a PathNode marking where you want to finish
    '''
    def findPath(self, start, goal):

        visited = [start]
        queue = [start]
        counter = 0
        while len(queue) != 0:
            currNode = queue.pop()
            if currNode == goal:
                goal.setPrevious(currNode.getPrevious())
                break
            successors = self.getSuccessors(currNode)
            for node in successors:
                #print(counter,node, node.getPrevious())
                if node not in visited:
                    visited.append(node)

                    queue.insert(0, node)
            counter+=1
    '''
    Prints the contents of maze row by row.
    '''
    def print(self):

        for row in self.mazeRows:
            for col in row:
                print(col, end=" ")
            print("\n")
