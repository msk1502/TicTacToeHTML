import logic

_name_ = '_main_'

if _name_ == '_main_':
    BoardTicTac = logic.Board() #makes empty board
    Stats = logic.Stats() #makes empty stats class
    winner = None #sets winner to none
    play = True #play is the condition that continues game if true
    gameID = 1

    #set up player 1
    Player1 = logic.Player('X', '1')
    Player2 = logic.Player('Y', '2')


    print('Lets play Tic Tac Toe!')
    print(BoardTicTac.board[0], '\n', BoardTicTac.board[1], '\n', BoardTicTac.board[2]) #prints empty board

    while play == True: #loop continues while play is true
        
        #Goes through players 1 turn and players 2 turn in order during each loop.  Checks if anyone won between turns
        if winner == None:
            BoardTicTac.board = Player1.move(BoardTicTac.board)
            winner = BoardTicTac.get_winner()
 
        if winner == None:
            BoardTicTac.board = Player2.move(BoardTicTac.board)
            winner = BoardTicTac.get_winner()

        #output if someone has won
        if winner != None:
            if winner == 'Draw':
                print('Game is a Draw!')
                playerWinner = Player1.name = 'Draw'

            else:
                if Player1.XorO == winner:
                    playerWinner = Player1.name
                else:
                    playerWinner = Player2.name
                print(winner, 'has won!')

            Stats.updateStats(gameID, Player1.name, Player2.name, playerWinner) #adds row to stats dataframe
            print(Stats.gameStats) #prints stats dataframe

            playAgain = input('Do you want to play again?(Y/N): ') #asks players if they want to play again

            #if yes restarts game with empty board 
            if playAgain == 'Y' or playAgain == 'y' or playAgain == 'Yes' or playAgain =='YES' or playAgain == 'yes':
                BoardTicTac.make_empty_board()
                gameID += 1

                #get player info
                Player1 = logic.Player('X', '1')
                Player2 = logic.Player('Y', '2')

                winner = None
            #if no ends loop completing program
            elif playAgain == 'N' or playAgain == 'n' or playAgain == 'No' or playAgain == 'NO' or playAgain == 'no':
                play = False
                print('Thanks for playing!')
