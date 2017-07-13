'''
Seth Stoudenmier
-----------------------------------
Statement of Authenticity: This work was done solely by myself.
-----------------------------------
File used to test the path finding capabilities in the Maze class.
'''

from Maze import Maze
from PathNode import PathNode

assignmentPath = "/Users/stoudenmiersh/Documents/CofC_Classes/CSCI_280/Assignment5/"

filename = "MapData.txt"

maze = Maze(assignmentPath + filename)

maze.print()

startRow = eval(input("Enter start row: "))
startCol = eval(input("Enter start col: "))
goalRow = eval(input("Enter goal row: "))
goalCol = eval(input("Enter goal col: "))

startNode = PathNode(startRow, startCol)
goalNode = PathNode(goalRow, goalCol)

maze.findPath(startNode, goalNode)

path = maze.buildPath(goalNode)

print("Solution from path",startNode,"to",goalNode)

for node in path:

    print(node)

print("Path length is", len(path))
