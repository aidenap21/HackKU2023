import asyncio
import pygame 
import sys
import os


# os.chdir("ConnectFour") # uncomment if running on system
pygame.init()
width = 639
height = 595
surface = pygame.display.set_mode((width,height))
background = pygame.image.load(os.path.join("assets", "modified_connectFourBoard.png"))
red_chip = pygame.image.load(os.path.join("assets", "red_chip.png"))
yellow_chip = pygame.image.load(os.path.join("assets", "yellow_chip.png"))
half_red_chip = pygame.image.load(os.path.join("assets", "half_red_chip.png"))
half_yellow_chip = pygame.image.load(os.path.join("assets", "half_yellow_chip.jpg"))
white_space = pygame.image.load(os.path.join("assets", "white_space.png"))
red_wins = pygame.image.load(os.path.join("assets", "Red_wins.png"))
yellow_wins = pygame.image.load(os.path.join("assets", "Yellow_wins.png"))
draw = pygame.image.load(os.path.join("assets", "Draw.png"))

current_position = [28,13]


running = True

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
        empty_row = True
        top_filled = False
        for row in range(6):  # Iterate through the board
            if self.board[row][column] != 0 :  # If there is a piece somewhere down the column, place the piece above it
                empty_row = False
                if row == 0:
                    top_filled = True
                    break
                else:
                    print("Piece at: " + str(row) + ',' + str(column))
                    self._mark(row-1,column)    # Mark the spot right above it 
                    self._move += 1
                    return [row-1,column]
            
        if empty_row:
            self._mark(5,column)
            self._move += 1
            return [5,column]
        if top_filled:
            return False
            

    def _mark(self,row,column): # Used to mark the place with either a red piece or yellow
        if self._move % 2 == 0:  # If it's red's turn\
            self.board[row][column] = 1  # Mark with a 1 to signify red placed
        else:   # Otherwise it's yellow's turn
            self.board[row][column] = 2  # Mark with a 2 to signify yellow placed

        
    def _pixel_to_column(self,pixelNum):
        if pixelNum == 28:
            return 0
        if pixelNum == 115:
            return 1
        if pixelNum == 202:
            return 2
        if pixelNum == 289:
            return 3
        if pixelNum == 376:
            return 4
        if pixelNum == 463:
            return 5
        if pixelNum == 550:
            return 6
        
    def _row_to_pixel(self,rowNum):
        if rowNum == 0:
            return 69
        if rowNum == 1:
            return 157
        if rowNum == 2:
            return 244
        if rowNum == 3:
            return 331
        if rowNum == 4:
            return 418
        if rowNum == 5:
            return 505
        
  

    def _col_to_pixel(self,colNum):
        if colNum == 0:
            return 28
        if colNum == 1:
            return 115
        if colNum == 2:
            return 202
        if colNum == 3:
            return 289
        if colNum == 4:
            return 376
        if colNum == 5:
            return 463
        if colNum == 6:
            return 550
        
    def _success(self, pos, dir, found):
        '''
        pos is tuple with coordinates
        dir is int from 1-9 for direction
        1 2 3
        8 X 4
        7 6 5
        found is list of found in direction [vertical, horizonal, increasing, decreasing]
        '''
        print(f'CURRENT POSITION: ({pos[0]}, {pos[1]})')
        if (dir == 1 or dir == 9): # runs if moving in 1 direction or 9 which is all directions
            if (pos[0] > 0 and pos[1] > 0): # ensures the pos is able to move in that direction and not out of bounds
                if (self.board[pos[0]][pos[1]] == self.board[pos[0] - 1][pos[1] - 1]) and (self.board[pos[0]][pos[1]] != 0): # compares the pos to the value in that direction
                    found[3] += 1 # increases the index of found in the checked direction
                    found = self._success((pos[0] - 1, pos[1] - 1), 1, found) # recurses in the direction and resets the found list to check

        if (dir == 2 or dir == 9): # runs if moving in 2 direction or 9 which is all directions
            if (pos[0] > 0): # ensures the pos is able to move in that direction and not out of bounds
                if (self.board[pos[0]][pos[1]] == self.board[pos[0] - 1][pos[1]]) and (self.board[pos[0]][pos[1]] != 0): # compares the pos to the value in that direction
                    found[0] += 1 # increases the index of found in the checked direction
                    found = self._success((pos[0] - 1, pos[1]), 2, found) # recurses in the direction and resets the found list to check

        if (dir == 3 or dir == 9): # runs if moving in 3 direction or 9 which is all directions
            if (pos[0] > 0 and pos[1] < 6): # ensures the pos is able to move in that direction and not out of bounds
                if (self.board[pos[0]][pos[1]] == self.board[pos[0] - 1][pos[1] + 1]) and (self.board[pos[0]][pos[1]] != 0): # compares the pos to the value in that direction
                    found[2] += 1 # increases the index of found in the checked direction
                    found = self._success((pos[0] - 1, pos[1] + 1), 3, found) # recurses in the direction and resets the found list to check

        if (dir == 4 or dir == 9): # runs if moving in 4 direction or 9 which is all directions
            if (pos[1] < 6): # ensures the pos is able to move in that direction and not out of bounds
                if (self.board[pos[0]][pos[1]] == self.board[pos[0]][pos[1] + 1]) and (self.board[pos[0]][pos[1]] != 0): # compares the pos to the value in that direction
                    found[1] += 1 # increases the index of found in the checked direction
                    found = self._success((pos[0], pos[1] + 1), 4, found) # recurses in the direction and resets the found list to check

        if (dir == 5 or dir == 9): # runs if moving in 5 direction or 9 which is all directions
            if (pos[0] < 5 and pos[1] < 6): # ensures the pos is able to move in that direction and not out of bounds
                if (self.board[pos[0]][pos[1]] == self.board[pos[0] + 1][pos[1] + 1]) and (self.board[pos[0]][pos[1]] != 0): # compares the pos to the value in that direction
                    found[3] += 1 # increases the index of found in the checked direction
                    found = self._success((pos[0] + 1, pos[1] + 1), 5, found) # recurses in the direction and resets the found list to check

        if (dir == 6 or dir == 9): # runs if moving in 6 direction or 9 which is all directions
            if (pos[0] < 5): # ensures the pos is able to move in that direction and not out of bounds
                if (self.board[pos[0]][pos[1]] == self.board[pos[0] + 1][pos[1]]) and (self.board[pos[0]][pos[1]] != 0): # compares the pos to the value in that direction
                    found[0] += 1 # increases the index of found in the checked direction
                    found = self._success((pos[0] + 1, pos[1]), 6, found) # recurses in the direction and resets the found list to check

        if (dir == 7 or dir == 9): # runs if moving in 7 direction or 9 which is all directions
            if (pos[0] < 5 and pos[1] > 0): # ensures the pos is able to move in that direction and not out of bounds
                if (self.board[pos[0]][pos[1]] == self.board[pos[0] + 1][pos[1] - 1]) and (self.board[pos[0]][pos[1]] != 0): # compares the pos to the value in that direction
                    found[2] += 1 # increases the index of found in the checked direction
                    found = self._success((pos[0] + 1, pos[1] - 1), 7, found) # recurses in the direction and resets the found list to check

        if (dir == 8 or dir == 9): # runs if moving in 8 direction or 9 which is all directions
            if (pos[1] > 0): # ensures the pos is able to move in that direction and not out of bounds
                if (self.board[pos[0]][pos[1]] == self.board[pos[0]][pos[1] - 1]) and (self.board[pos[0]][pos[1]] != 0): # compares the pos to the value in that direction
                    found[1] += 1 # increases the index of found in the checked direction
                    found = self._success((pos[0], pos[1] - 1), 8, found) # recurses in the direction and resets the found list to check

        return found # returns the list of found direction

        
    async def run(self):
        while (running):
            surface.blit(background,(0,0))
            pygame.display.flip()
            gameRunning = True

            while(gameRunning):
                while (self._move < 42): 
                    # Section for showing the chip at the top of the board
                    if self._move % 2 == 0:
                        surface.blit(half_red_chip,(current_position[0],current_position[1]))    # Put the chip at that spot and we will update if user presses
                    else:
                        surface.blit(half_yellow_chip,(current_position[0],current_position[1]))
                    pygame.display.flip()
                    for event in pygame.event.get():    # Waits for an event to occur
                            if event.type == pygame.KEYDOWN:    # If the user presses a key, we need to check which key it is
                                if pygame.key.get_pressed()[pygame.K_RIGHT]:    # If the right arrow is pressed
                                    if current_position[0] < 550:
                                        surface.blit(white_space,(current_position[0],current_position[1]))
                                        pygame.display.flip()
                                        current_position[0] += 87  # Update the current position to look at the next column
                                    else:
                                        surface.blit(white_space,(current_position[0],current_position[1]))
                                        pygame.display.flip()
                                        current_position[0] = 28

                                elif pygame.key.get_pressed()[pygame.K_LEFT]:   # If the left arrow is pressed
                                    if current_position[0] > 28:
                                        surface.blit(white_space,(current_position[0],current_position[1]))
                                        pygame.display.flip()
                                        current_position[0] -= 87 # Update the current position to look at the previous column
                                    else:
                                        surface.blit(white_space,(current_position[0],current_position[1]))
                                        pygame.display.flip()
                                        current_position[0] = 550

                                elif pygame.key.get_pressed()[pygame.K_SPACE]:
                                    surface.blit(white_space,(current_position[0],current_position[1]))
                                    pygame.display.flip()
                                    columnToPlace = self._pixel_to_column(current_position[0])  # Find the column to place that chip in 
                                    
                                    placed_position = self.placePiece(columnToPlace)    # Place the piece, and store the placed row and column in placed_position
                                    
                                    if placed_position is False:
                                        pass

                                    else:
                                    
                                        row = self._row_to_pixel(placed_position[0])    # Turn the placed row into a pixel number
                                        column = self._col_to_pixel(placed_position[1]) # Turn the placed column into a pixel number
                                    
                                    
                                        if (self._move-1) % 2 == 0: 
                                            surface.blit(red_chip,(column,row))
                                        else:
                                            surface.blit(yellow_chip,(column,row))
                                        pygame.display.flip()
                                        found = self._success(placed_position, 9, [0, 0, 0, 0])
                                        for i in found:
                                            if (i >= 3):
                                                if self.board[placed_position[0]][placed_position[1]] == 1:
                                                    print('Red wins!')
                                                    surface.blit(red_wins, (19.5, 149)) # outputs Draw screen message
                                                    pygame.display.flip() # flips to the display
                                                else:
                                                    print('Yellow wins!')
                                                    surface.blit(yellow_wins, (19.5, 149)) # outputs Draw screen message
                                                    pygame.display.flip() # flips to the display
                                                
                                                self._move = 43 # ends the while loop because the game is completed
                                    
                                for line in self.board:
                                    print(line)
                                print(self._move)

                if (self._move < 43): # runs if the board filled with no winner
                    surface.blit(draw, (19.5, 149)) # outputs Draw screen message
                    pygame.display.flip() # flips to the display
                    print('Draw!') # prints the draw message


                for event in pygame.event.get(): # waits for a mouse click event
                    if event.type == pygame.MOUSEBUTTONDOWN: # runs when the mouse click is lifted
                        self._move = 0
                        self.board = [[0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0]]
                        gameRunning = False # sets the value to false to reset the game loop and reset the board
                            
            await asyncio.sleep(0)