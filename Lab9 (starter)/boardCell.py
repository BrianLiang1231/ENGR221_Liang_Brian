"""
Name: Brian Liang
Date: April 2026
"""

from preferences import Preferences

from enum import Enum


class BoardCell:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        self.__cellType = self.CellType.EMPTY

        self.__addedToSearchList = False
        self.__parent = None

    def getRow(self):
        """ Get the row of this cell """
        return self.__row

    def getCol(self):
        """ Get the column of this cell """
        return self.__col

    def isWall(self):
        """ Return whether or not this cell is a wall """
        return self.__cellType == self.CellType.WALL

    def isEmpty(self):
        """ Return whether or not this cell is empty """
        return self.__cellType == self.CellType.EMPTY

    def isFood(self):
        """ Return whether or not this cell is food """
        return self.__cellType == self.CellType.FOOD

    def isHead(self):
        """ Return whether or not this cell is the head of the snake """
        return self.__cellType == self.CellType.HEAD

    def isBody(self):
        """ Return whether or not this cell is part of the snake's body """
        return self.__cellType == self.CellType.BODY

    def getCellColor(self):
        """ Return the color associated with this type of cell """
        return {
            self.CellType.WALL: Preferences.COLOR_WALL,
            self.CellType.FOOD: Preferences.COLOR_FOOD,
            self.CellType.EMPTY: Preferences.COLOR_EMPTY,
            self.CellType.HEAD: Preferences.COLOR_HEAD,
            self.CellType.BODY: Preferences.COLOR_BODY,
        }.get(self.__cellType)

    def becomeWall(self):
        """ Change this cell to a wall """
        self.__cellType = self.CellType.WALL

    def becomeFood(self):
        """ Change this cell to food """
        self.__cellType = self.CellType.FOOD

    def becomeEmpty(self):
        """ Change this cell to empty """
        self.__cellType = self.CellType.EMPTY

    def becomeHead(self):
        """ Change this cell to the snake's head """
        self.__cellType = self.CellType.HEAD

    def becomeBody(self):
        """ Change this cell part of the snake's body """
        self.__cellType = self.CellType.BODY

    def setAddedToSearchList(self):
        """ Indicate that this cell has been added to the search list """
        self.__addedToSearchList = True

    def alreadyAddedToSearchList(self):
        """ Return whether or not this cell has been added to the search list """
        return self.__addedToSearchList

    def clearSearchInfo(self):
        """ Reset the search attributes """
        self.__addedToSearchList = False
        self.__parent = None

    def setParent(self, parent):
        """ Set the parent of this cell """
        self.__parent = parent

    def getParent(self):
        """ Return the parent of this cell """
        return self.__parent

    def __str__(self):
        """ Specify the string representation of the cell. """
        return "[{}, {}, {}]".format(self.__row, self.__col, self.__cellType.value)

    def parentString(self):
        """ Format the parent of this cell, as a string """
        if self.__parent:
            return "[{}, {}]".format(self.__parent.getRow(), self.__parent.getCol())
        return "None"

    class CellType(Enum):
        WALL = "*"
        EMPTY = " "
        FOOD = "X"
        HEAD = "H"
        BODY = "B"