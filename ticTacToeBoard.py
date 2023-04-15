import pygame
pygame.init()

class TicTacToe:
    def __init__(self):
        self._board = [[0,0,0],[0,0,0],[0,0,0]] # initializes board as list of lists to stores moves
        self._turnNum = 0 # tracks which round the game is on

    def _place(self, x, y):
        if (self._turnNum == 9):
            return False
        
        elif (self._turnNum % 2 == 0):
            while (self._board[x][y] != 0):
                self._board[x][y] = 'x'
                break
            
        else:



        self._turnNum += 1
        self._winCheck()
        return True

    def _winCheck(self):
        if (self._turnNum == 9):
            