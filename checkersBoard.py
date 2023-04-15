from checkersPiece import CheckersPiece

class CheckersBoard:
    def __init__(self):
        self._board = [] # '-' is invalid spot, 'B' is black piece, 'R' is red piece, 'O' is open spot, 'BK' is black king, 'RK' is red king
        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
        self._board.append(['B', '-', 'B', '-', 'B', '-', 'B', '-'])
        self._board.append(['-', 'B', '-', 'B', '-', 'B', '-', 'B'])
        self._board.append(['O', '-', 'O', '-', 'O', '-', 'O', '-'])
        self._board.append(['-', 'O', '-', 'O', '-', 'O', '-', 'O'])
        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])
        self._board.append(['-', 'R', '-', 'R', '-', 'R', '-', 'R'])
        self._board.append(['R', '-', 'R', '-', 'R', '-', 'R', '-'])






