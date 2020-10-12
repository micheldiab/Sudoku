from Settings import *
from Check_Board import *
import pygame
import time
def drawGrid(win):
        for i in range(0, HEIGHT, CELLSIZE):
            if i % 3 == 0 and i != 0:
                pygame.draw.line(win, BLACK, (i, 0), (i, HEIGHT), 4)
            else:
                pygame.draw.line(win, BLACK, (i, 0), (i, HEIGHT))
        for j in range(0, WIDTH, CELLSIZE):
            if j % 3 == 0 and j != 0:
                pygame.draw.line(win, BLACK, (0, j), (WIDTH, j), 4)
            else:
                pygame.draw.line(win, BLACK, (0, j), (WIDTH, j))

def writeBoard(win,board,color):
    font = pygame.font.SysFont('arial', 50)
    for i in range(9):
        num_row = i * CELLSIZE
        for j in range(9):
            num_column =10+CELLSIZE*j
            if board[i][j] == 0:
                text = font.render(" ", True, color)
            else:
                text = font.render(str(board[i][j]), True, color)
                win.blit(text, (num_column,num_row))
    pygame.display.update()


def solve(win):  #Backtracking
    font = pygame.font.SysFont('arial', 50)
    win.fill(WHITE)
    drawGrid(win)
    writeBoard(win,work_board,BLACK)
    find = find_empty()
    if not find:
        return True
    else:
        row, column = find

    for value in range(1, 10):
        if valid(work_board, value, (row, column)):
            work_board[row][column] = value
            text = font.render(str(value),True, GREEN)
            win.blit(text, ((10 + (column * CELLSIZE)), (row * CELLSIZE)))
            pygame.display.update()
            time.sleep(0.1)
            if solve(win):  #Recursive
                return True
            work_board[row][column] = 0
    return False


def find_empty():
    for i in range(9):
        for j in range(9):
            if work_board[i][j] == 0:
                return (i, j)

    return None
