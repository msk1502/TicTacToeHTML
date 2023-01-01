import logic

Board1 = logic.Board()
Stats = logic.Stats()

#Test Boards
boardEmpty = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
        ]

boardXDiag = [
        ['X', None, '0'],
        [None, 'X', None],
        [None, 'O', 'X']
        ]

boardYDiag = [
        ['Y', None, 'X'],
        [None, 'Y', None],
        [None, 'X', 'Y']
        ]

boardXHoriz = [
        ['X', 'X', 'X'],
        [None, 'Y', None],
        ['Y', None, None]
        ]

boardYHoriz = [
        ['Y', 'Y', 'Y'],
        [None, 'X', None],
        ['X', None, None]
        ]

boardXVert = [
        ['X', None, 'Y'],
        ['X', 'Y', None],
        ['X', None, None]
        ]

boardYVert = [
        ['Y', None, 'X'],
        ['Y', 'X', None],
        ['Y', None, None]
        ]

boardDraw = [
        ['X', 'Y', 'Y'],
        ['Y', 'X', 'X'],
        ['X', 'X', 'Y']
        ]


#tests whether make_empty_board works
def test_make_empty_board(board):

        board.make_empty_board()
        assert board.board == boardEmpty, 'did not make empty board'
        print('test_make_empty_board success')

#tests whether get_winner works
def test_get_winner(Board, testBoard, XorY):
        Board1.board = testBoard
        curWinner  = Board.get_winner()
        assert curWinner == XorY, 'Did not return correct winner'
        print('test_get_winner success')

#tests whether move works
def test_move(XorO,firstOrSecond, board, expectedBoard):
        Player1 = logic.Player(XorO,firstOrSecond)
        print(board)
        curBoard = Player1.move(board)
        assert curBoard == expectedBoard, 'Returned board not expected'
        print('Test_move is success')

#tests whether updateStats works
def test_StatsUpdate(stats, gameID, player1, player2, winner):
        stats.updateStats(gameID, player1, player2, winner)
        print(stats.gameStats)

#test whether clearStats works
def test_clearStats(stats):
        print(stats.gameStats)
        stats.clearStats()
        print(stats.gameStats)


_name_='_main_'

if _name_ == '_main_':
        # test_make_empty_board(Board1)
        
        # Board1.board = boardYVert
        # test_get_winner(Board1, boardDraw, 'Draw')


        #test to see if move method in player class works
        testExpectedBoard = [
                [None, None, None],
                ['X', 'X', 'Y'],
                [None, None, None]
                ]
        Board1.board = [
                [None, None, None],
                ['X', 'X', None],
                [None, None, None]
                ]

        # test_move('Y', '1', Board1.board, testExpectedBoard)

        test_StatsUpdate(Stats, 1, 'testPlayer1', 'testPlayer2', 'testplayer2 winner')

        test_clearStats(Stats)

