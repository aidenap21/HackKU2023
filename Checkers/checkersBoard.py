import pygame 
import sys
import os


#Need to do
# - Add functionality for kings
# - Create board

pygame.init()
running = True
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 640
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

class CheckersBoard:
    def __init__(self):
        self._turn = 0
        self._rPiecesLeft = 12
        self._bPiecesLeft = 12
        self._bLocations = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        self._rLocations = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        self._board = [] # '-' is invalid spot, 'B' is black piece, 'R' is red piece, 'O' is open spot, 'BK' is black king, 'RK' is red king
        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
        self._board.append(['B', '-', 'B', '-', 'B', '-', 'B', '-'])
        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
        self._board.append(['O', '-', 'O', '-', 'O', '-', 'O', '-'])
        self._board.append(['-', 'O', '-', 'O', '-', 'O', '-', 'O'])
        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])
        self._board.append(['-', 'R', '-', 'R', '-', 'R', '-', 'R'])
        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])

    def run(self): #Initial run function to be called to start the process
        for i in range(8):
            for j in range(8):
                print(self._board[i][j])
            print('\n')
        print('\n')

        while (running): #Start the game
            while (self._rPiecesLeft != 0 or self._bPiecesLeft != 0 or self._rCanMove == False or self._bCanMove): #Check for end conditions

                x = self._coordsSelected[0]
                y = self._coordsSelected[1]

                curLocation = (self._select(x, y)[2][0], self._select(x, y)[2][1]) #Get the current selected location's coords
                if (self._board[curLocation[0]][curLocation[1]]):

                    self._locations(self._rPiecesLeft) #Update the locations of all the red pieces
                    self._locations(self._bPiecesLeft) #Update the locations of all the black pieces

                    jumpedLocation = (self._select(x, y)[3][0], self._select(x, y)[3][1])
                    leftMove = (self._select(x, y)[0][0], self._select(x, y)[0][1], self._select(x, y)[0][2]) #Get the selected locations' left move 
                    print(f'the left move at {self._select(x, y)[0][0]},{self._select(x, y)[0][1]} can {self._select(x, y)[0][2]}')
                    
                    rightMove = (self._select(x, y)[1][0], self._select(x, y)[1][1], self._select(x, y)[1][2]) #Get the selected locations' right move location
                    print(f'the right move at {self._select(x, y)[1][0]},{self._select(x, y)[1][1]} can {self._select(x, y)[1][2]}')

                    selectedCoord = self._coordsSelected() #Get the user's mouse input 
                    
                    if ((selectedCoord[0] == leftMove[0] and selectedCoord[1] == leftMove[1]) or (selectedCoord[0] == rightMove[0] and selectedCoord[1] == rightMove[1])):
                            self._move(curLocation[0], curLocation[1], selectedCoord[0], selectedCoord[1], leftMove[2], jumpedLocation[0], jumpedLocation[1])

                    for i in range(8):
                        for j in range(8):
                            print(self._board[i][j])
                        print('\n')
                    print('\n')
        
    def _select(self, x, y):
        if (self._turn == 0 and self._board[x][y] == 'R'):
                self._validMoves(self._turn, x,y)
        elif(self._turn == 1 and self._board[x][y] == 'B'):
                self._validMoves(self._turn, x,y)

    def _validMoves(self,curTurn, x,y):
        moves = [(0, 0, 0),(0, 0, 0),(x,y)]
        
        if(curTurn == 0):
            try:
                if(self._board[x-1][y+1] == 'O'):
                    moves[1][0] = x-1
                    moves[1][1] = y+1
                elif(self._board[x-1][y+1] == 'B'):  
                    if(self._canJump(x,y,x-2,y+2)):
                        moves[1][0] = x-2
                        moves[1][1] = y+2
                        moves[1][2] = 1

                        moves[3][0] = x-1
                        moves[3][1] = y+1
                    else:
                        raise RuntimeError
                elif(self._board[x-1][y+1] == 'R'):
                        raise RuntimeError
            except:
                moves[1][0] = -1
                moves[1][1] = -1

    #---------------------right^-----leftv------------------------------------------------        

            try:
                if(self._board[x+1][y+1] == 'O'):
                    moves[0][0] = x+1
                    moves[0][1] = y+1
                elif(self._board[x+1][y+1] == 'B'):  
                    if(self._canJump(x,y,x+2,y+2)):
                        moves[0][0] = x+2
                        moves[0][1] = y+2
                        moves[0][2] = 1

                        moves[3][0] = x+1
                        moves[3][1] = y+1
                    else:
                        raise RuntimeError
                elif(self._board[x+1][y+1] == 'R'):
                        raise RuntimeError
            except:
                moves[0][0] = -1
                moves[0][1] = -1


    #----------------------------Black Moves--------------------------------------------------------------------------
        elif(curTurn == 1):
                try:
                    if(self._board[x-1][y-1] == 'O'):
                        moves[1][0] = x-1
                        moves[1][1] = y-1
                    elif(self._board[x-1][y-1] == 'R'):  
                        if(self._canJump(x,y,x-2,y-2)):
                            moves[1][0] = x-2
                            moves[1][1] = y-2
                            moves[1][2] = 1

                            moves[3][0] = x-1
                            moves[3][1] = y-1
                        else:
                            raise RuntimeError
                    elif(self._board[x-1][y-1] == 'B'):
                            raise RuntimeError
                except:
                    moves[1][0] = -1
                    moves[1][1] = -1

        #---------------------right^-----leftv------------------------------------------------        
                try:
                    if(self._board[x+1][y-1] == 'O'):
                        moves[0][0] = x+1
                        moves[0][1] = y-1
                    elif(self._board[x+1][y+1] == 'R'):  
                        if(self._canJump(x,y,x+2,y-2)):
                            moves[0][0] = x+2
                            moves[0][1] = y-2
                            moves[0][2] = 1

                            moves[3][0] = x+1
                            moves[3][1] = y-1
                        else:
                            raise RuntimeError
                    elif(self._board[x+1][y-1] == 'B'):
                            raise RuntimeError
                except:
                    moves[0][0] = -1
                    moves[0][1] = -1
        return moves
    


    def _move(self, xOld, yOld, xNew, yNew, jump, xJump, yJump):
        self._board[xOld][yOld] = 'O'
        if(self._turn == 0):
            self._board[xNew][yNew] = 'R'
        elif(self._turn == 1):
            self._board[xNew][yNew] = 'B'

        if(jump == 1):
            self._board[xJump][yJump] = 'O'

            if (self._turn == 0):
                self._bPiecesLeft -= 1
                self._bLocations[xJump].pop(yJump)
            elif (self._turn == 1):
                self._rPiecesLeft -= 1
                self._rLocations[xJump].pop(yJump)

            jumpedLocation = (self._select(xNew, yNew)[3][0], self._select(xNew, yNew)[3][1])
            leftMove = (self._select(xNew, yNew)[0][0], self._select(xNew , yNew)[0][1], self._select(xNew, yNew)[0][2]) #Get the selected locations' left move 
            rightMove = (self._select(xNew, yNew)[1][0], self._select(xNew, yNew)[1][1], self._select(xNew, yNew)[1][2]) #Get the selected locations' right move
            
            if (leftMove[2] == 1):
                self._move(xNew, yNew, leftMove[0], leftMove[1], jumpedLocation[0], jumpedLocation[1])
            
            elif (rightMove[2] == 1):
                self._move(xNew, yNew, rightMove[0], rightMove[1], jumpedLocation[0], jumpedLocation[1])


        self._locations(self._rPiecesLeft) #Update the locations of all the red pieces
        self._locations(self._bPiecesLeft) #Update the locations of all the black pieces






    def _coordsSelected(self): #Get the users mouse input to find which tile they selected 
        x = 0
        y = 0
        for event in pygame.event.get(): # waits for a mouse click event
                if event.type == pygame.MOUSEBUTTONUP: # runs when the mouse click is lifted
                    pos = pygame.mouse.get_pos() # gets the position of the mouse on click
                    if (pos[0] < width/8):
                        y = 0
                    elif (pos[0] < 2*(width/8)):
                        y = 1
                    elif (pos[0] < 3*width/8):
                        y = 2
                    elif (pos[0] < 4*(width/8)):
                        y = 3
                    elif (pos[0] < 5*(width/8)):
                        y = 4
                    elif (pos[0] < 6*(width/8)):
                        y = 5
                    elif (pos[0] < 7*(width/8)):
                        y = 6
                    elif (pos[0] < (width)):
                        y = 7


                    if (pos[1] < height/8):
                        x = 0
                    elif (pos[1] < 2*(height/8)):
                        x = 1
                    elif (pos[1] < 3*(height/8)):
                        x = 2
                    elif (pos[1] < 4*(height/8)):
                        x = 3
                    elif (pos[1] < 5*(height/8)):
                        x = 4
                    elif (pos[1] < 6*(height/8)):
                        x = 5
                    elif (pos[1] < 7*(height)/8):
                        x = 6
                    elif (pos[1] < (height)):
                        x = 7

        return (x,y)



    def _bCanMove(self): #Run thru every current black piece's valid moves to check if they all can move
        for i in self._bLocations:
            if (self._validMoves(1, self._bLocations[i][0], self._bLocations[i][1])[0:3] != (0,0,0,0)):
                return True
        return False
    def _rCanMove(self): #Run thru every current red piece's valid moves to check if they all can move
        for i in self._rLocations:
            if (self._validMoves(1, self._rLocations[i][0], self._rLocations[i][1])[0:3] != (0,0,0,0)):
                return True
        return False

    def _locations(self): #Run thru the entire board to find the locations of every piece
        for point in range(self._bPiecesLeft):
            for i in range(8):
                for j in range(8):
                    if (self._board[i][j] == 'B'):
                        self._bLocations[point][0] = i
                        self._bLocations[point][1] = j

        for point in range(self._rPiecesLeft):
            for i in range(8):
                for j in range(8):
                    if (self._board[i][j] == 'R'):
                        self._bLocations[point][0] = i
                        self._bLocations[point][1] = j


        



