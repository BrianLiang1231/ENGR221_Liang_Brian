"""
Name: Brian Liang
Date: April 2026
Description: Controls the snake game, including keypresses, snake movement,
food updates, and game-over logic.
"""

from preferences import Preferences
from gameData import GameData
from boardDisplay import BoardDisplay

import pygame
from enum import Enum
from queue import Queue


class Controller:
    def __init__(self):
        self.__data = GameData()
        self.__display = BoardDisplay()
        self.__numCycles = 0

        try:
            pygame.mixer.init()
            self.__audioEat = pygame.mixer.Sound(Preferences.EAT_SOUND)
            self.__display.headImage = pygame.image.load(Preferences.HEAD_IMAGE)
        except:
            print("Problem error loading audio / images")
            self.__audioEat = None

        self.startNewGame()

    def startNewGame(self):
        """ Initialize the board for a new game """
        self.__data.placeSnakeAtStartLocation()

    def gameOver(self):
        """ Indicate that the player has lost """
        self.__data.setGameOver()

    def run(self):
        """ The main loop of the game """
        clock = pygame.time.Clock()

        while not self.__data.getGameOver():
            self.cycle()
            clock.tick(Preferences.SLEEP_TIME)

    def cycle(self):
        """ The main behavior of each time step """
        self.checkKeypress()
        self.updateSnake()
        self.updateFood()
        self.__numCycles += 1
        self.__display.updateGraphics(self.__data)

    def checkKeypress(self):
        """ Update the game based on user input """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameOver()

            elif event.type == pygame.KEYDOWN:
                if event.key in self.Keypress.REVERSE.value:
                    self.reverseSnake()

                elif event.key in self.Keypress.AI.value:
                    self.__data.setAIMode()

                elif event.key in self.Keypress.UP.value:
                    self.__data.setDirectionNorth()

                elif event.key in self.Keypress.DOWN.value:
                    self.__data.setDirectionSouth()

                elif event.key in self.Keypress.LEFT.value:
                    self.__data.setDirectionWest()

                elif event.key in self.Keypress.RIGHT.value:
                    self.__data.setDirectionEast()

    def updateSnake(self):
        """ Move the snake forward one step, either in the current direction, or as directed by the AI """
        if self.__numCycles % Preferences.REFRESH_RATE == 0:
            if self.__data.inAIMode():
                nextCell = self.getNextCellFromBFS()
            else:
                nextCell = self.__data.getNextCellInDir()

            try:
                self.advanceSnake(nextCell)
            except:
                print("Failed to advance snake")

    def advanceSnake(self, nextCell):
        """ Update the state of the world to move the snake's head to the given cell """
        if nextCell.isWall() or nextCell.isBody():
            self.gameOver()

        elif nextCell.isFood():
            self.playSound_eat()
            self.__data.moveSnakeToFoodCell(nextCell)

        elif nextCell.isEmpty():
            self.__data.moveSnakeToEmptyCell(nextCell)

    def updateFood(self):
        """ Add food every FOOD_ADD_RATE cycles or if there is no food """
        if self.__data.noFood() or (self.__numCycles % Preferences.FOOD_ADD_RATE == 0):
            self.__data.addFood()

    def getNextCellFromBFS(self):
        """ Uses BFS to search for the food closest to the head of the snake. """
        self.__data.resetCellsForSearch()

        cellsToSearch = Queue()

        head = self.__data.getSnakeHead()
        head.setAddedToSearchList()
        cellsToSearch.put(head)

        return self.__data.getRandomNeighbor(head)

    def getFirstCellInPath(self, foodCell):
        """ TODO COMMENT HERE """
        return foodCell

    def reverseSnake(self):
        """ TODO COMMENT HERE """
        pass

    def playSound_eat(self):
        """ Plays an eating sound """
        if self.__audioEat:
            pygame.mixer.Sound.play(self.__audioEat)
            pygame.mixer.music.stop()

    class Keypress(Enum):
        """ An enumeration defining valid keyboard inputs. """
        UP = pygame.K_i, pygame.K_UP
        DOWN = pygame.K_k, pygame.K_DOWN
        LEFT = pygame.K_j, pygame.K_LEFT
        RIGHT = pygame.K_l, pygame.K_RIGHT
        REVERSE = pygame.K_r,
        AI = pygame.K_a,


if __name__ == "__main__":
    Controller().run()