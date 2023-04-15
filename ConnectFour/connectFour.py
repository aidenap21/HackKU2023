



class connectFour:

    def __init__(self):
        self.move = 0
        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]
        
    def _placePiece(self,column):
        for row in self.board:  # Iterate through the board
            if self.board[row][column] != 0 :  # If there is a piece somewhere down the column, place the piece above it
                self._mark(row-1,column)
                self.move += 1
                break


    def _mark(self,row,column):
        if self.move % 2 == 0:  # If it's red's turn
            self.board[row][column] = 1  # Mark with a 1 to signify red placed
        else:   # Otherwise it's black's turn
            self.board[row][column] = 2  # Mark with a 2 to signify black placed

    def _whoMoves(self):
        if self.move % 2 == 0:
            return 'R'
    def _lineOfFour(self,row,column):
        



