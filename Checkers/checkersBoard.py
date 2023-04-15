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

class CheckersBoard:
    def __init__(self):
        self._turn = 0
        self._rPiecesLeft = 12
        self._bPiecesLeft = 12
        self._board = [] # '-' is invalid spot, 'B' is black piece, 'R' is red piece, 'O' is open spot, 'BK' is black king, 'RK' is red king
        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
        self._board.append(['B', '-', 'B', '-', 'B', '-', 'B', '-'])
        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
        self._board.append(['O', '-', 'O', '-', 'O', '-', 'O', '-'])
        self._board.append(['-', 'O', '-', 'O', '-', 'O', '-', 'O'])
        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])
        self._board.append(['-', 'R', '-', 'R', '-', 'R', '-', 'R'])
        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])

def _run(self):
    while (running):
        while (self._rPiecesLeft != 0 or self._bPiecesLeft != 0)
        turn = 0
        curLocation = (_select(turn)[2][0], _select(turn[2][1]))
        leftMove = (_select(turn)[0][0], _select(turn)[0][1])
        rightMove = (_select(turn)[1][0], _select(turn[1][1]))

        selectedCoord = _coordsSelected()

        if ((selectedCoord[0] == leftMove[0] and selectedCoord[1] == leftMove[1]) or (selectedCoord[0] == rightMove[0] and selectedCoord[1] == rightMove[1])):
            _move(curLocation[0], curLocation[1], selectedCoord[0], selectedCoord[1], turn)

def _move(self, xOld, yOld, xNew, yNew, turn):
    self._board[xOld][yOld] = 'O'
    if(turn == 0):
        self._board[xNew][yNew] = 'R'
    elif(turn == 1):
        self._board[xNew][yNew] = 'B'
    


def _select(self, turn):
    x = _coordsSelected[0]
    y = _coordsSelected[1]

    if (self._turn == 0):
        if (self._board[x][y] == 'R'):
            _validMoves(0, x,y)

    elif(self._turn == 1):
        if (self._board[x][y] == 'B'):
            _validMoves(1, x,y)

def _validMoves(self,curTurn, x,y):
    moves = [(0, 0),(0, 0),(x,y)]
    
    if(curTurn == 0):
        try:
            if(self._board[x-1][y+1] == 'O'):
                moves[1][0] = x-1
                moves[1][1] = y+1
            elif(self._board[x-1][y+1] == 'B'):  
                if(_canJump(x,y,x-3,y+3)):
                    moves[1][0] = x-3
                    moves[1][1] = y+3
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
                if(_canJump(x,y,x+3,y+3)):
                    moves[0][0] = x+3
                    moves[0][1] = y+3
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
                    if(_canJump(x,y,x-3,y-3)):
                        moves[1][0] = x-3
                        moves[1][1] = y-3
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
                    if(_canJump(x,y,x+3,y-3)):
                        moves[0][0] = x+3
                        moves[0][1] = y-3
                    else:
                        raise RuntimeError
                elif(self._board[x+1][y-1] == 'B'):
                        raise RuntimeError
            except:
                moves[0][0] = -1
                moves[0][1] = -1
    return moves



def _coordsSelected(self):
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





def _canJump(self,x,y, tryX, tryY):
    





