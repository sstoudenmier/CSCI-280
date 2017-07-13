'''
Seth Stoudenmier
--------------------------
Purpose: Represents the 2D grid of symbols and an inventory of sprites used to draw the tile map.

Properties owned:
    tileMap – list of rows of symbols
    numRows – number of rows in the tile map.
    numCols – number of columns in the tile map.
    spriteInventory – an OurSpriteInventory that holds the set of unique sprite tiles.
    spriteSize – size of each sprite in pixels. We assume all sprites are square (equal width and height).
Behaviors:
    init – Receives name of map data file and name of sprite list data file.
           Open map data file, read each line of input, fill in each row of tile map from each line of text.
           Sample Python code and a sample map file will be provided.
           Open sprite data file, read each line of input, create an OurSprite object from each line of input,
           insert the newly created OurSprite into the spriteInventory. Sample Python code and a sample map file will
           be provided.

    printMap – Receives nothing. Print symbols of map skipping a line after printing each row.
    drawMap – Receives a Pygame screen. Draw the tile map using sprites.
--------------------------
Statement of Authenticity: This work was done on my own with no assistance from anyone else.
'''


from OurSpriteInventory import OurSpriteInventory
from OurSprite import OurSprite

import pygame


class SpriteTileMap:

    def __init__(self, mapFileName, spriteFileName):

        self.tileMap = []
        self.spriteInventory = OurSpriteInventory()

        mapFile = open(mapFileName, 'r')
        spriteFile = open(spriteFileName, 'r')

        for line in mapFile:
            self.tileMap.append(line.split())

        tempSprite = None
        spriteFilePath = "/*/sprites/"

        for line in spriteFile:
            tempLine = line.split()
            tempLine[1] = spriteFilePath + tempLine[1]
            tempSprite = pygame.image.load(tempLine[1])
            self.spriteInventory.addSprite(OurSprite(tempLine[0], tempLine[1], tempSprite))

        self.numRows = len(self.tileMap)
        self.numCols = len(self.tileMap[0])
        self.spriteSize = tempSprite.get_width()

    '''
    Prints the symbols of the tile map
    '''
    def printMap(self):

        for row in self.tileMap:
            for col in row:
                print(col, end="  ")
            print("\n")

    '''
    Draws the tile map onto a screen.
    @param: screen - a pygame screen where the sprites are drawn
    '''
    def drawMap(self, screen):

        for y in range(self.numRows):
            for x in range(self.numCols):
                self.spriteInventory.getBySymbol(self.tileMap[y][x]).getPygameSprite().convert_alpha()
                screen.blit(self.spriteInventory.getBySymbol(self.tileMap[y][x]).getPygameSprite(),
                            (x * self.spriteSize, y * self.spriteSize))

    '''
    Gets the sprite size since every sprite should be the same size.
    @return: the size of the sprites
    '''
    def getSpriteSize(self):

        return self.spriteSize

    '''
    Gets the number of rows in the tile map.
    @return: the row count in the tile map
    '''
    def getNumRows(self):

        return self.numRows

    '''
    Gets the number of columns in the tile map.
    @return: the column count in the tile map
    '''
    def getNumCols(self):

        return self.numCols

    '''
    Gets the tile at a specific position.
    @param: row - the row position
            col - the column position
    @return: the symbol at a specific position in the tile map
    '''
    def getTile(self, row, col):

        return self.tileMap[row][col]

    '''
    Sets the tile at a specifc position.
    @param: row - the row position
            col - the column position
            symbol - the symbol to place inside the tile map
    '''
    def setTile(self, row, col, symbol):

        if 0 <= row < self.getNumRows() and 0 <= col < self.getNumCols():
            self.tileMap[row][col] = symbol
            return True
        return False








