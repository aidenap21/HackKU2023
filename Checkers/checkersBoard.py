import asyncio
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

#os.chdir('Checkers')
background = pygame.image.load(os.path.join('assets', 'checkersBoard.png'))
red_piece = pygame.image.load(os.path.join('assets', 'red_piece.png'))
black_piece = pygame.image.load(os.path.join('assets', 'black_piece.png'))
red_king = pygame.image.load(os.path.join('assets', 'red_king.png'))
black_king = pygame.image.load(os.path.join('assets', 'black_king.png'))

class CheckersBoard:
    def __init__(self):
        self._turn = 0
        self._rPiecesLeft = 12
        self._bPiecesLeft = 12
        self._bLocations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self._rLocations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self._board = [] # '-' is invalid spot, 'B' is black piece, 'R' is red piece, 'O' is open spot, 'BK' is black king, 'RK' is red king
        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
        self._board.append(['B', '-', 'B', '-', 'B', '-', 'B', '-'])
        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
        self._board.append(['O', '-', 'O', '-', 'O', '-', 'O', '-'])
        self._board.append(['-', 'O', '-', 'O', '-', 'O', '-', 'O'])
        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])
        self._board.append(['-', 'R', '-', 'R', '-', 'R', '-', 'R'])
        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])

    async def run(self): #Initial run function to be called to start the process

        self._printGrid()
        while (running): #Start the game
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0)) # outputs the background which is the tic tac toe board
            pygame.display.flip() # flips to the screen

            while (self._rPiecesLeft != 0 or self._bPiecesLeft != 0 or self._rCanMove == False or self._bCanMove): #Check for end conditions
                x = self._coordsSelected()[0]
                y = self._coordsSelected()[1]

                while((self._turn == 0 and self._board[x][y] != 'R') or (self._turn == 1 and self._board[x][y] != 'B')):
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP: # runs when the mouse click is lifted
                            x = self._coordsSelected()[0]
                            y = self._coordsSelected()[1]
                            print(f'{x},{y} = {self._board[x][y]}')
                            
                print(f'{x},{y}')
                moveInfo = self._select(x,y)

                curLocation = [moveInfo[2][0], moveInfo[2][1]] #Get the current selected location's coords

                self._updateLocations()

                if(moveInfo[3][0] == 1):
                    jumpedLocationLeft = (moveInfo[3][0], moveInfo[3][1],moveInfo[3][2])
                else:
                    jumpedLocationLeft = (0,0,0)
                if(moveInfo[4][0] == 1):
                    jumpedLocationRight = (moveInfo[4][0], moveInfo[4][1], moveInfo[4][2])
                else:
                    jumpedLocationRight = (0,0,0)
                
                
                leftMove = (moveInfo[0][0], moveInfo[0][1]) #Get the selected locations' left move             
                rightMove = (moveInfo[1][0], moveInfo[1][1]) #Get the selected locations' right move location

                
                print("select location to move to")
                if((leftMove[0] != -1 and leftMove[1] != -1) or (rightMove[0] != -1 and rightMove[1] != -1)):
                    print("has at least 1 move available")

                    newX = self._coordsSelected()[0]
                    newY = self._coordsSelected()[1]

                    while((newX != leftMove[0] and newY != leftMove[1]) or (newX != rightMove[0] and newY != rightMove[1])):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP: # runs when the mouse click is lifted
                                newX = self._coordsSelected()[0]
                                newY = self._coordsSelected()[1]
                                print(f'tried newX, newY = {newX},{newY} can only go {leftMove[0]},{leftMove[1]} or {rightMove[0]},{rightMove[1]}')
                    
                    print(f'{newX},{newY} worked')
                    selectedCoord = [newX, newY]
                    print(f'User selected {selectedCoord[0]},{selectedCoord[1]}')

                    if (selectedCoord[0] == leftMove[0] and selectedCoord[1] == leftMove[1]):
                        self._move(curLocation, selectedCoord, jumpedLocationLeft)
                        
                    elif(selectedCoord[0] == rightMove[0] and selectedCoord[1] == rightMove[1]):
                        self._move(curLocation, selectedCoord, jumpedLocationRight)

                    self._printGrid()
                else:
                    print("cannot move piece at all")

            await asyncio.sleep(0)

            
        
    def _select(self, x, y):
        print(f'recieved {x},{y} in select on turn {self._turn}')
        if (self._turn == 0 and self._board[x][y] == 'R'):
            return self._validMoves(x,y)
        elif(self._turn == 1 and self._board[x][y] == 'B'):
            return self._validMoves(x,y)


    def _validMoves(self, x,y):
        print(f'recieved {x},{y} in validMove')
        moves = [[0, 0],[0, 0],[x,y],[0,0,0],[0,0,0]] #[0] = left move, [1] = right move, [2] = original position, [3] =left jump, [4] = right jump

        print(f'Current Selection: {moves[2][0]},{moves[2][1]}')
        
        if(self._turn == 0):
            try:
                if(self._board[x-1][y+1] == 'O'):
                    moves[1][0] = x-1
                    moves[1][1] = y+1
                    print(f'right move @ {moves[1][0]},{moves[1][1]}')
                elif((self._board[x-1][y-1] == 'B') and (self._board[x-2][y+2] == 'O')):  
                    moves[1][0] = x-2
                    moves[1][1] = y+2
                    
                    moves[4][0] = 1
                    moves[4][1] = x-1
                    moves[4][2] = y+1
                    print(f'right move @ {moves[1][0]},{moves[1][1]}')

                elif(self._board[x-1][y+1] == 'R'):
                        raise RuntimeError
            except:
                moves[1][0] = -1
                moves[1][1] = -1
                print(f'right move @ {moves[1][0]},{moves[1][1]}')

    #---------------------right^-----leftv------------------------------------------------        

            try:
                if(self._board[x-1][y-1] == 'O'):
                    moves[0][0] = x-1
                    moves[0][1] = y-1
                    print(f'left move @ {moves[0][0]},{moves[0][1]}')
                elif((self._board[x-1][y-1] == 'B') and (self._board[x-2][y-2] == 'O')):  
                    if(self._canJump(x,y,x-2,y-2)):
                        moves[0][0] = x-2
                        moves[0][1] = y-2
                        
                        moves[3][0] = 1
                        moves[3][1] = x-1
                        moves[3][2] = y-1
                        print(f'left move @ {moves[0][0]},{moves[0][1]}')
                    else:
                        raise RuntimeError
                elif(self._board[x-1][y-1] == 'R'):
                        raise RuntimeError
            except:
                moves[0][0] = -1
                moves[0][1] = -1
                print(f'left move @ {moves[0][0]},{moves[0][1]}')
                


    #----------------------------Black Moves--------------------------------------------------------------------------
        elif(self._turn == 1):
                try:
                    if(self._board[x+1][y+1] == 'O'):
                        moves[1][0] = x+1
                        moves[1][1] = y+1
                        print(f'right move @ {moves[1][0]},{moves[1][1]}')
                    elif((self._board[x+1][y+1] == 'R') and (self._board[x+2][y+2] == 'O')):  
                        if(self._canJump(x,y,x+2,y+2)):
                            moves[1][0] = x+2
                            moves[1][1] = y+2
                            
                            moves[4][0] = 1
                            moves[4][1] = x+1
                            moves[4][2] = y+1
                            print(f'right move @ {moves[1][0]},{moves[1][1]}')
                        else:
                            raise RuntimeError
                    elif(self._board[x+1][y+1] == 'B'):
                            raise RuntimeError
                except:
                    moves[1][0] = -1
                    moves[1][1] = -1
                    print(f'right move @ {moves[1][0]},{moves[1][1]}')

        #---------------------right^-----leftv------------------------------------------------        
                try:
                    if(self._board[x+1][y-1] == 'O'):
                        moves[0][0] = x+1
                        moves[0][1] = y-1
                        print(f'left move @ {moves[0][0]},{moves[0][1]}')
                    elif((self._board[x+1][y-1] == 'R') and (self._board[x+2][y-2] == 'O')):  
                        if(self._canJump(x,y,x+2,y-2)):
                            moves[0][0] = x+2
                            moves[0][1] = y-2
                            
                            moves[3][0] = 1
                            moves[3][1] = x+1
                            moves[3][2] = y-1
                            print(f'left move @ {moves[0][0]},{moves[0][1]}')
                        else:
                            raise RuntimeError
                    elif(self._board[x+1][y-1] == 'B'):
                            raise RuntimeError
                except:
                    moves[0][0] = -1
                    moves[0][1] = -1
                    print(f'left move @ {moves[0][0]},{moves[0][1]}')
        return moves
    


    def _move(self, old, new, jump):
        self._board[old[0]][old[1]] = 'O'
        if(self._turn == 0):
            self._board[new[0]][new[1]] = 'R'
        elif(self._turn == 1):
            self._board[new[0]][new[1]] = 'B'

        if(jump[0] == 1):
            self._board[jump[1]][jump[2]] = 'O'

            if (self._turn == 0):
                self._bPiecesLeft -= 1
                self._bLocations[jump[1]].pop(jump[2])
            elif (self._turn == 1):
                self._rPiecesLeft -= 1
                self._rLocations[jump[1]].pop(jump[2])

            if (self._select(new[0], new[1])[3][0] == 1):
                jumpedLocation = (self._select(new[0], new[1])[3][0], self._select(new[0], new[1])[3][1], self._select(new[0], new[1])[3][2])
                leftMove = (self._select(new[0], new[1])[0][0], self._select(new[0], new[1])[0][1], self._select(new[0], new[1])[0][2]) #Get the selected locations' left move 
                self._move(new, leftMove, jumpedLocation)
            
            elif(self._select(new[0], new[1])[3][0] == 1):
                jumpedLocation = (self._select(new[0], new[1])[4][0], self._select(new[0], new[1])[4][1], self._select(new[0], new[1])[4][2])
                rightMove = (self._select(new[0], new[1])[1][0], self._select(new[0], new[1])[1][1], self._select(new[0], new[1])[1][2]) #Get the selected locations' right move
                self._move(new, rightMove, jumpedLocation)

        if (self._turn == 1):
            self._turn = 0
        elif (self._turn == 0):
            self._turn = 1
        print(self._turn)

        self._updateLocations()
        




    def _coordsSelected(self): #Get the users mouse input to find which tile they selected 

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

        return [x,y]

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

    def _updateLocations(self): #Run thru the entire board to find the locations of every piece
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

    def _printGrid(self):
        for i in range(8):
            for j in range(8):
                print(self._board[i][j],end='')
            print('')
        

        



