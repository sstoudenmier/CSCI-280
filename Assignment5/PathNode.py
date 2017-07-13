'''
Class representing a map location being searched. A map location is defined by its (row,
column) coordinates and the previous PathNode.
'''

class PathNode:

    def __init__(self, row=0, col=0, previous=None):

        self.row = row
        self.col = col
        self.previous = previous

    '''
    Gets the row number for the PathNode.
    @return: the value of the row for the PathNode
    '''
    def getRow(self):

        return self.row

    '''
    Gets the column number for the PathNode.
    @return: the value of the column for the PathNode
    '''
    def getCol(self):

        return self.col

    '''
    Gets the previous node for the PathNode.
    @return: the pathnode that was previous looked at
    '''
    def getPrevious(self):

        return self.previous

    '''
    Sets the previous node for the PathNode.
    @param: previous - value to set for the previous node
    '''
    def setPrevious(self, previous):

        self.previous = previous

    '''
    Override the equals method so that it can compare two PathNode objects.
    @param: other - another PathNode class to compare self to
    @return: true if self and other are equal in row and column; false otherwise
    '''
    def __eq__(self, other):

        if self.getRow() == other.getRow() and self.getCol() == other.getCol():
            return True
        return False

    '''
    Overide the hash method.
    @return: a hash value for the PathNode objects
    '''
    def __hash__(self):

        return 31 * self.getRow() + self.getCol()

    '''
    Override the toString method for PathNode so that it can print out the coordinates.
    @return: a string representation of the PathNode
    '''
    def __str__(self):

        return "(" + str(self.getRow()) + ", " + str(self.getCol()) + ")"
