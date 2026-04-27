"""
Name: Brian Liang
Date: April 2026
Description: Displays the snake game board using pygame based on the current
state stored in GameData.
"""

import pygame
from preferences import Preferences


class BoardDisplay:
    def __init__(self):
        # The display where the board is drawn
        self.__display = pygame.display.set_mode(
            (Preferences.GAME_BOARD_WIDTH, Preferences.GAME_BOARD_HEIGHT)
        )

        # Image to show as the "head"
        self.headImage = None

    def updateGraphics(self, gameData):
        """Re-draws the board, food, and snake based on the current state of the board"""

        # Clear the board
        self.clear()

        # Draw the board
        for row in range(Preferences.NUM_CELLS_TALL):
            for col in range(Preferences.NUM_CELLS_WIDE):
                cell = gameData.getCell(row, col)
                self.drawSquare(cell)

        # Draw the game over message, if appropriate
        if gameData.getGameOver():
            self.displayGameOver()

        # Update the display
        pygame.display.update()

    def clear(self):
        """Resets the background of the display"""
        self.__display.fill(Preferences.COLOR_BACKGROUND)

    def drawSquare(self, cell):
        """Draws a cell-sized square at the given location."""
        row = cell.getRow()
        col = cell.getCol()

        if cell.isHead() and self.headImage:
            self.drawImage(row, col, self.headImage)
        else:
            cellColor = cell.getCellColor()
            pygame.draw.rect(
                self.__display,
                cellColor,
                [
                    col * Preferences.CELL_SIZE,
                    row * Preferences.CELL_SIZE,
                    Preferences.CELL_SIZE,
                    Preferences.CELL_SIZE,
                ],
            )

    def drawImage(self, row, col, image):
        """Displays an image at the given cell location."""

        image = image.convert_alpha()

        # Uncomment if you want image to fit inside one cell
        # image = pygame.transform.scale(
        #     image,
        #     (Preferences.CELL_SIZE, Preferences.CELL_SIZE)
        # )

        imageRect = image.get_rect()

        imageRect.center = (
            (col * Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2),
            (row * Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2),
        )

        self.__display.blit(image, imageRect)

    def displayGameOver(self):
        """Displays the game over message"""

        font = Preferences.GAME_OVER_FONT

        text = font.render(
            Preferences.GAME_OVER_TEXT,
            True,
            Preferences.GAME_OVER_COLOR
        )

        textRect = text.get_rect()
        textRect.center = (Preferences.GAME_OVER_X, Preferences.GAME_OVER_Y)

        self.__display.blit(text, textRect)