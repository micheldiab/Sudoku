import pygame
from Settings import *
from Solve_Board import *
def main_start(win):
    running = True
    while running:
        pygame.init()
        win.fill(WHITE)
        drawGrid(win)
        writeBoard(win,work_board,BLACK)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    solve(win)
                    writeBoard(win,work_board,GREEN)
                    writeBoard(win,original_board,BLACK)
                    running = False
                    time.sleep(5)

win = pygame.display.set_mode((WIDTH, HEIGHT)) #Create display
pygame.display.set_caption('Sudoku')
main_start(win)  #Start
