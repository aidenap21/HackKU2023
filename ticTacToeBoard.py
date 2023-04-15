class TicTacToe:
    def __init__(self):
        self._board = [[0,0,0],[0,0,0],[0,0,0]] # initializes board as list of lists to stores moves
        self._turnNum = 0 # tracks which round the game is on

    def _place(self, x, y): #Function to place the mark
        if (self._turnNum == 9): #End condition when all moves have been played
            return False #Return false in this case
        
        elif (self._board[x][y] != 0): #Check if the current move is valid
            if (self._turnNum % 2 == 0): #Check if it's player 1's turn
                    self._board[x][y] = 'X' #If so, place an 'X' in the location
                    
            elif(self._turnNum % 2 == 1): #Check if it's player 2's turn
                self._board[x][y] = 'O' #If so, place an 'O' in the location
                
            else: #Else statement to catch invalid moves
                return False #Returns false in this case



        self._turnNum += 1
        self._winCheck()
        return True

    def _winCheck(self):
        if (self._turnNum == 9):
            return 'F'
        
        for i in range(0, 3):
            if (self._board[i][0] == self._board[i][1] == self._board[i][2] != 0):
                return self._board[i][0]
            elif (self._board[0][i] == self._board[1][i] == self._board[2][0] != 0):
                return self._board[0][i]
        