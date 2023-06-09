import asyncio
import pygame 
import sys
import os


#Need to do
# - Add functionality for kings

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
square = pygame.image.load(os.path.join('assets', 'square.png'))
red_wins = pygame.image.load(os.path.join('assets', 'Red_wins.png'))
black_wins = pygame.image.load(os.path.join('assets', 'Black_wins.png'))

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
        while (running): #Start the game
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0)) # outputs the background which is the tic tac toe board
            pygame.display.flip() # flips to the screen
            self._updateGrid()
            gameRunning = True

            while(gameRunning):
                #await asyncio.sleep(0)
                while (self._rPiecesLeft != 0 and self._bPiecesLeft != 0 and (self._rCanMove or self._bCanMove)): #Check for end conditions
                    for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP: # runs when the mouse click is lifted

                                x = self._coordsSelected()[0]
                                y = self._coordsSelected()[1]

                                print(f'{x},{y}')
                                
                                while((self._turn == 0 and (self._board[x][y] != 'R' and self._board[x][y] != 'K')) or (self._turn == 1 and (self._board[x][y] != 'B' and self._board[x][y] != 'Q'))):
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONUP: # runs when the mouse click is lifted
                                            x = self._coordsSelected()[0]
                                            y = self._coordsSelected()[1]
                                            print(f'{x},{y} = {self._board[x][y]}')
                                    await asyncio.sleep(0)
                                            
                                print(f'{x},{y}')
                                moveInfo = self._select(x,y)

                                self._updateLocations()

                                if(len(moveInfo) == 5):
                                    curLocation = [moveInfo[2][0], moveInfo[2][1]] #Get the current selected location's coords

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
                                    if(not((leftMove[0] < 0 or leftMove[1] < 0) and (rightMove[0] < 0 or rightMove[1] < 0))):
                                        print("has at least 1 move available")

                                        newX = self._coordsSelected()[0]
                                        newY = self._coordsSelected()[1]

                                        while((newX != leftMove[0] or newY != leftMove[1]) and (newX != rightMove[0] or newY != rightMove[1])):
                                            for event in pygame.event.get():
                                                if event.type == pygame.MOUSEBUTTONUP: # runs when the mouse click is lifted
                                                    newX = self._coordsSelected()[0]
                                                    newY = self._coordsSelected()[1]
                                                    print(f'tried newX, newY = {newX},{newY} can only go {leftMove[0]},{leftMove[1]} or {rightMove[0]},{rightMove[1]}')
                                            await asyncio.sleep(0)
                                        
                                        print(f'{newX},{newY} worked')
                                        selectedCoord = [newX, newY]
                                        print(f'User selected {selectedCoord[0]},{selectedCoord[1]}')

                                        if (selectedCoord[0] == leftMove[0] and selectedCoord[1] == leftMove[1]):
                                            self._move(curLocation, selectedCoord, jumpedLocationLeft)
                                            
                                        elif(selectedCoord[0] == rightMove[0] and selectedCoord[1] == rightMove[1]):
                                            self._move(curLocation, selectedCoord, jumpedLocationRight)

                                        if (self._turn == 0):
                                            self._turn = 1
                                        else:
                                            self._turn = 0

                                        self._printGrid()
                                    else:
                                        print("cannot move piece at all")

                                else:
                                    curLocation = [moveInfo[4][0], moveInfo[4][1]] #Get the current selected location's coords

                                    if(moveInfo[5][0] == 1):
                                        jumpedLocationLeft = (moveInfo[5][0], moveInfo[5][1],moveInfo[5][2])
                                    else:
                                        jumpedLocationLeft = (0,0,0)
                                    if(moveInfo[6][0] == 1):
                                        jumpedLocationRight = (moveInfo[6][0], moveInfo[6][1], moveInfo[6][2])
                                    else:
                                        jumpedLocationRight = (0,0,0)
                                    if(moveInfo[7][0] == 1):
                                        jumpedLocationBackLeft = (moveInfo[7][0], moveInfo[7][1],moveInfo[7][2])
                                    else:
                                        jumpedLocationBackLeft = (0,0,0)
                                    if(moveInfo[8][0] == 1):
                                        jumpedLocationBackRight = (moveInfo[8][0], moveInfo[8][1], moveInfo[8][2])
                                    else:
                                        jumpedLocationBackRight = (0,0,0)
                                    
                                    leftMove = (moveInfo[0][0], moveInfo[0][1]) #Get the selected locations' left move             
                                    rightMove = (moveInfo[1][0], moveInfo[1][1]) #Get the selected locations' right move location
                                    leftBackMove = (moveInfo[2][0], moveInfo[2][1]) #Get the selected locations' right move location
                                    rightBackMove = (moveInfo[3][0], moveInfo[3][1]) #Get the selected locations' right move location
                                    print("select location to move to")

                                    if(not((leftMove[0] < 0 or leftMove[1] < 0) and (rightMove[0] < 0 or rightMove[1] < 0) and (leftBackMove[0] < 0 or leftBackMove[1] < 0) and (rightBackMove[0] < 0 or rightBackMove[1] < 0))):
                                        print("has at least 1 move available")

                                        newX = self._coordsSelected()[0]
                                        newY = self._coordsSelected()[1]

                                        while((newX != leftMove[0] or newY != leftMove[1]) and (newX != rightMove[0] or newY != rightMove[1]) and (newX != leftBackMove[0] or newY != leftBackMove[1]) and (newX != rightBackMove[0] or newY != rightBackMove[1])):
                                            for event in pygame.event.get():
                                                if event.type == pygame.MOUSEBUTTONUP: # runs when the mouse click is lifted
                                                    newX = self._coordsSelected()[0]
                                                    newY = self._coordsSelected()[1]
                                                    print(f'tried newX, newY = {newX},{newY} can only go {leftMove[0]},{leftMove[1]} or {rightMove[0]},{rightMove[1]} or {leftBackMove[0]},{leftBackMove[1]} or {rightBackMove[0]},{rightBackMove[1]}')
                                            await asyncio.sleep(0)
                                        
                                        print(f'{newX},{newY} worked')
                                        selectedCoord = [newX, newY]
                                        print(f'User selected {selectedCoord[0]},{selectedCoord[1]}')

                                        if (selectedCoord[0] == leftMove[0] and selectedCoord[1] == leftMove[1]):
                                            self._move(curLocation, selectedCoord, jumpedLocationLeft)
                                            
                                        elif(selectedCoord[0] == rightMove[0] and selectedCoord[1] == rightMove[1]):
                                            self._move(curLocation, selectedCoord, jumpedLocationRight)
                                        
                                        elif(selectedCoord[0] == leftBackMove[0] and selectedCoord[1] == leftBackMove[1]):
                                            self._move(curLocation, selectedCoord, jumpedLocationBackLeft)

                                        elif(selectedCoord[0] == rightBackMove[0] and selectedCoord[1] == rightBackMove[1]):
                                            self._move(curLocation, selectedCoord, jumpedLocationBackRight)

                                        if (self._turn == 0):
                                            self._turn = 1
                                        else:
                                            self._turn = 0

                                        self._printGrid()
                                    else:
                                        print("cannot move piece at all")

                    await asyncio.sleep(0)

                #await asyncio.sleep(0)

                if (self._turn == 1):
                    print('Red wins!')
                    screen.blit(red_wins, (20, 160)) # outputs red wins screen message
                    pygame.display.flip() # flips to the display
                elif (self._turn == 0):
                    print('Black wins')
                    screen.blit(black_wins, (20, 160)) # outputs black wins screen message
                    pygame.display.flip() # flips to the display

                for event in pygame.event.get(): # waits for a mouse click event
                            if event.type == pygame.MOUSEBUTTONDOWN: # runs when the mouse click is lifted
                                        self._turn = 0
                                        self._rPiecesLeft = 12
                                        self._bPiecesLeft = 12
                                        self._bLocations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
                                        self._rLocations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
                                        self._board = [] # '-' is invalid spot, 'B' is black piece, 'R' is red piece, 'O' is open spot, 'Q' is black king, 'K' is red king
                                        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
                                        self._board.append(['B', '-', 'B', '-', 'B', '-', 'B', '-'])
                                        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
                                        self._board.append(['O', '-', 'O', '-', 'O', '-', 'O', '-'])
                                        self._board.append(['-', 'O', '-', 'O', '-', 'O', '-', 'O'])
                                        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])
                                        self._board.append(['-', 'R', '-', 'R', '-', 'R', '-', 'R'])
                                        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])
                                        gameRunning = False

                await asyncio.sleep(0)
            
            await asyncio.sleep(0)

            
        
    def _select(self, x, y):
        print(f'recieved {x},{y} in select on turn {self._turn}')
        return self._validMoves(x,y)


    def _validMoves(self, x,y):
        print(f'recieved {x},{y} in validMove')
        moveType = 0 # 0 behaves as B or R check and 1 behaves as K or Q check
        if (self._board[x][y] == 'R' or self._board[x][y] == 'B'):
            moves = [[0, 0],[0, 0],[x,y],[0,0,0],[0,0,0]] #[0] = left move, [1] = right move, [2] = original position, [3] =left jump, [4] = right jump
        else:
            moves = [[0, 0],[0, 0],[0, 0], [0, 0], [x,y],[0,0,0],[0,0,0], [0,0,0], [0,0,0]] #[0] = left forward move, []1 = right forward move, [2] = left back move, [3] = right back move, [4] = original position, [5] =left forward jump, [6] = right forward jump, [7] =left back jump, [8] = right back jump
            moveType = 1

        print(f'Current Selection: {moves[2][0]},{moves[2][1]}')
        
        if (moveType == 0):
            if(self._turn == 0):
                try:
                    if(self._board[x-1][y+1] == 'O'):
                        moves[1][0] = x-1
                        moves[1][1] = y+1
                        print(f'right move @ {moves[1][0]},{moves[1][1]}')
                    elif((self._board[x-1][y+1] == 'B' or self._board[x-1][y+1] == 'Q') and (self._board[x-2][y+2] == 'O')):  
                        moves[1][0] = x-2
                        moves[1][1] = y+2
                        
                        moves[4][0] = 1
                        moves[4][1] = x-1
                        moves[4][2] = y+1
                        print(f'right move @ {moves[1][0]},{moves[1][1]}')

                    elif(self._board[x-1][y+1] == 'R'):
                            raise RuntimeError
                    else:
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
                    elif((self._board[x-1][y-1] == 'B' or self._board[x-1][y-1] == 'Q') and (self._board[x-2][y-2] == 'O')):  
                        moves[0][0] = x-2
                        moves[0][1] = y-2
                        
                        moves[3][0] = 1
                        moves[3][1] = x-1
                        moves[3][2] = y-1
                        print(f'left move @ {moves[0][0]},{moves[0][1]}')
                    elif(self._board[x-1][y-1] == 'R'):
                            raise RuntimeError
                    else:
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
                        elif((self._board[x+1][y+1] == 'R' or self._board[x+1][y+1] == 'K') and (self._board[x+2][y+2] == 'O')):  
                            moves[1][0] = x+2
                            moves[1][1] = y+2
                            
                            moves[4][0] = 1
                            moves[4][1] = x+1
                            moves[4][2] = y+1
                            print(f'right move @ {moves[1][0]},{moves[1][1]}')
                        elif(self._board[x+1][y+1] == 'B'):
                                raise RuntimeError
                        else:
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
                        elif((self._board[x+1][y-1] == 'R' or self._board[x+1][y-1] == 'K') and (self._board[x+2][y-2] == 'O')):  
                            moves[0][0] = x+2
                            moves[0][1] = y-2
                            
                            moves[3][0] = 1
                            moves[3][1] = x+1
                            moves[3][2] = y-1
                            print(f'left move @ {moves[0][0]},{moves[0][1]}')
                        elif(self._board[x+1][y-1] == 'B'):
                                raise RuntimeError
                        else:
                            raise RuntimeError
                    except:
                        moves[0][0] = -1
                        moves[0][1] = -1
                        print(f'left move @ {moves[0][0]},{moves[0][1]}')
            return moves
        
        #------------------------------red king---------------------------------------------
        
        if (moveType == 1):
            if(self._turn == 0):
                #red king right forward
                try:
                    if(self._board[x-1][y+1] == 'O'):
                        moves[1][0] = x-1
                        moves[1][1] = y+1
                        print(f'right forward move @ {moves[1][0]},{moves[1][1]}')
                    elif((self._board[x-1][y+1] == 'B' or self._board[x-1][y+1] == 'Q') and (self._board[x-2][y+2] == 'O')):  
                        moves[1][0] = x-2
                        moves[1][1] = y+2
                        
                        moves[6][0] = 1
                        moves[6][1] = x-1
                        moves[6][2] = y+1
                        print(f'right forward move @ {moves[1][0]},{moves[1][1]}')

                    elif(self._board[x-1][y+1] == 'R'):
                            raise RuntimeError
                    else:
                        raise RuntimeError
                    
                except:
                    moves[1][0] = -1
                    moves[1][1] = -1
                    print(f'right forward move @ {moves[1][0]},{moves[1][1]}')

        #red king left forward        

                try:
                    if(self._board[x-1][y-1] == 'O'):
                        moves[0][0] = x-1
                        moves[0][1] = y-1
                        print(f'left forward move @ {moves[0][0]},{moves[0][1]}')
                    elif((self._board[x-1][y-1] == 'B' or self._board[x-1][y-1] == 'Q') and (self._board[x-2][y-2] == 'O')):  
                        moves[0][0] = x-2
                        moves[0][1] = y-2
                        
                        moves[5][0] = 1
                        moves[5][1] = x-1
                        moves[5][2] = y-1
                        print(f'left forward move @ {moves[0][0]},{moves[0][1]}')
                    elif(self._board[x-1][y-1] == 'R'):
                            raise RuntimeError
                    else:
                        raise RuntimeError
                except:
                    moves[0][0] = -1
                    moves[0][1] = -1
                    print(f'left forward move @ {moves[0][0]},{moves[0][1]}')
                    
