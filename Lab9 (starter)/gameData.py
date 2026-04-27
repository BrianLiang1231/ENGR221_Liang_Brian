"""
Name: Brian Liang
Date: April 2026
Description: Stores and updates the snake game state, including the board,
snake cells, food cells, movement direction, and game-over status.
"""

from boardCell import BoardCell
from preferences import Preferences

import random
from enum import Enum, auto


class GameData:
    def __init__(self):
        self.__height = Preferences.NUM_CELLS_TALL
        self.__width = Preferences.NUM_CELLS_WIDE

        self.__freeCells = self.__height * self.__width
        self.__totalCells = self.__height * self.__width

        self.__currentMode = self.SnakeMode.GOING_EAST

        self.__board = self.createBoard()

        self.__foodCells = []
        self.__snakeCells = []

        self.__gameOver = False

    def createBoard(self):
        """ Populate the starting state of the board. """
        board = [[BoardCell(row, col) for col in range(self.__width)]
                 for row in range(self.__height)]

        for row in range(self.__height):
            board[row][0].becomeWall()
            board[row][self.__width - 1].becomeWall()
            self.__freeCells -= 2

        for col in range(1, self.__width - 1):
            board[0][col].becomeWall()
            board[self.__height - 1][col].becomeWall()
            self.__freeCells -= 2

        return board

    def placeSnakeAtStartLocation(self):
        """ Place the snake in the upper left corner, facing east """
        head = self.getCell(1, 2)
        body = self.getCell(1, 1)

        head.becomeHead()
        body.becomeBody()

        self.__snakeCells.append(head)
        self.__snakeCells.append(body)

        self.__currentMode = self.SnakeMode.GOING_EAST

        self.__freeCells -= 2

    def inAIMode(self):
        """ Returns a boolean indicating whether or not we are in AI mode """
        return self.__currentMode == self.SnakeMode.AI_MODE

    def getCell(self, row, col):
        """ Returns the cell at the given row and column. """
        if (row >= 0 and row < self.__height) and (col >= 0 and col < self.__width):
            return self.__board[row][col]
        else:
            raise Exception("getCell tried to access cell outside of board: ({}, {})".format(row, col))

    def noFood(self):
        """ Returns a boolean indicating whether or not there is food on the board """
        return len(self.__foodCells) == 0

    def addFood(self):
        """ Adds food to an open spot on the board """
        row = random.randrange(1, self.__height)
        col = random.randrange(1, self.__width)
        cell = self.getCell(row, col)

        if cell.isEmpty():
            cell.becomeFood()
            self.__foodCells.append(cell)
            self.__freeCells -= 1

        elif self.__freeCells / self.__totalCells > 0.3:
            self.addFood()

        else:
            print("Not adding more food")

    def moveSnakeToEmptyCell(self, nextCell):
        """ Moves the snake into an empty cell. """
        oldHead = self.getSnakeHead()
        oldTail = self.getSnakeTail()

        oldHead.becomeBody()
        nextCell.becomeHead()

        self.__snakeCells.insert(0, nextCell)

        oldTail.becomeEmpty()
        self.__snakeCells.pop()

    def moveSnakeToFoodCell(self, nextCell):
        """ Moves the snake into a food cell and grows the snake. """
        oldHead = self.getSnakeHead()

        oldHead.becomeBody()
        nextCell.becomeHead()

        self.__snakeCells.insert(0, nextCell)
        self.__foodCells.remove(nextCell)

    def getNorthNeighbor(self, cell):
        """ Returns the cell to the north of the given cell """
        return self.getCell(cell.getRow() - 1, cell.getCol())

    def getSouthNeighbor(self, cell):
        """ Returns the cell to the south of the given cell """
        return self.getCell(cell.getRow() + 1, cell.getCol())

    def getEastNeighbor(self, cell):
        """ Returns the cell to the east of the given cell """
        return self.getCell(cell.getRow(), cell.getCol() + 1)

    def getWestNeighbor(self, cell):
        """ Returns the cell to the west of the given cell """
        return self.getCell(cell.getRow(), cell.getCol() - 1)

    def getHeadNorthNeighbor(self):
        """ Returns the cell to the north of the snake's head """
        return self.getNorthNeighbor(self.getSnakeHead())

    def getHeadSouthNeighbor(self):
        """ Returns the cell to the south of the snake's head """
        return self.getSouthNeighbor(self.getSnakeHead())

    def getHeadEastNeighbor(self):
        """ Returns the cell to the east of the snake's head """
        return self.getEastNeighbor(self.getSnakeHead())

    def getHeadWestNeighbor(self):
        """ Returns the cell to the west of the snake's head """
        return self.getWestNeighbor(self.getSnakeHead())

    def getNextCellInDir(self):
        """ Returns the next cell in the snake's path based on its current direction """
        if self.__currentMode == self.SnakeMode.GOING_NORTH:
            return self.getHeadNorthNeighbor()
        elif self.__currentMode == self.SnakeMode.GOING_SOUTH:
            return self.getHeadSouthNeighbor()
        elif self.__currentMode == self.SnakeMode.GOING_EAST:
            return self.getHeadEastNeighbor()
        elif self.__currentMode == self.SnakeMode.GOING_WEST:
            return self.getHeadWestNeighbor()
        else:
            return self.getRandomNeighbor(self.getSnakeHead())

    def getNeighbors(self, center):
        """ Returns a set of the neighbors around the given cell """
        return {
            self.getNorthNeighbor(center),
            self.getSouthNeighbor(center),
            self.getEastNeighbor(center),
            self.getWestNeighbor(center)
        }

    def getRandomNeighbor(self, center):
        """ Returns a random empty neighbor of the given cell """
        neighbors = self.getNeighbors(center)
        for cell in neighbors:
            if cell.isEmpty():
                return cell
        return random.choice(list(neighbors))

    def setDirectionNorth(self):
        """ Set the direction as north """
        self.__currentMode = self.SnakeMode.GOING_NORTH

    def setDirectionSouth(self):
        """ Set the direction as south """
        self.__currentMode = self.SnakeMode.GOING_SOUTH

    def setDirectionEast(self):
        """ Set the direction as east """
        self.__currentMode = self.SnakeMode.GOING_EAST

    def setDirectionWest(self):
        """ Set the direction as west """
        self.__currentMode = self.SnakeMode.GOING_WEST

    def setAIMode(self):
        """ Switch to AI mode """
        self.__currentMode = self.SnakeMode.AI_MODE

    def getSnakeHead(self):
        """ Return the cell containing the snake's head """
        return self.__snakeCells[0]

    def getSnakeTail(self):
        """ Return the cell containing the snake's tail """
        return self.__snakeCells[-1]

    def getSnakeNeck(self):
        """ Return the body cell adjacent to the snake's head """
        return self.__snakeCells[1]

    def getCellColor(self, row, col):
        """ Return the color of the cell at the given location. """
        return self.getCell(row, col).getCellColor()

    def resetCellsForSearch(self):
        for row in self.__board:
            for cell in row:
                cell.clearSearchInfo()

    def setGameOver(self):
        """ Set the game over flag to True """
        self.__gameOver = True

    def getGameOver(self):
        """ Check the game over value """
        return self.__gameOver

    def __str__(self):
        """ Returns a string representation of the board """
        out = ""
        for row in self.__board:
            for cell in row:
                out += str(cell)
            out += "\n"
        return out

    def toStringParents(self):
        """ Returns a string representation of the parents of each cell """
        out = ""
        for row in self.__board:
            for cell in row:
                out += "{}\t".format(cell.parentString())
            out += "\n"
        return out

    class SnakeMode(Enum):
        GOING_NORTH = auto()
        GOING_SOUTH = auto()
        GOING_EAST = auto()
        GOING_WEST = auto()
        AI_MODE = auto()