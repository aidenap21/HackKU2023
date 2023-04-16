import asyncio
import pygame 
import sys
import os


# os.chdir("ConnectFour") # uncomment if running on system
pygame.init()
width = 639
height = 553
surface = pygame.display.set_mode((width,height))
background = pygame.image.load(os.path.join("assets", "connectFourBoard.png"))
red_chip = pygame.image.load(os.path.join("assets", "red_chip.png"))
yellow_chip = pygame.image.load(os.path.join("assets", "yellow_chip.png"))
current_position = [29,27]


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
        for row in range(6):  # Iterate through the board
            if self.board[row][column] != 0 :  # If there is a piece somewhere down the column, place the piece above it
                print("Piece at: " + str(row) + ',' + str(column))
                self._mark(row-1,column)    # Mark the spot right above it 
                self._move += 1
                return [row-1,column]
            
        self._mark(5,column)
        self._move += 1
        return [5,column]
            

    def _mark(self,row,column): # Used to mark the place with either a red piece or yellow
        if self._move % 2 == 0:  # If it's red's turn\
            self.board[row][column] = 1  # Mark with a 1 to signify red placed
        else:   # Otherwise it's yellow's turn
            self.board[row][column] = 2  # Mark with a 2 to signify yellow placed

        
    def _pixel_to_column(self,pixelNum):
        if pixelNum == 29:
            return 0
        if pixelNum == 116:
            return 1
        if pixelNum == 203:
            return 2
        if pixelNum == 290:
            return 3
        if pixelNum == 377:
            return 4
        if pixelNum == 464:
            return 5
        if pixelNum == 551:
            return 6
        
    def _row_to_pixel(self,rowNum):
        if rowNum == 0:
            return 27
        if rowNum == 1:
            return 115
        if rowNum == 2:
            return 202
        if rowNum == 3:
            return 289
        if rowNum == 4:
            return 376
        if rowNum == 5:
            return 463
        


    def _col_to_pixel(self,colNum):
        if colNum == 0:
            return 29
        if colNum == 1:
            return 116
        if colNum == 2:
            return 203
        if colNum == 3:
            return 290
        if colNum == 4:
            return 377
        if colNum == 5:
            return 464
        if colNum == 6:
            return 551
        
    def _success(self, pos, dir, found):
        '''
        pos is tuple with coordinates
        dir is int from 1-9 for direction
        1 2 3
        8 X 4
        7 6 5
        found is list of found in direction [vertical, horizonal, increasing, decreasing]
        '''
        if (dir == 1 or dir == 9):
            if (pos[0] > 0 and pos[1] > 0):
                if (self.board[pos[0]][pos[1]] == self.board[pos[0] - 1][pos[1] - 1]) and (self.board[pos[0]][pos[1]] != 0):
                    


        if (dir == 2 or dir == 9):

        if (dir == 3 or dir == 9):

        if (dir == 4 or dir == 9):

        if (dir == 5 or dir == 9):

        if (dir == 6 or dir == 9):

        if (dir == 7 or dir == 9):

        if (dir == 8 or dir == 9):

        
    async def run(self):
        while (running):
            surface.blit(background,(0,0))
            pygame.display.flip()

            while (self._move < 42): 
                # Section for showing the chip at the top of the board
                if self._move % 2 == 0:
                    surface.blit(red_chip,(current_position[0],current_position[1]))    # Put the chip at that spot and we will update if user presses
                else:
                    surface.blit(yellow_chip,(current_position[0],current_position[1]))
                pygame.display.flip()
                for event in pygame.event.get():    # Waits for an event to occur
                        if event.type == pygame.KEYDOWN:    # If the user presses a key, we need to check which key it is
                            if pygame.key.get_pressed()[pygame.K_RIGHT]:    # If the right arrow is pressed
                                if current_position[0] < 551:
                                    current_position[0] += 87  # Update the current position to look at the next column
                                else:
                                    current_position[0] = 29

                            elif pygame.key.get_pressed()[pygame.K_LEFT]:   # If the left arrow is pressed
                                if current_position[0] > 29:
                                    current_position[0] -= 87 # Update the current position to look at the previous column
                                else:
                                    current_position[0] = 551

                            elif pygame.key.get_pressed()[pygame.K_SPACE]:
                                columnToPlace = self._pixel_to_column(current_position[0])  # Find the column to place that chip in 
                                placed_position = self.placePiece(columnToPlace)    # Place the piece, and store the placed row and column in placed_position
                                row = self._row_to_pixel(placed_position[0])    # Turn the placed row into a pixel number
                                column = self._col_to_pixel(placed_position[1]) # Turn the placed column into a pixel number
                                pos = [placed_position[0],placed_position[1]]
                                if (self._success()):
                                    print("We have a winner!")
                                if (self._move-1) % 2 == 0: 
                                    surface.blit(red_chip,(column,row))
                                else:
                                    surface.blit(yellow_chip,(column,row))
                                pygame.display.flip()


                        
                            for line in self.board:
                                print(line)
                            print(self._move)
                            
            await asyncio.sleep(0)