#-----------red king right back

                try:
                    if(self._board[x+1][y+1] == 'O'):
                        moves[3][0] = x+1
                        moves[3][1] = y+1
                        print(f'right back move @ {moves[3][0]},{moves[3][1]}')
                    elif((self._board[x+1][y+1] == 'B' or self._board[x+1][y+1] == 'Q') and (self._board[x+2][y+2] == 'O')):  
                        moves[3][0] = x+2
                        moves[3][1] = y+2
                        
                        moves[8][0] = 1
                        moves[8][1] = x+1
                        moves[8][2] = y+1
                        print(f'right back move @ {moves[3][0]},{moves[3][1]}')
                    elif(self._board[x+1][y+1] == 'R'):
                            raise RuntimeError
                    else:
                        raise RuntimeError
                except:
                    moves[3][0] = -1
                    moves[3][1] = -1
                    print(f'right back move @ {moves[3][0]},{moves[3][1]}')

        #------------------red king---left back-----------------------------------------------        
                try:
                    if(self._board[x+1][y-1] == 'O'):
                        moves[2][0] = x+1
                        moves[2][1] = y-1
                        print(f'left back move @ {moves[2][0]},{moves[2][1]}')
                    elif((self._board[x+1][y-1] == 'B' or self._board[x+1][y-1] == 'Q') and (self._board[x+2][y-2] == 'O')):  
                        moves[2][0] = x+2
                        moves[2][1] = y-2
                        
                        moves[7][0] = 1
                        moves[7][1] = x+1
                        moves[7][2] = y-1
                        print(f'left back move @ {moves[2][0]},{moves[2][1]}')
                    elif(self._board[x+1][y-1] == 'R'):
                            raise RuntimeError
                    else:
                        raise RuntimeError
                except:
                    moves[2][0] = -1
                    moves[2][1] = -1
                    print(f'left back move @ {moves[2][0]},{moves[2][1]}')

