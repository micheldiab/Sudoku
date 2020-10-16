import random
def make_random_board(board):
    temp_board1=[[0 for y in range(0,9)]for x in range (0,9)]
    for i in range(len(board)):
        for j in range(len(board[0])):
          temp_board1[i][j]=board[i][j]
    for i in range (0,100):
          row=random.randint(0,8)
          col = random.randint(0,8)
          value = random.randint(0, 9)
          temp_board1[row][col]=value
          if valid(temp_board1,value,(row,col)) and solve(temp_board1):
           board[row][col]=value
          for row_num in range(len(board)):#Copy the board again
              for col_num in range(len(board[0])):
                  temp_board1[row_num][col_num] = board[row_num][col_num]



def solve(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    x = pos[0] // 3
    y = pos[1] // 3

    for i in range(x*3,x*3 + 3):
        for j in range(y * 3, y*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None
