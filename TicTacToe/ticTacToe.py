import asyncio
import pygame 
import sys
import os

pygame.init()
running = True
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 640
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []

# path for images behaves correctly in pygbag but not when directly running main
background = pygame.image.load(os.path.join('assets', 'TicTacToeBoard.jpg'))
x_icon = pygame.image.load(os.path.join('assets', 'X_icon.png'))
o_icon = pygame.image.load(os.path.join('assets', 'O_icon.png'))
x_wins = pygame.image.load(os.path.join('assets', 'X_wins.png'))
o_wins = pygame.image.load(os.path.join('assets', 'O_wins.png'))



class TicTacToe:
    def __init__(self):
        self._board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] # initializes board as list of lists to stores moves
        self._turnNum = 0 # tracks which round the game is on

    def _place(self, x, y): #Function to place the mark
        if (0 <= x <= 2) and (0 <= y <= 2):
            if (self._board[x][y] == ' '): #Check if the current move is valid
                if (self._turnNum % 2 == 0): #Check if it's player 1's turn
                        self._board[x][y] = 'X' #If so, place an 'X' in the location
                        
                elif(self._turnNum % 2 == 1): #Check if it's player 2's turn
                    self._board[x][y] = 'O' #If so, place an 'O' in the location
                    
            else: #Else statement to catch invalid moves
                return False #Returns false in this case
        else:
            return False

        self._turnNum += 1 # increases the turnNum
        return True # returns True because the move was succesfully placed

    def _winCheck(self):
        for i in range(0, 3): # iterates from 0-3 to access every row
            if (self._board[i][0] == self._board[i][1] == self._board[i][2]): # checks the current i value row
                if (self._board[i][0] != ' '):
                    return True # returns the value of the winner if there are 3 of the same across
                
            if (self._board[0][i] == self._board[1][i] == self._board[2][i]): # checks the current i value column
                if (self._board[0][i] != ' '):
                    return True # returns the value of the winner if there are 3 of the same across
            
        if (self._board[0][0] == self._board[1][1] == self._board[2][2]): # checks a diagonal
            if (self._board[1][1] != ' '):
                return True # returns the value of the winner if there are 3 of the same diagonal
        if (self._board[0][2] == self._board[1][1] == self._board[2][0]): # checks a diagonal
            if (self._board[1][1] != ' '):
                return True # returns the value of the winner if there are 3 of the same diagonal
        
        return False
    
    async def run(self):
        while (running):
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0))
            pygame.display.flip()

            while (self._turnNum < 9): # runs while the board isn't full
                for event in pygame.event.get(): # waits for a mouse click event
                        if event.type == pygame.MOUSEBUTTONDOWN: # runs when the mouse click is lifted
                            pos = pygame.mouse.get_pos() # gets the position of the mouse on click

                            # following statements translate mouse position to the x and y coordinates needed for the place function
                            if (pos[0] < width/3):
                                y = 0
                            elif (pos[0] < 2*(width/3)):
                                y = 1
                            elif (pos[0] < width):
                                y = 2

                            if (pos[1] < height/3):
                                x = 0
                            elif (pos[1] < 2*(height/3)):
                                x = 1
                            elif (pos[1] < height):
                                x = 2

                            if (self._turnNum % 2 == 0): # runs if it is X's turn
                                if (self._place(x, y)): # calls place and will return True if successfully places
                                    # the following statements translate the pos to x and y so that the image outputs in the correct positon
                                    if (pos[0] < width/3):
                                        x = 20
                                    elif (pos[0] < 2*(width/3)):
                                        x = 220
                                    elif (pos[0] < width):
                                        x = 420

                                    if (pos[1] < height/3):
                                        y = 20
                                    elif (pos[1] < 2*(height/3)):
                                        y = 220
                                    elif (pos[1] < height):
                                        y = 420

                                    screen.blit(x_icon, (x, y)) # outputs the placed icon on the game screen
                                    pygame.display.flip() # flips to display

                                    
                                    for i in self._board: # iterates over the board to print
                                        print(f'{i[0]} {i[1]} {i[2]}') # prints the values of the current loop list
                                    print('')

                                    if (self._winCheck()): # checks if someone has won
                                        screen.blit(x_wins, (20, 320))
                                        pygame.display.flip()
                                        print('X wins!') # prints that X has won
                                        self._turnNum = 10 # sets the turnNum to 10 so that the draw message is not printed
                                        #running = False

                                else: # runs if the place function fails
                                    print('Invalid coordinates') # tells the user the coordinates are invalid

                            elif (self._turnNum % 2 == 1): # runs if it is O's move
                                if (self._place(x, y)): # calls place and will return True if successfully places
                                    # the following statements translate the pos to x and y so that the image outputs in the correct positon
                                    if (pos[0] < width/3):
                                        x = 20
                                    elif (pos[0] < 2*(width/3)):
                                        x = 220
                                    elif (pos[0] < width):
                                        x = 420

                                    if (pos[1] < height/3):
                                        y = 20
                                    elif (pos[1] < 2*(height/3)):
                                        y = 220
                                    elif (pos[1] < height):
                                        y = 420

                                    screen.blit(o_icon, (x, y)) # outputs the icon on the game screen
                                    pygame.display.flip() # flips to display


                                    for i in self._board: # iterates over the board to print
                                        print(f'{i[0]} {i[1]} {i[2]}') # prints the values of the current loop list
                                    print('')

                                    if (self._winCheck()): # checks if someone has won
                                        screen.blit(o_wins, (20, 320))
                                        pygame.display.flip()
                                        print('O wins!') # prints that X has won
                                        self._turnNum = 10 # sets the turnNum to 10 so that the draw message is not printed
                                        #running = False

                                else: # runs if the place function fails
                                    print('Invalid coordinates') # tells the user the coordinates are invalid
                await asyncio.sleep(0) # allows pygbag to function to run in browser

            for event in pygame.event.get(): # waits for a mouse click event
                        if event.type == pygame.MOUSEBUTTONDOWN: # runs when the mouse click is lifted
                            self._board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] # reinitializes board as list of lists to stores moves
                            self._turnNum = 0 # tracks which round the game is on

        if (self._turnNum < 10): # runs if the board filled with no winner
            print('Draw!') # prints the draw message