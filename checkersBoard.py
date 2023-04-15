from checkersPiece import CheckersPiece

class CheckersBoard:
    def __init__(self):
        self._turn = 0
        self._board = [] # '-' is invalid spot, 'B' is black piece, 'R' is red piece, 'O' is open spot, 'BK' is black king, 'RK' is red king
        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
        self._board.append(['B', '-', 'B', '-', 'B', '-', 'B', '-'])
        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
        self._board.append(['O', '-', 'O', '-', 'O', '-', 'O', '-'])
        self._board.append(['-', 'O', '-', 'O', '-', 'O', '-', 'O'])
        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])
        self._board.append(['-', 'R', '-', 'R', '-', 'R', '-', 'R'])
        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])

def _select(self, x, y):
    if (self._turn == 0):
        if (self._board[x][y] == 'R'):
            _validMoves(0, x,y)

    elif(self._turn == 1):
        if (self._board[x][y] == 'B'):
            _validMoves(1, x,y)

def _move(self, ):
       

def _jump(self):
    

def _validMoves(self,curTurn, x,y):
    moves = [(0, 0, 0),(0, 0, 0)]
    
    if(curTurn == 0):
        try:
            if(self._board[x-1][y+1] == 'O'):
                moves[0][0] = x-1
                moves[0][1] = y+1
            elif(self._board[x-1][y+1] == 'B'):  
                if(_canJump(x,y,x-3,y+3)):
                    moves[0][0] = x-3
                    moves[0][1] = y+3
                    moves[0][2] = 1 # acts as a flag that the move is a jump in order to call validMoves and move again
                else:
                    raise RuntimeError
            elif(self._board[x-1][y+1] == 'R'):
                    raise RuntimeError
        except:
            moves[0][0] = -1
            moves[0][1] = -1

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



    else(curTurn == 1):





def _canJump(self,x,y, tryX, tryY):
    





