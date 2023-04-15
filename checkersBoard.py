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
    moves = [0,0,0,0]
    
    if(curTurn == 0):
        if(self._board[x-1][y+1] == 'O'):
            moves[0] = x-1
            moves[1] = y+1
        elif(self._board[x-1][y+1] == 'B'):  
            if(_canJump(x,y)):
                moves[2] = 
        else:



def _canJump(self,x,y):
    





