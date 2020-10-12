from Settings import *
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

def writeBoard():
    font = pygame.font.SysFont('arial', 50)
    for i in range(9):
        num_width = 10+ i * CELLSIZE
        for j in range(9):
            num_height =CELLSIZE*j
            if board[i][j] == 0:
                text = font.render(" ", True, BLACK)
            else:
                text = font.render(str(board[i][j]), True, BLACK)
                win.blit(text, (num_width,num_height))
    pygame.display.update()


def main_start(win):
    running = True
    while running:
        pygame.init()
        win.fill(WHITE)
        drawGrid()
        writeBoard()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #Solve
                    running = False
                    time.sleep(5)

win = pygame.display.set_mode((WIDTH, HEIGHT)) #Create display
pygame.display.set_caption('Sudoku')
main_start(win)  #Start
