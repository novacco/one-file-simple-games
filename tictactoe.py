from IPython.display import clear_output
import os
import sys
import subprocess
from random import randint
from time import sleep as slep

def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

test_board = [' ']*10

def first_player_input():
    marker = ''

    #ask player 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O ')
    
    player1 = marker

    #assign player 2
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)

player1_marker, player2_marker = first_player_input()
last_marker = ''

def win_check(board):
    global last_marker
    if (board[1] == board[4] == board[7] == 'X') or (board[2] == board[5] == board[8] == 'X') or (board[3] == board[6] == board[9] == 'X') or (board[1] == board[5] == board[9] == 'X') or (board[3] == board[5] == board[7] == 'X') or (board[7] == board[8] == board[9] == 'X') or (board[4] == board[5] == board[6] == 'X') or (board[1] == board[2] == board[3] == 'X'):
        if last_marker == 'X':
            print('Player X wins')
            return True
    elif (board[1] == board[4] == board[7] == 'O') or (board[2] == board[5] == board[8] == 'O') or (board[3] == board[6] == board[9] == 'O') or (board[1] == board[5] == board[9] == 'O') or (board[3] == board[5] == board[7] == 'O') or (board[7] == board[8] == board[9] == 'O') or (board[4] == board[5] == board[6] == 'O') or (board[1] == board[2] == board[3] == 'O'):
        if last_marker == 'O':
            print('Player O wins')
            return True
    return False

def remis(board):
    new = 0
    i=1
    while i < 10:
        if board[i] != ' ':
            new +=1
        i+=1
    if new ==9:
        return True
        print("R E M I S")
    else:
        return False
    
goes_on = True

def player_input(board):
    global last_marker
    if remis(test_board) == True:
        global goes_on
        goes_on = False
    else:
        if last_marker == 'O':
            where = int(input('Player X, click the number'))
            if board[where] != ' ':
                print('Give other number')
            else:
                last_marker = 'X'
                board[where] = 'X'
        elif last_marker == 'X':
            where = int(input('Player O, click the number'))
            if board[where] != ' ':
                print('Give other number')
            else:
                last_marker = 'O'
                board[where] = 'O'
    
def clear():
    os.system('clear')

### function that randomly choose who goes first

def whogoesfirst():
    x = randint(1,20)
    global last_marker
    if x%2 == 0:
        last_marker = 'X'
    else:
        last_marker = 'O'


def game(board):
    whogoesfirst()
    display_board(test_board)
    while(win_check(board) != True and remis(board) != True):
        if goes_on == False:
            print('REMIS')
            remis(board)
            break
        player_input(board)
        slep(2)
        clear()
        display_board(test_board)

game(test_board)