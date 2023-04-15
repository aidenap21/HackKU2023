import pygame 
import sys

pygame.init()
running = True
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 640
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []




class TicTacToe:
    def __init__(self):
        self._board = [[0,0,0],[0,0,0],[0,0,0]] # initializes board as list of lists to stores moves
        self._turnNum = 0 # tracks which round the game is on

    def _place(self, x, y): #Function to place the mark
        if (0 <= x <= 2) and (0 <= y <= 2):
            if (self._board[x][y] == 0): #Check if the current move is valid
                if (self._turnNum % 2 == 0): #Check if it's player 1's turn
                        self._board[x][y] = 'X' #If so, place an 'X' in the location
                        
                elif(self._turnNum % 2 == 1): #Check if it's player 2's turn
                    self._board[x][y] = 'O' #If so, place an 'O' in the location
                    
            else: #Else statement to catch invalid moves
                return False #Returns false in this case
        else:
            return False

        self._turnNum += 1
        return True

    def _winCheck(self):
        for i in range(0, 3): # iterates from 0-3 to access every row
            if (self._board[i][0] == self._board[i][1] == self._board[i][2]): # checks the current i value row
                if (self._board[i][0] == ('X' or 'O')):
                    return True # returns the value of the winner if there are 3 of the same across
            if (self._board[0][i] == self._board[1][i] == self._board[2][0] == ('X' or 'O')): # checks the current i value column
                if (self._board[0][i] == ('X' or 'O')):
                    return True # returns the value of the winner if there are 3 of the same across
            
        if (self._board[0][0] == self._board[1][1] == self._board[2][2]): # checks a diagonal
            if (self._board[1][1] == ('X' or 'O')):
                return True # returns the value of the winner if there are 3 of the same diagonal
        if (self._board[0][2] == self._board[1][1] == self._board[2][0]): # checks a diagonal
            if (self._board[1][1] == ('X' or 'O')):
                return True # returns the value of the winner if there are 3 of the same diagonal
        
        return False
    
    def run(self):
        while (running):
            while (self._turnNum < 9): # runs while the board isn't full
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos = pygame.mouse.get_pos()

                            if (pos[0] < 213):
                                x = 0
                            elif (pos[0] < 426):
                                x = 1
                            elif (pos[0] < 640):
                                x = 2

                            if (pos[1] < 213):
                                y = 0
                            elif (pos[1] < 426):
                                y = 1
                            elif (pos[1] < 640):
                                y = 2

                            if (self._turnNum % 2 == 0): # runs if it is X's turn
                                if (self._place(x, y)): # calls place and will return True if successfully places
                                    for i in self._board: # iterates over the board to print
                                        print(f'{i[0]} {i[1]} {i[2]}') # prints the values of the current loop list

                                    if (self._winCheck()): # checks if someone has won
                                        print('X wins!') # prints that X has won
                                        self._turnNum = 10 # sets the turnNum to 10 so that the draw message is not printed

                                else: # runs if the place function fails
                                    print('Invalid coordinates') # tells the user the coordinates are invalid

                            elif (self._turnNum % 2 == 1): # runs if it is O's move
                                x = int(input('Enter x coordinate for O move: ')) # gets the x coordinate input from the user
                                y = int(input('Enter y coordinate for O move: ')) # gets the y coordinate input from the user

                                if (self._place(x, y)): # calls place and will return True if successfully places
                                    for i in self._board: # iterates over the board to print
                                        print(f'{i[0]} {i[1]} {i[2]}') # prints the values of the current loop list

                                    if (self._winCheck()): # checks if someone has won
                                        print('O wins!') # prints that X has won
                                        self._turnNum = 10 # sets the turnNum to 10 so that the draw message is not printed

                                else: # runs if the place function fails
                                    print('Invalid coordinates') # tells the user the coordinates are invalid

        if (self._turnNum < 10): # runs if the board filled with no winner
            print('Draw!') # prints the draw message