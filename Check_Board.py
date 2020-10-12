def valid(board,value, position):
    #check row
    for i in range(9):
        if board[position[0]][i] == value and position[1] != i:
            return False

    #check column
    for i in range(9):
        if board[i][position[1]] == value and position[0] != i:
            return False

    #check  box
    x = position[0] // 3
    y = position[1] // 3

    for i in range(x*3, x*3 + 3):
        for j in range(y*3, y*3 + 3):
            if board[i][j] == value and (i,j) != position:
                return False
    return True