#-----------------black king---------------

            elif(self._turn == 1):
                try:
                    #black king right back
                    if(self._board[x-1][y+1] == 'O'):
                        moves[1][0] = x-1
                        moves[1][1] = y+1
                        print(f'right back move @ {moves[1][0]},{moves[1][1]}')
                    elif((self._board[x-1][y+1] == 'R' or self._board[x-1][y+1] == 'K') and (self._board[x-2][y+2] == 'O')):  
                        moves[1][0] = x-2
                        moves[1][1] = y+2
                        
                        moves[6][0] = 1
                        moves[6][1] = x-1
                        moves[6][2] = y+1
                        print(f'right back move @ {moves[1][0]},{moves[1][1]}')

                    elif(self._board[x-1][y+1] == 'B'):
                            raise RuntimeError
                    else:
                        raise RuntimeError
                    
                except:
                    moves[1][0] = -1
                    moves[1][1] = -1
                    print(f'right back move @ {moves[1][0]},{moves[1][1]}')

        #---------------------black king left back------------------------------------------------        

                try:
                    if(self._board[x-1][y-1] == 'O'):
                        moves[0][0] = x-1
                        moves[0][1] = y-1
                        print(f'left back move @ {moves[0][0]},{moves[0][1]}')
                    elif((self._board[x-1][y-1] == 'R' or self._board[x-1][y-1] == 'K') and (self._board[x-2][y-2] == 'O')):  
                        moves[0][0] = x-2
                        moves[0][1] = y-2
                        
                        moves[5][0] = 1
                        moves[5][1] = x-1
                        moves[5][2] = y-1
                        print(f'left back move @ {moves[0][0]},{moves[0][1]}')
                    elif(self._board[x-1][y-1] == 'B'):
                            raise RuntimeError
                    else:
                        raise RuntimeError
                except:
                    moves[0][0] = -1
                    moves[0][1] = -1
                    print(f'left back move @ {moves[0][0]},{moves[0][1]}')
                    


        #-----------black king right forward
                try:
                    if(self._board[x+1][y+1] == 'O'):
                        moves[3][0] = x+1
                        moves[3][1] = y+1
                        print(f'right forward move @ {moves[3][0]},{moves[3][1]}')
                    elif((self._board[x+1][y+1] == 'R' or self._board[x+1][y+1] == 'K') and (self._board[x+2][y+2] == 'O')):  
                        moves[3][0] = x+2
                        moves[3][1] = y+2
                        
                        moves[8][0] = 1
                        moves[8][1] = x+1
                        moves[8][2] = y+1
                        print(f'right forward move @ {moves[3][0]},{moves[3][1]}')
                    elif(self._board[x+1][y+1] == 'B'):
                            raise RuntimeError
                    else:
                        raise RuntimeError
                except:
                    moves[3][0] = -1
                    moves[3][1] = -1
                    print(f'right forward move @ {moves[3][0]},{moves[3][1]}')

        #----------------black king left forward------------------------------------------------        
                try:
                    if(self._board[x+1][y-1] == 'O'):
                        moves[2][0] = x+1
                        moves[2][1] = y-1
                        print(f'left forward move @ {moves[2][0]},{moves[2][1]}')
                    elif((self._board[x+1][y-1] == 'R' or self._board[x+1][y-1] == 'K') and (self._board[x+2][y-2] == 'O')):  
                        moves[2][0] = x+2
                        moves[2][1] = y-2
                        
                        moves[7][0] = 1
                        moves[7][1] = x+1
                        moves[7][2] = y-1
                        print(f'left forward move @ {moves[2][0]},{moves[2][1]}')
                    elif(self._board[x+1][y-1] == 'B'):
                            raise RuntimeError
                    else:
                        raise RuntimeError
                except:
                    moves[2][0] = -1
                    moves[2][1] = -1
                    print(f'left forward move @ {moves[2][0]},{moves[2][1]}')
            return moves


    def _move(self, old, new, jump):
        print(f'value beingn moved from {old} is {self._board[old[0]][old[1]]}')
        if (self._board[old[0]][old[1]] == 'R' or self._board[old[0]][old[1]] == 'B'):
            self._board[old[0]][old[1]] = 'O'
            if(self._turn == 0):
                self._board[new[0]][new[1]] = 'R'
            elif(self._turn == 1):
                self._board[new[0]][new[1]] = 'B'
            
            if(jump[0] == 1):
                self._board[jump[1]][jump[2]] = 'O'

                if (self._turn == 0):
                    self._bPiecesLeft -= 1
                    self._bLocations.remove([jump[1], jump[2]])
                elif (self._turn == 1):
                    self._rPiecesLeft -= 1
                    self._rLocations.remove([jump[1], jump[2]])

                if (self._select(new[0], new[1])[3][0] == 1):
                    jumpedLocation = (self._select(new[0], new[1])[3][0], self._select(new[0], new[1])[3][1], self._select(new[0], new[1])[3][2])
                    leftMove = (self._select(new[0], new[1])[0][0], self._select(new[0], new[1])[0][1]) #Get the selected locations' left move 
                    self._move(new, leftMove, jumpedLocation)
                
                elif(self._select(new[0], new[1])[4][0] == 1):
                    jumpedLocation = (self._select(new[0], new[1])[4][0], self._select(new[0], new[1])[4][1], self._select(new[0], new[1])[4][2])
                    rightMove = (self._select(new[0], new[1])[1][0], self._select(new[0], new[1])[1][1]) #Get the selected locations' right move
                    self._move(new, rightMove, jumpedLocation)
        
        else:
            self._board[old[0]][old[1]] = 'O'
            if(self._turn == 0):
                self._board[new[0]][new[1]] = 'K'
            elif(self._turn == 1):
                self._board[new[0]][new[1]] = 'Q'

            if(jump[0] == 1):
                self._board[jump[1]][jump[2]] = 'O'

                if (self._turn == 0):
                    self._bPiecesLeft -= 1
                    self._bLocations.remove([jump[1], jump[2]])
                elif (self._turn == 1):
                    self._rPiecesLeft -= 1
                    self._rLocations.remove([jump[1], jump[2]])

                if (self._select(new[0], new[1])[5][0] == 1):
                    jumpedLocation = (self._select(new[0], new[1])[5][0], self._select(new[0], new[1])[5][1], self._select(new[0], new[1])[5][2])
                    leftMove = (self._select(new[0], new[1])[0][0], self._select(new[0], new[1])[0][1]) #Get the selected locations' left move 
                    self._move(new, leftMove, jumpedLocation)
                
                elif(self._select(new[0], new[1])[6][0] == 1):
                    jumpedLocation = (self._select(new[0], new[1])[6][0], self._select(new[0], new[1])[6][1], self._select(new[0], new[1])[6][2])
                    rightMove = (self._select(new[0], new[1])[1][0], self._select(new[0], new[1])[1][1]) #Get the selected locations' right move
                    self._move(new, rightMove, jumpedLocation)

                elif(self._select(new[0], new[1])[7][0] == 1):
                    jumpedLocation = (self._select(new[0], new[1])[7][0], self._select(new[0], new[1])[7][1], self._select(new[0], new[1])[7][2])
                    leftBackMove = (self._select(new[0], new[1])[2][0], self._select(new[0], new[1])[2][1]) #Get the selected locations' right move
                    self._move(new, leftBackMove, jumpedLocation)

                elif(self._select(new[0], new[1])[8][0] == 1):
                    jumpedLocation = (self._select(new[0], new[1])[8][0], self._select(new[0], new[1])[8][1], self._select(new[0], new[1])[8][2])
                    rightBackMove = (self._select(new[0], new[1])[3][0], self._select(new[0], new[1])[3][1]) #Get the selected locations' right move
                    self._move(new, rightBackMove, jumpedLocation)

        if (self._turn == 1):
            if new[0] == 7:
                self._board[new[0]][new[1]] = 'Q'
        elif (self._turn == 0):
            if new[0] == 0:
                self._board[new[0]][new[1]] = 'K'

        self._updateLocations()
        self._updateGrid()
        




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
        for i in range(self._bPiecesLeft):
            self._bLocations.pop()
        
        for i in range(self._rPiecesLeft):
            self._rLocations.pop()

        for i in range(8):
            for j in range(8):
                if (self._board[i][j] == 'B' or self._board[i][j] == 'Q'):
                    self._bLocations.append([i,j])

        for i in range(8):
            for j in range(8):
                if (self._board[i][j] == 'R' or self._board[i][j] == 'K'):
                    self._rLocations.append([i,j])
                        

        print(f'B locations: {self._bLocations}')
        print(f'R locations: {self._rLocations}')

    def _printGrid(self):
        for i in range(8):
            for j in range(8):
                print(self._board[i][j],end='')
            print('')
    
    def _updateGrid(self):
        for x in range(8): # iterates through the lists
            for y in range(8): # iterates through the indices of the lists
                if (self._board[x][y] == 'B'): # runs if the current piece is black
                    screen.blit(black_piece, (y * 80, x * 80)) # places the piece
                    pygame.display.flip() 

                elif (self._board[x][y] == 'R'): # runs if the current piece is red
                    screen.blit(red_piece, (y * 80, x * 80)) # places the piece
                    pygame.display.flip()

                elif (self._board[x][y] == 'K'): # runs if the current piece is red king
                    screen.blit(red_king, (y * 80, x * 80)) # places the piece
                    pygame.display.flip()

                elif (self._board[x][y] == 'Q'): # runs if the current piece is black king
                    screen.blit(black_king, (y * 80, x * 80)) # places the piece
                    pygame.display.flip()

                elif (self._board[x][y] == 'O'): # runs if the current piece is open
                    screen.blit(square, (y * 80, x * 80)) # places the piece
                    pygame.display.flip()