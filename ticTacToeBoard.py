class TicTacToe:
    def __init__(self):
        self._board = [[0,0,0],[0,0,0],[0,0,0]] # initializes board as list of lists to stores moves
        self._turnNum = 0 # tracks which round the game is on

    def _place(self, x, y): #Function to place the mark
        if (self._board[x][y] == 0 and (0 <= x <= 2) and (0 <= y <= 2)): #Check if the current move is valid
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
        for i in range(0, 3): # iterates from 0-3 to access every row
            if (self._board[i][0] == self._board[i][1] == self._board[i][2] != 0): # checks the current i value row
                return self._board[i][0] # returns the value of the winner if there are 3 of the same across
            elif (self._board[0][i] == self._board[1][i] == self._board[2][0] != 0): # checks the current i value column
                return self._board[0][i] # returns the value of the winner if there are 3 of the same across
            
        if (self._board[0][0] == self._board[1][1] == self._board[2][2] != 0): # checks a diagonal
            return self._board[0][0] # returns the value of the winner if there are 3 of the same diagonal
        elif (self._board[0][2] == self._board[1][1] == self._board[2][0] != 0): # checks a diagonal
            return self._board[0][2] # returns the value of the winner if there are 3 of the same diagonal
        
        return 'F'
    
    def run(self):
        while (self._turnNum < 9):
            if (self._turnNum % 2 == 0):
                x = int(input('Enter x coordinate for X move: '))
                y = int(input('Enter y coordinate for Y move: '))
                if (not(self._place())