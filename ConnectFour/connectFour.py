
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
red_chip = pygame.image.load(os.path.join('TicTacToe', 'assets', 'X_icon.png'))
yellow_chip = pygame.image.load(os.path.join('TicTacToe', 'assets', 'O_icon.png'))
class connectFour:

    def __init__(self):
        self.move = 0
        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]
        
    def _placePiece(self,column):
        for row in self.board:  # Iterate through the board
            if self.board[row][column] != 0 :  # If there is a piece somewhere down the column, place the piece above it
                self._mark(row-1,column)
                self.move += 1
                break


    def _mark(self,row,column):
        if self._whoMoves == 'R':  # If it's red's turn
            self.board[row][column] = 1  # Mark with a 1 to signify red placed
        else:   # Otherwise it's yellow's turn
            self.board[row][column] = 2  # Mark with a 2 to signify yellow placed

    def _whoMoves(self):
        if self.move % 2 == 0:
            return 'R'
        else:
            return 'Y'

    def _lineOfFour(self,row,column):


    def run(self):

        



