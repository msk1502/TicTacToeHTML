import pandas as pd

class Stats: #stats class which contains dataframe and relevant functions
    def __init__(self):
        #creates empty dataframe with columns
        self.gameStats = pd.DataFrame(columns=[ 
            'Game ID',
            'Player 1',
            'Player 2',
            'Winner',
        ])

    def updateStats(self, gameID, player1, player2, winner): #updates Stats dataframe with new row
        newRow = {'Game ID' : gameID, 'Player 1' : player1, 'Player 2' : player2,'Winner' : winner,}
        self.gameStats = self.gameStats.append(newRow, ignore_index = True)

    def clearStats(self): #clears dataframe, currently unused
        self.gameStats.drop(self.gameStats.index,inplace=True) 

class Player:
    def __init__(self, XorO, firstOrSecond):

        #checks whether player is AI.  Will continue loop until recieve expected input
        AIConfirm = None
        while AIConfirm == None:
            AIConfirm = input('Is player' + firstOrSecond + ' an AI?(Y or N) ')
            if AIConfirm == 'Y' or AIConfirm == 'y' or AIConfirm == 'Yes' or AIConfirm =='YES' or AIConfirm == 'yes':
                self.AI = True
            elif AIConfirm == 'N' or AIConfirm == 'n' or AIConfirm == 'No' or AIConfirm == 'NO' or AIConfirm == 'no':
                self.AI = False
            else:
                print('Did not recognize input.  Try Again')
                AIConfirm = None
       
        #inputs name of player
        if self.AI == True:
            self.name = 'AI' + firstOrSecond
        elif self.AI == False:
            self.name = input('Player' + firstOrSecond + ' what is your name? ')
        self.XorO = XorO
        print(self.name + ' is ' + XorO)

    #move function for both AI and human players
    def move(self, board):

        #checks if AI
        if self.AI == True:
            #checks who is the opponent
            if self.XorO == 'X':
                oppon = 'O'
            else:
                oppon = 'X'

            columns = [[] for i in range(4)] #empty list of list to build columns

            #checks if two X or O in a row.  Return updated board with move to block win
            y = 0
            for row in board:
                if row.count(oppon) == 2 and row.count(None) == 1: #checks if two of O or X
                    x = row.index(None)
                    board[y][x] = self.XorO
                    print(board[0], '\n', board[1], '\n', board[2])
                    return board

            #builds columns
                for i in range(len((row))):
                    columns[i].append(row[i])
            
                y +=1

    
            #checks if two X or O in a column.  Return updated board with move to block win
            y = 0
            for column in columns:
                if column.count(oppon) == 2 and column.count(None) == 1: #checks if two of O or X
                    x = column.index(None)
                    board[x][y] = self.XorO
                    print(board[0], '\n', board[1], '\n', board[2])
                    return board

                y += 1
    
            #builds list of list of diagnols
            Diags = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]

            #checks if two X or O in a column.  Return updated board with move to block win
            DiagNum = 0
            for Diag in Diags:
                if Diag.count(oppon) == 2 and Diag.count(None) == 1: #checks if two of O or X
            
                    #if statements to get coordinates of move
                    indexNone = Diag.index(None)
                    if indexNone == 1:
                        board[1][1] = self.XorO
                    elif indexNone == 0:
                        if DiagNum == 0:
                            board[0][0] = self.XorO
                        else:
                            board[0][2] = self.XorO
                    elif indexNone == 2:
                        if DiagNum == 0:
                            board[2][2] = self.XorO
                        else:
                            board[2][0] = self.XorO
                    print(board[0], '\n',board[1], '\n', board[2])
                    return board

                DiagNum += 1

            #if no emminent win returns coordinates of first unoccupied space
            for x in range(len(board)):
                for y in range(len(board)):
                    if board[y][x] == None:
                        board[y][x] = self.XorO
                        print(board[0], '\n', board[1], '\n', board[2])
                        return board
        else:
            #get player inputs
            print(self.name, 'it is your turn!')
            x = int(input('Enter X coordinate: '))
            y = int(input('Enter Y coordinate: '))


            if 0 > x  or x > 2 or  0 > y or y > 2:  
                #checks if it is outside the image's bounds
                print('Outside Board.  Please enter new coordinates between 0 and 2')
                return self.move(board) #returns board
            elif board[y][x] != None:
                #checks if the selected space does not equal none
                print('Spot already taken.  Please enter new coordinates')
                return self.move(board) #returns board

            #updates a board to player's move
            board[y][x] = self.XorO

            #prints current board
            print(board[0], '\n', board[1], '\n', board[2])
            return board


    


class Board:
    def __init__(self):
        self.board =[
                [None, None, None],
                [None, None, None],
                [None, None, None],
                ]

    def make_empty_board(self):
        #creates and returns empty board
        self.board = [
                [None, None, None],
                [None, None, None],
                [None, None, None],
                ]

    #checks if there is a winner.  If there is returns X or O depending upon who won.  Returns None if no winner
    def get_winner(self):
    
        Winner = None #The Winner of the game. X, O or None if draw
        Outcome = None #eventual return value

        for i in range(3):
        
            #Check Rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2]: #checks to see if each entry in a row is the same
                return self.board[i][0]
        
            #Check Columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i]: #checks to see if a each entry in a column is the same
                return self.board[0][i]
        
        #Check Diagnols
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] or
        self.board[0][2] == self.board[1][1] == self.board[2][0]): #checks to see if a each entry in the diagnols is the same
            return self.board[1][1]

        #check for draw
        flat_Board = [item for row in self.board for item in row]
        if flat_Board.count(None) == 0:
            return 'Draw'
