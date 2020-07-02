import pygame
from pygame.locals import *


grid = [ [None, None, None], \
         [None, None, None], \
         [None, None, None] ]

XO = 'X'
winner = None

def initBoard(ttt):
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    #vertical lines
    pygame.draw.line (background, (0,0,0), (100,0), (100,300), 2)
    pygame.draw.line (background, (0,0,0), (200,0), (200,300), 2)

    #horizontal lines
    pygame.draw.line (background, (0,0,0), (0,100), (300,100), 2)
    pygame.draw.line (background, (0,0,0), (0,200), (300,200), 2)

    return background

def drawStaus(board):
    global XO, winner
    if winner is None:
        message = XO + "'s turn"
    else:
        message = winner + " won"

    #render status
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (10, 10, 10))

    board.fill((250,250,250), (0, 300, 300, 25))
    board.blit(text, (10,300))

def showBoard(ttt, board):
    #render the game board on displ

    drawStaus(board)
    ttt.blit (board, (0,0))
    pygame.display.flip()

def boardPos (mouseX, mouseY):

    #determine which row is used
    if (mouseY < 100):
        row = 0
    elif (mouseY < 200):
        row = 1
    elif (mouseY < 300):
        row = 2

    #determine which column is used

    if (mouseX < 100):
        col = 0
    elif (mouseX <200):
        col = 1
    elif (mouseX < 300):
        col = 2

    return (row, col)

def drawMove (board, boardRow, boardCol, Piece):

    #draws a move on the board (displ)

    centerX = ((boardCol) * 100) + 50
    centerY = ((boardRow) * 100) + 50

    if Piece == 'O':
        pygame.draw.circle (board, (0,0,0), (centerX, centerY), 44, 2)
    else:
        pygame.draw.line (board, (0,0,0), (centerX - 22, centerY - 22), (centerX + 22, centerY + 22), 2)
        pygame.draw.line (board, (0,0,0), (centerX + 22, centerY - 22), (centerX - 22, centerY + 22), 2)

    grid[boardRow][boardCol] = Piece

def clickBoard(board):

    global grid, XO

    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos(mouseX,mouseY)

    if grid[row][col] is not None:
        return

    drawMove(board, row, col, XO)

    if XO == 'X':
        XO = 'O'
    else:
        XO = 'X'

def gameWon(board):

    global grid, winner

    #check for winner row
    for row in range (0, 3):
        if ((grid[row][0] == grid[row][1] == grid[row][2]) and (grid[row][0] is not None)):
            #this row won
            winner = grid[row][0]
            pygame.draw.line(board, (250,0,0), (0, (row + 1)*100 - 50), (300, (row + 1)*100 - 50), 2)
            break

    #check for winner col
    for col in range (0, 3):
        if ((grid[0][col] == grid[1][col] == grid[2][col]) and (grid[0][col] is not None)):
            winner = grid[0][col]
            pygame.draw.line(board, (250,0,0), ((col + 1)*100 - 50, 0), ((col + 1)*100 - 50, 300), 2)
            break

        if ((grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] is not None)):
            #left to right
            winner = grid[0][0]
            pygame.draw.line(board, (250,0,0), (50,50), (250,250),2)

        if ((grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] is not None)):
            #right to left
            winner = grid[0][2]
            pygame.draw.line(board, (250,0,0), (250,50), (50,250), 2)


pygame.init()
ttt = pygame.display.set_mode((300,325))
pygame.display.set_caption('Tic-Tac-Toe')

#create the board

board = initBoard(ttt)

running = 1

while (running == 1):
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
        elif event.type is MOUSEBUTTONDOWN:
            #user clicked
            clickBoard(board)

    gameWon(board)
    showBoard(ttt, board)

