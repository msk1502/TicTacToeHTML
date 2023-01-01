#note for self: code to run is: flask --app server.py --debug run

from flask import Flask, render_template, request, url_for, redirect
import logic
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

#program variables
BoardTicTac = logic.Board() #makes empty board
players = {'player1' : '', 'player2': ''} #dictionary that stores player names
state = {'current' : 'X'} #keeps track of whose turn it is
boardMap = {'ul' : (0,0), 'um' : (0,1), 'ur' : (0,2), 'ml' : (1,0), 'mm' : (1,1), 'mr' : (1,2), 'bl' : (2,0), 'bm' : (2,1), 'br' : (2,2)} #maps board areas to array locations
values = {} #values represented on the HTML webpage
winnerCounts = {}

#function maps the board to the values dictionary
def updateValues():
    for (key, val) in boardMap.items():
        values[key] = BoardTicTac.board[val[0]][val[1]]
        
updateValues()

@app.route('/', methods=['POST', 'GET'])
def index():

    #makes empty bord
    BoardTicTac.make_empty_board()
    updateValues()

    if request.method == 'POST': #post method come from Start game button and page link buttons

        # links to other views
        if 'game' in request.get_data(as_text = True): #goes to game view and sets turn to X
            state["current"] = 'X'
            return redirect('game')
        elif 'stats' in request.get_data(as_text = True): #goes to stats view
            return redirect('stats')

        #updates player dictionary with entered names
        Names = request.get_data(as_text = True).split('&') 
        players['player1'] = Names[0][8:]
        players['player2'] = Names[1][8:]
       
        return redirect('game') #begins new game when start game button is pressed

    return render_template('index.html') #renders index html view

@app.route('/game', methods=['POST', 'GET']) 
def game():
    outcome = None #Outcome of the current game

    if request.method == 'POST':

        # links to other views and other buttons
        if 'home' in request.get_data(as_text = True): #redirects to home (index.html) page
            return redirect('/')
        elif 'stats' in request.get_data(as_text = True): #redirects to stats page
            return redirect('stats') 
        elif 'new' in request.get_data(as_text=True): #starts a new game and makes an empty board
            state['current'] = 'X'
            BoardTicTac.make_empty_board() 
            updateValues()

        else:
            replace = request.get_data(as_text = True)[0:2] #button from game.html
            index = boardMap[replace] #maps from tic tac toe board location to location in array
            if BoardTicTac.board[index[0]][index[1]] == None: #checks to see if clicked square has been taken
                values[replace] = state["current"] #replaces value at square clicked with X or O depending upon whoses turn it is
                BoardTicTac.board[index[0]][index[1]] = state['current'] #updates tic tac toe board with current move

                #changes turn from x to o and vice versa
                if state["current"] == 'X':
                    state["current"] = 'O'
                else:
                    state["current"] = 'X'
    
        outcome = BoardTicTac.get_winner() #used get_winner function to see if anyone has wone or if there is a draw

        #adds outcome to statistics
        if outcome in ['X', 'O']:
            if outcome == 'X':
                winnerName = players['player1']
            else:
                winnerName = players['player2']
            if winnerName not in winnerCounts.keys():
                winnerCounts[winnerName] = 1
            else:
                winnerCounts[winnerName] = winnerCounts[winnerName] + 1

    return render_template('game.html', **values, **players, **state, outcome = outcome)   

@app.route('/stats', methods=['POST', 'GET'])
def stats():

    #buttons on stats page
    if 'clear' in request.get_data(as_text = True): #clears all stats
        winnerCounts.clear()
    elif 'home' in request.get_data(as_text = True): #link to home page
        return redirect('/')
    elif 'game' in request.get_data(as_text = True): #link to game page
        return redirect('game')   

    #creates bar graph of all winners
    if winnerCounts != None:
        fig, TicTacPlot = plt.subplots()

        TicTacPlot.bar(list(winnerCounts.keys()), list(winnerCounts.values()))

        TicTacPlot.set_ylabel('Outcomes')
        TicTacPlot.set_title("Tic Tac Toes Outcomes")

        plt.savefig('./static/TicTacStats.png')

    return render_template('stats.html')