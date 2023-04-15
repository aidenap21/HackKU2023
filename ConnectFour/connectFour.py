
import pygame 
import sys
#from pygame.locals import *
import os

pygame.init()
running = True
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 640
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []

background = pygame.image.load(os.path.join('ConnectFour', 'assets', 'connectFourBoard.jpg'))
red_chip = pygame.image.load(os.path.join('ConnectFour', 'assets', 'red_chip.png'))
yellow_chip = pygame.image.load(os.path.join('ConnectFour', 'assets', 'yellow_chip.png'))

x = 

class connectFour:

    def __init__(self):
        self._move = 0
        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]
        
    def placePiece(self,column):   # The act of "falling down the board."
        for row in self.board:  # Iterate through the board
            if self.board[row][column] != 0 :  # If there is a piece somewhere down the column, place the piece above it
                self._mark(row-1,column)    # Mark the spot right above it 
                self._move += 1
                break

    def _mark(self,row,column): # Used to mark the place with either a red piece or yellow
        if self._whoMoves == 'R':  # If it's red's turn
            self.board[row][column] = 1  # Mark with a 1 to signify red placed
        else:   # Otherwise it's yellow's turn
            self.board[row][column] = 2  # Mark with a 2 to signify yellow placed

    def _whoMoves(self):
        if self._move % 2 == 0:
            return 'R'
        else:
            return 'Y'

    def _lineOfFour(self,row,column):


    def run(self):
        while (running):
            screen.fill(255,255,255)
            screen.blit(background,0,0)
            pygame.draw.rect()
            pygame.display.flip()

            while (self._move < 42):    # Runs until the max amount of moves, which is 42
                for event in pygame.event.get():    # Waits for an event to occur

                    if (self._whoMoves == 'R'):

                        if event.type == pygame.KEYDOWN:    # If the user presses a key, we need to check which key it is
                            if event.key == pygame.K_RIGHT:
                                # If we move right, we want to update the current position we're looking at

                                # We need an extra check if we are all the way right

                            elif event.key == pygame.K_LEFT:
                                # If we move right, we want to update the current position we're looking at

                                # We need an extra check if we are all the way right

                            elif event.key == pygame.K_SPACE:
                                self.placePiece()
                                # If we press space, we want to place the piece

                    elif (self._whoMoves == 'Y'):
                        if event.type == pygame.KEYDOWN:    # If the user presses a key, we need to check which key it is

                            if event.key == pygame.K_RIGHT:


                            elif event.key == pygame.K_LEFT:


                            elif event.key == pygame.K_SPACE:
                            