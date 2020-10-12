from Settings import *
from Check_Board import *
import pygame
import time
def drawGrid():
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

def writeBoard(board,color):
    font = pygame.font.SysFont('arial', 50)
    for i in range(9):
        num_width = i * CELLSIZE
        for j in range(9):
            num_height =10+CELLSIZE*j
            if board[i][j] == 0:
                text = font.render(" ", True, color)
            else:
                text = font.render(str(board[i][j]), True, color)
                win.blit(text, (num_height,num_width))
    pygame.display.update()


def solve():  #Backtracking
    font = pygame.font.SysFont('arial', 50)
    win.fill(WHITE)
    drawGrid()
    writeBoard(work_board,BLACK)
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
            if solve():  #Recursive
                return True
            work_board[row][column] = 0
    return False


def find_empty():
    for i in range(9):
        for j in range(9):
            if work_board[i][j] == 0:
                return (i, j)

    return None
def main_start(win):
    running = True
    while running:
        pygame.init()
        win.fill(WHITE)
        drawGrid()
        writeBoard(work_board,BLACK)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    solve()
                    writeBoard(work_board,GREEN)
                    writeBoard(original_board,BLACK)
                    running = False
                    time.sleep(5)

win = pygame.display.set_mode((WIDTH, HEIGHT)) #Create display
pygame.display.set_caption('Sudoku')
main_start(win)  #Start
