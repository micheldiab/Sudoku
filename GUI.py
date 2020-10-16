import pygame
from Check_Board import *
pygame.init()
BLACK = (0,0,0)
WHITE=(255,255,255)
GREY=(128,128,128)
LIGHTBLUE=(173,216,230)
GREEN=(0,255,0)
class Grid:

    def __init__(self,width,height,rows,cols):
        self.width=width
        self.height=height
        self.rows = rows
        self.cols = cols
        self.selected=None
        self.temp_board=None
        self.board = [
        [0, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 0, 0, 7, 8],
        [0, 0, 7, 0, 0, 0, 2, 0, 0],
        [0, 0, 1, 0, 5, 0, 0, 3, 0],
        [9, 0, 4, 0, 0, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 0, 2],
        [1, 0, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7]
    ]
        make_random_board(self.board)
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]


    def drawBoard(self,win):
        cellsize = self.width // 9
        for i in range(self.rows):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, BLACK, (0, i * cellsize), (self.width, i * cellsize), thick)
            pygame.draw.line(win,BLACK, (i * cellsize, 0), (i * cellsize, self.height), thick)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].drawCube(win,cellsize)

    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

            self.cubes[row][col].selected = True
            self.selected = (row, col)

    def press(self, pos):
            if pos[0] < self.width and pos[1] < self.height:
                cellsize = self.width // 9
                x = pos[0] // cellsize
                y = pos[1] // cellsize
                return x, y
            else:
                return None

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def put(self, val,win):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_val(val)
            self.update()

            if valid(self.temp_board, val, (row,col)) and solve(self.temp_board):
                return True
            self.cubes[row][col].set_val(0)
            self.cubes[row][col].set_temp(0)
            self.update()

        return False

    def update(self):
        self.temp_board= [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def delete(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True



class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def drawCube(self, win,cellsize):
        font = pygame.font.SysFont('arial', 50)
        x = self.col * cellsize+15
        y = self.row * cellsize

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), 1, GREY)
            win.blit(text, (x, y))
        elif not(self.value == 0):
            text = font.render(str(self.value), 1, BLACK)
            win.blit(text, (x, y))

        if self.selected:
            pygame.draw.rect(win, LIGHTBLUE, (x-15,y,cellsize ,cellsize), 4)

    def set_temp(self, val):
        self.temp = val

    def set_val(self, val):
        self.value = val

def main():
    win = pygame.display.set_mode((540,540))
    pygame.display.set_caption("Sudoku")
    board = Grid(540, 540,9,9)
    key = None
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9

                if event.key == pygame.K_h:
                    if not board.selected:
                        key=None
                        break
                    i, j = board.selected
                    for k in range (1,10):
                        if board.put(k, win):
                            break
                    key = None
                if event.key == pygame.K_DELETE:
                    if not board.selected:
                        key=None
                        break
                    board.delete()
                    key = None
                if event.key == pygame.K_RETURN:
                    if not board.selected:
                        key=None
                        break
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        board.put(board.cubes[i][j].temp,win)
                        key = None

                if board.is_finished():
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.press(pos)
                if clicked:
                    board.select(clicked[1], clicked[0])
                    key = None
        if board.selected and key != None:
            board.sketch(key)
        win.fill(WHITE)
        board.drawBoard(win)
        pygame.display.update()

main()
pygame.quit()

